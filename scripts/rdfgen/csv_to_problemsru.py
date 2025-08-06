# https://docs.google.com/spreadsheets/d/e/2PACX-1vT1Cbs-66PXXr45JreveYV5pa3rojZO1MNWn9Fce_P3ggNtXBOjFKFYym41tM3bGQ1fhUnin0g5_ihs/pub?gid=0&single=true&output=csv

from rdflib import Graph, Namespace, URIRef, Literal, RDF
import csv
import rdflib
import requests
import copy as cp

eliozo_ns = "http://www.dudajevagatve.lv/eliozo#"

RDF_NS = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
SKOS = "http://www.w3.org/2004/02/skos/core#"

def getGoogleSpreadsheet(URL_GOOGLE_SPREADSHEET, csv_file):
    if (not URL_GOOGLE_SPREADSHEET):
        # Use default URL
        URL_GOOGLE_SPREADSHEET = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vT1Cbs-66PXXr45JreveYV5pa3rojZO1MNWn9Fce_P3ggNtXBOjFKFYym41tM3bGQ1fhUnin0g5_ihs/pub?gid=0&single=true&output=csv'
    response = requests.get(URL_GOOGLE_SPREADSHEET)
    open(csv_file, "wb").write(response.content)

def readCSVfile(in_file, topicDictionary, depthDictionary, allIDs, allAttributes):
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    line_count = 0
    with open(in_file, 'r',  encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            line_count += 1
            if line_count == 1:
                continue
            elif row[0] == '':
                print(f'WARNING: empty topicID in line {line_count}')
                continue
            else:
                topicID = row[0]
                parentTopicId = row[1]
                # parentDepth = int(row[1])
                siblingNum = int(row[2])
                myTitle = row[3].strip()
                myDescription = row[4].strip()
                myURL = row[6].strip()
                if topicID in topicDictionary: 
                    print(f'ERROR: topicID not unique on line {line_count}')
                else:
                    topicDictionary[topicID] = []
                if not parentTopicId in topicDictionary: 
                    print(f'ERROR: parent undefined on line {line_count}')
                
                print(f"len(topicDictionary)={len(topicDictionary)}")
                topicDictionary[parentTopicId].append(topicID)
                if siblingNum != len(topicDictionary[parentTopicId]): 
                    expectedSiblingNum = len(topicDictionary[parentTopicId])
                    print(f'WARNING: wrong sibling number {siblingNum} (expected {expectedSiblingNum}) on line {line_count}')
                depthDictionary[topicID] = cp.copy(depthDictionary[parentTopicId])
                depthDictionary[topicID].append(letters[siblingNum-1])
                tempValue = depthDictionary[topicID]
                # print(f'depthDictionary[{topicID}] = {tempValue}')
                # if parentDepth != len(depthDictionary[topicID]) - 1: 
                #     print(f'WARNING: wrong depth on line {line_count}')
                sortingLabel = ".".join(depthDictionary[topicID])
                allIDs[sortingLabel] = topicID
                allAttributes[topicID] = {'parentID': parentTopicId, 'title': myTitle, 'descr': myDescription, 'url': myURL}

    print(f'line_count = {line_count}')

# topicDescription ir string mainīgais, kurā glabājas RDF objekta vērtība
def addToRdfGraph(g, topicID, sorter, topicTitle, topicDescription, topicUrl, parentTopicID):
    global eliozo_ns
    topic_node = rdflib.URIRef(eliozo_ns+topicID) # RDF subjekts
    topic_id_property = rdflib.URIRef(eliozo_ns+'topicID') # 'proofsByEstimateAndExample'
    topic_sorter_property = rdflib.URIRef(eliozo_ns+'sorter') # 'G.L'
    topic_description_property = rdflib.URIRef(eliozo_ns+'topicDescription') # Fiksēts URL, kas apraksta RDF predikātu
    topic_title_property = rdflib.URIRef(eliozo_ns+'topicTitle') # ''
    topic_url_property = rdflib.URIRef(SKOS+'topicUrl')
    topic_rdf_type_property = rdflib.URIRef(RDF_NS+'type')
    topic_broader_property = rdflib.URIRef(SKOS+'broader')
    topic_narrower_property = rdflib.URIRef(SKOS+'narrower')

    g.add((topic_node, topic_id_property, rdflib.term.Literal(topicID)))
    g.add((topic_node, topic_sorter_property, rdflib.term.Literal(sorter)))
    g.add((topic_node, topic_title_property, rdflib.term.Literal(topicTitle)))
    g.add((topic_node, topic_description_property, rdflib.term.Literal(topicDescription)))
    g.add((topic_node, topic_rdf_type_property, rdflib.URIRef(eliozo_ns+"Topic")))
    g.add((topic_node, topic_url_property, rdflib.term.Literal(topicUrl)))
    if parentTopicID != '' and parentTopicID != 'TOP':
        parent_topic_node = rdflib.URIRef(eliozo_ns+parentTopicID)
        g.add((topic_node, topic_broader_property, parent_topic_node)) # bērns iedur vecākam
        g.add((parent_topic_node, topic_narrower_property, topic_node)) # vecāks iedur bērnam
    

def produceCSVtoRDF(in_file, out_file): # Pārveido CSV failu par RDF failu

    global SKOS

    g = rdflib.Graph()

    g.bind("skos", SKOS)
    g.bind("eliozo", eliozo_ns)

    # Atver JSON failu
    # f = open(in_file)

    topicDictionary = dict()
    topicDictionary['TOP'] = []

    depthDictionary = dict()
    depthDictionary['TOP'] = []

    allIDs = dict()

    allAttributes = dict()
    readCSVfile(in_file, topicDictionary, depthDictionary, allIDs, allAttributes)

    allSortingLabels = list(allIDs.keys())
    allSortingLabels.sort()
    for kk in allSortingLabels:
        topicID = allIDs[kk]
        
        parentTopicID = allAttributes[topicID]['parentID']
        title = allAttributes[topicID]['title']
        description = allAttributes[topicID]['descr']
        url = allAttributes[topicID]['url']
        addToRdfGraph(g, topicID, kk, title, description, url, parentTopicID)

    g.serialize(destination=out_file)


class CsvToTopics:
    url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vT1Cbs-66PXXr45JreveYV5pa3rojZO1MNWn9Fce_P3ggNtXBOjFKFYym41tM3bGQ1fhUnin0g5_ihs/pub?gid=0&single=true&output=csv'
    
    def __init__(self, csv_url):
        self.url = csv_url

    def export_to_turtle(self, output):
        # Replace "ttl" with "csv" extension:
        idx = output.rfind(".")
        file_no_extension = output[0:idx] if idx > 0 else output
        csv_file = f"{file_no_extension}.csv"
        getGoogleSpreadsheet(self.url, csv_file)
        produceCSVtoRDF(csv_file, output)

# if __name__ == '__main__':
#     getGoogleSpreadsheet() # Izsauc funkciju, kas iegūst skos dokumentu CSV faila formātā
#     produceCSVtoRDF(in_file="resources/spreadsheet_topics.csv", out_file="resources/topics.ttl")

