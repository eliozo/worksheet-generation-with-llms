import os
import sys
from dotenv import load_dotenv

# Ensure the parent directory is in the sys.path
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(script_dir, '..'))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from scripts.eliozo_client import EliozoClient

def main():
    # Load environment variables (e.g. OPENAI_API_KEY)
    load_dotenv()
    
    weaviate_url = os.getenv("WEAVIATE_URL", "NA")
    weaviate_api_key = os.getenv("WEAVIATE_API_KEY", "NA")
    openai_api_key = os.getenv("OPENAI_API_KEY", "NA")
    fuseki_url = os.getenv("FUSEKI_URL", "NA")
    fuseki_user = os.getenv("FUSEKI_USER", "NA")
    fuseki_password = os.getenv("FUSEKI_PASSWORD", "NA")

    client = EliozoClient(weaviate_url, weaviate_api_key, openai_api_key, fuseki_url, fuseki_user, fuseki_password)
    client.set_command("add-metadata")

    # Define the base directory containing the LV.AMO directories
    base_dir = os.path.normpath(os.path.join(script_dir, "..", "..", "math", "problembase", "LV.AMO"))
    
    print(f"Searching for content_lv.md files in: {base_dir}")
    
    if not os.path.exists(base_dir):
        print(f"Error: Directory not found: {base_dir}")
        return

    # Walk through all subdirectories
    for root, dirs, files in os.walk(base_dir):
        if "content_lv.md" in files:
            md_file = os.path.join(root, "content_lv.md")
            output_file = os.path.join(root, "content_lv2.md")
            
            print(f"\nProcessing {md_file} ...")
            
            # Try to find a local problemdata.json to use as reference, or use a default
            reference_file = os.path.join(root, "problemdata.json")
            if os.path.exists(reference_file):
                client.set_reference(reference_file)
            else:
                client.set_reference("NA.json")

            # Call add_metadata directly, skipping command-line invocation
            client.add_metadata(md_file, "hasSolutionConcept", "gpt-4o", output_file)
            

if __name__ == "__main__":
    main()
