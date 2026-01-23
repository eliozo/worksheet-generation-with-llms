#!/bin/bash 
export PYTHONPATH=..
export RDF_PREF="setup/temp"

# rm -fr problemdata.json
# python eliozo_client.py drop-vectors eliozo-model --reference problemdata.json
# python eliozo_client.py create-schema-vectors eliozo-model --reference problemdata.json
# echo "Schema created"
# School/Preparation olympiads
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-sol-2020-content_lv.ttl --reference problemdata.json


# Content in English
# Skip for now - as they may have empty metadata... 
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-amo-2022b-content_en.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/ww-imoshl-2022-content_en.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-nol-2023-content_en.ttl --reference problemdata.json




# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-amo-2003-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-amo-2004-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-amo-2005-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-amo-2006-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-amo-2007-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-amo-2008-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-amo-2009-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-amo-2010-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-amo-2011-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-amo-2012-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-amo-2013-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-amo-2014-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-amo-2015-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-amo-2016-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-amo-2017-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-amo-2018-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-amo-2019-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-amo-2022A-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-amo-2022B-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-amo-2023-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-amo-2024-content_lv.ttl --reference problemdata.json


# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-vol-2004-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-vol-2005-content_lv.ttl --reference problemdata.json
# python3 eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-vol-2006-content_lv.ttl --reference problemdata.json
# python3 eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-vol-2007-content_lv.ttl --reference problemdata.json
# python3 eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-vol-2008-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-vol-2009-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-vol-2010-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-vol-2011-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-vol-2012-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-vol-2013-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-vol-2014-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-vol-2015-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-vol-2016-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-vol-2017-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-vol-2018-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-vol-2019-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-vol-2020-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-vol-2021-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-vol-2022-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-vol-2023-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-vol-2024-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-vol-2025-content_lv.ttl --reference problemdata.json

# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-nol-2004-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-nol-2005-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-nol-2006-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-nol-2007-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-nol-2008-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-nol-2009-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-nol-2010-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-nol-2011-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-nol-2012-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-nol-2013-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-nol-2014-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-nol-2015-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-nol-2016-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-nol-2017-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-nol-2018-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-nol-2019-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-nol-2020-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-nol-2021-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-nol-2022-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-nol-2023-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-nol-2024-content_lv.ttl --reference problemdata.json
# python eliozo_client.py ingest-vectors eliozo-model ${RDF_PREF}/lv-nol-2025-content_lv.ttl --reference problemdata.json


# TODO: Also migrate and ingest AMO.2025; NOL.2026 data.