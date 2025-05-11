from enum import Enum
import json
import os

from scripts.openai_utils import OpenaiUtils
from scripts.style_rules_utils import StyleRulesUtils

class AdaptExtension(Enum):
    TITLE = "Title"
    THEORY = "Theory"
    STYLE_RULES = "AmandaRules"
    SHORTENED_SOLUTIONS = "ShortenedSolutions"
    CONCEPTS = "Concepts"
    HINTS = "Hints"
    INSTRUCTOR_NOTES = "InstructorNotes"

# Consider merging this class with OpenaiUtils. 
class AdaptUtils: 
    openai_api_key = "NA"
    prompts = {
        AdaptExtension.THEORY: """Consider the following collection of math problems: 
        ```{input}```
        Please return an extended JSON structure containing the given  
        snippets (problems and solutions), and add additional snippets - 
        theorems and (optionally) proofs of these theorems that may be 
        necessary for subsequent proofs.

        Do NOT change the original JSON snippets (problems, solutions) 
        in any way and preserve them all 
        in your response. Do not change the order of problems and solutions.
        For example, if the input looks like this:
        ```
        {{ "snippets": [
        {{ "type": "problem", "value": "PROB.ID.1. Pulciņā ir $13$ skolēni. Pierādīt, ka starp tiem atradīsies divi, kas dzimuši tajā pašā mēnesī." }},
        {{ "type": "solution", "value": "$13$ skolēnus sadala $12$ grupās (atkarībā no dzimšanas mēneša). Pēc Dirihlē principa noteikti būs mēnesis, kurā ir dzimuši vismaz divi skolēni." }},
        {{ "type": "problem", "value": "PROB.ID.2. Pierādīt, ka starp septiņiem naturāliem skaitļiem var izvēlēties tādus divus, kuru starpība dalās ar $7$." }},
        {{ "type": "solution", "value": "Naturālis skaitlis, dalot ar $7$, var dot kādu no sekojošiem atlikumiem: $0; 1; 2; 3; 4; 5; 6$. Dotos astoņus skaitļus uzskatām par „trušiem”, savukārt vienā 'būri' ievietosim tos skaitļus, kad vienādās atlikumu dalījumi ar $7$, tādai ir $7$ 'būru' principi: pēc Dirihlē principa 'būri' nonāks vismaz divi 'truši' jeb vismaz divi skaitļi dod vienādus atlikumus, dalot ar $7$. Šo skaitļu starpība dalās ar $7$." }}, 
        ]}}
        ```
        then your output could be formatted like this:
        ```
        {{ "snippets": [
        {{ "type": "theorem", "value": "**Dirihlē princips**: Ja $n$ priekšmeti jāsadala pa $m$ kastēm un ja $n > m$, tad vismaz vienā kastē nonāk ne mazāk kā divi priekšmeti." }},
        {{ "type": "proof", "value": "Pieņemsim pretējo: katrā no $m$ kastēm ir ne vairāk kā viens priekšmets. Tad kopā būtu ne vairāk kā $m$ priekšmeti. Bet mums ir $n > m$ priekšmeti, kas būtu pretruna. Secinām, ka vismaz vienā kastē ir vismaz divi priekšmeti." }},
        {{ "type": "problem", "value": "PROB.ID.1. Pulciņā ir $13$ skolēni. Pierādīt, ka starp tiem atradīsies divi, kas dzimuši tajā pašā mēnesī." }},
        {{ "type": "solution", "value": "$13$ skolēnus sadala $12$ grupās (atkarībā no dzimšanas mēneša). Pēc Dirihlē principa noteikti būs mēnesis, kurā ir dzimuši vismaz divi skolēni." }},
        {{ "type": "theorem", "value": "Ja divi veseli skaitļii dod vienādus atlikumus, dalot ar naturālu skaitli $n$, tad šo skaitļu starpība dalās ar $n$." }},
        {{ "type": "proof", "value": "Pieņemsim, ka skaitļu $a$ un $b$ atlikumi, dalot ar $n$ ir vienādi. Tad $a \\\\equiv b \\\\; \\\\pmod n$, tāpēc 
        $a - b \\\\equiv 0 \\; \\\\pmod n$, proti, skaitļa $a - b$ atlikums, dalot ar $n$, ir 0." }},
        {{ "type": "problem", "value": "PROB.ID.2. Pierādīt, ka starp septiņiem naturāliem skaitļiem var izvēlēties tādus divus, kuru starpība dalās ar $7$." }},
        {{ "type": "solution", "value": "Naturālis skaitlis, dalot ar $7$, var dot kādu no sekojošiem atlikumiem: $0; 1; 2; 3; 4; 5; 6$. Dotos astoņus skaitļus uzskatām par „trušiem”, savukārt vienā 'būri' ievietosim tos skaitļus, kad vienādās atlikumu dalījumi ar $7$, tādai ir $7$ 'būru' principi: pēc Dirihlē principa 'būri' nonāks vismaz divi 'truši' jeb vismaz divi skaitļi dod vienādus atlikumus, dalot ar $7$. Šo skaitļu starpība dalās ar $7$." }}, 
        ]}}
        ```
        The theorems you insert should remind about math results that are being used in 
        subsequent proofs implicitly or explicitly.
        Newly inserted theorems should be inserted BEFORE the problem where they are 
        used. A theorem should NOT be inserted in-between a problem and 
        its solution.  
        """, 
        AdaptExtension.TITLE: """Consider the following collection of math problems: 
        ```{input}```
        Please summarize the problems and any accompanying texts in a short title 
        (about 2 to 7 words). Please return your response as a JSON structure 
        like this: 
        ```
        {{ "snippets": [
        {{ "type": "title", "value": "Insert your suggested title here" }}
        ]}}
        ```
        Your JSON should not contain any other information - just this array 
        of a single snippet.
        """,
        AdaptExtension.STYLE_RULES: """Consider the following style rules how to 
        improve a math worksheet in Latvian:
        ```
        {rules}
        ```
        (1) "id" is a unique identifier for a style rule; 
        (2) "original" shows an example sentence - how some problematic sentence is likely to appear. The most characteristic phrases are highlighted with asterisks and provided with numbers (1), (2), or (3). Sometimes "original" combines several problematic things -- they may appear in isolation as well. 
        (3) "modified" shows how to fix the style in this sentence. 
        (4) "explanations" provide additional comments - the reasoning behind the replacements in English. 

        Consider the following JSON file containing a worksheet: 
        ```
        {input}
        ```
        If any snippet has "value" that is somewhat similar to the "original" for any of the rules (contains phrases similar to the ones highlighted with the asterisks), please insert that snippet into your response; insert (1), (2), or (3) when appropriate, also provide suggested fix as "value_fixed" and "rule" - which rule was applied. For example, if the original snippet is this: 
        ```
        {{ "snippets": [
        {{ "type": "problem", "value": "Vai pozitīva skaitļa kvadrātsakne noteikti ir mazāka par pašu skaitli?" }}
        }}
        ```
        then replace it by this: 
        ```
        {{ "snippets": [
        {{ "type": "problem", "value": "Vai pozitīva skaitļa kvadrātsakne noteikti ir (1) mazāka par pašu skaitli?", "value_fixed": "Vai pozitīva skaitļa kvadrātsaknei noteikti jābūt mazākai par pašu skaitli?", rule:"P006E" }}
        }}
        ```
        """

    }
    sysmessages = {
        AdaptExtension.THEORY: """Please return your response as JSON structure with 
        a single key "snippets" pointing to an array of snippets as shown in the prompt. 
        All the snippets from the input file are preserved; snippets of type 
        "theorem" and "proof" should be inserted whenever appropriate.

        The new snippets should be formatted as Markdown with LaTeX formulas 
        enclosed between dollar signs ($) and 
        properly escaped. Please remember that all LaTeX commands involving 
        backslashes should have doubled backslashes in your JSON output to avoid 
        breaking the syntax of JSON.
        For example, "$n \\\\leq m$" is preferred compared to 
        "n ≤ m".
        """, 
        AdaptExtension.TITLE: """Please return your response as JSON structure with 
        a single key "snippets" pointing to an array of snippets 
        of length 1. It should contain a snippet of type "title" - your suggested 
        title becomes the "value" of this snippet. 
        Try to write the title in concise and accurate Latvian lanugage; 
        do not use math expressions in the title.""", 
        # AdaptExtension.STYLE_RULES: """Please return the JSON dictionary snippets array with one key "snippets" 
        # mapped to an array with all the style fixed like this:
        # ```
        # { "snippets": [
        # { "type": "problem", "value": "Vai pozitīva skaitļa kvadrātsakne noteikti ir (1) mazāka par pašu skaitli?", "value_fixed": "Vai pozitīva skaitļa kvadrātsaknei noteikti jābūt mazākai par pašu skaitli?", rule:"P006E" }, 
        # // ... 
        # ]}
        # ```
        # "value" should be taken from the original "snippets" JSON (unchanged). 
        # "rule" should point to an existing rule in the given list of style rules."""
        AdaptExtension.STYLE_RULES: """Please return JSON dictionary with one key "snippets" 
        mapped to an array with all the style fixes like this:
        ```
        { "snippets" : [{
        "type": "solution",
        "value": "Ja katrā mēnesī būtu dzimis ne vairāk kā viens skolēns, tad visos mēnešos kopā būtu dzimuši ne vairāk kā $12$ skolēnu, bet pulciņā ir $13$ skolēni. Tātad noteikti ir tāds mēnesis, kurā dzimuši vismaz divi no šī pulciņa skolēniem.",
        "value_fixed": "Ja katrā mēnesī būtu dzimis ne vairāk kā viens skolēns, tad visos mēnešos kopā būtu dzimuši ne vairāk kā $12$ skolēnu, bet pulciņā ir $13$ skolēni. Tātad noteikti jābūt tādam mēnesim, kurā dzimuši vismaz divi no šī pulciņa skolēniem.",
        "rule": "P006L"
        },
        {
        "type": "solution",
        "value": "Ievērosim, ka skaitli 5 var izteikt kā trīs naturālu skaitļu summu tikai divos veidos: $3 + 1 + 1$ un $2 + 2 + 1$ (ja nav būtiska saskaitāmo secība). Taču, ņemot vērā arī to, kura no konfetēm pirmajā gadījumā ir dāvināta 3 eksemplāros un kura no konfektem otrajā gadījumā -- vienā eksemplārā, iegūstam 6 dažādas iespējas:\n\n![](pigeonhole_2025_page2A.png)\n\nTā kā ir 7 rūķīši un 6 dažādas iespējas, kā uzdāvināt konfektes, tad pēc Dirihlē principa noteikti ir tādi divi rūķīši, kam Sniegbaltīte uzdāvināja vienādas konfekšu komplektus.",
        "value_fixed": "Ievērosim, ka skaitli 5 var izteikt kā trīs naturālu skaitļu summu tikai divos veidos: $3 + 1 + 1$ un $2 + 2 + 1$ (ja nav būtiska saskaitāmo secība). Taču, ņemot vērā arī to, kura no konfetēm pirmajā gadījumā ir dāvināta 3 eksemplāros un kura no konfektem otrajā gadījumā -- vienā eksemplārā, iegūstam 6 dažādas iespējas:\n\n![](pigeonhole_2025_page2A.png)\n\nTā kā ir 7 rūķīši un 6 dažādas iespējas, kā uzdāvināt konfektes, tad pēc Dirihlē principa noteikti jābūt diviem rūķīšiem, kam Sniegbaltīte uzdāvināja vienādas konfekšu komplektus.",
        "rule": "P006L"
        }]
        }
        ```
        """
    }


    def __init__(self, OPENAI_API_KEY):
        self.openai_api_key = OPENAI_API_KEY

    def extend(self, input_worksheet, extension_value):
        if isinstance(extension_value, AdaptExtension):
            print(f"Applying extension {extension_value} to {input_worksheet}")
        else:
            raise ValueError("Invalid extension value")
        
        with open(input_worksheet, 'r', encoding='utf-8') as file:
            input_content = file.read()

        openaiUtils = OpenaiUtils(self.openai_api_key)
        promptTemplate = self.prompts[extension_value]

        if extension_value == AdaptExtension.STYLE_RULES:
            styleRulesUtils = StyleRulesUtils(self.openai_api_key)
            if os.path.exists("rules.json"):
                print("File rules.json exists; skipping download")
            else:
                url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQaIJcHTzwXoWefYcfgrHU1NX5zzwLYDRY5NIW09i6bYt7EnWvuGFP9M_8-idBvBgxAaKzecTOAkP82/pub?gid=0&single=true&output=csv"
                rules_file = "rules.json"
                styleRulesUtils.download_rules(url, rules_file)
            with open("rules.json", 'r', encoding='utf-8') as file:
                rules_content = file.read()
            prompt = promptTemplate.format(rules = rules_content, input = input_content)
        else:
            prompt = promptTemplate.format(input = input_content)

        system_message = self.sysmessages[extension_value]
        output_json = openaiUtils.json_request(prompt, system_message, 42)

        return output_json

