#!/bin/bash

export PYTHONPATH=../..
export RDF_PREF="../../../qualification-project/migration-script/resources"

rm -fr temp
mkdir temp
python ../eliozo_client.py metadata-to-turtle \
    "https://docs.google.com/spreadsheets/d/e/2PACX-1vQvAsYeFYhuFLmLgtMiYFeQFeeO4e0DgteRXRg1zpQ2iMcWZr-mIgdyDYnh1IoKq4l5v9C-JAE1-Qcy/pub?gid=462395741&single=true&output=csv" \
    topics temp/skos-topics.ttl --reference problemdata.json

python ../eliozo_client.py metadata-to-turtle \
    "https://docs.google.com/spreadsheets/d/e/2PACX-1vQvAsYeFYhuFLmLgtMiYFeQFeeO4e0DgteRXRg1zpQ2iMcWZr-mIgdyDYnh1IoKq4l5v9C-JAE1-Qcy/pub?gid=1894093694&single=true&output=csv" \
    methods temp/skos-methods.ttl --reference problemdata.json

python ../eliozo_client.py metadata-to-turtle \
    "https://docs.google.com/spreadsheets/d/e/2PACX-1vQvAsYeFYhuFLmLgtMiYFeQFeeO4e0DgteRXRg1zpQ2iMcWZr-mIgdyDYnh1IoKq4l5v9C-JAE1-Qcy/pub?gid=1943031484&single=true&output=csv" \
    domains temp/skos-domains.ttl --reference problemdata.json

python ../eliozo_client.py metadata-to-turtle \
    "https://docs.google.com/spreadsheets/d/e/2PACX-1vQvAsYeFYhuFLmLgtMiYFeQFeeO4e0DgteRXRg1zpQ2iMcWZr-mIgdyDYnh1IoKq4l5v9C-JAE1-Qcy/pub?gid=56933932&single=true&output=csv" \
    questions temp/skos-questions.ttl --reference problemdata.json

python ../eliozo_client.py metadata-to-turtle \
    "https://docs.google.com/spreadsheets/d/e/2PACX-1vQvAsYeFYhuFLmLgtMiYFeQFeeO4e0DgteRXRg1zpQ2iMcWZr-mIgdyDYnh1IoKq4l5v9C-JAE1-Qcy/pub?gid=1895950034&single=true&output=csv" \
    olympiads temp/list-olympiads.ttl --reference problemdata.json

python ../eliozo_client.py metadata-to-turtle \
    "https://docs.google.com/spreadsheets/d/e/2PACX-1vSsIUjRXRU6L_MGgEmgUZlfwvygclZun964ilvH-l6F3TZ9w0I2MDce9VXqJgd4p2GZxF7vJ6OY5jcT/pub?gid=133948398&single=true&output=csv" \
    concepts temp/list-concepts.ttl --reference problemdata.json

python ../eliozo_client.py metadata-to-turtle \
    "https://docs.google.com/spreadsheets/d/e/2PACX-1vSithTBvdSFhQeovJbYVCstpt7JkDUZAKXSPOjYraqfCFW2SqNjvN5Yd_xYeIfvtSjVktmBAPo2_dDf/pub?gid=0&single=true&output=csv" \
    videos temp/list-videos.ttl --reference problemdata.json



# python eliozo_client.py ingest-rdf abc ${RDF_PREF}/skos_topic.ttl --reference problemdata.json


# python eliozo_client.py ingest-rdf abc ${RDF_PREF}/concepts.ttl --reference problemdata.json
# python eliozo_client.py ingest-rdf abc ${RDF_PREF}/data_olympiads.ttl --reference problemdata.json
# python eliozo_client.py ingest-rdf abc ${RDF_PREF}/skos_method.ttl --reference problemdata.json
# python eliozo_client.py ingest-rdf abc ${RDF_PREF}/skos_subdomain.ttl --reference problemdata.json
# python eliozo_client.py ingest-rdf abc ${RDF_PREF}/skos_topic.ttl --reference problemdata.json
# python eliozo_client.py ingest-rdf abc ${RDF_PREF}/topics.ttl --reference problemdata.json
# python eliozo_client.py ingest-rdf abc ${RDF_PREF}/youtube.ttl --reference problemdata.json