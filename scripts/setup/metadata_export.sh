#!/bin/bash

export PYTHONPATH=../..
export RDF_PREF="../../../qualification-project/migration-script/resources"

rm -fr resources/*.ttl
python ../eliozo_client.py metadata-to-turtle \
    "https://docs.google.com/spreadsheets/d/e/2PACX-1vQvAsYeFYhuFLmLgtMiYFeQFeeO4e0DgteRXRg1zpQ2iMcWZr-mIgdyDYnh1IoKq4l5v9C-JAE1-Qcy/pub?gid=462395741&single=true&output=csv" \
    topics resources/skos-topics.ttl --reference problemdata.json

python ../eliozo_client.py metadata-to-turtle \
    "https://docs.google.com/spreadsheets/d/e/2PACX-1vQvAsYeFYhuFLmLgtMiYFeQFeeO4e0DgteRXRg1zpQ2iMcWZr-mIgdyDYnh1IoKq4l5v9C-JAE1-Qcy/pub?gid=1894093694&single=true&output=csv" \
    methods resources/skos-methods.ttl --reference problemdata.json

python ../eliozo_client.py metadata-to-turtle \
    "https://docs.google.com/spreadsheets/d/e/2PACX-1vQvAsYeFYhuFLmLgtMiYFeQFeeO4e0DgteRXRg1zpQ2iMcWZr-mIgdyDYnh1IoKq4l5v9C-JAE1-Qcy/pub?gid=1943031484&single=true&output=csv" \
    domains resources/skos-domains.ttl --reference problemdata.json

python ../eliozo_client.py metadata-to-turtle \
    "https://docs.google.com/spreadsheets/d/e/2PACX-1vQvAsYeFYhuFLmLgtMiYFeQFeeO4e0DgteRXRg1zpQ2iMcWZr-mIgdyDYnh1IoKq4l5v9C-JAE1-Qcy/pub?gid=56933932&single=true&output=csv" \
    questions resources/skos-questions.ttl --reference problemdata.json

python ../eliozo_client.py metadata-to-turtle \
    "https://docs.google.com/spreadsheets/d/e/2PACX-1vQvAsYeFYhuFLmLgtMiYFeQFeeO4e0DgteRXRg1zpQ2iMcWZr-mIgdyDYnh1IoKq4l5v9C-JAE1-Qcy/pub?gid=1895950034&single=true&output=csv" \
    olympiads resources/list-olympiads.ttl --reference problemdata.json

python ../eliozo_client.py metadata-to-turtle \
    "https://docs.google.com/spreadsheets/d/e/2PACX-1vQvAsYeFYhuFLmLgtMiYFeQFeeO4e0DgteRXRg1zpQ2iMcWZr-mIgdyDYnh1IoKq4l5v9C-JAE1-Qcy/pub?gid=1391589989&single=true&output=csv" \
    sources resources/list-sources.ttl --reference problemdata.json

python ../eliozo_client.py metadata-to-turtle \
    "https://docs.google.com/spreadsheets/d/e/2PACX-1vSsIUjRXRU6L_MGgEmgUZlfwvygclZun964ilvH-l6F3TZ9w0I2MDce9VXqJgd4p2GZxF7vJ6OY5jcT/pub?gid=133948398&single=true&output=csv" \
    concepts resources/list-concepts.ttl --reference problemdata.json

python ../eliozo_client.py metadata-to-turtle \
    "https://docs.google.com/spreadsheets/d/e/2PACX-1vSithTBvdSFhQeovJbYVCstpt7JkDUZAKXSPOjYraqfCFW2SqNjvN5Yd_xYeIfvtSjVktmBAPo2_dDf/pub?gid=0&single=true&output=csv" \
    videos resources/list-videos.ttl --reference problemdata.json

python ../eliozo_client.py metadata-to-turtle \
    "https://docs.google.com/spreadsheets/d/e/2PACX-1vQvAsYeFYhuFLmLgtMiYFeQFeeO4e0DgteRXRg1zpQ2iMcWZr-mIgdyDYnh1IoKq4l5v9C-JAE1-Qcy/pub?gid=1619668403&single=true&output=csv" \
    problemsru resources/list-problemsru.ttl --reference problemdata.json


python ../eliozo_client.py ingest-rdf abc resources/skos-topics.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc resources/skos-methods.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc resources/skos-domains.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc resources/skos-questions.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc resources/list-olympiads.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc resources/list-sources.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc resources/list-concepts.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc resources/list-videos.ttl --reference problemdata.json
