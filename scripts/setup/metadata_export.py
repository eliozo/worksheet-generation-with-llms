import os
import sys
import glob

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '../..'))
sys.path.insert(0, project_root)

from scripts.eliozo_client import EliozoClient

def main():
    client = EliozoClient('NA', 'NA', 'NA', 'NA', 'NA', 'NA')

    resources_dir = os.path.join(current_dir, 'resources')
    if not os.path.exists(resources_dir):
        os.makedirs(resources_dir)

    for ttl_file in glob.glob(os.path.join(resources_dir, "*.ttl")):
        os.remove(ttl_file)

    sources = [
        (
            "https://docs.google.com/spreadsheets/d/e/2PACX-1vQvAsYeFYhuFLmLgtMiYFeQFeeO4e0DgteRXRg1zpQ2iMcWZr-mIgdyDYnh1IoKq4l5v9C-JAE1-Qcy/pub?gid=462395741&single=true&output=csv",
            "topics",
            "resources/skos-topics.ttl"
        ),
        (
            "https://docs.google.com/spreadsheets/d/e/2PACX-1vQvAsYeFYhuFLmLgtMiYFeQFeeO4e0DgteRXRg1zpQ2iMcWZr-mIgdyDYnh1IoKq4l5v9C-JAE1-Qcy/pub?gid=1894093694&single=true&output=csv",
            "methods",
            "resources/skos-methods.ttl"
        ),
        (
            "https://docs.google.com/spreadsheets/d/e/2PACX-1vQvAsYeFYhuFLmLgtMiYFeQFeeO4e0DgteRXRg1zpQ2iMcWZr-mIgdyDYnh1IoKq4l5v9C-JAE1-Qcy/pub?gid=1943031484&single=true&output=csv",
            "domains",
            "resources/skos-domains.ttl"
        ),
        (
            "https://docs.google.com/spreadsheets/d/e/2PACX-1vQvAsYeFYhuFLmLgtMiYFeQFeeO4e0DgteRXRg1zpQ2iMcWZr-mIgdyDYnh1IoKq4l5v9C-JAE1-Qcy/pub?gid=56933932&single=true&output=csv",
            "questions",
            "resources/skos-questions.ttl"
        ),
        (
            "https://docs.google.com/spreadsheets/d/e/2PACX-1vQvAsYeFYhuFLmLgtMiYFeQFeeO4e0DgteRXRg1zpQ2iMcWZr-mIgdyDYnh1IoKq4l5v9C-JAE1-Qcy/pub?gid=1895950034&single=true&output=csv",
            "olympiads",
            "resources/list-olympiads.ttl"
        ),
        (
            "https://docs.google.com/spreadsheets/d/e/2PACX-1vQvAsYeFYhuFLmLgtMiYFeQFeeO4e0DgteRXRg1zpQ2iMcWZr-mIgdyDYnh1IoKq4l5v9C-JAE1-Qcy/pub?gid=1391589989&single=true&output=csv",
            "sources",
            "resources/list-sources.ttl"
        ),
        (
            "https://docs.google.com/spreadsheets/d/e/2PACX-1vSsIUjRXRU6L_MGgEmgUZlfwvygclZun964ilvH-l6F3TZ9w0I2MDce9VXqJgd4p2GZxF7vJ6OY5jcT/pub?gid=133948398&single=true&output=csv",
            "concepts",
            "resources/list-concepts.ttl"
        ),
        (
            "https://docs.google.com/spreadsheets/d/e/2PACX-1vSithTBvdSFhQeovJbYVCstpt7JkDUZAKXSPOjYraqfCFW2SqNjvN5Yd_xYeIfvtSjVktmBAPo2_dDf/pub?gid=0&single=true&output=csv",
            "videos",
            "resources/list-videos.ttl"
        ),
        (
            "https://docs.google.com/spreadsheets/d/e/2PACX-1vQvAsYeFYhuFLmLgtMiYFeQFeeO4e0DgteRXRg1zpQ2iMcWZr-mIgdyDYnh1IoKq4l5v9C-JAE1-Qcy/pub?gid=1619668403&single=true&output=csv",
            "problemsru",
            "resources/list-problemsru.ttl"
        ),
    ]

    print("Generating Turtle files from Google Sheets...")
    for url, prop, output_rel in sources:
        output_path = os.path.join(current_dir, output_rel)
        print(f"  {prop} -> {output_rel}")
        client.metadata_to_turtle(url, prop, output_path)
    print("Done.")

if __name__ == "__main__":
    main()
