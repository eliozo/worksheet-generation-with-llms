import mistletoe
import mistletoe.ast_renderer
import requests
import csv
import os
import shutil
from scripts.markdown_proc.mdchunk_reader import markdown_md_to_turtle
import sys

def getGoogleSpreadsheet(url_spreadsheet, directory):
    response = requests.get(url_spreadsheet)
    csv_file_name = os.path.join(directory, "spreadsheet.csv")
    with open(csv_file_name, "wb") as file: 
        file.write(response.content)

# Atgriežam sarakstu, kurā ir pārīši row_1, row[3]
def readCSVfile(file_path):  # Funkcija, kas lasa CSV failu
    result = []
    # with open(os.path.join(directory, "spreadsheet.csv"), 'r',  encoding='utf-8') as csv_file:
    with open(file_path, 'r',  encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            elif row[5].lower() == 'no':
                print(f'Skipping {row[4]}') 
            else:
                result.append((row[1], row[2], row[3], row[4]))
                line_count += 1
        print(f'Processed {line_count} lines.')
    return result

def getMarkdownFile(URL, content_file_name, file_suffix, directory): # Funkcija, kas iegūst Markdown failu no GitHub repozitorija
    URL = URL.replace('github.com','raw.githubusercontent.com')
    URL = URL + '/' + content_file_name + '.md'
    URL = URL.replace('/tree', '')
    print(f'Getting markdown: {URL}')
    response = requests.get(URL)
    with open(os.path.join(directory, file_suffix+'-'+content_file_name + '.md'), "wb") as file: 
        file.write(response.content)

def markdown_repository_to_turtle(output_dir, csv_spreadsheet):
    # if csv_spreadsheet.startswith("http"):
    #     getGoogleSpreadsheet(csv_spreadsheet, output)
    # else: 
    #     shutil.copy2(csv_spreadsheet, os.path.join(output, "spreadsheet.csv"))
    os.makedirs(output_dir, exist_ok=True)
    results = readCSVfile(csv_spreadsheet)
    outputs = []
    for result in results:
        print(f'result is {result}')
        getMarkdownFile(result[0].strip(), result[1].strip(), result[3].strip(), output_dir)
        # print(f'result[0].strip() = {result[0].strip()}')
        # print(f'result[1].strip() = {result[1].strip()}')
        lang_code = result[1].strip().split('_')[-1]
        # print(f'lang = {lang_code}')
        # print(f'result[2].strip() = {result[2].strip()}')
        # print(f'result[3].strip() = {result[3].strip()}')
        # sys.exit(1)

        md_path = os.path.join(output_dir, result[3] + '-' + result[1].strip() + '.md')
        ttl_path = os.path.join(output_dir, result[3] + '-' + result[1].strip() + '.ttl')
        # print(f'md_path = {md_path}')
        # print(f'ttl_path = {ttl_path}')
        # sys.exit(1)
        markdown_md_to_turtle(md_path, ttl_path, lang_code, result[2].strip() == 'Master')
        outputs.append(ttl_path)
    return outputs


def crawl_markdown_problemdata(problemdata):
    # TODO
    return "spreadsheet.csv"