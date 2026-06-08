import os
import sys
import shutil

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '../..'))
sys.path.insert(0, project_root)

from scripts.eliozo_client import EliozoClient

import requests

def main():
    client = EliozoClient('NA', 'NA', 'NA', 'NA', 'NA', 'NA')

    temp_dir = os.path.join(current_dir, 'temp')
    reference_file = os.path.join(current_dir, 'problemdata.json')
    client.set_reference(reference_file)

    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    os.makedirs(temp_dir)

    if os.path.exists(reference_file):
        os.remove(reference_file)

    csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vT1Il_-qJURh8sZHRN1oJSwok4kRUjcA7VCOhDfg1PnTUC14k4skRRl3NrUDEbd1vELQq_ALwEU9Ltx/pub?gid=0&single=true&output=csv"

    csv_file_path = os.path.join(temp_dir, "spreadsheet.csv")
    print(f"Downloading CSV to {csv_file_path}...")
    r = requests.get(csv_url, stream=True, timeout=30)
    r.raise_for_status()
    with open(csv_file_path, "wb") as f:
        for chunk in r.iter_content(8192):
            f.write(chunk)

    print(f"Converting Markdown problems to Turtle in {temp_dir} ...")
    client.md_repository_csv_to_turtle(temp_dir, csv_file_path)
    print("Done.")

if __name__ == "__main__":
    main()
