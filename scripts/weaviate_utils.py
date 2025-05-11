import os
from dotenv import load_dotenv
from rdflib import Graph, URIRef, Namespace, RDF
import weaviate
from weaviate.classes.init import Auth
import weaviate.classes.config as wc
from weaviate.classes.query import MetadataQuery
import sys
import requests
import asyncio
#from weaviate import WeaviateAsyncClient
from weaviate import WeaviateAsyncClient


class WeaviateUtils:
    weaviate_url = "NA"
    weaviate_api_key = "NA"
    openai_api_key = "NA"
    # RDF namespace to find relevant items in Turtle files
    eliozoNS = Namespace("http://www.dudajevagatve.lv/eliozo#")
    # Weaviate client initialized in constructor __init__(...), see below
    client = None
    skipping_mode = False

    def __init__(self, weaviate_url, weaviate_api_key, openai_api_key): 
        self.weaviate_url = weaviate_url
        self.weaviate_api_key = weaviate_api_key
        self.openai_api_key = openai_api_key

        self.client = weaviate.connect_to_weaviate_cloud(
            cluster_url=weaviate_url,
            auth_credentials=Auth.api_key(weaviate_api_key),
            headers={
                "X-OpenAI-Api-Key": openai_api_key
            }
        )

    def close_client(self):
        if self.client is not None: 
            self.client.close()
            self.client = None

    def set_skipping_mode(self, skipping_mode):
        self.skipping_mode = skipping_mode
 
    # Private method to drop a single collection by its name
    def drop_collection(self, collection):
        url = f"{self.weaviate_url}/v1/schema/{collection}"
        headers = {
            "Authorization": f"Bearer {self.weaviate_api_key}"
        }

        try:
            response = requests.delete(url, headers=headers)
            if response.status_code == 200:
                print(f"Successfully deleted collection: {collection}")
            else:
                print(f"Failed to delete collection: {collection}")
                print(f"Status Code: {response.status_code}")
                print(f"Response: {response.text}")

        except requests.exceptions.RequestException as e:
            print(f"Exception in drop_collection(): {str(e)}")

    def drop_collections(self):
        if not self.client.is_ready():
            print("Weaviate client is not ready!")
            sys.exit(1)

        try:
            self.drop_collection("Problem")
            self.drop_collection("Olympiad")
        except Exception as e:
            print(f"Exception in drop_collections(): {e}")
        finally:
            self.client.close()
        return (0, {'keyNN':'drop_collections'})


    # This function attempts to create collections "Olympiad", "Problem", "Classifier"
    # If they already exist, then there are no changes (and a message is printed). 
    def create_schema(self):
        if not self.client.is_ready():
            print("Weaviate client is not ready!")
            sys.exit(1)
        
        try:
            collection_names = self.client.collections.list_all()
            if "Classifier" in collection_names:
                print(f"Collection 'Classifier' already exists; skip creation")
            else:
                print(f"Creating collection 'Classifier'")
                classifiers  = self.client.collections.create(
                    name="Classifier", 
                    properties=[
                        wc.Property(name="property", data_type=wc.DataType.TEXT, skip_vectorization=True), 
                        wc.Property(name="label", data_type=wc.DataType.TEXT, skip_vectorization=True), 
                        wc.Property(name="shortName", data_type=wc.DataType.TEXT), 
                        wc.Property(name="description", data_type=wc.DataType.TEXT)
                    ],
                    # vectorizer_config=wc.Configure.Vectorizer.text2vec_cohere(),
                    vectorizer_config=wc.Configure.Vectorizer.text2vec_openai(),
                    generative_config=wc.Configure.Generative.openai()
                )
                print(classifiers.config.get(simple=False))

        except Exception as e:
            print(f"Exception in create_schema(): {e}")

        try: 
            collection_names = self.client.collections.list_all()
            if "Olympiad" in collection_names:
                print(f"Collection 'Olympiad' already exists; skip creation")
            else:
                olympiads  = self.client.collections.create(
                    name="Olympiad", 
                    properties=[
                        wc.Property(name="olympiadCode", data_type=wc.DataType.TEXT, skip_vectorization=True), 
                        wc.Property(name="olympiadCountry", data_type=wc.DataType.TEXT, skip_vectorization=True), 
                        wc.Property(name="olympiadDescription_en", data_type=wc.DataType.TEXT), 
                        wc.Property(name="olympiadDescription_lt", data_type=wc.DataType.TEXT), 
                        wc.Property(name="olympiadDescription_lv", data_type=wc.DataType.TEXT), 
                        wc.Property(name="olympiadID", data_type=wc.DataType.TEXT, skip_vectorization=True),
                        wc.Property(name="olympiadName_en", data_type=wc.DataType.TEXT),
                        wc.Property(name="olympiadName_lt", data_type=wc.DataType.TEXT),
                        wc.Property(name="olympiadName_lv", data_type=wc.DataType.TEXT)
                    ],
                    # vectorizer_config=wc.Configure.Vectorizer.text2vec_cohere(),
                    vectorizer_config=wc.Configure.Vectorizer.text2vec_openai(),
                    generative_config=wc.Configure.Generative.openai()
                )
                print(olympiads.config.get(simple=False))
        except Exception as e:
            print(f"Exception in create_schema(): {e}")


        try: 
            collection_names = self.client.collections.list_all()
            if "Problem" in collection_names:
                print(f"Collection 'Problem' already exists; skip creation")
            else:
                problems = self.client.collections.create(
                    name="Problem", 
                    properties=[
                        wc.Property(name="problemID", data_type=wc.DataType.TEXT, skip_vectorization=True), 
                        wc.Property(name="problemGrade", data_type=wc.DataType.INT, skip_vectorization=True), 
                        wc.Property(name="problemText_lv", data_type=wc.DataType.TEXT), 
                        wc.Property(name="solutionText_lv", data_type=wc.DataType.TEXT), 
                        wc.Property(name="olympiadType", data_type=wc.DataType.TEXT, skip_vectorization=True), 
                        wc.Property(name="problemYear", data_type=wc.DataType.INT, skip_vectorization=True)
                    ],
                    # vectorizer_config=wc.Configure.Vectorizer.text2vec_cohere(),
                    vectorizer_config=wc.Configure.Vectorizer.text2vec_openai(),
                    generative_config=wc.Configure.Generative.openai()
                )
                print(problems.config.get(simple=False))

        except Exception as e:
            print(f"Exception in create_schema(): {e}")
        finally:
            self.client.close()
        return (0, {'keyNN':'create_schema'})



    def ingest_to_weaviate(self, filename):
        print(f'Importing {filename} to  Weaviate')
        graph = Graph()
        graph.parse(filename, format="ttl")

        if not self.client.is_ready():
            print('Weaviate client is not ready!')
            sys.exit(1)


        problemCount = 0
        for subj in graph.subjects(predicate=RDF.type, 
                                    object=self.eliozoNS.Problem):

            problemID = "NA"
            olympiadType = "NA"
            problemGrade = 0
            problemYear = 0

            try:
                val = graph.value(subj, self.eliozoNS.problemID)
                problemID = str(val)
            except Exception as e:
                print(f"Error converting problemID={val} for {problemCount}; skipping insert")
                continue
            problemCount += 1
            print(f'Ingesting {problemID}...')
            # Extract properties that don't require language specification


            try:
                val = graph.value(subj, self.eliozoNS.olympiadType)
                olympiadType = str(val)
            except Exception as e:
                print(f"Error converting olympiadType={val} for {problemCount}; skipping insert")
                continue


            try: 
                val = graph.value(subj, self.eliozoNS.problemGrade)
                problemGrade = int(val)
            except Exception as e:
                print(f"Error converting problemGrade={val} for {problemCount}; skipping insert")
                continue

            try: 
                val = graph.value(subj, self.eliozoNS.problemYear)
                problemYear = int(val)
            except Exception as e:
                print(f"Error converting problemYear={val} for {problemCount}; skipping insert")
                continue



            # Initialize the data object with non-language properties
            data_object = {
                "problemID": problemID,
                "problemGrade": problemGrade, 
                "olympiadType": olympiadType, 
                "problemYear": problemYear
            }
            # print(f'data_object = {data_object}')


            for lang in ['lv']:
                for obj in graph.objects(subj, self.eliozoNS.problemText):
                    if obj.language == lang:
                        data_object[f"problemText_{lang}"] = str(obj)

                for solution_obj in graph.objects(subj, self.eliozoNS.problemSolution): 
                    for solution_text in graph.objects(solution_obj, self.eliozoNS.solutionText):
                        if solution_text.language == lang:
                            if f"solutionText_{lang}" in data_object:
                                data_object[f"solutionText_{lang}"] = data_object[f"solutionText_{lang}"] + '\n\n' + str(solution_text)
                            else:
                                data_object[f"solutionText_{lang}"] = str(solution_text)
                
            if not self.skipping_mode:
                olympiads_collection = self.client.collections.get("Problem")

                olympiads_collection.data.insert(
                    properties=data_object,
                    references={}
                )
        return (0, {'keyMM':'ingest_to_weaviate'})
    

    # def create_classifier_schema(self):
    #     if not self.client.is_ready():
    #         print("Weaviate client is not ready!")
    #         sys.exit(1)
        

        
    #     try:
    #         collection_names = self.client.collections.list_all()
    #         if "Classifier" in collection_names:
    #             print(f"Collection 'Classifier' exists; skip schema creation")
    #         else:
    #             print(f"Creating collection 'Classifier'")
    #             classifiers  = self.client.collections.create(
    #                 name="Classifier", 
    #                 properties=[
    #                     wc.Property(name="property", data_type=wc.DataType.TEXT, skip_vectorization=True), 
    #                     wc.Property(name="label", data_type=wc.DataType.TEXT, skip_vectorization=True), 
    #                     wc.Property(name="shortName", data_type=wc.DataType.TEXT), 
    #                     wc.Property(name="description", data_type=wc.DataType.TEXT)
    #                 ],
    #                 # vectorizer_config=wc.Configure.Vectorizer.text2vec_cohere(),
    #                 vectorizer_config=wc.Configure.Vectorizer.text2vec_openai(),
    #                 generative_config=wc.Configure.Generative.openai()
    #             )
    #             print(classifiers.config.get(simple=False))

    #     except Exception as e:
    #         print(f"Exception in create_schema(): {e}")
    #     finally:
    #         self.client.close()
    #     return (0, {'keyNN':'create_schema'})



    # Currently only imports property=topic
    def ingest_classifier_data(self, property, filename):
        print(f'Importing classifier {property} to Weaviate')
        graph = Graph()
        graph.parse(filename, format="ttl")

        if not self.client.is_ready():
            print('Weaviate client is not ready!')
            sys.exit(1)

        print(f"Found triples: {len(graph)}")
        itemCount = 0
        # for subj, obj in graph.subject_objects(predicate=RDF.type):
        #     print(f"Subject: {subj}, RDF.type: {obj}")
        #     itemCount += 1

        # print(f"Total items with RDF.type: {itemCount}")






        for subj in graph.subjects(predicate=RDF.type, 
                                    object=self.eliozoNS.Topic):
            
            topicNumber = "X.X.X.X.X"
            try:
                val = graph.value(subj, self.eliozoNS.topicNumber)
                topicNumber = str(val)
            except Exception as e:
                print(f"Error converting problemID={val} for {itemCount}; skipping insert")
                continue
            if topicNumber.endswith(".0.0.0.0"):
                print(f"skipping {topicNumber}")
                continue
            
            if (topicNumber.startswith("2.") or topicNumber.startswith("4.")) and topicNumber.endswith(".0.0.0"): 
                print(f"skipping {topicNumber}")
                continue

            if (topicNumber.startswith("1.") or topicNumber.startswith("3.")) and not topicNumber.endswith(".0.0.0"): 
                print(f"skipping {topicNumber}")
                continue

            if not topicNumber.endswith("0.0"):
                print(f"skipping {topicNumber}")
                continue



            label = "NA"
            shortName = "NA"
            description = "NA"

            try:
                val = graph.value(subj, self.eliozoNS.topicID)
                label = str(val)
                val = graph.value(subj, self.eliozoNS.topicName)
                shortName = str(val)
                val = graph.value(subj, self.eliozoNS.topicDescription)
                description = str(val)
            except Exception as e:
                print(f"Error converting problemID={val} for {itemCount}; skipping insert")
                continue
            itemCount += 1
            print(f'Ingesting {itemCount}...')
            # Extract properties that don't require language specification


            # Initialize the data object with non-language properties
            data_object = {
                "property": property,
                "label": label, 
                "shortName": shortName, 
                "description": description
            }
            #print(f'data_object = {data_object}')

            classifiers_collection = self.client.collections.get("Classifier")

            classifiers_collection.data.insert(
                properties=data_object,
                references={}
            )
        self.client.close()
        return (0, {'keyMM':'ingest_to_weaviate'})
    


    # Private method called by "find_problems"
    def near_search(self, collection, myquery, mylimit): 
        problems = self.client.collections.get(collection)
        print(f'Searching query "{myquery}" with limit "{mylimit}"')
        response = problems.query.near_text(
            query=myquery,
            limit=mylimit,
            return_metadata=MetadataQuery(distance=True), 
        )
        result = []
        for o in response.objects:
            result.append(o.properties)
        self.client.close()
        return result
        
    # async def near_search(self, collection, myquery, mylimit):
    #     async_client = WeaviateAsyncClient(
    #         cluster_url=self.weaviate_url, 
    #         auth_credentials=self.weaviate_api_key,
    #     )
    #     topics = await async_client.collections.get(collection)
    #     print(f'Searching query "{myquery}" with limit "{mylimit}"')
    #     try:
    #         response = await topics.query.near_text(
    #             query=myquery,
    #             limit=mylimit,
    #             return_metadata=MetadataQuery(distance=True),
    #         )
    #     except Exception as e:
    #         print(f"Query failed: {e}")
    #         return []
    #     finally:
    #        async_client.close()

    #     result = [o.properties for o in response.objects]
    #     return result


    def get_problems(self, query, mylimit):
        if not self.client.is_ready():
            print("Weaviate client is not ready!")
            sys.exit(1)
        results = []
        try:
            results = self.near_search("Problems", query, mylimit)
        except Exception as e:
            print(f"{e.message}")
        finally:
            self.client.close()
        return (0, {'problems':results})



