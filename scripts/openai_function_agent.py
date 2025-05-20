import os
import json
import uuid
import openai

import pprint
from scripts.weaviate_utils import WeaviateUtils
from scripts.fuseki_utils import FusekiUtils

# This class implements "get-problems" for EliozoClient
# This is an integrated function. 
class OpenaiFunctionAgent:
    openai_api_key = "NA"
    weaviate_url = "NA"
    weaviate_api_key = "NA"
    gpt_model = "gpt-4.1"
    #task_data = ""
    topic_list = []

    function_specs2 = [
        {
            "type": "function",
            "function": {
                "name": "list_subtopics",
                "description": "Find subtopics (labels, names and descriptions) of the given topic.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "parent_label": { "type": "string", "description": "A label for the topic or a math domain ('Alg', 'Comb', 'Geom', 'NT')" }
                    },
                    "required": ["parent_label"]
                }
            }
        },
    ]

    function_specs = [
        {
            "type": "function",
            "function": {
                "name": "find_topics",
                "description": "Find problem topics that best match a user-provided query."
                # "parameters": {
                #     "type": "object",
                #     "properties": {
                #         "user_query": { "type": "string", "description": "User prompt about desired math problems." }
                #     },
                #     "required": ["user_query"]
                # }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "query_fuseki",
                "description": "Submit a SPARQL query to Fuseki for problems on a topic.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "label": { "type": "string", "description": "Topic label to query." },
                        "grade": { "type": "integer", "description": "Grade if specified." },
                        "count": { "type": "integer", "description": "Number of problems to retrieve." },
                        "complexity": { "type": "string", "description": "Complexity filter." }
                    },
                    "required": ["label"]
                }
            }
        }
    ]
    SYSTEM_PROMPT_FIND_SUBTOPICS = """
    You are analyzing a worksheet request by a math teacher. Please analyze the given query and try to find 
    all topic labels corresponding to the query.
    Arrange labels starting from the best match. Try to find 2-5 topic labels. 
    All topics represent different mathematical skills. They are arranged in a tree-like structure.
    There are altogether 4 topic tree roots - one per each domain. 
    Domains are 'Alg'(Algebra), 'Comb'(Combinatorics), 'Geom'(Geometry) and 'NT'(Number Theory).
    Use the tool 'list_subtopics' to get topic labels. It takes one argument - either a topic root ('Alg', 'Comb', 'Geom', 'NT')
    or some topic label. This function lists all immediate children of the given node from the topic tree.
    JSON example:
    ```{ "subtopics": [ "topic_label1", "topic_label2", "topic_label3"]}```
    Please include just the JSON in your response, do not add any explanations before or after.
    """

    SYSTEM_PROMPT = """
    You are a worksheet generator for math teachers. Analyze the worksheet request, 
    use the tools 'find_topics' and 'query_fuseki' to get at least the estimated_problem_count
    specified in the worksheet request. 
    Arrange them in a logical, teaching-friendly order and output as JSON. 
    Please write all mathematical expressions as LaTeX between $-signs for inline formulas
    or between $$-signs if they are wide formulas. Use proper JSON escaping - for example: $a \\cdot b$.
    JSON example (may be unrelated to the requested content):
    ```
    {
	"snippets": [
	  {
	    "type": "title",
		"value": "Dirihlē princips un kombinatorika 8. klasei"
	  },
	  {
	    "type": "section_title",
		"value": "Ievaduzdevumi"
	  },
	  {
		"type": "annotation",
		"value": "Divi iesildoši uzdevumi, lai atgādinātu matemātiskās loģikas pamatus un praktisko domāšanu."
	  },
	  {
		"type": "problem",
        "problemid" : "LV.AMO.2004.8.2"
		"problemtext": "Mākslinieku grupa Arcane pasaulē vēlas sadalīt 25 portretus piecās izstādēs tā, ka katrā izstādē ir vismaz viens portrets. Vai tas vienmēr ir iespējams? Ja jā/nē, paskaidro, kāpēc."
        "problemsolution": "Nav obligāti iespējams, ja portretus nedrīkst likt vienā izstādē: ja visi portreti tiek ielikti vienā izstādē, pārējās būs tukšas."
	  },
	 // Any more problems that belong to section "Ievaduzdevumi"
	  {
	  	"type": "section_title",
		"value": "Teorijas pārskats"
	  },
	  {
	    "type": "theorem",
		"value": "Dirihlē princips (pigeonhole principle): Ja starp n objektiem samet m kastēs un n > m, kādā kastē noteikti būs vismaz 2 objekti."
	  },
	// Any more theorems that belong to section "Teorijas pārskats"
	  {
		"type": "section_title",
		"value": "Uzdevumi"
	  },
	  {
		"type": "annotation",
		"value": "Uzdevumi ar pieaugošu grūtību, aptverot kombinatoriku, ģeometriju, skaitļu teoriju. Dažādi tipiski risināšanas uzdevumu piemēri."
	  }
	]
    }
    ``` 
    Please adapt about 2/3 of all problems from those returned by query_fuseki and about 1/3 should be newly generated.
    If snippet is of "type": "problem" and the problem text is derived from a Fuseki database problem,
    then it must have "problemid" returned by query_fuseki function. 
    If a problem is generated by you, then it should contain "problemid": "NEW". 
    """

    def __init__(self, openai_api_key, fuseki_url, fuseki_user, fuseki_password, weaviate_url, weaviate_api_key, task_data):
        self.weaviate_url = weaviate_url
        self.weaviate_api_key = weaviate_api_key
        self.openai_api_key = openai_api_key
        self.fuseki_url = fuseki_url
        self.fuseki_user = fuseki_user
        self.fuseki_password = fuseki_password
        self.topic_list = task_data.get('found_topics', [])


    def read_json(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)

    def write_json(self, filename, obj):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(obj, f, indent=2, ensure_ascii=False)

    def find_topics(self):
        # topics = json.loads(self.topic_list)
        return self.topic_list

    def find_topics_weaviate(self, user_query):
        # HOW TO TEST: python eliozo_client.py get-problems --worksheet ../tests/get-problems/worksheet.json  --reference ../tests/get-problems/task.json
        print(f'CALLED find_topics({user_query})')
        # Replace this with your actual (encoder/transformer) logic
        # return ["PigeonholePrincipleBasic", "PigeonholePrincipleGeneralized", "PigeonholePrincipleGeometry"]
        weaviateUtils = WeaviateUtils(self.weaviate_url, 
                            self.weaviate_api_key, 
                            self.openai_api_key)

        print(f'get_classifiers: Getting classifier data from Weaviate')
        #(retvalue, data) = weaviateUtils.ingest_classifier_data(property, turtle)
        results = weaviateUtils.near_search("Classifier", user_query, 10)
        print(results)
        # TODO ar for ciklu iet cauri results un katram masīva elementam izvelk vērtību atslēgai label
        #  un piešķir tos jaunam sarakstam
        # Atgriezt nevis results, bet sarakstu, kurā ir tikai labels vērtības. 
        # Paraugs, kā tam būtu jāizskatās - # return ["PigeonholePrincipleBasic", "PigeonholePrincipleGeneralized", "PigeonholePrincipleGeometry"]
        return results
        #return (0, {}) 

    # TODO:
    # Šobrīd pēc dotā label atrod tikai uzdevumu problemid un tekstus
    # Daudzām darba lapām vajag atrisinājumus, un varētu SPARQL pamainīt, tā, lai līdz ar katru uzdevumu atrastu arī viņa atrisinājumu
    # Paraugi, kā to izdarīt ir qualification-project init py failā.
    # Atgriežamo uzdevumu sarakstā var pievienot jaunu atribūtu solution
    def list_subtopics(self, parent_label):
        fuseki_utils = FusekiUtils(self.fuseki_url, self.fuseki_user, self.fuseki_password)
        mydict = {'Alg':'Algebra', 'Comb':'Combinatorics', 'Geom': 'Geometry', 'NT':'NumTheory'}
        if parent_label in ['Alg', 'Comb', 'Geom', 'NT']:
            parent_label = mydict[parent_label]
        myquery = """PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
SELECT ?topicID ?label ?num ?name ?description WHERE {{
?parentTopic skos:prefLabel '{parent_label}' .
?topicID skos:broader ?parentTopic ;
    skos:prefLabel ?label ;
    eliozo:topicName ?name ;
    eliozo:topicDescription ?description ;
    eliozo:topicNumber ?num .
}} ORDER BY ?num"""
        print(f'CALLED list_subtopics ({parent_label}')
        res = []
        myquery = myquery.format(parent_label = parent_label)
        print(f"Myquery = {myquery}")
        results = fuseki_utils.execute_query("abc", myquery)
        for item in results['results']['bindings']:
            res.append({
                "label": item['label']['value'],
                "name": item['name']['value'],
                "description": item['description']['value'],
            })
        return res

    # TODO 2:
    # Šobrīd vaicājums ignorē grade (grade ne lielāku par to, kas ir uzdots, piemēram 8kl var rēķināt arī 7,6kl utt.)
    #  un count (fuseki vaicājumā tas būtu, piemēram, limit 10)
    # Pielabot šo funkciju, kas atrastu atrisinājumu, jāpiekabina pie datiem, kurus atgriežam
    def query_fuseki(self, label, grade=None, count=None, complexity=None):
        print(f'CALLED query_fuseki({label}, {grade}, {count}, {complexity})')
        res = []
        fuseki_utils = FusekiUtils(self.fuseki_url, self.fuseki_user, self.fuseki_password)
        myquery = """PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>

SELECT DISTINCT ?problem ?problemid ?text ?grade 
       (GROUP_CONCAT(DISTINCT ?solution; separator="<br/><br/>") AS ?solutions)
       (GROUP_CONCAT(DISTINCT ?solutiontext; separator="<br/><br/>") AS ?solutiontexts)
WHERE {{
    ?parent skos:prefLabel '{label}' .
    ?parent skos:narrower* ?subtopic .
    ?problem eliozo:topic ?subtopic ;
             eliozo:problemGrade ?grade ;
             eliozo:problemID ?problemid ;
             eliozo:problemTextHtml ?text ;
             eliozo:problemSolution ?solution .
    ?solution eliozo:solutionTextHtml ?solutiontext .
}}
GROUP BY ?problem ?problemid ?text ?grade
ORDER BY ?grade"""
        myquery = myquery.format(label = label)
        print(f"Myquery = {myquery}")
        results = fuseki_utils.execute_query("abc", myquery)
        for item in results['results']['bindings']:
            res.append({
                "problemid": item['problemid']['value'],
                "topic": label,
                "text": item['text']['value'],
                "solution" : item['solutiontexts']['value'],
                "grade": int(item['grade']['value'])
            })
        return res

    # ---- OpenAI tool/function definition ----
    def ask_to_find_topics(self, task_data): # List with topics
        openai.api_key = self.openai_api_key

        merged_task = task_data.copy() # A cloned copy to save back into task.json

        messages = [
            {"role": "system", "content": self.SYSTEM_PROMPT_FIND_SUBTOPICS},
            {"role": "user", "content": f"For the given user request please return a JSON structure with a single key 'subtopics' mapping to an array of labels - the identifiers of topics corresponding to the user query: {json.dumps(merged_task['task'], ensure_ascii=False)}"}
        ]
        functions_map = {"list_subtopics": self.list_subtopics}

        topics_used = []
        max_iterations = 10

        for _ in range(max_iterations):
            completion = openai.chat.completions.create(
                model=self.gpt_model,
                messages=messages,
                tools=self.function_specs2,
                tool_choice="auto"
            )
            msg = completion.choices[0].message

            if msg.tool_calls:
                # For each tool_call, do the call and gather response
                tool_responses = []
                for tool_call in msg.tool_calls:
                    fn_name = tool_call.function.name
                    fn_args = json.loads(tool_call.function.arguments)
                    ret = functions_map[fn_name](**fn_args)
                    tool_responses.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,  # must match!
                        "name": fn_name,
                        "content": json.dumps(ret)
                    })
                messages.append({"role": "assistant", "content": None, "tool_calls": msg.tool_calls})
                messages.extend(tool_responses)
            else:
                try:
                    completion = msg.content
                    start = completion.find('{')
                    end = completion.rfind('}')
                    if start != -1 and end != -1:
                        completion = completion[start:end+1]
                    # Expecting the assistant to reply with a JSON of topics
                    assistant_reply = json.loads(completion)
                    # Example format: { "subtopics": [ "label1", "label2" ]}
                    if "subtopics" in assistant_reply:
                        topics_used = assistant_reply["subtopics"]
                        break
                except Exception as e:
                    print("[WARN] Could not parse assistant reply as JSON. Got:", msg.content)
                    break

        # Inject found topics into task data
        merged_task['found_topics'] = topics_used
        # Store for use in find_topics
        self.last_found_topics = topics_used

        return (0, merged_task)
        # return (0, {}) - neder
        # TODO:
        # Vajadzētu dabūt no OpenAI kurus topic labels viņš atgriež
        # Vajag merged_task papildināt ar topikiem ar labels, kurus atrada OpenAI un to vajag atgriezt
        # return (0, merged_task)

    def set_task_data(self, task_data):
        self.task_data = task_data # Saving task_data to object
        
    def get_problems_for_query(self, task_data, worksheet):
        openai.api_key = self.openai_api_key

        # Step 1: Read user query from file
        user_query = task_data["task"]["query"]

        merged_task = task_data.copy()

        # Function-calling workflow to assemble problems
        messages = [
            {"role": "system", "content": self.SYSTEM_PROMPT},
            {"role": "user", "content": f"Generate problems for worksheet: {json.dumps(merged_task['task'], ensure_ascii=False)}"}
        ]
        functions_map = {"find_topics": self.find_topics, "query_fuseki": self.query_fuseki}

        finished = False
        worksheet_json = None
        collected_problems = []
        topics_used = []
        max_iterations = 3  # Avoid infinite loops


        for _ in range(max_iterations):
            completion = openai.chat.completions.create(
                model=self.gpt_model,
                messages=messages,
                tools=self.function_specs,
                tool_choice="auto"
            )
            msg = completion.choices[0].message

            if msg.tool_calls:
                # For each tool_call, do the call and gather response
                tool_responses = []
                for tool_call in msg.tool_calls:
                    fn_name = tool_call.function.name
                    fn_args = json.loads(tool_call.function.arguments)
                    ret = functions_map[fn_name](**fn_args)
                    tool_responses.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,  # must match!
                        "name": fn_name,
                        "content": json.dumps(ret)
                    })
                    # Optionally: collect for outside use
                    if fn_name == 'find_topics':
                        topics_used = ret
                    elif fn_name == 'query_fuseki':
                        collected_problems.extend(ret)
                # Append the tool response(s) to the history
                messages.append({"role": "assistant", "content": None, "tool_calls": msg.tool_calls})
                messages.extend(tool_responses)
                # Now continue to next loop iteration (awaiting new assistant reply)
                continue

            # If not tool_calls: assistant is giving a normal answer/output
            try:
                worksheet_json = json.loads(msg.content)
                finished = True
                break
            except Exception as e:
                print("Did not get valid worksheet JSON. Got:\n", msg.content)
                raise e


        # for _ in range(max_iterations):

        #     # print("\n===== FULL MESSAGE HISTORY =====")
        #     # pprint.pprint(messages)
        #     # print("===== END MSG =====\n")

        #     completion = openai.chat.completions.create(
        #         model=self.gpt_model,
        #         messages=messages,
        #         tools=self.function_specs,
        #         tool_choice="auto"
        #     )
        #     msg = completion.choices[0].message
        #     if msg.tool_calls:
        #         for tool_call in msg.tool_calls:
        #             fn_name = tool_call.function.name
        #             fn_args = json.loads(tool_call.function.arguments)
        #             ret = functions_map[fn_name](**fn_args)
        #             # Show LLM the tool result as an assistant message (tool response)
        #             messages.append({
        #                 "role": "tool",
        #                 "tool_call_id": tool_call.id,
        #                 "name": fn_name,
        #                 "content": json.dumps(ret)
        #             })
                    
        #             # Save used topics to avoid repeating
        #             if fn_name == 'find_topics':
        #                 topics_used = ret
        #             elif fn_name == 'query_fuseki':
        #                 collected_problems.extend(ret)
        #         continue
        #     # If not calling tools, it's a user-facing answer (worksheet)
        #     try:
        #         worksheet_json = json.loads(msg.content)
        #         finished = True
        #         break
        #     except Exception as e:
        #         print("Did not get valid worksheet JSON. Got:\n", msg.content)
        #         raise e
            



        if not finished:
            print("[FAIL] LLM did not finish in allowed iterations.")
        else:
            self.write_json(worksheet, worksheet_json)
            print("[OK] Worksheet written to worksheet.json")

        return (0, merged_task)
