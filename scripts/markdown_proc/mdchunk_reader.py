import re
import os
import sys
import markdown
from collections import defaultdict
from typing import List

# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../eliozoapp/eliozo')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../eliozoapp/eliozo')))

# from .webmd_utils import extract_latex, replace_placeholders, proc_markdown
from scripts.markdown.webmd_utils import extract_latex, replace_placeholders, proc_markdown

import rdflib
# from rdflib.namespace import RDF, FOAF, SKOS, XSD

from rdflib import Graph, RDF, FOAF, SKOS, XSD, URIRef, Namespace

RDF_NS = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
eliozo_ns = "http://www.dudajevagatve.lv/eliozo#"
ELIOZO = rdflib.Namespace("http://www.dudajevagatve.lv/eliozo#")

def add_new_problem(g, title):
    problem_node = rdflib.URIRef(eliozo_ns+title)
    problem_rdf_property = rdflib.URIRef(RDF_NS + 'type')
    g.add((problem_node, problem_rdf_property, rdflib.URIRef(eliozo_ns + "Problem")))
    return problem_node

# for example, key='country', value='LV'
def add_problem_literal_prop(g, problem_node, key, value):
    problem_property = rdflib.URIRef(eliozo_ns + key)
    g.add((problem_node, problem_property, rdflib.term.Literal(value)))


def add_problem_literal_prop_lang(g, problem_node, key, value, lang):
    problem_property = rdflib.URIRef(eliozo_ns + key)
    g.add((problem_node, problem_property, rdflib.term.Literal(value, lang=lang)))


# for example, key='grade', value=10
def add_problem_integer_prop(g, problem_node, key, value):
    problem_property = rdflib.URIRef(eliozo_ns + key)
    g.add((problem_node, problem_property, rdflib.term.Literal(value, datatype=XSD.integer)))


def add_problem_topiclike_prop(g, problem_node, key, value):
    problem_property = rdflib.URIRef(eliozo_ns + key)
    value_resource = rdflib.URIRef(eliozo_ns + value)
    g.add((problem_node, problem_property, value_resource))

def addSolutionToRdfProblem(g, title, i, solution_text, theLang):
    problem_node = rdflib.URIRef(eliozo_ns + title)  # subjekts
    solution_node = rdflib.URIRef(eliozo_ns + f"SOLN.{title}.SUB{i}")
    problem_rdf_property = rdflib.URIRef(RDF_NS + 'type')
    g.add((solution_node, problem_rdf_property, rdflib.URIRef(eliozo_ns + "Solution")))
    add_problem_literal_prop_lang(g, solution_node, 'solutionText', solution_text, theLang)
    add_problem_integer_prop(g, solution_node, 'solutionNum', i)
    add_problem_literal_prop_lang(g, solution_node, 'solutionTextHtml',
                                  proc_markdown(solution_text), theLang)
    problem_problemsolution_property = rdflib.URIRef(eliozo_ns + 'problemSolution')
    g.add((problem_node, problem_problemsolution_property, solution_node))


def addImageToRDFGraph(g, title, image_src, image_width):
    global eliozo_ns
    problem_node = rdflib.URIRef(eliozo_ns + title) # subjekts
    image_node = rdflib.URIRef(eliozo_ns + "IMG." + image_src)
    problem_rdf_property = rdflib.URIRef(RDF_NS + 'type')
    g.add((image_node, problem_rdf_property, rdflib.URIRef(eliozo_ns + "Image")))
    add_problem_literal_prop(g, image_node, 'imageSrc', image_src)
    add_problem_literal_prop(g, image_node, 'imageWidth', image_width)
    problem_problemimage_property = rdflib.URIRef(eliozo_ns+'problemImage')
    g.add((problem_node, problem_problemimage_property, image_node))


def extract_problem(text):
    problem_text = []
    lines = text.split('\n')
    for line in lines:
        if line.startswith('# '):
            continue
        elif re.fullmatch(r'^\s*<small>\s*', line) or re.fullmatch(r'## .*', line):
            break
        else:
            problem_text.append(line)
    return '\n'.join(problem_text)


def get_image_filename(arg):
    pattern = r'!\[\]\(([^\(\)]*\.png)\)'
    match = re.search(pattern, arg)
    if match:
        return match.group(1)
    return None


# Drop the question/meta portions from 'text'; leave only solutions.
# def extract_solution_part(text):
#     # Drop the starting portion
#     f1 = text.find('</small>')
#     f2 = text.find('<text num=')
#     f3 = text.find('## Atrisin')
#     if f1 >= 0:
#         text = text[f1 + len('</small>'):]
#     elif f2 >= 0:
#         text = text[f2:]
#     elif f3 >= 0:
#         text = text[f3:]
#     return text


def extract_solution_part(text):
    # Drop the starting portion
    f1 = text.find('</small>')
    f2 = text.find('## Atrisin')
    f3 = text.find('## Solution')
    if f1 >= 0:
        text = text[f1 + len('</small>'):]
    elif f2 >= 0:
        text = text[f2:]
    elif f3 >= 0:
        text = text[f3:]
    return text


import re
from typing import List

def get_solutions(input: str) -> List[str]:
    if not input:
        return []

    # H2 header line: "## Atrisinājums" or "## Atrisinājums-<digits>"
    # ^ and $ are multiline anchors; we allow extra spaces after '##'.
    header_re = re.compile(r'(?m)^##\s+(Atrisinājums|Solution)(?:-\d+)?\s*$')

    matches = list(header_re.finditer(input))
    if not matches:
        return [input]

    sections = []
    for i, m in enumerate(matches):
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(input)
        sections.append(input[start:end])
    return sections


# def extract_solutions(title, text):
#     # # Drop the starting portion
#     # f1 = text.find('</small>')
#     # f2 = text.find('<text num=')
#     # f3 = text.find('## Atrisin')
#     # if f1 >= 0:
#     #     text = text[f1 + len('</small>'):]
#     # elif f2 >= 0:
#     #     text = text[f2:]
#     # elif f3 >= 0:
#     #     text = text[f3:]

#     # pattern1 = r'<text\s+num="[0-9]+"\s+lang="lv">'

#     m1 = text.find('<text num=')

#     # Plain list of solutions in Latvian; no delimiters
#     if m1 == -1:
#         solutions = dict()
#         current_solution = []
#         lines = text.split('\n')

#         ii = 0
#         for line in lines:
#             if re.fullmatch(r'## Atrisin.*', line):
#                 # append the previous solution
#                 if current_solution != []:
#                     ii += 1
#                     solutions[ii] = {'lv': '\n'.join(current_solution)}
#                 current_solution = [line]
#             elif current_solution != []:
#                 # before seeing the first title, we do not append anything
#                 current_solution.append(line)
#         # Append the last solution, when input ends
#         if current_solution != []:
#             ii += 1
#             solutions[ii] = {'lv': '\n'.join(current_solution)}
#         return solutions

#     # Solutions with delimiters
#     else:
#         pattern = r'<text\s+num="([0-9]+)"\s+lang="([a-z]+)">\s*(.*?)\s*</text>'
#         # Compile the regex pattern
#         regex = re.compile(pattern, re.DOTALL)

#         # Find all matching text blocks
#         matches = regex.findall(text)

#         # Initialize variables to store the results
#         result = dict()
#         current_num = None
#         current_dict = defaultdict(str)

#         # Process each match
#         for match in matches:
#             num, lang, content = match
#             num = int(num)

#             # Check if we've encountered a new "num" value
#             if not num in result:
#                 # If there is an existing dictionary, add it to the result list
#                 if current_dict:
#                     result[current_num] = current_dict

#                 # Start a new dictionary for the new "num" value
#                 current_dict = defaultdict(str)
#                 current_num = num

#             # Add the content to the current dictionary
#             current_dict[lang] = content.strip()

#         # Don't forget to add the last dictionary to the result list
#         if current_dict:
#             result[current_num] = current_dict

#         return result


def extract_metadata(text):
    metadata = dict()
    lines = text.split('\n')
    meta_opened = False
    for line in lines:
        if re.fullmatch(r'\s*<small>\s*', line):
            meta_opened = True
        elif re.fullmatch(r'\s*</small>\s*', line):
            meta_opened = False
            break
        elif meta_opened:
            if line.startswith('* ['):
                continue
            key_val = line.split(":")
            if len(key_val) == 2:
                key = key_val[0]
                if key.startswith('* '):
                    key = key[2:]
                values = key_val[1].split(",")
                if key in metadata:
                    metadata[key].extend([i.strip() for i in values])
                else:
                    metadata[key] = [i.strip() for i in values]
    return metadata


def extract_images(text):
    images = []
    lines = text.split('\n')
    image_regex = re.compile(r"^!\[.*\]\((.*)\)(\{\s*width=(\S*)\s*\})?")  # LV.AO.2000.7.1
    for line in lines:
        line = line.strip()
        match_id = image_regex.match(line)
        if match_id:
            image_id = match_id.group(1)
            width = ''
            if match_id.group(3):
                width = match_id.group(3)
            images.append((image_id, width))
    return images


# Read problems one by one from Markdown file "filepath"
def extract_sections_from_md(filepath):
    section_titles = []
    current_section = None
    sections = []
    title = "NA"

    heading_re = re.compile(r'^#\s+<lo-sample/>\s+(.*)')

    with open(filepath, 'r', encoding='UTF-8') as file:
        for line in file:
            m = heading_re.match(line)
            if m:
                new_title = m.group(1)
                # append the previous (title, current_section)
                if current_section is not None:
                    sections.append((title, current_section))
                title = new_title
                current_section = line
            elif current_section is not None:
                # before seeing the first title, we do not append anything
                current_section += line
    # Append the last (title, current_section)
    if current_section:
        sections.append((title, current_section))
    return sections


# def remove_translation_tags(text):
#     result = {}
#     lv_tag = '<text lang="lv">'
#     if text.find(lv_tag) == -1:
#         pattern = re.compile(r'<text lang=.*?>.*?</text>', re.DOTALL)
#         result['lv'] = re.sub(pattern, '', text)

#     pattern = r'<text lang="(?P<lang>\w+)">\s*(?P<content>.*?)\s*</text>'
#     matches = re.finditer(pattern, text, re.DOTALL)
#     for match in matches:
#         lang = match.group('lang')
#         content = match.group('content').strip()  # Strip any leading/trailing whitespace
#         result[lang] = content
#     return result


def get_suffix(arg):
    if not isinstance(arg, str):
        raise ValueError("Input should be a string")
    last_dot_index = arg.rfind('.')
    if last_dot_index == -1:
        return arg
    return arg[:last_dot_index]


# [('Contest','Konkurss'), ('Book','Grāmata'), ('RegionalOrOpen', 'Reģionu vai atklātā'),
# ('National', 'Nacionālā'), ('TeamSelection', 'Papildsacensības'), ('International', 'Starptautiska')] %}
# Return olympiadType - a single string value
# TODO: This should be taken from data_olympiads.ttl
def get_olympiad_type(title):
    result = 'Contest'
    title_list = title.split(".")
    prefix2 = ".".join(title_list[0:2])
    if prefix2 in ['EE.LVS', 'EE.LVT', 'EE.PK', 'EE.PKTEST', 
                   'LT.SAV', 'LT.LJMO', 'LT.VUMIF', 'LV.SOL', 'LV.NOL', 'LV.AMO']:
        result = 'RegionalOrOpen'
    elif prefix2 in ['EE.LO', 'LT.LMMO', 'LT.LKMMO', 'LV.VOL']:
        result = 'National'
    elif prefix2 in ['EE.TST', 'LT.TST', 'LV.TST']:
        result = 'TeamSelection'
    elif prefix2.startswith('WW'):
        result = 'International'
    elif prefix2.startswith('BBK2012'):
        result = 'Book'
    return result

def get_suggested_grade(title):
    title_list = title.split(".")
    suffix2 = title_list[-2]
    if suffix2 in ['5', '6', '7', '8', '9', '10', '11', '12']:
        return [int(suffix2)]
    if title.startswith('BBK2012'):
        return [9,10,11,12]
    if title.startswith('WW'):
        return [10,11,12]
    if title.startswith('EE.TST') or title.startswith('LT.TST') or title.startswith('LV.TST'):
        return [10,11,12]
    if title.startswith('LT.LKMMO'):
        return [9,10,11,12]
    if suffix2.find('_'):
        return [int(x) for x in suffix2.split('_')]
    else:
        print(f'UNDEFINED suggestedGrade for {title}')
        return []


def markdown_md_to_turtle(md_file_path, ttl_file_path, lang_code, is_master):
    sections = extract_sections_from_md(md_file_path)

    # sections = sections[0:1]

    g = rdflib.Graph()
    g.bind("foaf", FOAF)
    g.bind("skos", SKOS)
    g.bind("eliozo", ELIOZO)

    olympiad_problem_id = re.compile(r"(EE|LV|LT|UA|PL)\.(\w+)\.(\d{4}[A-Z]*)\.([0-9_]+)\.([A-Z])?(\d+)") # LV.AO.2000.7.1
    book_problem_id = re.compile(r"([A-Z0-9]+)\.(.*)\.(\d+)")  # BBK2012.P1.1 or BBK2012.P1.E2.1 or similar
    inter_problem_id = re.compile(r"(WW)\.(\w+)\.(\d{4}[A-Z]*)\.([A-Z])?(\d+)") # WW.IMOSHL.2022.A1

    for i, (title,section) in enumerate(sections):
        title = title.strip()
        section = section.strip()
        suffix = get_suffix(title)
        suggestGrade = get_suggested_grade(title)
        olympiadType = get_olympiad_type(title)
        problem_node = add_new_problem(g, title)
        match_id = olympiad_problem_id.match(title)

        book_match_id = book_problem_id.match(title)
        inter_match_id = inter_problem_id.match(title)

        if is_master and match_id:
            country = match_id.group(1)
            olympiad = match_id.group(2)
            timeID = match_id.group(3)
            if len(timeID) > 4:
                year = int(timeID[0:4])
            else:
                year = int(timeID)
            rawGrade = match_id.group(4)
            grade_underscore = rawGrade.find("_")
            if grade_underscore == -1:
                grade = int(rawGrade)
            else:
                grade = int(rawGrade[0:grade_underscore])
            problem_number = match_id.group(5)

            add_problem_literal_prop(g, problem_node, 'country', country)
            add_problem_literal_prop(g, problem_node, 'olympiadCode', olympiad)
            add_problem_literal_prop(g, problem_node, 'olympiad', country + '.' + olympiad)
            add_problem_literal_prop(g, problem_node, 'event', country + '.' + olympiad + '.' + timeID)
            add_problem_literal_prop(g, problem_node, 'suffix', suffix)
            add_problem_integer_prop(g, problem_node, 'problemYear', year)
            add_problem_literal_prop(g, problem_node, 'problemTimeID', timeID)
            add_problem_integer_prop(g, problem_node, 'problemGrade', grade)
            add_problem_integer_prop(g, problem_node, 'problem_number', problem_number)
            add_problem_literal_prop(g, problem_node, 'problemID', title)

        elif is_master and book_match_id:
            book_name = book_match_id.group(1)
            section_name = book_match_id.group(2)
            problem_number = book_match_id.group(3)
            add_problem_literal_prop(g, problem_node, 'problemBook', book_name)
            add_problem_literal_prop(g, problem_node, 'problemBookSection', section_name)
            add_problem_literal_prop(g, problem_node, 'suffix', suffix)
            add_problem_integer_prop(g, problem_node, 'problem_number', problem_number)
            add_problem_literal_prop(g, problem_node, 'problemID', title)

        elif is_master and inter_match_id:
            country = match_id.group(1)
            olympiad = inter_match_id.group(2)
            timeID = inter_match_id.group(3)
            if len(timeID) > 4:
                year = int(timeID[0:4])
            else:
                year = int(timeID)
            grade = 12
            problem_type = inter_match_id.group(4)
            problem_number = inter_match_id.group(5)
            if problem_type:
                suffix = suffix + "." + problem_type
           
            add_problem_literal_prop(g, problem_node, 'country', country)
            add_problem_literal_prop(g, problem_node, 'olympiad', olympiad)
            add_problem_literal_prop(g, problem_node, 'olympiadCode', olympiad)
            add_problem_literal_prop(g, problem_node, 'event', olympiad + '.' + timeID)
            add_problem_integer_prop(g, problem_node, 'problemYear', year)
            add_problem_literal_prop(g, problem_node, 'problemTimeID', timeID)
            add_problem_literal_prop(g, problem_node, 'suffix', suffix)
            add_problem_integer_prop(g, problem_node, 'problem_number', problem_number)
            add_problem_integer_prop(g, problem_node, 'problemGrade', grade)
            add_problem_literal_prop(g, problem_node, 'problemID', title)

        elif not is_master:
            pass 

        else:
            print(f"***** WARNING: ***** Invalid problemID: {title}")

        # Get everything above <small>...</small> metadata block
        problem_text_md = extract_problem(section).strip()


        # return a dictionary of all problem translations
        # (Latvian text can be without <text lang="lv">)

        # problem_text_dict = remove_translation_tags(problem_text_md)

        # for theLang, problem_text_md in problem_text_dict.items():
        #     problem_text_html = proc_markdown(problem_text_md).strip()

        #     add_problem_literal_prop_lang(g, problem_node, 'problemText', problem_text_md, theLang)
        #     add_problem_literal_prop_lang(g, problem_node, 'problemTextHtml', problem_text_html, theLang)

        #     img_file = get_image_filename(problem_text_md)
        #     if img_file is not None: 
        #         add_problem_literal_prop(g, problem_node, 'image_file', img_file)


        problem_text_html = proc_markdown(problem_text_md).strip()
        add_problem_literal_prop_lang(g, problem_node, 'problemText', problem_text_md, lang_code)
        add_problem_literal_prop_lang(g, problem_node, 'problemTextHtml', problem_text_html, lang_code)


        if is_master:
            add_problem_literal_prop(g, problem_node, 'olympiadType', olympiadType)
            for sug_grade in suggestGrade:
                add_problem_integer_prop(g, problem_node, 'suggestedGrade', sug_grade)

            meta_dict = extract_metadata(section)
            for k, vvv in meta_dict.items():
                for vv in vvv:
                    if k == 'topic' and vv != '':
                        add_problem_topiclike_prop(g, problem_node, 'topic', vv)
                    elif k == 'subdomain' and vv != '': 
                        add_problem_topiclike_prop(g, problem_node, 'subdomain', vv)
                    elif k == 'method' and vv != '': 
                        add_problem_topiclike_prop(g, problem_node, 'method', vv)                  
                    elif k == 'concepts' and vv != '':
                        add_problem_topiclike_prop(g, problem_node, 'concepts', "TRM-"+vv)
                    else:
                        add_problem_literal_prop(g, problem_node, k, vv)


        solution_part = extract_solution_part(section)

        solutions = get_solutions(solution_part)

        for i, soln_text in enumerate(solutions):
            soln_text = soln_text.strip()
            addSolutionToRdfProblem(g, title, i, soln_text, lang_code)

        # solutions = extract_solutions(title,solution_part)

        # for i, soln_text_dict in solutions.items():
        #     for theLang, soln_text in soln_text_dict.items():
        #         soln_text = soln_text.strip()
        #         addSolutionToRdfProblem(g, title, i, soln_text, theLang)
    g.serialize(destination=ttl_file_path)


