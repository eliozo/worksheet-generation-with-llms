#!/bin/bash

if [[ "$(uname -s)" == "Linux" ]]; then
export ELIOZO_PYTHON_PATH=/opt/myenv
source "$ELIOZO_PYTHON_PATH/bin/activate"
fi

export PYTHONPATH=../..

rm -fr temp
mkdir temp
rm -f problemdata.json

python ../eliozo_client.py md-repository-to-turtle temp --csv \
    "https://docs.google.com/spreadsheets/d/e/2PACX-1vT1Il_-qJURh8sZHRN1oJSwok4kRUjcA7VCOhDfg1PnTUC14k4skRRl3NrUDEbd1vELQq_ALwEU9Ltx/pub?gid=0&single=true&output=csv" \
    --reference problemdata.json

# python ../eliozo_client.py md-to-turtle temp/ww-imoshl-2022-content_en.md temp/ww-imoshl-2022-content_en.ttl en --master \
#     --reference problemdata.json

# python ../eliozo_client.py md-to-turtle temp/lv-vol-2024-content_lv.md temp/lv-vol-2024-content_lv.ttl lv --master \
#     --reference problemdata.json


python ../eliozo_client.py drop-rdf abc --reference problemdata.json
python ../eliozo_client.py create-rdf-dataset abc --reference problemdata.json



python ../eliozo_client.py ingest-rdf abc temp/bbk2012-p1-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/bbk2012-p3-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-amo-2003-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-amo-2004-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-amo-2005-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-amo-2006-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-amo-2007-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-amo-2008-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-amo-2009-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-amo-2010-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-amo-2011-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-amo-2012-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-amo-2013-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-amo-2014-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-amo-2015-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-amo-2016-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-amo-2017-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-amo-2018-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-amo-2019-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-amo-2022a-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-amo-2022b-content_en.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-amo-2022b-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-amo-2023-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-amo-2024-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-nol-2004-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-nol-2005-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-nol-2006-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-nol-2007-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-nol-2008-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-nol-2009-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-nol-2010-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-nol-2011-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-nol-2012-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-nol-2013-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-nol-2014-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-nol-2015-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-nol-2016-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-nol-2017-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-nol-2018-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-nol-2019-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-nol-2020-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-nol-2021-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-nol-2022-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-nol-2023-content_en.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-nol-2023-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-nol-2024-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-nol-2025-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-sol-2020-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-vol-2004-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-vol-2005-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-vol-2006-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-vol-2007-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-vol-2008-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-vol-2009-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-vol-2010-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-vol-2011-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-vol-2012-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-vol-2013-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-vol-2014-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-vol-2015-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-vol-2016-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-vol-2017-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-vol-2018-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-vol-2019-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-vol-2020-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-vol-2021-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-vol-2022-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-vol-2023-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-vol-2024-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/lv-vol-2025-content_lv.ttl --reference problemdata.json
python ../eliozo_client.py ingest-rdf abc temp/ww-imoshl-2022-content_en.ttl --reference problemdata.json

