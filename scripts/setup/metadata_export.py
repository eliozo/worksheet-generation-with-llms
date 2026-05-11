import os
import sys
import glob
from dotenv import load_dotenv

# Add project root to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '../..'))
sys.path.insert(0, project_root)

# Import EliozoClient
from scripts.eliozo_client import EliozoClient

def main():
    load_dotenv()

    # Set environment variables expected by some internal logic if needed
    # The bash script set: export RDF_PREF="../../../qualification-project/migration-script/resources"
    # We should replicate this.
    os.environ['RDF_PREF'] = "../../../qualification-project/migration-script/resources"

    # Credentials
    weaviate_url = os.getenv('WEAVIATE_URL', 'NA')
    weaviate_api_key = os.getenv('WEAVIATE_API_KEY', 'NA')
    openai_api_key = os.getenv('OPENAI_API_KEY', 'NA')
    fuseki_url = os.getenv('FUSEKI_URL', 'NA')
    fuseki_user = os.getenv('FUSEKI_USER', 'NA')
    fuseki_password = os.getenv('FUSEKI_PASSWORD', 'NA')

    client = EliozoClient(weaviate_url, weaviate_api_key, openai_api_key, fuseki_url, fuseki_user, fuseki_password)
    
    # 1. Cleanup
    print("Cleaning up resources/*.ttl ...")
    resources_dir = os.path.join(current_dir, 'resources')
    # If the script is run from scripts/setup, current_dir is correct.
    # The bash script did `rm -fr resources/*.ttl`.
    # Let's verify where 'resources' is expected to be.
    # The bash script is in scripts/setup. It calls `python ../eliozo_client.py ... resources/skos-topics.ttl`.
    # This implies 'resources' is a subdirectory of the current working directory (scripts/setup).
    
    # However, checking the file structure would be good. 
    # Assuming 'resources' is in 'scripts/setup/resources'.
    
    resources_dir = os.path.join(current_dir, 'resources')
    if not os.path.exists(resources_dir):
        os.makedirs(resources_dir)
        
    for ttl_file in glob.glob(os.path.join(resources_dir, "*.ttl")):
        os.remove(ttl_file)

    # 2. Define Data Sources
    # Format: (url, property, output_filename)
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
        )
    ]

    # 3. Generate Turtle Files
    print("Generating Turtle files from Google Sheets...")
    for url, prop, output_rel in sources:
        # Resolve output path relative to script directory
        output_path = os.path.join(current_dir, output_rel)
        print(f"Exporting {prop} to {output_rel}...")
        client.metadata_to_turtle(url, prop, output_path)

    sys.exit(0)

    # 4. Ingest into Fuseki
    dataset = "abc"
    print(f"Ingesting into Fuseki dataset '{dataset}'...")
    for _, _, output_rel in sources:
        output_path = os.path.join(current_dir, output_rel)
        if os.path.exists(output_path):
            print(f"Ingesting {output_rel}...")
            client.ingest_rdf(dataset, output_path)
        else:
            print(f"Warning: {output_rel} not found, skipping ingestion.")

    print("Metadata export and ingestion complete.")

if __name__ == "__main__":
    main()
