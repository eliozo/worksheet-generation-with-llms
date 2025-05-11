import os
import sys
import requests
import json
import pandas as pd
import io


class StyleRulesUtils:
    openai_api_key = "NA"

    def __init__(self, openai_api_key): 
        self.openai_api_key = openai_api_key


    def download_rules(self, url, rules_file): 
        response = requests.get(url)
        response.raise_for_status()

        with open("rules.csv", "wb") as file:
            file.write(response.content)
        print("rules.csv has been downloaded.")
        df = pd.read_csv("rules.csv", encoding='utf-8')

        df_selected = df[['ID', 'Original', 'Modified', 'ExplanationsEn']]
        df_selected.columns = ['id', 'original', 'modified', 'explanations']
        rules = df_selected.to_dict(orient='records')
        with open(rules_file, 'w', encoding='utf-8') as json_file:
            json.dump(rules, json_file, ensure_ascii=False, indent=4)

        print("rules.json has been created.")