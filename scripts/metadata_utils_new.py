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
        self.subdomains = self._load_subdomains()

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
                    if label:
                        subdomin_list.append(f"{label} ({desc})")
        except Exception as e:
            print(f"Error loading subdomains: {e}")
        return subdomin_list

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
        elif property == MetadataProperties.SUBDOMAIN:
            return f"""
            You are a helpful assistant. Respond only with a valid JSON object like:
            {{"subdomain": "DOM_Inequalities"}}. Do not explain anything.
            """
    
    def make_prompt(self, property, problem_text):
        if property == MetadataProperties.QUESTION_TYPE:
            return f"""
            Atrodi matemātikas uzdevuma tipu.
            Atbildi **tikai** ar JSON formātā: {{"uzdevuma_tips": "..."}}.
            Uzdevums:

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
        elif property == MetadataProperties.SUBDOMAIN:
            subdomain_str = "\\n".join(self.subdomains)
            return f"""
            Atrodi uzdevumam atbilstošāko apakšnozari (subdomain).
            Atbildi **tikai** ar JSON formātā: {{"subdomain": "DOM_..."}}.
            
            Uzdevums:
            {problem_text.strip()}

            Iespējamās apakšnozares ir:
            {subdomain_str}
            """

    def classify_problem(self, problem_text, problem_solution, property):
        prompt = self.make_prompt(property, problem_text)
        system_message = self.make_sys_instructions(property)
        openaiUtils = OpenaiUtils(self.openai_api_key)
        result = openaiUtils.json_request(prompt, system_message, 42)
        try:
            if property == MetadataProperties.QUESTION_TYPE:
                return result.get('uzdevuma_tips', 'NA')
            elif property == MetadataProperties.SUBDOMAIN:
                return result.get('subdomain', 'NA')
            return "NA"
        except (AttributeError, TypeError):
             # result might be string if error occurred or parsing failed inside openaiUtils but it returns dict usually
             pass

        # Fallback if result is string or dict access failed strangely
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

    match = re.search(r'<small>\s*\n(.*?)\n\s*</small>', md_text, re.DOTALL)
    if not match:
        return md_text  # no <small> block found

    content = match.group(1)

    lines = [line.rstrip() for line in content.splitlines() if line.strip()]

    # Skip if already present
    if any("_questionType:" in line for line in lines):
        return md_text

    lines.append(f"* _questionType: {generated_qtype}")

    # Reconstruct with exactly one newline after <small>
    new_small_block = "<small>\n" + "".join(lines) + "</small>"

    return md_text[:match.start()] + new_small_block + md_text[match.end():]

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
