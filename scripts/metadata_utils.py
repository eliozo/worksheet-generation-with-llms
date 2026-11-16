import os
import sys
import re
import json
import requests
import time
import yaml
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


# Properties that "eliozo_client.py add-metadata" can generate, with what each
# one means and what the LLM classifies it from.
ADD_METADATA_PROPERTIES = {
    MetadataProperties.QUESTION_TYPE:
        'Question type, e.g. Prove, FindAll, FindOptimal (from the problem text)',
    MetadataProperties.DOMAIN:
        'Mathematical domain(s): Alg, Comb, Geom, NT (from the problem text)',
    MetadataProperties.HAS_SOLUTION_STRUCTURE:
        'Structure of the expected solution, e.g. eliozo:FindAll (from the problem text)',
    MetadataProperties.HAS_SOLUTION_CONCEPT:
        'Concepts used in the solution, and its reading difficulty (from the problem and solution)',
    MetadataProperties.HAS_REASONING_METHOD:
        'Reasoning methods used in the solution (from the problem, solution and its domain)',
    MetadataProperties.HAS_REASONING_MISTAKE:
        'Typical reasoning mistakes for the problem (from the problem, solution and its domain)',
}

# Prompts and system instructions, one entry per property (see the file's header)
PROMPTS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'metadata_utils.yaml')
PLACEHOLDER_RE = re.compile(r'\{(\w+)\}')


def load_prompts(path=PROMPTS_FILE):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def fill_placeholders(template, values):
    """Replace {name} for the names in *values*, in one pass (inserted texts are not
    scanned again); all other braces stay as they are."""
    return PLACEHOLDER_RE.sub(lambda m: values.get(m.group(1), m.group(0)), template)


class MetadataUtils:
    def __init__(self, openai_api_key, provider=None): 
        self.openai_api_key = openai_api_key
        self.provider = provider
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {openai_api_key}'
        }
        self.subdomains = self._load_subdomains()
        self.question_types = self._load_question_types()
        self.prompts = load_prompts()
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


    def _load_question_types(self):
        """The questionType values to choose from: the QTY_ leaves (L2 != 0) of questionTypes2.csv."""
        csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'setup', 'resources', 'questionTypes2.csv')
        import csv
        with open(csv_path, 'r', encoding='utf-8') as f:
            return [row for row in csv.DictReader(f)
                    if row['Label'].startswith('QTY_') and row['L2'].strip() not in ('', '0')]

    def _question_types_text(self):
        """The question type vocabulary for the prompt, in Latvian."""
        parts = []
        for row in self.question_types:
            lines = [f"* {row['Label']} – {row['TitleLv']}",
                     f"  Kanoniskais jautājums: {row['QuestionLv']}"]
            if row['OtherQuestionsLv'].strip():
                lines.append(f"  Citi tipiski formulējumi: {row['OtherQuestionsLv']}")
            lines.append(f"  Nepieciešamās atrisinājuma daļas: {row['RequiredPartsLv']}")
            lines.append(f"  Apraksts: {row['DescriptionLv']}")
            parts.append("\n".join(lines))
        return "\n\n".join(parts)

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
        entry = self.prompts.get(property.value)
        return entry['system'] if entry else None

    def make_prompt(self, property, title, problem_text, solution_text="", meta_dict=None):
        """The user message for *property*: its template in metadata_utils.yaml with the placeholders filled in."""
        entry = self.prompts.get(property.value)
        if not entry:
            return None
        values = {
            'problem_text': problem_text.strip(),
            'solution_text': solution_text.strip(),
            'title': title.strip(),
        }
        if property == MetadataProperties.QUESTION_TYPE:
            values['question_types'] = self._question_types_text()
        elif property == MetadataProperties.SUBDOMAIN:
            values['subdomains'] = "\n".join(item['formatted'] for item in self.subdomains)
        elif property == MetadataProperties.HAS_SOLUTION_CONCEPT:
            concepts_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'setup', 'resources', 'concepts.csv')
            try:
                with open(concepts_path, 'r', encoding='utf-8') as f:
                    values['concepts'] = f.read()
            except Exception as e:
                print(f"Warning: could not read concepts.csv: {e}")
                values['concepts'] = ''
        elif property in (MetadataProperties.HAS_REASONING_METHOD, MetadataProperties.HAS_REASONING_MISTAKE):
            domain_list = (meta_dict or {}).get('domain', [])
            domain = domain_list[0] if domain_list else 'Comb'
            values['domain'] = domain
            values['domain_methods'] = self.reasoning_methods.get(domain, '').strip()
            values['domain_mistakes'] = self.reasoning_mistakes.get(domain, '').strip()
        return fill_placeholders(entry['prompt'], values)

    def _checked_value(self, property, value):
        """A questionType answer outside the vocabulary counts as no answer ('NA')."""
        if property == MetadataProperties.QUESTION_TYPE:
            allowed = {row['Label'] for row in self.question_types}
            if not isinstance(value, str) or value.strip() not in allowed:
                if value != 'NA':
                    print(f"Warning: questionType '{value}' is not one of {', '.join(sorted(allowed))}")
                return 'NA'
            return value.strip()
        return value

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
            return self._checked_value(property, result.get(json_key, 'NA'))
        except AttributeError:
            pass # result might be a string
        except json.JSONDecodeError:
            pass
            
        if isinstance(result, str):
            match = re.search(r'\{.*?\}', result, re.DOTALL)
            if match:
                try:
                    parsed_result = json.loads(match.group(0))
                    return self._checked_value(property, parsed_result.get(json_key, 'NA'))
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
