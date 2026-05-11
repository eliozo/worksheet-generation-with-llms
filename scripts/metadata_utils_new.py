import os
import sys
import re
import json
import requests
import time
from enum import Enum
from scripts.openai_utils import OpenaiUtils

class MetadataProperties(Enum):
    QUESTION_TYPE = "questionType"
    HAS_SOLUTION_STRUCTURE = "hasSolutionStructure"
    HAS_SOLUTION_CONCEPT = "hasSolutionConcept"
    DOMAIN = "domain"
    SUBDOMAIN = "subdomain"
    CONCEPTS = "concepts"
    TOPIC = "topic"
    METHOD = "method"
    COMPLEXITY = "complexity"

class MetadataUtils:
    def __init__(self, openai_api_key): 
        self.openai_api_key = openai_api_key
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {openai_api_key}'
        }

    def make_sys_instructions(self, property):
        if property == MetadataProperties.QUESTION_TYPE:
            return f"""
            You are a helpful assistant. Respond only with a valid JSON object like:
            {{"uzdevuma_tips": "Prove"}}. Do not explain anything.
            """
        elif property == MetadataProperties.DOMAIN:
            return f"""
            You are a helpful assistant. Respond only with a valid JSON object like:
            {{"domain": "Alg"}}. Do not explain anything.
            """
        elif property == MetadataProperties.HAS_SOLUTION_STRUCTURE:
            return f"""
            You are a helpful assistant. Respond only with a valid JSON object like:
            {{"hasSolutionStructure": "eliozo:FindAll"}}. Do not explain anything.
            """
        elif property == MetadataProperties.HAS_SOLUTION_CONCEPT:
            return f"""
            You are a helpful assistant. Respond only with a valid JSON object like:
            {{"solutionConcepts": ["PrimeNumbers", "DivisibilityRelation", "ParityInvariant"]}}.
            Do not explain anything.
            """
    
    def make_prompt(self, property, title, problem_text, solution_text=""):
        if property == MetadataProperties.QUESTION_TYPE:
            return f"""
            Lūdzu, atrodi matemātikas uzdevuma tipu.
            Atbildi **tikai** ar JSON formātā: {{"uzdevuma_tips": "..."}}.
            Uzdevuma nosaukums:

            {problem_text.strip()}

            Iespējamie jautājumu tipi ir:
            'FindAll' (uzdevumi, kuros jāatrod visi atrisinājumi);
            'FindCount' (uzdevumi, kuros jāsaskaita cik iespēju vai atrisinājumu skaits); 
            'FindOptimal' (uzdevumi, kuros jāatrod maksimālais vai minimālais risinājums); 
            'FindExample' (uzdevumi, kuros jāatrod 1 piemērs vai pretpiemērs); 
            'Prove' (uzdevumi, kuros jāpierāda apgalvojums); 
            'ProveDisprove' (uzdevumi, kuros apgalvojums ir jāpierāda vai jāapgāž); 
            'Algorithm' (uzdevumi, kuros jāatrod procedūra vai spēles stratēģija).
            """

        if property == MetadataProperties.HAS_SOLUTION_STRUCTURE: 
            return f"""
            Lūdzu, atrodi uzdevuma jautājumam atbilstošo atrisinājuma struktūru.
            Atbildi **tikai** ar JSON formātā: {{"hasSolutionStructure": "..."}}.
            Uzdevums:

            ```{problem_text.strip()}```

            Iespējamās atrisinājumu struktūras ir:

            * 'eliozo:FindAll' (Uzdevumi, kur jāatrod visi atrisinājumi. 
              Jautājumu piemēri: "Kāds var būt...?", "Cik...?", "Atrisināt vienādojumu". 
              Atrisinājumā norādāmas visas atbildes + pierādījums, ka citu nav.)
            * 'eliozo:FindOptimal' (Uzdevumi, kur jāatrod maksimālā vai minimālā vērtība.
              Jautājumu piemēri: "Kāds lielākais (mazākais)...?".
              Atrisinājumā dots piemērs, kas dod optimālo vērtību + pierādījums, ka labāka nav.) 
            * 'eliozo:ProveOrDisproveExists' (Uzdevumi, kur jāpierāda vai jāapgāž eksistence.
              Jautājumu piemēri: "Vai var...?", "Vai iespējams...?", "Vai eksistē...?"
              vai arī "Pierādiet, ka eksistē...". 
              Atrisinājumā vai nu 'Jā' (un piemērs) vai 'Nē' (vispārīgs pierādījums, kāpēc neeksistē).
            * 'eliozo:ProveOrDisproveForAll' (Uzdevumi, kur jāpierāda vai jāapgāž vispārīgs apgalvojums.
              Jautājumu piemēri: "Vai visiem...?", "Vai noteikti...?" 
              vai arī "Pierādiet, ka visiem...", "Pamatojiet, ka...". 
              Atrisinājumā vai nu 'Jā' (vispārīgs pierādījums) vai 'Nē' (pretpiemērs)). 
            * 'eliozo:ConstructOrDescribe' (Uzdevumi, kur jāatrod konstrukcija algoritms vai spēles stratēģija.
              Jautājumu piemēri: "Parādi, kā...", "Apraksti stratēģiju...", "Kā svērt..." 
              vai arī "Pierādiet, ka var...", ja sagaidāms konstruktīvs pamatojums. 
              Atrisinājumā ir konstrukcija/algoritms + pārbaude, ka tā vienmēr strādā.
            """

        elif property == MetadataProperties.HAS_SOLUTION_CONCEPT:
            concepts_csv = ""
            current_dir = os.path.dirname(os.path.abspath(__file__))
            concepts_path = os.path.join(current_dir, 'setup', 'resources', 'concepts.csv')
            try:
                with open(concepts_path, 'r', encoding='utf-8') as f:
                    concepts_csv = f.read()
            except Exception as e:
                print(f"Warning: could not read concepts.csv: {e}")

            return f"""
            Lūdzu, identificē matemātiskos jēdzienus un struktūras, kas parādās šajā uzdevumā
            vai ir nepieciešami tā risināšanai. 

            Uzdevums: "{title.strip()}"

            ```{problem_text.strip()}```

            Atrisinājums:

            ```{solution_text.strip()}```

            Pieejamo jēdzienu saraksts (CSV formātā ar kolonnām 
            Label, TitleLv, TitleEn, DescriptionLv, Domain, ConceptGroup, Grade):

            ```
            {concepts_csv}
            ```
            
            ## Norādījumi atlasei

            **Ko atlasīt.** Atlasi tos jēdzienus, kurus uzdevuma risinātājam ir 
            jāatpazīst uzdevuma tekstā vai jāizmanto risinājumā. Tie var būt:
            - jēdzieni, kas tieši nosaukti uzdevuma formulējumā 
            (piem., "naturāls skaitlis", "trijstūris", "pirmskaitlis");
            - matemātiskās struktūras, kas slēpjas aiz vārdiskā formulējuma 
            (piem., "pilsētas un aviolīnijas" → GraphConcept; 
            "skolēni saka patiesību vai melo" → TruthTellersAndLiars; 
            "pārkārto ciparus" → DigitRepresentation);
            - struktūras, ko risinājumā nepieciešams ieviest, lai uzdevumu atrisinātu 
            (piem., uzdevumā par monētu svēršanu var nebūt vārda "grafs", 
            bet risinājumā parādās lēmumu koks → DecisionTree).

            **Cik daudz jēdzienu atlasīt.** Tipiski 2-5 jēdzieni vienam uzdevumam. 
            Mērķis ir atrast būtiskākos, ne visus iespējami saistītos. Ja uzdevums 
            ir vienkāršs (piemēram, dalāmības pārbaude), pietiek ar 1-2 jēdzieniem; 
            sarežģītākos olimpiāžu uzdevumos var būt 4-6.

            **No kā izvairīties.**
            - Neuzskaiti jēdzienus, kas ir tikai netieši klātesoši (piem., 
            ja uzdevumā ir vārds "skaitlis", tas pats par sevi nenozīmē, 
            ka jāmin PositiveIntegers, ja vien skaitļu kopa nav būtiska).
            - Neatlasi tādus jēdzienus, kuru `Grade` ir krietni lielāks par 
            uzdevuma virsrakstā norādīto klasi 
            Meklē vienkāršāku alternatīvu, ar kuru pietiek (piem., 
            dod priekšroku ParityInvariant nevis 
            ModularArithmetic 5. klases uzdevumā).
            Klase dota virsrakstā, piemēram "LV.AMO.2024.7.5" norāda uz "7.klases" uzdevumu.

            - Neatlasi visu attiecīgās ConceptGroup saturu — atlasi tikai tos 
            konkrētos jēdzienus, kas patiešām piedalās uzdevumā.

            **Identifikatoru pieraksts.** Atbildē izmanto tieši tos Label, 
            kas parādās CSV failā. Saglabā precīzu rakstību (CamelCase, bez 
            atstarpēm). Ja nepieciešamais jēdziens CSV failā nav atrodams, 
            izlaid to (vēlāk papildināsim sarakstu).
            
            **Lasāmība (readingDifficulty):** "low", ja uzdevumā matemātiskie 
            jēdzieni saukti parastajos vārdos; "medium", ja uzdevumā izmantoti 
            daži standarti teksta uzdevumu paņēmieni (velosipēdisti, kas ilustrē 
            vienmērīgu kustību; monētu svēršana, kas ilustrē salīdzināšanas darbības). 
            "high", ja uzdevumā lasītājam ir aktīvi jāinterpretē teksts, nestandartā 
            veidā jāatrod jēdzieni un modeļi, kuri der dotajā situācijā.

            **Atbildes formāts.** Atgriež **tikai** JSON objektu ar divām atslēgām: 
            (1) `concepts`, kuras vērtība ir Label saraksts. Saraksta secība — 
            no būtiskākā uz mazāk būtisko. 
            (2) `readingDifficulty`: <low|medium|high>
            Neiekļauj paskaidrojumus, komentārus vai citus laukus.

            Atbildes piemērs:
            ```{{"concepts": ["TruthTellersAndLiars", "LogicalCaseAnalysis", "ExhaustiveCheck"], 
                 "readingDifficulty": "medium"}}```
            """

    def classify_problem(self, title, problem_text, problem_solution, property):
        prompt = self.make_prompt(property, title, problem_text, problem_solution)
        system_message = self.make_sys_instructions(property)
        openaiUtils = OpenaiUtils(self.openai_api_key)
        result = openaiUtils.json_request(prompt, system_message, 42)
        
        if property == MetadataProperties.HAS_SOLUTION_CONCEPT:
            if isinstance(result, str):
                match = re.search(r'\{.*?\}', result, re.DOTALL)
                if match:
                    try:
                        result = json.loads(match.group(0))
                    except:
                        pass
            return result

        json_key = 'uzdevuma_tips'
        if property == MetadataProperties.HAS_SOLUTION_STRUCTURE:
            json_key = 'hasSolutionStructure'
        elif property == MetadataProperties.DOMAIN:
            json_key = 'domain'
            
        try:
            return result.get(json_key, 'NA')
        except AttributeError:
            pass # result might be a string
        except json.JSONDecodeError:
            pass
            
        if isinstance(result, str):
            match = re.search(r'\{.*?\}', result, re.DOTALL)
            if match:
                try:
                    parsed_result = json.loads(match.group(0))
                    return parsed_result.get(json_key, 'NA')
                except:
                    return "NA"
        return "NA"


input_md_file = 'C:/Users/eozolina/Documents/workspace-private/nms-uzdevumi/lv-vol-2019/content.md'
output_md_file = 'C:/Users/eozolina/Documents/workspace-private/nms-uzdevumi/lv-vol-2019/content_with_questiontypes.md'

def classify_markdown_file(self, input_md_path, output_md_path, prop="questionType"):
    print(f"🔍 Reading: {input_md_path}")
    problems = self._extract_sections_from_md(input_md_path)
    updated_sections = []

    for title, full_problem in problems:
        # Apstrādā to vietu, ja md failā jau eksistē questionType
        if "_questionType:" in full_problem:
            print(f"Skipping {title} — already has _questionType.")
            updated_sections.append(f"# <lo-sample/> {title}\n\n{full_problem.strip()}\n")
            continue

        print(f"\nClassifying task: {title}")
        
        clean_problem = self._normalize_text(full_problem)

        try:
            response = self.classify_problem(clean_problem, "", prop)
            if isinstance(response, dict):
                predicted_qtype = response.get("uzdevuma_tips", "NA")
            else:
                predicted_qtype = "NA"
        except Exception as e:
            print(f"Error for {title}: {e}")
            predicted_qtype = "NA"

        updated = self._add_generated_question_type(full_problem, predicted_qtype)
        updated_sections.append(f"# <lo-sample/> {title}\n\n{updated.strip()}\n")

    with open(output_md_path, 'w', encoding='utf-8') as out:
        out.write("\n\n".join(updated_sections))
    print(f"\nOutput saved to: {output_md_path}")

def extract_sections_from_md(self, filepath):
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

def normalize_text(self, text):
    meta_start = text.find('<small>')
    return text[:meta_start].strip() if meta_start > 0 else text.strip()

def add_generated_question_type(self, md_text, generated_qtype):

    small_block_re = re.compile(r'(<small>)(.*?)(</small>)', re.DOTALL)
    match = small_block_re.search(md_text)

    if not match:
        return md_text  # no <small> block found

    before_tag = match.group(1)
    middle_block = match.group(2)
    after_tag = match.group(3)

    if "_questionType:" in middle_block:
        return md_text

    updated_middle = "\n\n" + middle_block.strip() + f"\n* _questionType: {generated_qtype}\n\n"

    return (
        md_text[:match.start()] +
        before_tag + updated_middle + after_tag +
        md_text[match.end():]
    )

if __name__ == '__main__':
    api_key = os.environ.get("OPENAI_API_KEY") or "sk-your-key-here"
    metadata_utils = MetadataUtils(api_key)

    problemList = extract_sections_from_md(input_md_file)
    updated_sections = []

    for (title, full_problem) in problemList:
        clean_problem = normalize_text(full_problem)
        try:
            predicted_qtype = metadata_utils.classify_problem(clean_problem, "", 'questionType')
        except Exception as e:
            print(f"Error with {title}: {e}")
            predicted_qtype = 'NA'

        new_section = add_generated_question_type(full_problem, predicted_qtype)
        updated_sections.append(f'# <lo-sample/> {title}\n\n{new_section.strip()}\n')

        print(f'Processed: {title} | _questionType: {predicted_qtype}')

    with open(output_md_file, 'w', encoding='utf-8') as out:
        out.write('\n\n'.join(updated_sections))

    print(f'Output written to: {output_md_file}')
