import os
import sys
import glob

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '../..'))
sys.path.insert(0, project_root)

from scripts.eliozo_client import EliozoClient

# Every sheet below is a tab of the same "Eliozo metadata" workbook, published
# to the web as CSV. To add or re-point a tab, publish it (File > Share >
# Publish to web > CSV) and paste its gid here.
METADATA_WORKBOOK = (
    "https://docs.google.com/spreadsheets/d/e/2PACX-1vQvAsYeFYhuFLmLgtMiYFeQ"
    "FeeO4e0DgteRXRg1zpQ2iMcWZr-mIgdyDYnh1IoKq4l5v9C-JAE1-Qcy/pub"
    "?gid={gid}&single=true&output=csv"
)

VIDEO_WORKBOOK = (
    "https://docs.google.com/spreadsheets/d/e/2PACX-1vSithTBvdSFhQeovJbYVCst"
    "pt7JkDUZAKXSPOjYraqfCFW2SqNjvN5Yd_xYeIfvtSjVktmBAPo2_dDf/pub"
    "?gid={gid}&single=true&output=csv"
)

# The concept vocabulary still lives in its own older workbook. A replacement
# tab exists in METADATA_WORKBOOK (gid=1549620638) but it uses CamelCase labels
# (TRM-AlgebraicIdentities, ...) while the problem TTL files still annotate
# eliozo:concepts with the hyphenated ids from this workbook (TRM-gcd, ...).
# Switching before the problem annotations are re-tagged empties /concepts.
CONCEPT_WORKBOOK = (
    "https://docs.google.com/spreadsheets/d/e/2PACX-1vSsIUjRXRU6L_MGgEmgUZlf"
    "wvygclZun964ilvH-l6F3TZ9w0I2MDce9VXqJgd4p2GZxF7vJ6OY5jcT/pub"
    "?gid={gid}&single=true&output=csv"
)

# (source CSV url, property name understood by EliozoClient.metadata_to_turtle,
#  output Turtle file relative to this directory)
SOURCES = [
    (METADATA_WORKBOOK.format(gid=2064489418), "topics",     "resources/skos-topics.ttl"),
    (METADATA_WORKBOOK.format(gid=295466032),  "methods",    "resources/skos-methods.ttl"),
    (METADATA_WORKBOOK.format(gid=203131352),  "domains",    "resources/skos-domains.ttl"),
    (METADATA_WORKBOOK.format(gid=1929564498), "questions",  "resources/skos-questions.ttl"),
    (METADATA_WORKBOOK.format(gid=1895950034), "olympiads",  "resources/list-olympiads.ttl"),
    (METADATA_WORKBOOK.format(gid=1391589989), "sources",    "resources/list-sources.ttl"),
    (CONCEPT_WORKBOOK.format(gid=133948398),   "concepts",   "resources/list-concepts.ttl"),
    (METADATA_WORKBOOK.format(gid=1619668403), "problemsru", "resources/list-problemsru.ttl"),
    (VIDEO_WORKBOOK.format(gid=0),             "videos",     "resources/list-videos.ttl"),
]

# Published METADATA_WORKBOOK tabs that have no exporter yet, kept here so the
# gids are not lost:
#   hintTypes -> gid=964486517
#   models    -> gid=1391678755
#   concepts  -> gid=1549620638  (see CONCEPT_WORKBOOK note above)


def main():
    client = EliozoClient('NA', 'NA', 'NA', 'NA', 'NA', 'NA')

    resources_dir = os.path.join(current_dir, 'resources')
    os.makedirs(resources_dir, exist_ok=True)

    for ttl_file in glob.glob(os.path.join(resources_dir, "*.ttl")):
        os.remove(ttl_file)

    print("Generating Turtle files from Google Sheets...")
    for url, prop, output_rel in SOURCES:
        output_path = os.path.join(current_dir, output_rel)
        print(f"  {prop} -> {output_rel}")
        client.metadata_to_turtle(url, prop, output_path)
    print("Done.")


if __name__ == "__main__":
    main()
