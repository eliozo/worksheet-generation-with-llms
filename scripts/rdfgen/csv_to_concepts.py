from rdflib import Graph, Namespace, URIRef, Literal, RDF
import csv
import rdflib
import requests
import copy as cp

eliozo_ns = "http://www.dudajevagatve.lv/eliozo#"
RDF_NS = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
SKOS = "http://www.w3.org/2004/02/skos/core#"


# def getGoogleSpreadsheet(fname):  # Funkcija, kas iegūst Google Spreadsheet dokumentu ar olimpiāžu uzdevumu datiem
#     URL_GOOGLE_SPREADSHEET = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSsIUjRXRU6L_MGgEmgUZlfwvygclZun964ilvH-l6F3TZ9w0I2MDce9VXqJgd4p2GZxF7vJ6OY5jcT/pub?output=csv'
#     response = requests.get(URL_GOOGLE_SPREADSHEET)
#     open(fname, "wb").write(response.content)


def getGoogleSpreadsheet(URL, outpath):
    response = requests.get(URL)
    with open(outpath, "wb") as file: 
        file.write(response.content)


# skillDescription ir string mainīgais, kurā glabājas RDF objekta vērtība
def addToRdfGraph(g, conceptID, termLV, descLV, termEN=None):
    rdf_type_property = rdflib.URIRef(RDF_NS + 'type')
    topic_node = rdflib.URIRef(eliozo_ns + "TRM-" + conceptID)
    g.add((topic_node, rdf_type_property, rdflib.URIRef(eliozo_ns + "Concept")))
    if not termEN:
        termEN = conceptID.replace("-", " ")
    termEN_property = rdflib.URIRef(eliozo_ns + 'termEN')
    termLV_property = rdflib.URIRef(eliozo_ns + 'termLV')
    descLV_property = rdflib.URIRef(eliozo_ns + 'descLV')
    conceptID_property = rdflib.URIRef(eliozo_ns + 'conceptID')
    g.add((topic_node, termEN_property, rdflib.term.Literal(termEN, lang=u'en')))
    g.add((topic_node, termLV_property, rdflib.term.Literal(termLV, lang=u'lv')))
    g.add((topic_node, conceptID_property, rdflib.term.Literal(conceptID, lang=u'en')))
    if descLV and descLV != "" and descLV != "NA":
        g.add((topic_node, descLV_property, rdflib.term.Literal(descLV, lang=u'lv')))


def resolveColumns(header):
    """Return (id_col, termLV_col, descLV_col, termEN_col) for this sheet.

    The original sheet was a bare "en,lv,skaidrojums" triple. The current one
    is a full metadata tab (L1,L2,Label,TitleLv,TitleEn,DescriptionLv,...), so
    resolve the columns by header name and fall back to the old fixed layout.
    """
    by_name = {name.strip(): i for i, name in enumerate(header)}
    if 'Label' not in by_name:
        return 0, 1, 2, None
    return (by_name['Label'],
            by_name.get('TitleLv', by_name.get('lv', 1)),
            by_name.get('DescriptionLv', 2),
            by_name.get('TitleEn'))


def produceCSVtoRDF(in_file, out_file):
    g = rdflib.Graph()
    g.bind("skos", SKOS)
    g.bind("eliozo", eliozo_ns)
    with open(in_file, 'r', encoding='utf-8') as csv_file:
        csv_data = list(csv.reader(csv_file, delimiter=','))

    if not csv_data:
        print(f'WARNING: {in_file} is empty')
        return

    id_col, termLV_col, descLV_col, termEN_col = resolveColumns(csv_data[0])

    for line_count, row in enumerate(csv_data, start=1):
        if line_count == 1:
            # skip header
            continue
        if len(row) <= descLV_col or row[id_col] == '':
            print(f'WARNING: empty concept on line {line_count}')
            continue
        termEN = row[termEN_col] if termEN_col is not None and len(row) > termEN_col else None
        addToRdfGraph(g, row[id_col], row[termLV_col], row[descLV_col], termEN)
    g.serialize(destination=out_file)

# if __name__ == '__main__':
#     fname = "resources/spreadsheet_concepts.csv"
#     getGoogleSpreadsheet(fname)
#     produceCSVtoRDF(in_file=fname, out_file="resources/concepts.ttl")

class CsvToConcepts: 
    url = "NA"

    def __init__(self, url):
        self.url = url
    
    def export_to_turtle(self, output):
        idx = output.rfind(".")
        file_no_extension = output[0:idx] if idx > 0 else output
        csv_file_name = f"{file_no_extension}.csv"
        getGoogleSpreadsheet(self.url, csv_file_name)
        produceCSVtoRDF(csv_file_name, output)

