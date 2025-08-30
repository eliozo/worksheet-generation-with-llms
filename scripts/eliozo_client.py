import os
import requests
from requests.auth import HTTPBasicAuth
import sys
import json
from datetime import datetime
from dotenv import load_dotenv
import argparse
import shutil
import time
import re
import asyncio
import urllib3



script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(script_dir, '..'))
sys.path.insert(0, parent_dir)

from scripts.fuseki_utils import FusekiUtils
from scripts.weaviate_utils import WeaviateUtils
from scripts.word_utils import WordUtils
from scripts.openai_utils import OpenaiUtils
from scripts.openai_utils import AnalysisType
from scripts.openai_function_agent import OpenaiFunctionAgent
from scripts.metadata_utils_new import MetadataUtils
from scripts.metadata_utils_new import MetadataProperties
from scripts.adapt_utils import AdaptExtension, AdaptUtils
from scripts.markdown_proc.convert_to_ttl_main import markdown_repository_to_turtle, crawl_markdown_problemdata
from scripts.markdown_proc.mdchunk_reader import markdown_md_to_turtle

from scripts.rdfgen.csv_to_skos import CsvToSkos
from scripts.rdfgen.csv_to_table import CsvToTable
from scripts.rdfgen.csv_to_concepts import CsvToConcepts
from scripts.rdfgen.csv_to_nested_table import CsvToNestedTable
from scripts.rdfgen.csv_to_problemsru import CsvToProblemsru

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# Used to create backup copies of "worksheet.json" or "task.json" as it is updated
def copy_with_incremented_name(file_path):
    dir_name = os.path.dirname(file_path)
    base_name = os.path.basename(file_path)
    name_parts = base_name.split(".")
    if len(name_parts) != 2: 
        print(f"{base_name} must be a file with an extension - it should have a single dot (.)")
    name = name_parts[0]
    ext = name_parts[1]
    print(f"(name, ext) = ({name}, {ext})")

    if (name, ext) != ("worksheet", "json") and (name, ext) != ("task", "json"):
        print(f"In copy_with_incremented_name({file_path})")
        print(f"base_name = {base_name}")
        raise ValueError("The file must be named 'worksheet.json' or 'task.json'")
    
    n = 1
    while True:
        new_filename = f"{name}.{n}.{ext}"
        new_file_path = os.path.join(dir_name, new_filename)
        if not os.path.exists(new_file_path):
            break
        n += 1

    shutil.copy2(file_path, new_file_path)
    return new_filename

def get_json_field(fname, field_list):
    if fname is None:
        return None
    else:
        with open(fname, 'r', encoding="utf-8") as file:
            json_fragment = json.load(file)
        for ff in field_list:
            json_fragment = json_fragment[ff]
        return json_fragment


class EliozoClient:
    reference = "NA.json"
    command = "NA"
    weaviate_url = "NA"
    weaviate_api_key = "NA"
    openai_api_key = "NA"
    fuseki_url = "NA"
    fuseki_user = "NA"
    fuseki_password = "NA"

    def __init__(self, weaviate_url, weaviate_api_key, openai_api_key, fuseki_url, fuseki_user, fuseki_password):
        self.weaviate_url = weaviate_url
        self.weaviate_api_key = weaviate_api_key
        self.openai_api_key = openai_api_key
        self.fuseki_url = fuseki_url
        self.fuseki_user = fuseki_user
        self.fuseki_password = fuseki_password
        print("Client created")

    def set_reference(self, reference):
        self.reference = reference

    def set_command(self, command): 
        self.command = command

    # Store reference file for preliminary (data preparation) commands
    def store_prelim(self, command, data):
        try:
            with open(self.reference, 'r', encoding='utf-8') as f:
                current = json.load(f)
                if not isinstance(current, dict):
                    current = {}
        except (FileNotFoundError, json.JSONDecodeError):
            current = {}
        workflow = current.get("preliminary-workflow")
        if not isinstance(workflow, list):
            workflow = []

        workflow.append({command: data})
        current["preliminary-workflow"] = workflow

        dir_path = os.path.dirname(self.reference)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)
        with open(self.reference, 'w', encoding='utf-8') as f:
            json.dump(current, f, indent=4, ensure_ascii=False)


    # Store task.json with worksheet-related data
    def store_task(self, data): 
        with open(self.reference, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)


#     def add_metadata(self, md_file, prop, provider, output):
#         print(f'Command = {self.command}(md_file = {md_file}, prop = {prop}, provider = {provider}, output= {output})')
#         #return (0, {'key17':'value1'})
#         metadataUtils = MetadataUtils(self.openai_api_key)
#         result = metadataUtils.classify_problem("""Uz tāfeles pa reizei uzrakstīti visi naturālie skaitļi no $1$ līdz $n$ ieskaitot. 
# Ar vienu gājienu var izvēlēties divus uz tāfeles uzrakstītus skaitļus 
# (apzīmēsim tos ar $a$ un $b$), nodzēst tos un to vietā uzrakstīt $\left| a^2-b^2 \right|$. 
# Pēc $n-1$ gājiena uz tāfeles paliek viens skaitlis.  
# Vai tas var būt $0$, ja **(a)** $n=8$, **(b)** $n=9$?""", '', 'questionType')
#         return (0, {'key17': result})

    def add_metadata(self, md_file, prop, provider, output):
        print(f'Command = {self.command}(md_file = {md_file}, prop = {prop}, provider = {provider}, output= {output})')

        metadata_utils = MetadataUtils(self.openai_api_key)

        # Read markdown and extract tasks
        def extract_sections_from_md(filepath):
            heading_re = re.compile(r'^#\s+<lo-sample/>\s+(.*)')
            current_section = None
            sections = []
            title = "NA"

            with open(filepath, 'r', encoding='utf-8') as file:
                for line in file:
                    m = heading_re.match(line)
                    if m:
                        new_title = m.group(1)
                        if current_section is not None:
                            sections.append((title, current_section))
                        title = new_title
                        current_section = ''
                    elif current_section is not None:
                        current_section += line
            if current_section:
                sections.append((title, current_section))
            return sections

        def normalize_text(text):
            meta_start = text.find('<small>')
            return text[:meta_start].strip() if meta_start > 0 else text.strip()

        def add_generated_question_type(md_text, generated_qtype):
            small_block_re = re.compile(r'(<small>)(.*?)(</small>)', re.DOTALL)
            match = small_block_re.search(md_text)

            if match:
                before_tag = match.group(1)
                middle_block = match.group(2)
                after_tag = match.group(3)

                if '_questionType:' in middle_block:
                    return md_text

                updated_middle = middle_block.strip() + f"\n* _questionType: {generated_qtype}\n"
                return (
                    md_text[:match.start()] +
                    before_tag + updated_middle + after_tag +
                    md_text[match.end():]
                )
            else:
                return md_text

        # Read tasks from markdown
        problemList = extract_sections_from_md(md_file)
        updated_sections = []

        for (title, full_problem) in problemList:
            clean_problem = normalize_text(full_problem)

            try:
                # predicted_qtype = metadata_utils.classify_problem(clean_problem, "", prop)
                if prop == "questionType":
                    predicted_qtype = metadata_utils.classify_problem(clean_problem, "", MetadataProperties.QUESTION_TYPE)
                if isinstance(predicted_qtype, dict):
                    predicted_qtype = predicted_qtype.get('uzdevuma_tips', 'NA')
            except Exception as e:
                print(f"❌ Error classifying {title}: {e}")
                predicted_qtype = 'NA'

            updated_problem = add_generated_question_type(full_problem, predicted_qtype)
            updated_sections.append(f"# <lo-sample/> {title}\n\n{updated_problem.strip()}\n")

            print(f"✅ Processed: {title} | _questionType: {predicted_qtype}")

        # Ensure folder exists
        os.makedirs(os.path.dirname(output) or ".", exist_ok=True)

        with open(output, 'w', encoding='utf-8') as out:
            out.write('\n\n'.join(updated_sections))

        print(f"\n✅ Output written to: {output}")
        return (0, {"status": "success", "output": output})

    def md_to_turtle(self, markdown, turtle):
        # print(f'Command = {self.command}(markdown = {markdown}, turtle = {turtle})')
        # print(f'Command not supported')
        markdown_md_to_turtle(markdown, turtle)
        return (0, {'key2':'value2'})
    
    def md_repository_csv_to_turtle(self, output, csv): 
        ttls = markdown_repository_to_turtle(output, csv)
        return (0, {'output':output, 'csv':csv, 'ttls': ttls})

    def md_repository_dir_to_turtle(self, output, problemdata):
        csv = crawl_markdown_problemdata(problemdata)
        ttls = markdown_repository_to_turtle(output, csv)
        return (0, {'output':output, 'problemdata':'problemdata', 'ttls': ttls})

    def metadata_to_turtle(self, url, property, output):
        print(f"called metadata_to_turtle({url, property, output})")
        if property in ['topics', 'methods', 'domains', 'questions']: 
            exporter = CsvToSkos(url, property)
            exporter.export_to_turtle(output)
        elif property in ['olympiads', 'sources']:
            exporter = CsvToTable(url, property)
            exporter.export_to_turtle(output)        
        elif property in ['concepts']: 
            exporter = CsvToConcepts(url)
            exporter.export_to_turtle(output)
        elif property in ['videos']: 
            exporter = CsvToNestedTable(url)
            exporter.export_to_turtle(output)
        elif property in ['problemsru']:
            exporter = CsvToProblemsru(url)
            exporter.export_to_turtle(output)
        return (0, {'property':property, 'output':output})
    
    def drop_rdf(self, dataset):
        print(f"FUSEKI_URL is {self.fuseki_url}")
        rdfUtilities = FusekiUtils(self.fuseki_url, self.fuseki_user, self.fuseki_password)
        rdfUtilities.drop_all(dataset)
        return (0, {'status':'Success'})
    
    def create_rdf_dataset(self, dataset):
        print(f"FUSEKI_URL is {self.fuseki_url}")
        rdfUtilities = FusekiUtils(self.fuseki_url, self.fuseki_user, self.fuseki_password)
        rdfUtilities.create_dataset(dataset)
        return (0, {'status':'Success'})

    def ingest_rdf(self, dataset, turtle):
        rdfUtilities = FusekiUtils(self.fuseki_url, self.fuseki_user, self.fuseki_password)
        rdfUtilities.ingest_data(dataset, turtle)
        return (0, turtle)
    
    def drop_vectors(self, cluster):
        print(f'Dropping all collections from Weaviate cluster {cluster}')
        utils = WeaviateUtils(self.weaviate_url, 
                              self.weaviate_api_key, 
                              self.openai_api_key)
        (retvalue, data) = utils.drop_collections()                
        return (retvalue, data)
    
    def create_schema_vectors(self, cluster): 
        print(f'Creating schema for Weaviate cluster {cluster}')
        utils = WeaviateUtils(self.weaviate_url, 
                              self.weaviate_api_key, 
                              self.openai_api_key)
        (retvalue, data) = utils.create_schema() 
        return (retvalue, data)
 
    
    def ingest_vectors(self, cluster, turtle):
        print(f'ingest_vectors: Importing data to Weaviate {cluster}')
        utils = WeaviateUtils(self.weaviate_url, 
                              self.weaviate_api_key, 
                              self.openai_api_key)
        (retvalue, data) = utils.ingest_to_weaviate(turtle)
        utils.close_client()
        return (retvalue, data)

    def ingest_classifiers(self, cluster, property, turtle):
        weaviateUtils = WeaviateUtils(self.weaviate_url, 
                              self.weaviate_api_key, 
                              self.openai_api_key)

        print(f'ingest_classifiers: Importing classifier data to Weaviate {cluster}')
        (retvalue, data) = weaviateUtils.ingest_classifier_data(property, turtle)
        return (retvalue, data)

    def get_classifiers(self):
        print(f'get_classifiers: Getting classifier data from OpenAI function agent')
        with open(self.reference, 'r', encoding='utf-8') as f:
            task_data = json.load(f)
        agentUtils = OpenaiFunctionAgent(self.openai_api_key, self.fuseki_url, self.fuseki_user, self.fuseki_password, self.weaviate_url, self.weaviate_api_key, task_data)
        (retvalue, new_task_data) = agentUtils.ask_to_find_topics(task_data)
        return (retvalue, new_task_data)

    def create_task(self, query):
        retcode = 0
        openaiUtils = OpenaiUtils(self.openai_api_key)
        seed = 42
        (retcode, analysis1) = openaiUtils.analyze(query, AnalysisType.TASK_ANALYSIS)
        dir_name = os.path.dirname(self.reference)
        task_data = {
            "task": { 
                "query": query,
                #"title": analysis1['title'], 
                "grade": analysis1['grade'],
                "age": analysis1['age'],
                "problemcount": analysis1['estimated_problem_count'], 
                "worksheet": f"{dir_name}/worksheet.json",
                "template": "templates/regular.rst.jinja"
            },
            "result": {
            }
        }
        (retcode, analysis2) = openaiUtils.analyze(query, AnalysisType.TASK_DOMAIN)
        task_data['task']['domain'] = analysis2['domain']
        (retcode, analysis3) = openaiUtils.analyze(query, AnalysisType.TASK_LEARNERS)
        task_data['task']['learners'] = analysis3
        (retcode, analysis4) = openaiUtils.analyze(query, AnalysisType.TASK_FORMAT)
        task_data['task']['format_notes'] = analysis4['format_notes']

        return (retcode, task_data)
    
    def get_problems_rdf(self, output): 
        print(f'Getting problems from Fuseki to output {output}')
        lists_to_initialize = ["domain", "subdomain", "questionType", "grade", "topic", "method"]
        initialized_lists = {key: [] for key in lists_to_initialize}
        with open(self.reference, 'r', encoding='utf-8') as f:
            task_data = json.load(f)
            for key in lists_to_initialize:
                initialized_lists[key] = task_data.get('task', {}).get(key, [])
        rdfUtilities = FusekiUtils(self.fuseki_url, self.fuseki_user, self.fuseki_password)
        theQuery = rdfUtilities.build_filtering_query(initialized_lists)
        (retvalue, data) = rdfUtilities.execute_query("abc", theQuery)

        with open(output, 'w', encoding ='utf8') as output_file:
            json.dump(data, output_file, indent=4, ensure_ascii=False)
        return (retvalue, task_data)

    def get_problems_vectors(self, output): 
        weaviateUtils = WeaviateUtils(self.weaviate_url, 
                              self.weaviate_api_key, 
                              self.openai_api_key)
        with open(self.reference, 'r', encoding='utf-8') as f:
            task_data = json.load(f)
        # This is actually a bad idea to ask Weaviate, 
        # It would be better to generate some sample problem and then search for similar problems
        query = task_data['task']['query']

        (retvalue, data) = weaviateUtils.get_problems(query, 10)
        with open(output, 'w', encoding ='utf8') as output_file:
            json.dump(data, output_file, indent=4, ensure_ascii=False)
        return (retvalue, task_data)
        
    def get_problems(self, worksheet):
        with open(self.reference, 'r', encoding='utf-8') as f:
            task_data = json.load(f)
        print("BBBBBBBBBBBB")
        print(json.dumps(task_data))
        agentUtils = OpenaiFunctionAgent(self.openai_api_key, self.fuseki_url, self.fuseki_user, self.fuseki_password, self.weaviate_url, self.weaviate_api_key, task_data)
        (retvalue, new_task_data) = agentUtils.get_problems_for_query(task_data, worksheet)
        return (retvalue, new_task_data)


    # def adapt_topics(self, topics):
    #     print(f'Command not supported')
    #     return (0, {'key8':'value8'})
    
    # def adapt_style(self, style):
    #     print(f'Command not supported')
    #     return (0, {'key9':'value9'})
    
    def adapt_worksheet(self, property, value, location):
        with open(self.reference, 'r', encoding='utf-8') as f:
            task_data = json.load(f)
        if location != "*":
            print(f'Command adapt-worksheet only supported for location=*')
            return (1, task_data)
        if property != "extend": 
            print(f"Property {property} not supported; use 'extend'")
            return (1, task_data)
        if value not in ["Theory", "Title", "StyleRules"]:
            print(f"Only values 'Theory' and 'Title' are allowed; you are using {value}.")
            return (1, task_data)

        current_worksheet = task_data['result']['current_worksheet']
        print(f'Run adapt-worksheet {property} {value} on {current_worksheet}')
        adaptUtils = AdaptUtils(self.openai_api_key)
        if value == "Theory":
            output_json = adaptUtils.extend(current_worksheet, AdaptExtension.THEORY)
            backup_worksheet = copy_with_incremented_name(current_worksheet)
            with open(current_worksheet, 'w', encoding='utf-8') as file:
                json.dump(output_json, file, indent=4, ensure_ascii=False)
            task_data['result']['worksheet_before_theory'] = backup_worksheet

        elif value == "Title": 
            json_title = adaptUtils.extend(current_worksheet, AdaptExtension.TITLE)
            backup_worksheet = copy_with_incremented_name(current_worksheet)
            with open(current_worksheet, 'r', encoding='utf-8') as file:
                worksheet_content = json.load(file)
            # Pievieno "title" pašā "snippets" masīva sākumā
            worksheet_content["snippets"].insert(0, json_title['snippets'][0])
            with open(current_worksheet, 'w', encoding='utf-8') as file:
                json.dump(worksheet_content, file, indent=4, ensure_ascii=False)
            task_data['result']['worksheet_before_title'] = backup_worksheet

        elif value == "StyleRules":
            adaptUtils = AdaptUtils(self.openai_api_key)

            json_fixes = adaptUtils.extend(current_worksheet, AdaptExtension.STYLE_RULES)
            with open("rule_fixes.json", 'w', encoding='utf-8') as file:
                json.dump(json_fixes, file, indent=4, ensure_ascii=False)

            if ('snippets' in json_fixes) and len(json_fixes['snippets']) > 0: 
                backup_worksheet = copy_with_incremented_name(current_worksheet)
                with open(current_worksheet, 'r', encoding='utf-8') as file:
                    worksheet_content = json.load(file)
                worksheet_content["snippets"].append({"type": "section_title", "value": "Kļūdu labojumi"})
                for snip in json_fixes["snippets"]:
                    worksheet_content["snippets"].append({
                        "type": "text", 
                        "value": snip['value']
                    })
                    worksheet_content["snippets"].append({
                        "type": "fix",
                        "value": f"[{snip['rule']}]. {snip['value_fixed']}"
                    })
                with open(current_worksheet, 'w', encoding='utf-8') as file:
                    json.dump(worksheet_content, file, indent=4, ensure_ascii=False)
                task_data['result']['worksheet_before_style_rules'] = backup_worksheet

        retvalue = 0
        return (retvalue, task_data)
  
    
    def convert_worksheet(self, input, output, template_file=None):
        # print(f'Command not supported')
        # with open(self.reference, 'r', encoding='utf-8') as f:
        #     task_data = json.load(f)
        wordUtils = WordUtils()

        # if input.endswith('.json') and output.endswith('.docx'):
        #     wordUtils.build_rst(input, f'{input}.rst')
        #     wordUtils.rst_to_doc(f'{input}.rst', output)
        if input.endswith('.json') and output.endswith('.rst'):
            wordUtils.transform_md_to_rst(input, output, template_file)
        elif input.endswith('.rst') and output.endswith('.docx'):
            wordUtils.rst_to_doc(input, output)
        else: 
            print('Input and output are not compatible for convert-worksheet')
        return (0, {})   
    
    

def main(WEAVIATE_URL, WEAVIATE_API_KEY, OPENAI_API_KEY, FUSEKI_URL, FUSEKI_USER, FUSEKI_PASSWORD):
    parser = argparse.ArgumentParser(prog='eliozo_client.py', description='Manage Eliozo metadata and run generative LLMs. User Guide is in https://docs.google.com/document/d/12gHg2EbUH6pjKOIes43WG2uw9jjTIHn8Rs9KzB8APiU/edit?usp=sharing')
    subparsers = parser.add_subparsers(dest='command', help='Commands')

    cmd_h = {
        'add-metadata': 'Add a machine-generated metadata property to a markdown file',
        'md-to-turtle': 'Convert a markdown file to RDF Turtle',
        'md-repository-to-turtle': 'Convert all problems to RDF Turtle',
        'metadata-to-turtle': 'Download ELIOZO classifiers from Google docs to Turtle',
        'drop-rdf': 'Drop all RDF data from a SPARQL database (Fuseki etc.)',
        'create-rdf-dataset': 'Create RDF dataset (Fuseki etc.)',
        'ingest-rdf': 'Import RDF data to a SPARQL database (Fuseki etc.)',
        'drop-vectors': 'Delete all data from a vector database (Weaviate etc.)', 
        'create-schema-vectors': 'Create schemas for collections (Weaviate etc.)',
        'ingest-vectors': 'Import RDF data to a vector database (Weaviate etc.)',
        'ingest-classifiers': 'Schema, data for problem classifiers (Weaviate etc.)', 
        'get-classifiers': 'Find ELIOZO classifiers for the given user query',
        'create-task': 'Create a JSON reference for a worksheet generation task',
        'set-topic': 'Deselect a topic or reset its level in the reference file', 
        'set-style': 'Redefine a style guideline in the reference file',
        'get-problems-rdf': 'Get problems with SPARQL queries',
        'get-problems-vectors': 'Get problems with Weaviate/GraphQL queries',
        'get-problems': 'Get problems from LLM using RAG augmentation (rdf+vectors)',
        'drop-problem': 'Drop a problem from the current worksheet',
        'derive-problem': 'Derive a new problem from an existing problem',
        'extend-worksheet': 'Add supplementary text; apply transformation filters',
        'adapt-worksheet': 'Evaluate prototype; create structured feedback',
        'convert-worksheet': 'Convert worksheet to MS Word or PDF'
    }
            
    HELP_REFERENCE = 'JSON file accumulating cmd status (defaults to task.json)'

    arg_h = {
        'add-metadata': {
            'markdown': 'A markdown file to be processed',
            'property': 'Which Eliozo ontology property should be added',
            '--output' : 'Location to place Markdown with added metadata',
            '--mode': 'What input is used for classification',
            '--provider': 'Which classifier is used; OpenAI GPT-4o by default',
            '--reference': HELP_REFERENCE
        },

        'md-to-turtle': {
            'markdown': 'Markdown input file', 
            'turtle': 'Path to save RDF (Turtle format)',
            '--reference': HELP_REFERENCE
        },

        'md-repository-to-turtle': {
            'output': 'The output directory to place Turtle (and temporary MD) files',
            'problemdata': 'Parent directory with all content_xx.md files to scan',
            '--csv': 'Link or path to a CSV spreadsheet with a list of olympiads',
            '--reference': HELP_REFERENCE
        },

        'metadata-to-turtle': {
            'url': 'Link to a Google Docs file',
            'property': 'topics, methods, domains, questions, concepts, olympiads, sources, videos',
            'turtle': 'Path to save RDF (Turtle format)',
            '--reference': HELP_REFERENCE 
        },

        'drop-rdf': {
            'dataset': 'Dataset to drop such as "abc"',
            '--reference': HELP_REFERENCE
        },

        'create-rdf-dataset': {
            'dataset': 'Dataset to create such as "abc"',
            '--reference': HELP_REFERENCE
        },

        'ingest-rdf': {
            'dataset': 'Targeted dataset',
            'turtle': 'RDF file to ingest (Turtle format)',
            '--reference': HELP_REFERENCE
        },

        'drop-vectors': {
            'cluster': 'Cluster to delete',
            '--reference': HELP_REFERENCE
        },

        'create-schema-vectors': {
            'cluster': 'Cluster where to create collections',
            '--reference': HELP_REFERENCE
        },

        'ingest-vectors': {
            'cluster': 'Targeted cluster',
            'turtle': 'RDF file to ingest (RDF format)',
            '--reference': HELP_REFERENCE
        }, 

        'ingest-classifiers': {
            'cluster': 'Targeted cluster',
            'property': 'One of these: domain, subdomain, questionType, topic, method, concepts', 
            'turtle': 'RDF file to import (it contains the hierarchy property)',
            '--reference': HELP_REFERENCE
        },

        'get-classifiers': {
            'query': 'User request expressed in human language', 
            '--reference': HELP_REFERENCE
        },

        'create-task': {
            '--query': 'User request expressed in human language',
            '--reference': HELP_REFERENCE
        }, 

        'set-topic': {
            'topic': 'Which topic to modify',
            'level': 'Level of exposition',
            '--reference': HELP_REFERENCE
        },

        'set-style': {
            'property': 'Which style property to modify',
            'value': 'Style guideline in natural language', 
            '--reference': HELP_REFERENCE
        },

        'get-problems-rdf': {
            '--worksheet': 'JSON worksheet with problems; defaults to worksheet.json', 
            '--reference': HELP_REFERENCE
        },

        'get-problems-vectors': {
            '--worksheet': 'JSON worksheet with problems; defaults to worksheet.json', 
            '--reference': HELP_REFERENCE
        },

        'get-problems': {
            '--worksheet': 'JSON output file; defaults to worksheet.json', 
            '--reference': HELP_REFERENCE
        },

        'drop-problem': {
            'problemID': 'ID of the problem to drop', 
            '--reference': HELP_REFERENCE
        },

        'derive-problem': {
            'problemID': 'ID of the problem to derive from', 
            '--reference': HELP_REFERENCE
        },

        'extend-worksheet': {
            '--reference': HELP_REFERENCE
        },

        'adapt-worksheet': {
            'property': 'The language/content property to adapt (complexity, register, extension, paraphrase, reorder)', 
            'value': 'How to adapt the propert (see User Guide)',
            '--location': 'The path in worksheet.json to modify',
            '--reference': HELP_REFERENCE
        }, 

        'convert-worksheet': {
            'input': 'Input as JSON file', 
            'output': 'Output (e.g. MS Word or PDF file - use extension *.docx, or *.pdf)',
            '--template': 'Jinja2 template (only used for *.json to *.rst conversion) - overrides one in reference', 
            '--reference': HELP_REFERENCE
        }
    }



    

    add_metadata_parser = subparsers.add_parser('add-metadata', help=cmd_h['add-metadata'])
    add_metadata_parser.add_argument('markdown', type=str, help=arg_h['add-metadata']['markdown'])
    add_metadata_parser.add_argument('property', type=str, help=arg_h['add-metadata']['property'])
    add_metadata_parser.add_argument('--output', type=str, default=None, help=arg_h['add-metadata']['--output'])
    add_metadata_parser.add_argument('--mode', type=str, help=arg_h['add-metadata']['--mode'])    
    add_metadata_parser.add_argument('--provider', type=str, default=None, help=arg_h['add-metadata']['--provider'])
    add_metadata_parser.add_argument('--reference', type=str, default=None, help=arg_h['add-metadata']['--reference'])

    md_to_turtle_parser = subparsers.add_parser('md-to-turtle', help=cmd_h['md-to-turtle'])
    md_to_turtle_parser.add_argument('markdown', type=str, help=arg_h['md-to-turtle']['markdown'])
    md_to_turtle_parser.add_argument('turtle', type=str, help=arg_h['md-to-turtle']['turtle'])
    md_to_turtle_parser.add_argument('--reference', type=str, default=None, help=arg_h['md-to-turtle']['--reference'])

    md_repository_to_turtle_parser = subparsers.add_parser('md-repository-to-turtle', help=cmd_h['md-repository-to-turtle'])
    md_repository_to_turtle_parser.add_argument('output', type=str, help=arg_h['md-repository-to-turtle']['output'])
    md_repository_to_turtle_parser.add_argument('problemdata', type=str, nargs="?", default=None, help=arg_h['md-repository-to-turtle']['problemdata'])
    md_repository_to_turtle_parser.add_argument('--csv', type=str, default=None, help=arg_h['md-repository-to-turtle']['--csv'])
    md_repository_to_turtle_parser.add_argument('--reference', type=str, default=None, help=arg_h['md-repository-to-turtle']['--reference'])

    metadata_to_turtle_parser = subparsers.add_parser('metadata-to-turtle', help=cmd_h['metadata-to-turtle'])
    metadata_to_turtle_parser.add_argument('url', type=str, help=arg_h['metadata-to-turtle']['url'])
    metadata_to_turtle_parser.add_argument('property', type=str, help=arg_h['metadata-to-turtle']['property'])
    metadata_to_turtle_parser.add_argument('output', type=str, help=arg_h['metadata-to-turtle']['turtle'])
    metadata_to_turtle_parser.add_argument('--reference', type=str, default=None, help=arg_h['metadata-to-turtle']['--reference'])

    drop_rdf_parser = subparsers.add_parser('drop-rdf', help=cmd_h['drop-rdf'])
    drop_rdf_parser.add_argument('dataset', type=str, help=arg_h['drop-rdf']['dataset'])
    drop_rdf_parser.add_argument('--reference', type=str, default=None, help=arg_h['drop-rdf']['--reference'])

    create_rdf_dataset_parser = subparsers.add_parser('create-rdf-dataset', help=cmd_h['create-rdf-dataset'])
    create_rdf_dataset_parser.add_argument('dataset', type=str, help=arg_h['create-rdf-dataset']['dataset'])
    create_rdf_dataset_parser.add_argument('--reference', type=str, default=None, help=arg_h['create-rdf-dataset']['--reference'])

    ingest_rdf_parser = subparsers.add_parser('ingest-rdf', help=cmd_h['ingest-rdf'])
    ingest_rdf_parser.add_argument('dataset', type=str, help=arg_h['ingest-rdf']['dataset'])
    ingest_rdf_parser.add_argument('turtle', type=str, help=arg_h['ingest-rdf']['turtle'])
    ingest_rdf_parser.add_argument('--reference', type=str, default=None, help=arg_h['ingest-rdf']['--reference'])

    drop_vectors_parser = subparsers.add_parser('drop-vectors', help=cmd_h['drop-vectors'])
    drop_vectors_parser.add_argument('cluster', type=str, help=arg_h['drop-vectors']['cluster'])
    drop_vectors_parser.add_argument('--reference', type=str, default=None, help=arg_h['drop-vectors']['--reference'])

    create_schema_vectors = subparsers.add_parser('create-schema-vectors', help=cmd_h['create-schema-vectors'])
    create_schema_vectors.add_argument('cluster', type=str, help=arg_h['create-schema-vectors']['cluster'])
    create_schema_vectors.add_argument('--reference', type=str, default=None, help=arg_h['create-schema-vectors']['--reference'])

    ingest_vectors_parser = subparsers.add_parser('ingest-vectors', help=cmd_h['ingest-vectors'])
    ingest_vectors_parser.add_argument('cluster', type=str, help=arg_h['ingest-vectors']['cluster'])
    ingest_vectors_parser.add_argument('turtle', type=str, help=arg_h['ingest-vectors']['turtle'])
    ingest_vectors_parser.add_argument('--reference', type=str, default=None, help=arg_h['ingest-vectors']['--reference'])

    ingest_classifiers_parser = subparsers.add_parser('ingest-classifiers', help=cmd_h['ingest-classifiers'])
    ingest_classifiers_parser.add_argument('cluster', type=str, help=arg_h['ingest-classifiers']['cluster'])
    ingest_classifiers_parser.add_argument('property', type=str, help=arg_h['ingest-classifiers']['property'])
    ingest_classifiers_parser.add_argument('turtle', type=str, help=arg_h['ingest-classifiers']['turtle'])
    ingest_classifiers_parser.add_argument('--reference', type=str, default=None, help=arg_h['ingest-classifiers']['--reference'])

    get_classifiers_parser = subparsers.add_parser('get-classifiers', help=cmd_h['get-classifiers'])
    #get_classifiers_parser.add_argument('query', type=str, help=arg_h['get-classifiers']['query'])
    get_classifiers_parser.add_argument('--reference', type=str, default=None, help=arg_h['get-classifiers']['--reference'])

    create_task_parser = subparsers.add_parser('create-task', help=cmd_h['create-task'])
    create_task_parser.add_argument('--query', type=str, help=arg_h['create-task']['--query'])
    create_task_parser.add_argument('--reference', type=str, default=None, help=arg_h['create-task']['--reference'])

    adapt_topics_parser = subparsers.add_parser('set-topic', help=cmd_h['set-topic'])
    adapt_topics_parser.add_argument('topic', type=str, help=arg_h['set-topic']['topic'])
    adapt_topics_parser.add_argument('level', type=str, help=arg_h['set-topic']['level'])
    adapt_topics_parser.add_argument('--reference', type=str, default=None, help=arg_h['set-topic']['--reference'])

    adapt_style_parser = subparsers.add_parser('set-style', help=cmd_h['set-style'])
    adapt_style_parser.add_argument('property', type=str, help=arg_h['set-style']['property'])
    adapt_style_parser.add_argument('value', type=str, help=arg_h['set-style']['value'])
    adapt_style_parser.add_argument('--reference', type=str, default=None, help=arg_h['set-style']['--reference'])

    get_problems_rdf_parser = subparsers.add_parser('get-problems-rdf', help=cmd_h['get-problems-rdf'])
    get_problems_rdf_parser.add_argument('--worksheet', type=str, default=None, help=arg_h['get-problems-rdf']['--worksheet'])
    get_problems_rdf_parser.add_argument('--reference', type=str, default=None, help=arg_h['get-problems-rdf']['--reference'])

    get_problems_vectors_parser = subparsers.add_parser('get-problems-vectors', help=cmd_h['get-problems-vectors'])
    get_problems_vectors_parser.add_argument('--worksheet', type=str, default=None, help=arg_h['get-problems-vectors']['--worksheet'])
    get_problems_vectors_parser.add_argument('--reference', type=str, default=None, help=arg_h['get-problems-vectors']['--reference'])

    get_problems_parser = subparsers.add_parser('get-problems', help=cmd_h['get-problems'])
    get_problems_parser.add_argument('--worksheet', type=str, default=None, help=arg_h['get-problems']['--worksheet'])
    get_problems_parser.add_argument('--reference', type=str, default=None, help=arg_h['get-problems']['--reference'])

    # drop_problem_parser = subparsers.add_parser('drop-problem', help=cmd_h['drop-problem'])
    # drop_problem_parser.add_argument('problemID]', type=str, help=arg_h['drop-problem']['problemID'])
    # drop_problem_parser.add_argument('--reference', type=str, default=None, help=arg_h['drop-problem']['--reference'])

    # derive_problem_parser = subparsers.add_parser('derive-problem', help=cmd_h['derive-problem'])
    # derive_problem_parser.add_argument('problemID]', type=str, help=arg_h['derive-problem']['problemID'])
    # derive_problem_parser.add_argument('--reference', type=str, default=None, help=arg_h['derive-problem']['--reference'])

    # extend_worksheet_parser = subparsers.add_parser('extend-worksheet', help=cmd_h['extend-worksheet'])
    # extend_worksheet_parser.add_argument('--reference', type=str, default=None, help=arg_h['extend-worksheet']['--reference'])

    adapt_worksheet_parser = subparsers.add_parser('adapt-worksheet', help=cmd_h['adapt-worksheet'])
    adapt_worksheet_parser.add_argument('property', type=str, help=arg_h['adapt-worksheet']['property'])
    adapt_worksheet_parser.add_argument('value', type=str, help=arg_h['adapt-worksheet']['value'])
    adapt_worksheet_parser.add_argument('--location', type=str, default=None, help=arg_h['adapt-worksheet']['--location'])
    adapt_worksheet_parser.add_argument('--reference', type=str, default=None, help=arg_h['adapt-worksheet']['--reference'])

    convert_worksheet_parser = subparsers.add_parser('convert-worksheet', help=cmd_h['convert-worksheet'])
    convert_worksheet_parser.add_argument('input', type=str, help=arg_h['convert-worksheet']['input'])
    convert_worksheet_parser.add_argument('output', type=str, help=arg_h['convert-worksheet']['output'])
    convert_worksheet_parser.add_argument('--template', type=str, default=None, help=arg_h['convert-worksheet']['--template'])
    convert_worksheet_parser.add_argument('--reference', type=str, default=None, help=arg_h['convert-worksheet']['--reference'])


    args = parser.parse_args()

    # User called eliozo_client.py with no command-line arguments at all
    if args.command is None:
        parser.print_help()
        sys.exit(1)

    eliozo_client = EliozoClient(WEAVIATE_URL, WEAVIATE_API_KEY, OPENAI_API_KEY, FUSEKI_URL, FUSEKI_USER, FUSEKI_PASSWORD)
    eliozo_client.set_command(args.command)
    (retvalue, data) = (-1, None)

    if args.reference:
        eliozo_client.set_reference(args.reference)

    if args.command == 'add-metadata':
        provider = args.provider if args.provider else 'OpenAI'
        if args.output == None:
            print("--output is mandatory for add-metadata")
            sys.exit(1)
        (retvalue, data) = eliozo_client.add_metadata(args.markdown, args.property, provider, args.output)

    elif args.command == 'md-to-turtle':
        (retvalue, data) = eliozo_client.md_to_turtle(args.markdown, args.turtle)

    elif args.command == 'md-repository-to-turtle':
        if args.problemdata:
            (retvalue, data) = eliozo_client.md_repository_dir_to_turtle(args.output, args.problemdata)
        else:
            csv_value = args.csv
            csv_path = args.csv

            # If we receive URL, first download to output/spreadsheet.csv
            if not os.path.isfile(csv_value): 
                if csv_value.startswith("http"):
                    os.makedirs(args.output, exist_ok=True)
                    file_path = os.path.join(args.output, "spreadsheet.csv")
                    try:
                        r = requests.get(
                            csv_value,
                            stream=True,
                            timeout=30,
                            headers={"User-Agent": "csv-downloader/1.0", "Accept": "text/csv,text/plain,*/*;q=0.1"},
                        )
                        r.raise_for_status()

                        ctype = r.headers.get("Content-Type", "").split(";", 1)[0].lower()
                        if ctype == "text/html" or ("csv" not in ctype and not ctype.startswith("text/") and ctype not in ("application/octet-stream", "application/vnd.ms-excel")):
                            print(f"Error: URL did not return a downloadable CSV/plaintext file (Content-Type: {ctype or 'unknown'}).")
                        else:
                            os.makedirs(os.path.dirname(file_path) or ".", exist_ok=True)
                            with open(file_path, "wb") as f:
                                for chunk in r.iter_content(8192):
                                    if chunk:
                                        f.write(chunk)

                    except Exception as e:
                        print(f"Error: could not download to {file_path}: {e}")
                        sys.error(1)
                    csv_path = file_path
                else:
                    print(f"Parameter --csv should point to a file or a valid URL")
                    sys.error(1)
            (retvalue, data) = eliozo_client.md_repository_csv_to_turtle(args.output, csv_path)



    elif args.command == 'metadata-to-turtle':
        (retvalue, data) = eliozo_client.metadata_to_turtle(args.url, args.property, args.output)

    elif args.command == 'drop-rdf':
        (retvalue, data) = eliozo_client.drop_rdf(args.dataset)

    elif args.command == 'create-rdf-dataset': 
        (retvalue, data) = eliozo_client.create_rdf_dataset(args.dataset)

    elif args.command == 'ingest-rdf': 
        (retvalue, data) = eliozo_client.ingest_rdf(args.dataset, args.turtle)
    
    elif args.command == 'drop-vectors':
        (retvalue, data) = eliozo_client.drop_vectors(args.cluster)

    elif args.command == 'create-schema-vectors':
        (retvalue, data) = eliozo_client.create_schema_vectors(args.cluster)

    elif args.command == 'ingest-vectors':
        (retvalue, data) = eliozo_client.ingest_vectors(args.cluster, args.turtle)

    elif args.command == 'ingest-classifiers':
        (retvalue, data) = eliozo_client.ingest_classifiers(args.cluster, args.property, args.turtle)

    elif args.command == 'get-classifiers':
        (retvalue, data) = eliozo_client.get_classifiers()
        #(retvalue, data) = asyncio.run(eliozo_client.get_classifiers(args.query))

    elif args.command == 'create-task':
        retvalue = 0
        query_file = args.query
        with open(query_file, "r", encoding='utf-8') as file:
            content = file.read()
        (retvalue, data) = eliozo_client.create_task(content)

    elif args.command == 'set-topic': 
        (retvalue, data) = eliozo_client.set_topic(args.topic, args.level)

    elif args.command == 'set-style': 
        (retvalue, data) = eliozo_client.extract_style(args.property, args.value)

    elif args.command == 'get-problems-rdf':
        worksheet = args.worksheet if args.worksheet else 'worksheet.json'
        (retvalue, data) = eliozo_client.get_problems_rdf(worksheet)

    elif args.command == 'get-problems-vectors':
        worksheet = args.worksheet if args.worksheet else 'worksheet.json'
        (retvalue, data) = eliozo_client.get_problems_vectors(worksheet)

    elif args.command == 'get-problems':
        worksheet = args.worksheet if args.worksheet else 'worksheet.json'
        (retvalue, data) = eliozo_client.get_problems(worksheet)

    # elif args.command == 'drop-problem':
    #     (retvalue, data) = eliozo_client.drop_problem(args.problemID)

    # elif args.command == 'derive-problem':
    #     (retvalue, data) = eliozo_client.derive_problem(args.problemID)

    # elif args.command == 'extend-worksheet':
    #     (retvalue, data) = eliozo_client.extend_worksheet()

    elif args.command == 'adapt-worksheet':
        location = args.location if args.location else '*'
        (retvalue, data) = eliozo_client.adapt_worksheet(args.property, args.value, location)

    elif args.command == 'convert-worksheet':
        if args.template is None:
            template = get_json_field(args.reference, ["task", "template"])
        else: 
            template = args.template
        (retvalue, data) = eliozo_client.convert_worksheet(args.input, args.output, template)

    else:
        parser.print_help()
        print(f"Invalid Parameters: Command name '{args.command}' not supported.")
        sys.exit(3)

    if args.command in ['add-metadata', 'md-to-turtle', 'md-repository-to-turtle', 
                        'metadata-to-turtle', 'drop-rdf', 'create-rdf-dataset', 
                        'ingest-rdf', 'drop-vectors', 'create-schema-vectors', 
                        'ingest-vectors', 'ingest-classifiers']:
        eliozo_client.store_prelim(args.command, data)
    else: 
        eliozo_client.store_task(data)

    sys.exit(retvalue)


if __name__ == "__main__":
    load_dotenv()
    # Create your local .env file under $ProjectRoot/scripts with WEAVIATE_URL, WEAVIATE_API_KEY, OPENAI_API_KEY
    weaviate_url = os.getenv('WEAVIATE_URL', 'NA')
    weaviate_api_key = os.getenv('WEAVIATE_API_KEY', 'NA') 
    openai_api_key = os.getenv('OPENAI_API_KEY', 'NA')
    fuseki_url = os.getenv('FUSEKI_URL', 'NA')
    fuseki_user = os.getenv('FUSEKI_USER', 'NA')
    fuseki_password = os.getenv('FUSEKI_PASSWORD', 'NA')
    main(weaviate_url, weaviate_api_key, openai_api_key, fuseki_url, fuseki_user, fuseki_password)
