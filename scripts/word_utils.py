import pypandoc
import json
import re
from jinja2 import Environment, FileSystemLoader
import os

def replace_latex(snip_text, infile_json):                    
    latex_pattern0 = r'\s+\$\$(.*?)\$\$\s+'
    snip_text = re.sub(latex_pattern0, r'\n\n.. math::\n\n    \1\n\n', snip_text)

    latex_pattern = r'\$(.*?)\$'
    snip_text = re.sub(latex_pattern, r':math:`\1`', snip_text)

    dir_name = os.path.dirname(infile_json)

    # Markdown image with ReStructured Text image replacement fun
    def replacement(match):
        img_name = match.group(1)
        path = dir_name.replace('\\', '/') 
        return f"\n\n.. figure:: {path}/{img_name}.png\n   :width: 246px\n\n"


    latex_pattern_img = r'!\[\]\((\w+)\.png\)\s*'
    # snip_text = re.sub(latex_pattern_img, r'\n\n.. figure:: ../tests/worksheets/\1.png\n   :width: 2in\n\n', snip_text)
    # snip_text = re.sub(latex_pattern_img, r'\n\n.. figure:: ../tests/worksheets/invarianti-2015-amo/\1.png\n   :width: 246px\n\n', snip_text)
    snip_text = re.sub(latex_pattern_img, replacement, snip_text)

    return snip_text

class WordUtils:
    data = {}

    def __init__(self, data):
        self.data = data

    def rst_to_doc(self, infile_rst, outfile_docx): 
        with open(infile_rst, 'r', encoding='utf-8') as file:
            reST_content = file.read()
        pypandoc.convert_text(reST_content, format='rst', to='docx', outputfile=outfile_docx)
        print(f"Conversion complete: {outfile_docx}")

    def preferred_template(self): 
        template = self.data["task"]["template"] if self.data["task"]["template"] else "templates/default.rst.jinja"
        return template

    # def build_rst(self, infile_json, outfile_rst):
    #     with open(infile_json, 'r', encoding='utf-8') as f:
    #         data = json.load(f)
    #     env = Environment(loader=FileSystemLoader('.'))
    #     template_file = self.preferred_template()
    #     template = env.get_template(template_file)

    #     problem_data = data['problems']
    #     for i, prob in enumerate(problem_data): 
    #         prob_text = prob['problemText_lv']
    #         latex_pattern = r'\$(.*?)\$'
    #         prob_text = re.sub(latex_pattern, r':math:`\1`', prob_text)
    #         problem_data[i]['problemText_lv'] = prob_text

    #     output = template.render(problems=problem_data)
    #     with open(outfile_rst, 'w', encoding='utf-8') as f:
    #         f.write(output)


    def transform_md_to_rst(self, infile_json, outfile_rst, template_file): 
        with open(infile_json, 'r', encoding='utf-8') as f:
            data = json.load(f)
        env = Environment(loader=FileSystemLoader('.'))
        # template_file = self.preferred_template()
        template = env.get_template(template_file)

        # snippet_data = data['snippets']
        for i, snip in enumerate(data['snippets']): 
            if snip['type'] in ['annotation']:
                snip_text = snip['value']
                latex_pattern = r'\s*\$(.*?)\$\s*'
                snip_text = re.sub(latex_pattern, r'* :math:`\1` *', snip_text)
            else:
                if 'value' in snip:
                    new_value = replace_latex(snip['value'], infile_json)
                    data['snippets'][i]['value'] = new_value
                if 'problemtext' in snip:
                    new_value = replace_latex(snip['problemtext'], infile_json)
                    data['snippets'][i]['problemtext'] = new_value
                if 'problemsolution' in snip:
                    new_value = replace_latex(snip['problemsolution'], infile_json)
                    data['snippets'][i]['problemsolution'] = new_value
            

        # Just for debugging
        # with open(f'{infile_json}.txt', 'w', encoding='utf-8') as file:
        #     json.dump(data, file, indent=4)
        print("CCCCCCCCCCCCCCCCCCCCCCCC")
        print(data)
        output = template.render(main=data)
        with open(outfile_rst, 'w', encoding='utf-8') as f:
            f.write(output)
