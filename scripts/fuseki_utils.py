import requests
from requests.auth import HTTPBasicAuth
import json

class FusekiUtils:
    fuseki_url = "NA"
    fuseki_user = "NA"
    fuseki_password = "NA"

    def __init__(self, FUSEKI_URL, FUSEKI_USER, FUSEKI_PASSWORD):
        self.fuseki_url = FUSEKI_URL
        self.fuseki_user = FUSEKI_USER
        self.fuseki_password = FUSEKI_PASSWORD

    def drop_all(self, dataset_name):
        url = f"{self.fuseki_url}/$/datasets/{dataset_name}"

        response = requests.delete(url, auth=HTTPBasicAuth(self.fuseki_user, self.fuseki_password))

        if response.status_code == 200:
            print(f"Dataset '{dataset_name}' successfully deleted.")
        else:
            print(f"Failed to delete dataset '{dataset_name}'. Status code: {response.status_code}")
            print(response.text)


    def create_dataset(self, dataset_name): 
        url = f"{self.fuseki_url}/$/datasets"
        payload = {
            "dbName": dataset_name,
            "dbType": "tdb",  # Using TDB for persistent storage
        }
        response = requests.post(url, data=payload, auth=HTTPBasicAuth(self.fuseki_user, self.fuseki_password))
        if response.status_code in [200, 201]:
            print(f"Dataset '{dataset_name}' successfully created.")
        else:
            print(f"Failed to create dataset '{dataset_name}'. Status code: {response.status_code}")
            print(response.text)

    def ingest_data(self, dataset_name, turtle_path): 
        url = f"{self.fuseki_url}/{dataset_name}/data"

        with open(turtle_path, 'rb') as file:
            headers = {
                "Content-Type": "text/turtle"
            }
            response = requests.post(url, headers=headers, data=file, auth=HTTPBasicAuth(self.fuseki_user, self.fuseki_password))

        if response.status_code in [200, 201]:
            print(f"Data '{turtle_path}' successfully uploaded to dataset '{dataset_name}'.")
        else:
            print(f"Failed to upload data to dataset '{dataset_name}'. Status code: {response.status_code}")
            print(response.text)


    def build_filtering_query(self, filters): 

        prefixes = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
        """
        
        select_clause = "SELECT ?problemid ?text WHERE {"
        where_clauses = []
        
        # Base clauses
        where_clauses.append("?problem eliozo:problemID ?problemid ;")
        where_clauses.append("eliozo:problemText ?text ;")
        
        # Add filters based on initialized lists
        if "grade" in filters and filters["grade"] != []:
            grades = " ".join(str(grade) for grade in filters["grade"])
            where_clauses.append(f"eliozo:suggestedGrade {grades} ;")
        
        if "domain" in filters and filters["domain"] != []:
            domains = " ".join(f'"{domain}"' for domain in filters["domain"])
            where_clauses.append(f"eliozo:domain {domains} ;")
        
        if "method" in filters and filters["method"] != []:
            method = filters["method"][0]
            where_clauses.append("eliozo:method ?mymethod ;")
            where_clauses.append(f"?mymethod skos:broader* eliozo:{method} .")
        
        # Construct the query
        query = f"{prefixes}\n{select_clause}\n" + "\n".join(where_clauses) + "\n}"
        
        return query


    def execute_query(self, dataset, query): 
        url = f"{self.fuseki_url}/{dataset}/query"
        headers = {
            "Accept": "application/sparql-results+json"
        }
        
        response = requests.post(
            url,
            headers=headers,
            data={'query': query},
            auth=HTTPBasicAuth(self.fuseki_user, self.fuseki_password)
        )
        
        if response.status_code == 200:
            results = response.json()
            return results
            # problems = []
            # for result in results["results"]["bindings"]:
            #     problems.append({
            #         "problemID": result['problemid']['value'],
            #         "text": result['text']['value']
            #     })
            # return (0,{"problems": problems})
        else:
            print(f"Failed to execute query. Status code: {response.status_code}")
            print(response.text)
            return None


    def save_query(self, dataset, query, file_name, openai_key):
        json_input = self.execute_query(dataset, query)[1]
        problems = json_input["problems"]
        snippets = []
        for problem in problems:
            item = {"type": "problem", "value": f"{problem['problemID']}. {problem['text']}"}
            # item = {"type": "problem", "value": problem['text']}
            snippets.append(item)
        json_output = {"snippets": snippets}
        # json_string = json.dumps(json_output, indent=4)
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(json_output, file, indent=4)

