#!/bin/bash

export PYTHONPATH=../..
export RDF_PREF="../../../qualification-project/migration-script/resources"

rm -fr temp
mkdir temp
python ../eliozo_client.py md-repository-to-turtle \
    "https://docs.google.com/spreadsheets/d/e/2PACX-1vT1Il_-qJURh8sZHRN1oJSwok4kRUjcA7VCOhDfg1PnTUC14k4skRRl3NrUDEbd1vELQq_ALwEU9Ltx/pub?output=csv" \
    temp --reference ../tests/md-to-turtle/task.json

python eliozo_client.py drop-rdf abc --reference problemdata.json
python eliozo_client.py create-rdf-dataset abc --reference problemdata.json

python eliozo_client.py ingest-rdf abc temp/LV-AMO-2003-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-AMO-2004-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-AMO-2005-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-AMO-2006-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-AMO-2007-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-AMO-2008-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-AMO-2009-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-AMO-2010-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-AMO-2011-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-AMO-2012-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-AMO-2013-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-AMO-2014-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-AMO-2015-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-AMO-2016-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-AMO-2017-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-AMO-2018-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-AMO-2019-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-AMO-2022A-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-AMO-2022B-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-AMO-2023-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-AMO-2024-content.ttl --reference problemdata.json

python eliozo_client.py ingest-rdf abc temp/LV-NOL-2004-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-NOL-2005-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-NOL-2006-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-NOL-2007-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-NOL-2008-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-NOL-2009-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-NOL-2010-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-NOL-2011-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-NOL-2012-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-NOL-2013-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-NOL-2014-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-NOL-2015-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-NOL-2016-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-NOL-2017-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-NOL-2018-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-NOL-2019-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-NOL-2020-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-NOL-2021-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-NOL-2022-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-NOL-2023-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-NOL-2024-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-NOL-2025-content.ttl --reference problemdata.json

python eliozo_client.py ingest-rdf abc temp/LV-SOL-2020-content.ttl --reference problemdata.json

python eliozo_client.py ingest-rdf abc temp/LV-VOL-2004-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-VOL-2005-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-VOL-2006-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-VOL-2007-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-VOL-2008-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-VOL-2009-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-VOL-2010-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-VOL-2011-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-VOL-2012-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-VOL-2013-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-VOL-2014-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-VOL-2015-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-VOL-2016-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-VOL-2017-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-VOL-2018-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-VOL-2019-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-VOL-2020-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-VOL-2021-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-VOL-2022-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-VOL-2023-content.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc temp/LV-VOL-2024-content.ttl --reference problemdata.
python eliozo_client.py ingest-rdf abc temp/LV-VOL-2025-content.ttl --reference problemdata.


python eliozo_client.py ingest-rdf abc ${RDF_PREF}/concepts.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc ${RDF_PREF}/data_olympiads.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc ${RDF_PREF}/skos_method.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc ${RDF_PREF}/skos_subdomain.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc ${RDF_PREF}/skos_topic.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc ${RDF_PREF}/topics.ttl --reference problemdata.json
python eliozo_client.py ingest-rdf abc ${RDF_PREF}/youtube.ttl --reference problemdata.json
