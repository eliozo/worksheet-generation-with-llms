# https://docs.google.com/spreadsheets/d/e/2PACX-1vT1Cbs-66PXXr45JreveYV5pa3rojZO1MNWn9Fce_P3ggNtXBOjFKFYym41tM3bGQ1fhUnin0g5_ihs/pub?gid=0&single=true&output=csv

from rdflib import Graph, Namespace, URIRef, Literal, RDF
import csv
import rdflib
import requests
import copy as cp


RDF_NS = 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'
RDFS_NS = 'http://www.w3.org/2000/01/rdf-schema#'
OWL_NS = 'http://www.w3.org/2002/07/owl#'
XSD_NS = 'http://www.w3.org/2001/XMLSchema#'

SKOS = 'http://www.w3.org/2004/02/skos/core#'
ELIOZO_NS = 'http://www.dudajevagatve.lv/eliozo#'


def getGoogleSpreadsheet(url_spreadsheet, csv_file_name):
    response = requests.get(url_spreadsheet)
    with open(csv_file_name, "wb") as file: 
        file.write(response.content)

def add_new_resource(g, ID, EliozoType):
    problem_node = rdflib.URIRef(ELIOZO_NS + ID)
    problem_rdf_property = rdflib.URIRef(RDF_NS + 'type')
    g.add((problem_node, problem_rdf_property, rdflib.URIRef(OWL_NS + 'NamedIndividual')))
    g.add((problem_node, problem_rdf_property, rdflib.URIRef(ELIOZO_NS + EliozoType)))
    return problem_node


def add_literal_prop(g, problem_node, key, value, lang):
    problem_property = rdflib.URIRef(ELIOZO_NS + key)
    if lang == '':
        g.add((problem_node, problem_property, rdflib.term.Literal(value)))
    else:
        g.add((problem_node, problem_property, rdflib.term.Literal(value, lang=lang)))


def produceCSVtoRDF(in_file, out_file, class_name):

    g = rdflib.Graph()
    g.bind("eliozo", ELIOZO_NS)

    properties = dict()
    properties['olympiads'] = {
        'cname': ('Olympiad', ''),
        'cnameID': ('OlympiadID', ''),  
        'olympiadCountry': ('olympiadCountry', ''),
        'olympiadCode': ('olympiadCode', ''),
        'olympiadDescriptionEn': ('olympiadDescription', 'en'),
        'olympiadDescriptionLt': ('olympiadDescription', 'lt'),
        'olympiadDescriptionLv': ('olympiadDescription', 'lv'),
        'olympiadNameEn': ('olympiadName', 'en'),
        'olympiadNameLt': ('olympiadName', 'lt'),
        'olympiadNameLv': ('olympiadName', 'lv')
    }
    properties['sources'] = {
        'cname': ('Source', ''),
        'cnameID': ('SourceID', ''),
        'url': ('sourceUrl', ''),
        'label': ('sourceLabel', ''),
        'sourceNameEn': ('sourceName', 'en'),
        'sourceNameLt': ('sourceName', 'lt'),
        'sourceNameLv': ('sourceName', 'lv'),
        'sourceDescriptionEn': ('sourceDescription', 'en'),
        'sourceDescriptionLt': ('sourceDescription', 'lt'),
        'sourceDescriptionLv': ('sourceDescription', 'lv')
    }

    line_count = 0
    current_resource = ''
    current_node = None
    with open(in_file, 'r',  encoding='utf-8') as csv_file:
        csv_lines = list(csv.reader(csv_file, delimiter=','))
        
    for row in csv_lines:
        resource = row[0]
        IDs = resource.split(':')
        if len(IDs) != 2:
            continue
        ID = IDs[1]
        if resource != current_resource:
            current_resource = resource
            current_node = add_new_resource(g, ID, properties[class_name]['cname'][0])
            add_literal_prop(g, current_node, properties[class_name]['cnameID'][0], ID, '')
        key = row[1]
        val = row[2]
        (prop, lang) = properties[class_name][key]
        add_literal_prop(g, current_node, prop, val, lang)

    g.serialize(destination=out_file)


class CsvToTable: 
    url = "NA"
    class_name = 'NA'

    def __init__(self, url, class_name):
        self.url = url
        self.class_name = class_name
    
    def export_to_turtle(self, output):
        idx = output.rfind(".")
        file_no_extension = output[0:idx] if idx > 0 else output
        csv_file_name = f"{file_no_extension}.csv"
        getGoogleSpreadsheet(self.url, csv_file_name)
        produceCSVtoRDF(csv_file_name, output, self.class_name)