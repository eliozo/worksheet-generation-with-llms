import os
import sys
import shutil
import glob
from dotenv import load_dotenv

# Add project root to sys.path to allow imports from scripts
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '../..'))
sys.path.insert(0, project_root)

# Import EliozoClient after setting up the path
from scripts.eliozo_client import EliozoClient

def main():
    # Load environment variables
    # Assuming .env is in scripts/ or project root. 
    # eliozo_client.py loads it, but we might need to load it here too or just rely on eliozo_client's loading if we imported it?
    # eliozo_client.py has load_dotenv() in __main__ block, so we need to call it here.
    load_dotenv()

    # Get credentials from environment
    weaviate_url = os.getenv('WEAVIATE_URL', 'NA')
    weaviate_api_key = os.getenv('WEAVIATE_API_KEY', 'NA')
    openai_api_key = os.getenv('OPENAI_API_KEY', 'NA')
    fuseki_url = os.getenv('FUSEKI_URL', 'NA')
    fuseki_user = os.getenv('FUSEKI_USER', 'NA')
    fuseki_password = os.getenv('FUSEKI_PASSWORD', 'NA')

    # Initialize client
    client = EliozoClient(weaviate_url, weaviate_api_key, openai_api_key, fuseki_url, fuseki_user, fuseki_password)

    # Define paths
    temp_dir = os.path.join(current_dir, 'temp')
    reference_file = os.path.join(current_dir, 'problemdata.json')
    client.set_reference(reference_file)

    # 1. Cleanup
    print("Cleaning up...")
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    os.makedirs(temp_dir)

    if os.path.exists(reference_file):
        os.remove(reference_file)

    # 2. Data Generation (md-repository-to-turtle)
    print("Generating Turtle files...")
    csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vT1Il_-qJURh8sZHRN1oJSwok4kRUjcA7VCOhDfg1PnTUC14k4skRRl3NrUDEbd1vELQq_ALwEU9Ltx/pub?gid=0&single=true&output=csv"
    
    # md_repository_csv_to_turtle requires `output` (directory) and `csv` (path or URL)
    # The bash script used `temp` as the output directory.
    # But wait, the bash script called:
    # python ../eliozo_client.py md-repository-to-turtle temp --csv "..." --reference problemdata.json
    
    # We need to handle the CSV download if it's a URL, similar to how eliozo_client.py does it in its main block?
    # In eliozo_client.py's main block:
    # if args.command == 'md-repository-to-turtle':
    #     if args.problemdata: ...
    #     else:
    #         csv_value = args.csv
    #         if csv_value.startswith("http"):
    #             ... downloads to output/spreadsheet.csv ...
    #             csv_path = file_path
    #         ...
    #         (retvalue, data) = eliozo_client.md_repository_csv_to_turtle(args.output, csv_path)
    
    # Since I am not using the main block logic of eliozo_client.py, I should replicate the download logic or 
    # invoke the method if it handles URL. 
    # Looking at `eliozo_client.py`: `md_repository_csv_to_turtle` takes `csv` argument.
    # `markdown_repository_to_turtle` inside it probably expects a file path.
    # So I should replicate the download logic here.

    import requests
    csv_path = csv_url
    if csv_url.startswith("http"):
        csv_file_path = os.path.join(temp_dir, "spreadsheet.csv")
        print(f"Downloading CSV to {csv_file_path}...")
        try:
            r = requests.get(csv_url, stream=True, timeout=30)
            r.raise_for_status()
            with open(csv_file_path, "wb") as f:
                for chunk in r.iter_content(8192):
                    f.write(chunk)
            csv_path = csv_file_path
        except Exception as e:
            print(f"Error downloading CSV: {e}")
            sys.exit(1)

    print(f"Converting using CSV: {csv_path}")
    client.md_repository_csv_to_turtle(temp_dir, csv_path)

    sys.exit(0)

    # 3. Fuseki Reset
    dataset = "abc"
    print(f"Dropping RDF dataset '{dataset}'...")
    client.drop_rdf(dataset)
    
    print(f"Creating RDF dataset '{dataset}'...")
    client.create_rdf_dataset(dataset)

    # 4. Ingestion Loop
    print("Ingesting Turtle files...")
    # Get all .ttl files in temp directory
    ttl_files = glob.glob(os.path.join(temp_dir, "*.ttl"))
    
    # Sort files to match the order in bash script if possible, or just alphabetical
    # The bash script had explicit list of files. 
    # If the user wants ALL generated files, glob is better. 
    # The bash script seemingly listed many files, but `md-repository-to-turtle` generates them.
    # So iterating over what was generated is safer and more dynamic.
    
    for ttl_file in sorted(ttl_files):
        # We need relative path for display or just pass absolute path?
        # The bash script passed `temp/filename.ttl`.
        # ingest_rdf takes `turtle` path.
        print(f"Ingesting {os.path.basename(ttl_file)}...")
        client.ingest_rdf(dataset, ttl_file)

    print("Done!")

if __name__ == "__main__":
    main()
