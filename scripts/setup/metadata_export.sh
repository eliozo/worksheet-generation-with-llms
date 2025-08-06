#!/bin/bash

export PYTHONPATH=../..
export RDF_PREF="../../../qualification-project/migration-script/resources"

rm -fr temp
mkdir temp
# python ../eliozo_client.py metadata-to-turtle \
#     "https://docs.google.com/spreadsheets/d/e/2PACX-1vQvAsYeFYhuFLmLgtMiYFeQFeeO4e0DgteRXRg1zpQ2iMcWZr-mIgdyDYnh1IoKq4l5v9C-JAE1-Qcy/pub?gid=462395741&single=true&output=csv" \
#     topic temp/skos-topic.ttl --reference problemdata.json

# python ../eliozo_client.py metadata-to-turtle \
#     "https://docs.google.com/spreadsheets/d/e/2PACX-1vQvAsYeFYhuFLmLgtMiYFeQFeeO4e0DgteRXRg1zpQ2iMcWZr-mIgdyDYnh1IoKq4l5v9C-JAE1-Qcy/pub?gid=1894093694&single=true&output=csv" \
#     method temp/skos-method.ttl --reference problemdata.json

# python ../eliozo_client.py metadata-to-turtle \
#     "https://docs.google.com/spreadsheets/d/e/2PACX-1vQvAsYeFYhuFLmLgtMiYFeQFeeO4e0DgteRXRg1zpQ2iMcWZr-mIgdyDYnh1IoKq4l5v9C-JAE1-Qcy/pub?gid=1943031484&single=true&output=csv" \
#     domain temp/skos-domain.ttl --reference problemdata.json

python ../eliozo_client.py metadata-to-turtle \
    "https://docs.google.com/spreadsheets/d/e/2PACX-1vQvAsYeFYhuFLmLgtMiYFeQFeeO4e0DgteRXRg1zpQ2iMcWZr-mIgdyDYnh1IoKq4l5v9C-JAE1-Qcy/pub?gid=56933932&single=true&output=csv" \
    question temp/skos-question.ttl --reference problemdata.json


python ../eliozo_client.py metadata-to-turtle \
    "https://docs.google.com/spreadsheets/d/e/2PACX-1vQvAsYeFYhuFLmLgtMiYFeQFeeO4e0DgteRXRg1zpQ2iMcWZr-mIgdyDYnh1IoKq4l5v9C-JAE1-Qcy/pub?gid=1895950034&single=true&output=csv" \
    olympiad temp/list-olympiad.ttl --reference problemdata.json


# python eliozo_client.py ingest-rdf abc ${RDF_PREF}/skos_topic.ttl --reference problemdata.json


# python eliozo_client.py ingest-rdf abc ${RDF_PREF}/concepts.ttl --reference problemdata.json
# python eliozo_client.py ingest-rdf abc ${RDF_PREF}/data_olympiads.ttl --reference problemdata.json
# python eliozo_client.py ingest-rdf abc ${RDF_PREF}/skos_method.ttl --reference problemdata.json
# python eliozo_client.py ingest-rdf abc ${RDF_PREF}/skos_subdomain.ttl --reference problemdata.json
# python eliozo_client.py ingest-rdf abc ${RDF_PREF}/skos_topic.ttl --reference problemdata.json
# python eliozo_client.py ingest-rdf abc ${RDF_PREF}/topics.ttl --reference problemdata.json
# python eliozo_client.py ingest-rdf abc ${RDF_PREF}/youtube.ttl --reference problemdata.json