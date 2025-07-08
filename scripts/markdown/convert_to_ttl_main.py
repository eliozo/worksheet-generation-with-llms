import mistletoe
import mistletoe.ast_renderer
import requests
import csv
import os
from scripts.markdown.mdchunk_reader import markdown_md_to_turtle

def getGoogleSpreadsheet(URL_GOOGLE_SPREADSHEET, directory):
    response = requests.get(URL_GOOGLE_SPREADSHEET)
    open(os.path.join(directory, "spreadsheet.csv"), "wb").write(response.content)

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
    # print(f'URL = {URL}')
    URL = URL.replace('github.com','raw.githubusercontent.com')
    URL = URL + '/' + content_file_name + '.md'
    URL = URL.replace('/tree', '')
    print(f'Getting markdown: {URL}')
    response = requests.get(URL)
    open(os.path.join(directory, file_suffix+'-'+content_file_name + '.md'), "wb").write(response.content)


def markdown_repository_to_turtle(URL_GOOGLE_SPREADSHEET, directory):
    if URL_GOOGLE_SPREADSHEET == '': 
        URL_GOOGLE_SPREADSHEET = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vT1Il_-qJURh8sZHRN1oJSwok4kRUjcA7VCOhDfg1PnTUC14k4skRRl3NrUDEbd1vELQq_ALwEU9Ltx/pub?output=csv'
    getGoogleSpreadsheet(URL_GOOGLE_SPREADSHEET, directory)
    results = readCSVfile(directory)
    for result in results:
        # print("****{}, {}, {}".format(result[0], result[1], result[2]))
        getMarkdownFile(result[0].strip(), result[1].strip(), result[2].strip(), directory)
        md_path = os.path.join(directory, result[2] + '-' + result[1].strip() + '.md')
        ttl_path = os.path.join(directory, result[2] + '-' + result[1].strip() + '.ttl')

        markdown_md_to_turtle(md_path, ttl_path)

