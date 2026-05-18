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
    HAS_REASONING_METHOD = "hasReasoningMethod"
    HAS_REASONING_MISTAKE = "hasReasoningMistake"
    DOMAIN = "domain"
    SUBDOMAIN = "subdomain"
    CONCEPTS = "concepts"
    TOPIC = "topic"
    METHOD = "method"
    COMPLEXITY = "complexity"

class MetadataUtils:
    def __init__(self, openai_api_key, provider=None): 
        self.openai_api_key = openai_api_key
        self.provider = provider
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {openai_api_key}'
        }
        self.subdomains = self._load_subdomains()
        self.reasoning_methods = self._load_reasoning_methods()
        self.reasoning_mistakes = self._load_reasoning_mistakes()

    def _load_reasoning_methods(self):
        methods_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'setup', 'reasoning_methods')
        domain_file_map = {
            'Alg': 'alg_reasoning_methods.md',
            'Comb': 'comb_reasoning_methods.md',
            'Geom': 'geom_reasoning_methods.md',
            'NT': 'nt_reasoning_methods.md',
        }
        result = {}
        for domain_code, filename in domain_file_map.items():
            filepath = os.path.join(methods_dir, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    result[domain_code] = f.read()
            except Exception as e:
                print(f"Warning: could not read {filepath}: {e}")
                result[domain_code] = ''
        return result

    def _load_reasoning_mistakes(self):
        mistakes_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'setup', 'reasoning_mistakes')
        domain_file_map = {
            'Alg': 'alg_reasoning_mistakes.md',
            'Comb': 'comb_reasoning_mistakes.md',
            'Geom': 'geom_reasoning_mistakes.md',
            'NT': 'nt_reasoning_mistakes.md',
        }
        result = {}
        for domain_code, filename in domain_file_map.items():
            filepath = os.path.join(mistakes_dir, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    result[domain_code] = f.read()
            except Exception as e:
                print(f"Warning: could not read {filepath}: {e}")
                result[domain_code] = ''
        return result


    def _load_subdomains(self):
        subdomin_list = []
        csv_path = os.path.join(os.path.dirname(__file__), 'setup/resources/skos-domains.csv')
        try:
            with open(csv_path, 'r', encoding='utf-8') as f:
                import csv
                reader = csv.DictReader(f)
                for row in reader:
                    label = row.get('Label')
                    desc = row.get('DescriptionLv') or row.get('DescriptionEn')
                    l1 = row.get('L1', '')
                    
                    branch = "Other"
                    if l1 == '1': 
                        branch = "Algebra"
                    elif l1 == '2': 
                        branch = "Combinatorics"
                    elif l1 == '3': 
                        branch = "Geometry"
                    elif l1 == '4': 
                        branch = "NumberTheory"

                    if label:
                        subdomin_list.append({
                            "label": label,
                            "desc": desc,
                            "branch": branch,
                            "formatted": f"{label} [Branch: {branch}] ({desc})"
                        })
        except Exception as e:
            print(f"Error loading subdomains: {e}")
        return subdomin_list

    def make_sys_instructions(self, property):
        if property == MetadataProperties.QUESTION_TYPE:
            return f"""
            Respond only with a valid JSON object like:
            {{"uzdevuma_tips": "Prove"}}. Do not explain anything.
            """
        elif property == MetadataProperties.DOMAIN:
            return f"""
            You are a helpful assistant. Respond only with a valid JSON  
            object like: {{"domain": ["Alg"]}}. Do not explain anything.
            """
        elif property == MetadataProperties.HAS_SOLUTION_STRUCTURE:
            return f"""
            You are a helpful assistant. Respond only with a valid JSON object like:
            {{"hasSolutionStructure": "eliozo:FindAll"}}. Do not explain anything.
            """
        elif property == MetadataProperties.HAS_SOLUTION_CONCEPT:
            return f"""
            You are a helpful assistant. Respond only with a valid JSON object like:
            {{"solutionConcepts": ["PrimeNumbers", "DivisibilityRelation", "ParityInvariant"], 
            "readingDifficulty": <"low"|"medium"|"high"> }}.
            Do not explain anything.
            """
        elif property == MetadataProperties.SUBDOMAIN:
            return f"""
            Respond only with a valid JSON object like:
            {{"subdomain": ["DOM_Inequalities"], "subdomain_alternative": "My_Label"}}. 
            Do not append any additional text to the JSON object.
            """
        elif property == MetadataProperties.HAS_REASONING_METHOD:
            return f"""
            You are a helpful assistant. Respond only with a valid JSON object like:
            {{"methods": ["MethodLabel1", "MethodLabel2"], "newMethod": null}}.
            Do not explain anything.
            """
        elif property == MetadataProperties.HAS_REASONING_MISTAKE:
            return f"""
            You are a helpful assistant. Respond only with a valid JSON object like:
            {{"mistakes": ["MistakeLabel1", "MistakeLabel2"], "mistakesFit": <"low"|"medium"|"high">}}.
            Do not explain anything.
            """
    
    def make_prompt(self, property, title, problem_text, solution_text="", meta_dict=None):
        if property == MetadataProperties.QUESTION_TYPE:
            return f"""
            Atrodi matemātikas uzdevuma tipu.
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
        
        elif property == MetadataProperties.DOMAIN:
            return f"""
            Atrodi matemātikas uzdevuma nozari (domain).
            Ir 4 galvenās nozares: 
            * Algebra - darbības ar skaitļiem (it īpaši, ja nav 
              uzsvērts, ka skaitļi ir veseli un nav jāaplūko dalāmības 
              attiecība un atlikumi). 
              Arī teksta uzdevumi, kam veido algebrisku modeli. 
            * Kombinatorika - uzdevumi par objektu skaitīšanu un izlasēm 
              galīgās kopās. Arī algoritmu veidošana un vairums 
              spēļu stratēģiju, ja spēles objekti tieši neattiecas uz citu nozari.  
            * Ģeometrija - uzdevumi par plaknes un telpas figūrām, 
              leņķiem, attālumiem, laukumiem, tilpumiem.
              Arī figūru konfigurācijas un kombinatoriskā ģeometrija ar 
              rūtiņām, krāsojumiem, simetriju utml.
            * Skaitļu teorija - uzdevumi par veseliem skaitļiem. 
              Arī uzdevumi par pierakstu decimālajā un citās skaitīšanas 
              sistēmās un ciparu rēbusi. Veselu skaitļu spēles. 

            Retos gadījumos var būt uzdevums vairākās nozarēs vienlaikus
            (piemēram, kvadrātvienādojuma saknes kļūst par nogriežņu 
            garumiem). Šādos gadījumos jāatgriež 
            saraksts, piemēram: {{"domain": ["Alg", "Geom"]}}, 
            sākot ar svarīgāko nozari. 
            
            Uzdevuma teksts:

            ```
            {problem_text.strip()}
            ```

            Nozares apzīmē šādi:
            'Alg' (algebra);
            'Comb' (kombinatorika);
            'Geom' (ģeometrija);
            'NT' (skaitļu teorija).

            Biežākais atbildes formāts:
            {{
                "domain": ["Alg"]
            }}

            Rets atbildes formāts, ja uzdevums būtiski pieder 2 nozarēm:
            {{
                "domain": ["Alg", "Comb"]
            }}

            Atbildē neiekļauj paskaidrojumus, komentārus vai citus laukus.
            """

        elif property == MetadataProperties.SUBDOMAIN:
            subdomain_str = "\\n".join([item['formatted'] for item in self.subdomains])
            return f"""
            Atrodi uzdevumam atbilstošāko apakšnozari (subdomain).
            
            1. Atbildi **tikai** ar JSON formātā.
            2. "subdomain" laukā ievieto sarakstu (array) ar vienu vai vairākām atbilstošām 
               apakšnozarēm no saraksta. Gandrīz vienmēr (95% gadījumu) ir tikai viena vērtība, bet dažreiz uzdevuma 
               teksts var atbilst 2 apakšnozarēm.
            3. Retos gadījumos, kad esošās apakšnozares neapraksta uzdevumu precīzi, 
                vari piedāvāt savu variantu laukā "subdomain_alternative" (piemēram, kā "Domain_XYZ").
            4. Uzdevumos par veseliem skaitļiem dodiet priekšroku apakšnozarēm, kam [Branch: NumberTheory].
               Uzdevumos par reāliem skaitļiem dodiet priekšroku apakšnozarēm, kam [Branch: Algebra].
            
            Piemērs 1 (visbiežākais atbildes formāts):
            {{
                "subdomain": ["DOM_And_So_On"]
            }}

            Piemērs 2 (reti - ja pieder 2 apakšnozarēm; nelieto 3 vai vairāk apakšnozares):
            {{
                "subdomain": ["DOM_And_So_On", "DOM_Another_One"]
            }}

            Piemērs 3 (reti - ja esošās apakšnozares neapraksta uzdevumu precīzi):
            {{
                "subdomain": ["DOM_Best_Guess"],
                "subdomain_alternative": "Domain_XYZ"
            }}

            Uzdevums:
            {problem_text.strip()}

            Iespējamās apakšnozares ir:
            {subdomain_str}
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
        
        elif property == MetadataProperties.HAS_REASONING_METHOD:
            if meta_dict is None:
                meta_dict = {}
            domain_list = meta_dict.get('domain', [])
            domain = domain_list[0] if domain_list else 'Comb'
            domain_methods = self.reasoning_methods.get(domain, '')

            return f"""
            Lūdzu, identificē spriedumu un secināšanas metodes, kas faktiski izmantotas šī uzdevuma
            oficiālajā atrisinājumā. Uzdevuma matemātiskā nozare ir **{domain}**.
            
            Uzdevums: "{title.strip()}"
            
            ```{problem_text.strip()}```
            
            Atrisinājums:
            
            ```{solution_text.strip()}```
            
            Pieejamo spriedumu metožu saraksts (Markdown formātā, ar CamelScript Label, īsu nosaukumu
            latviski un angliski, vienas rindkopas aprakstu un 2–3 raksturīgiem piemēriem):
            
            ```
            {domain_methods.strip()}
            ```
            
            ## Norādījumi atlasei
            
            **Ko atlasīt.** Atlasi tās metodes no saraksta, kuras patiešām tiek lietotas atrisinājumā kā
            spriedumu solis vai pamatojuma paņēmiens. Tās var būt:
            - skaidri saskatāmas metodes (piem., risinājumā parādās leņķu izteikšana ar mainīgo $\\alpha$
            un trijstūra leņķu summas izmantošana → AngleChasing un TriangleAngleSum; vai ciparu summa
            tiek pārbaudīta dalāmībai ar 9 → DigitSumProperty);
            - metodes, kas atrisinājumā ir izmantotas implicīti, bet kuru loģiskā funkcija ir skaidra
            (piem., autors nesaka "pierādījums no pretējā", bet sāk ar "pieņemsim pretējo, ka...");
            - pamata aritmētiskās vai algebriskās identitātes, kas izmantotas pārveidojumos
            (piem., kvadrātu starpība $a^2 - b^2 = (a-b)(a+b)$ → FactoringAlgebraicExpressions).
            
            **Cik daudz metožu atlasīt.** Tipiski 2–5 metodes vienam uzdevumam. Olimpiāžu uzdevums
            parasti izmanto vairākas metodes vienlaikus — piemēram, leņķu meklēšana savienota ar
            vienādu trijstūru pazīmes lietojumu un palīglīnijas vilkšanu. Vienkāršos 5.–6. klases
            uzdevumos var pietikt ar 1–2 metodēm; sarežģītākos 8.–9. klases uzdevumos var būt 4–6.
            
            **No kā izvairīties.**
            - Neuzskaiti metodes, kas tikai netieši saistītas ar uzdevumu, bet atrisinājumā neparādās
            (piem., ja atrisinājumā nav nevienas modulārās aritmētikas darbības, neuzskaiti
            ModularArithmetic, pat ja teorētiski uzdevumu varētu risināt ar to).
            - Neatlasi tādas metodes, kuru tipiskā lietojuma klase (Label apraksta "(1) No N.klases") ir
            krietni augstāka nekā uzdevuma klase. Klase ir lasāma no virsraksta — piem.,
            "LV.AMO.2024.7.3" norāda uz 7. klases uzdevumu. Dod priekšroku vienkāršākai metodei, ja
            tā paskaidro atrisinājuma loģiku (piem., ParityInvariant 5.–6. klasē, nevis
            ModularArithmetic; LastDigitAnalysis 7. klasē, nevis pilna kongruences valoda).
            - Neuzskaiti visu metožu sarakstu — atlasi tikai tās, kas patiesi parādās atrisinājumā.
            - Neatlasi metodi tikai tāpēc, ka atrisinājumā parādās atbilstošs jēdziens; metodei jābūt
            spriedumu solim (piem., ja uzdevumā ir trijstūris, bet tas tiek tikai aprakstīts, nevis
            izmantots trijstūra leņķu summa, neatlasi TriangleAngleSum).
            
            **Identifikatoru pieraksts.** Atbildē izmanto tieši tos Label, kas parādās metožu sarakstā.
            Saglabā precīzu rakstību (CamelScript, bez atstarpēm).
            
            **Jaunas metodes pievienošana (konservatīvi).** Ja atrisinājumā ir spriedumu solis, kuram
            nav atbilstoša Label esošajā sarakstā, drīksti pievienot **ne vairāk kā vienu** jaunu
            metodi. Lieto šo iespēju tikai tad, ja patiešām nekas no esošā saraksta neatbilst — ne
            pat tuvi. Ja nepieciešamais ir tikai esošās metodes specializēts variants, izvēlies esošo
            metodi. Jaunā metode jāpieraksta ar:
            - `label`: jauna CamelScript identifikators, kas neatkārtojas ar esošajiem;
            - `shortDescriptionEn`: īsa (5–12 vārdi) apraksts angliski.
            
            **Atbildes formāts.** Atgriež **tikai** JSON objektu ar divām atslēgām:
            (1) `methods`: Label saraksts no esošajām metodēm, kuras atrisinājumā tiek lietotas.
                Saraksts sakārtots no būtiskākās uz mazāk būtisko (būtiskākā = bez kuras risinājums
                neizdotos; mazāk būtiskā = palīgsolis vai tehniska identitāte).
            (2) `newMethod`: jaunās metodes apraksts (ja nepieciešams), formātā
                `{{"label": "<CamelScriptLabel>", "shortDescriptionEn": "<short description>"}}`,
                vai `null`, ja jauna metode nav nepieciešama.
            
            Neiekļauj paskaidrojumus, komentārus vai citus laukus.
            
            Atbildes piemēri:
            
            Bez jaunas metodes:
            ```{{"methods": ["AngleChasing", "IsoscelesTriangleProperties", "TriangleAngleSum"],
                "newMethod": null}}```
            
            Ar jaunu metodi:
            ```{{"methods": ["DivisibilityRules", "PositionalNotation"],
                "newMethod": {{"label": "RepunitFactorization",
                                "shortDescriptionEn": "Using factorization of repunits like 111 = 3·37 or 1001 = 7·11·13"}}}}```
            """

        elif property == MetadataProperties.HAS_REASONING_MISTAKE:
            if meta_dict is None:
                meta_dict = {}
            domain_list = meta_dict.get('domain', [])
            domain = domain_list[0] if domain_list else 'Comb'
            domain_mistakes = self.reasoning_mistakes.get(domain, '')

            return f"""
            Lūdzu, identificē spriedumu un secināšanas kļūdas, kas var būt izplatītas, 
            risinot šādu uzdevumu. Uzdevuma matemātiskā nozare ir **{domain}**.
            
            Uzdevums: "{title.strip()}"
            
            ```{problem_text.strip()}```
            
            Atrisinājums:
            
            ```{solution_text.strip()}```
            
            Tipisko kļūdu saraksts šai nozarei (Markdown, ar CamelScript Label, īsu nosaukumu
            latviski un angliski, vienas rindkopas aprakstu un dažiem piemēriem):
            
            ```
            {domain_mistakes.strip()}
            ```
            
            ## Norādījumi atlasei
            
            **Ko atlasīt.** Atlasi 0-3 iespējamās kļūdas (to CamelScriptLabel sarakstu) 
            no dotā kļūdu dokumenta, ja tās var būt izplatītas, risinot citēto uzdevumu. 
            Ja uzdevums nemēdz novest pie "tipiskām", apspriežamām kļūdām, atgriez tukšu sarakstu 
            ar 0 labels: `{{"mistakes": []}}`. 
            
            Iespējamās neuzmanības kļūdas, pārpratumi, un arī izlaistas sadaļas atrisinājumā 
            (ja vien uzdevuma formulējums īpaši neveicina šādu izlaišanu vai atrisinājuma 
            struktūras sajaukšanu) nav jānorāda vai jāmeklē tām label-s, 
            jo tādas būs praktiski katrā uzdevumā.
            
            **Identifikatoru pieraksts.** Atbildē izmanto tos Label, kas sastopami kļūdu sarakstā.
            Katru label raksta precīzi (CamelScript, bez atstarpēm). Sākt ar tiem Label, kuri 
            varētu būt visizplatītākās kļūdas šim uzdevuma tipam.
            
            **Atrast "mistakesFit":** Cik tipisks piemērs ir šis uzdevuma tips kādai 
            no "mistakes" sarakstā apzīmētajām kļūdām. Izvēlēties no 3 vērtībām: 

            * "low" - "mistakes" saraksts ir tukšs, vai arī uzdevumu parasti neuzskata par 
              tipisku piemēru kādai no "mistakes" kļūdām. 
            * "medium" - uzdevums ir tipisks piemērs kādai kļūdai "mistake" sarakstā. 
            * "high" - uzdevums ir tipisks piemērs kādai kļūdai "mistakes" sarakstā; 
              bez tam var radīt arī citus uzdevuma nosacījuma pārpratumus, nepareizus 
              spriedumus vai neatbilstošu atrisinājuma struktūru. 

            **Atbildes formāts.** Atgriež **tikai** JSON objektu ar divām atslēgām:
            (1) `mistakes`: Label saraksts (0-3 labels) no Markdown dokumentā dotā kļūdu saraksta.
            (2) `mistakesFit`: <"low"|"medium"|"high"> - kā aprakstīts augstāk. 

            Neiekļauj paskaidrojumus, komentārus vai citus laukus.
            Atbildes piemērs:
            
            ```{{"mistakes": ["IncorrectTranslationOfWordProblem", "SignFlipForgottenInInequality"],
                "mistakesFit": "medium"}}```
            """


    def classify_problem(self, title, problem_text, problem_solution, property, meta_dict=None):
        prompt = self.make_prompt(property, title, problem_text, problem_solution, meta_dict=meta_dict)
        system_message = self.make_sys_instructions(property)
        openaiUtils = OpenaiUtils(self.openai_api_key, self.provider)
        result = openaiUtils.json_request(prompt, system_message, 42)
        
        if property == MetadataProperties.HAS_REASONING_METHOD:
            if isinstance(result, str):
                match = re.search(r'\{.*\}', result, re.DOTALL)
                if match:
                    try:
                        result = json.loads(match.group(0))
                    except:
                        pass
            return result

        if property == MetadataProperties.HAS_SOLUTION_CONCEPT:
            if isinstance(result, str):
                match = re.search(r'\{.*?\}', result, re.DOTALL)
                if match:
                    try:
                        result = json.loads(match.group(0))
                    except:
                        pass
            return result

        if property == MetadataProperties.HAS_REASONING_MISTAKE:
            if isinstance(result, str):
                match = re.search(r'\{.*\}', result, re.DOTALL)
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

# if __name__ == '__main__':
#     api_key = os.environ.get("OPENAI_API_KEY") or "sk-your-key-here"
#     metadata_utils = MetadataUtils(api_key)

#     problemList = extract_sections_from_md(input_md_file)
#     updated_sections = []

#     for (title, full_problem) in problemList:
#         clean_problem = normalize_text(full_problem)
#         try:
#             predicted_qtype = metadata_utils.classify_problem(clean_problem, "", 'questionType')
#         except Exception as e:
#             print(f"Error with {title}: {e}")
#             predicted_qtype = 'NA'

#         new_section = add_generated_question_type(full_problem, predicted_qtype)
#         updated_sections.append(f'# <lo-sample/> {title}\n\n{new_section.strip()}\n')

#         print(f'Processed: {title} | _questionType: {predicted_qtype}')

#     with open(output_md_file, 'w', encoding='utf-8') as out:
#         out.write('\n\n'.join(updated_sections))

#     print(f'Output written to: {output_md_file}')
