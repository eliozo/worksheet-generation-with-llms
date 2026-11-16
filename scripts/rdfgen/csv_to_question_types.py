"""Convert the question type vocabulary (questionTypes2.csv) to Turtle.

Rows on the QuestionType axis (QTY_...) become eliozo:Question resources, rows on
the ResponseFormat axis (RSP_...) eliozo:ResponseFormat resources, e.g.

    eliozo:QTY_FindAll a eliozo:Question ;
        eliozo:questionID "QTY_FindAll" ;
        eliozo:questionNumber "1.1" ;
        eliozo:sorter_L1 1 ; eliozo:sorter_L2 1 ;
        eliozo:questionName "Atrast visus atrisinājumus"@lv, "Find All Solutions"@en ;
        eliozo:questionCanonical "Atrodi visus …"@lv, "Find all …"@en ;
        eliozo:questionOtherForms ..., eliozo:questionRequiredParts ...,
        eliozo:questionDescription ... ;
        skos:prefLabel "QTY_FindAll" ;
        skos:broader eliozo:QTY_Find ;
        skos:related eliozo:QTY_FindValue .

(ResponseFormat resources have the same properties named responseFormat...).
The source can be a local CSV file or a published Google Sheets CSV URL.
"""

import csv
import io

import rdflib
import requests
from rdflib import Literal, Namespace, RDF, SKOS, XSD

ELIOZO = Namespace("http://www.dudajevagatve.lv/eliozo#")

# Axis column value -> (RDF class, property name prefix)
AXES = {
    'QuestionType': ('Question', 'question'),
    'ResponseFormat': ('ResponseFormat', 'responseFormat'),
}

# Property suffix -> CSV column prefix; each column exists as ...Lv and ...En
LANGUAGE_COLUMNS = {
    'Name': 'Title',
    'Canonical': 'Question',
    'OtherForms': 'OtherQuestions',
    'RequiredParts': 'RequiredParts',
    'Description': 'Description',
}


def read_rows(source):
    if source.startswith(('http://', 'https://')):
        response = requests.get(source, timeout=30)
        response.raise_for_status()
        text = response.content.decode('utf-8')
    else:
        with open(source, encoding='utf-8') as f:
            text = f.read()
    return list(csv.DictReader(io.StringIO(text)))


def question_types_graph(rows):
    g = rdflib.Graph()
    g.bind('eliozo', ELIOZO)
    g.bind('skos', SKOS)
    groups = {(r['Axis'], r['L1'].strip()): r['Label'].strip() for r in rows if r['L2'].strip() == '0'}

    for row in rows:
        if row.get('Axis') not in AXES or not row['Label'].strip():
            continue
        cls, prefix = AXES[row['Axis']]
        label = row['Label'].strip()
        l1, l2 = int(row['L1']), int(row['L2'])
        node = ELIOZO[label]
        g.add((node, RDF.type, ELIOZO[cls]))
        g.add((node, ELIOZO[prefix + 'ID'], Literal(label)))
        g.add((node, ELIOZO[prefix + 'Number'], Literal(f'{l1}.{l2}')))
        g.add((node, ELIOZO.sorter_L1, Literal(l1, datatype=XSD.integer)))
        g.add((node, ELIOZO.sorter_L2, Literal(l2, datatype=XSD.integer)))
        g.add((node, SKOS.prefLabel, Literal(label)))
        for suffix, column in LANGUAGE_COLUMNS.items():
            for lang in ('Lv', 'En'):
                value = (row.get(column + lang) or '').strip()
                if value:
                    g.add((node, ELIOZO[prefix + suffix], Literal(value, lang=lang.lower())))
        if l2 != 0 and (row['Axis'], str(l1)) in groups:
            parent = ELIOZO[groups[(row['Axis'], str(l1))]]
            g.add((node, SKOS.broader, parent))
            g.add((parent, SKOS.narrower, node))
        for related in (row.get('SeeAlso') or '').split(';'):
            if related.strip():
                g.add((node, SKOS.related, ELIOZO[related.strip()]))
    return g


class CsvToQuestionTypes:
    def __init__(self, source):
        self.source = source

    def export_to_turtle(self, output):
        question_types_graph(read_rows(self.source)).serialize(destination=output)
