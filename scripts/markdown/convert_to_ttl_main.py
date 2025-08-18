import mistletoe
import mistletoe.ast_renderer
import requests
import csv
import os
import shutil
from scripts.markdown.mdchunk_reader import markdown_md_to_turtle

def getGoogleSpreadsheet(url_spreadsheet, directory):
    response = requests.get(url_spreadsheet)
    csv_file_name = os.path.join(directory, "spreadsheet.csv")
    with open(csv_file_name, "wb") as file: 
        file.write(response.content)

# Atgriežam sarakstu, kurā ir pārīši row_1, row[3]
def readCSVfile(directory):  # Funkcija, kas lasa CSV failu
    result = []
    with open(os.path.join(directory, "spreadsheet.csv"), 'r',  encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            elif row[5].lower() == 'no':
                print(f'Skipping {row[4]}') 
            else:
                result.append((row[1], row[2], row[4]))
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

def markdown_repository_to_turtle(output, csv_spreadsheet):
    if csv_spreadsheet.startswith("http"):
        getGoogleSpreadsheet(csv_spreadsheet, output)
    else: 
        shutil.copy2(csv_spreadsheet, os.path.join(output, "spreadsheet.csv"))
    results = readCSVfile(output)
    outputs = []
    for result in results:
        getMarkdownFile(result[0].strip(), result[1].strip(), result[2].strip(), output)
        md_path = os.path.join(output, result[2] + '-' + result[1].strip() + '.md')
        ttl_path = os.path.join(output, result[2] + '-' + result[1].strip() + '.ttl')
        markdown_md_to_turtle(md_path, ttl_path)
        outputs.append(ttl_path)
    return outputs


def crawl_markdown_problemdata(problemdata):
    # TODO
    return "spreadsheet.csv"