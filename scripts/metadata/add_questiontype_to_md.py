import re
import sys
import json
# from get_metadata_from_openai import classify_math_problem
from scripts.metadata_utils import MetadataUtils

input_md_file = 'C:/Users/eozolina/Documents/workspace-private/nms-uzdevumi/lv-vol-2019/content.md'
output_md_file = 'C:/Users/eozolina/Documents/workspace-private/nms-uzdevumi/lv-vol-2019/content_with_questiontypes.md'

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
    small_block_re = re.compile(r'(<small>.*?\n)(.*?)(</small>)', re.DOTALL)
    match = small_block_re.search(md_text)

    if match:
        before = match.group(1)
        middle = match.group(2)
        after = match.group(3)

        if '_questionType:' in middle:
            return md_text

        updated_middle = middle.strip() + f"\n_questionType:{generated_qtype}\n"
        return md_text[:match.start()] + before + updated_middle + after + md_text[match.end():]
    else:
        return md_text

if __name__ == '__main__':
    problemList = extract_sections_from_md(input_md_file)
    updated_sections = []

    for (title, full_problem) in problemList:
        clean_problem = normalize_text(full_problem)

        try:
            predicted_qtype = classify_math_problem(clean_problem, 'questionType')
        except Exception as e:
            print(f"Error with {title}: {e}")
            predicted_qtype = 'NA'

        new_section = add_generated_question_type(full_problem, predicted_qtype)
        updated_sections.append(f'# <lo-sample/> {title}\n\n{new_section.strip()}\n')

        print(f'Processed: {title} | _questionType: {predicted_qtype}')

    with open(output_md_file, 'w', encoding='utf-8') as out:
        out.write('\n\n'.join(updated_sections))

    print(f'Output written to: {output_md_file}')
