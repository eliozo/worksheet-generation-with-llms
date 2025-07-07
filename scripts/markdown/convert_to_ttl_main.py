import mistletoe
import mistletoe.ast_renderer
import requests
import csv
from mdchunk_reader import markdown_md_to_turtle

def getGoogleSpreadsheet(URL_GOOGLE_SPREADSHEET):
    response = requests.get(URL_GOOGLE_SPREADSHEET)
    open("resources/spreadsheet.csv", "wb").write(response.content)

# Atgriežam sarakstu, kurā ir pārīši row_1, row[3]
def readCSVfile():  # Funkcija, kas lasa CSV failu
    result = []
    with open('resources/spreadsheet.csv', 'r',  encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            elif row[5].lower() != 'no':
                print(f'Skipping {row[4]}') 
            else:
                result.append((row[1], row[2], row[4]))
                line_count += 1
        print(f'Processed {line_count} lines.')
    return result

def getMarkdownFile(URL, content_file_name, file_suffix): # Funkcija, kas iegūst Markdown failu no GitHub repozitorija
    # print(f'URL = {URL}')
    URL = URL.replace('github.com','raw.githubusercontent.com')
    URL = URL + '/' + content_file_name + '.md'
    URL = URL.replace('/tree', '')
    print(f'Getting markdown: {URL}')
    response = requests.get(URL)
    open('resources/'+file_suffix+'-'+content_file_name + '.md', "wb").write(response.content)


def markdown_repository_to_turtle(URL, directory):
    if URL == '': 
        URL = URL_GOOGLE_SPREADSHEET = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vT1Il_-qJURh8sZHRN1oJSwok4kRUjcA7VCOhDfg1PnTUC14k4skRRl3NrUDEbd1vELQq_ALwEU9Ltx/pub?output=csv'
    getGoogleSpreadsheet(URL_GOOGLE_SPREADSHEET)
    results = readCSVfile()
    for result in results:
        # print("****{}, {}, {}".format(result[0], result[1], result[2]))
        getMarkdownFile(result[0].strip(), result[1].strip(), result[2].strip())
        md_path = 'resources/' + result[2] + '-' + result[1].strip() + '.md'
        ttl_path = 'resources/' + result[2] + '-' + result[1].strip() + '.ttl'

        markdown_md_to_turtle(md_path, ttl_path)

