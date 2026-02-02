#!/bin/bash

# Get the directory of this script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../../" && pwd)"

# Activate virtual environment if not already active
if [ -z "$VIRTUAL_ENV" ]; then
    if [ -f "$PROJECT_ROOT/wsheet-env/bin/activate" ]; then
        source "$PROJECT_ROOT/wsheet-env/bin/activate"
    else
        echo "Warning: Virtual environment not found at $PROJECT_ROOT/wsheet-env/bin/activate"
    fi
fi
ELIOZO_HOME="$PROJECT_ROOT/scripts"

MATH_HOME="/Users/kapsitis/workspace-public/math/problembase"

echo "Starting subdomain classification..."

# python3 $ELIOZO_HOME/eliozo_client.py add-metadata $MATH_HOME/LV.VOL/lv-vol-2004/content_lv.md subdomain --output ./lv-vol-2004/content_lv.md --reference problemdata.json
# python3 $ELIOZO_HOME/eliozo_client.py add-metadata $MATH_HOME/LV.VOL/lv-vol-2005/content_lv.md subdomain --output ./lv-vol-2005/content_lv.md --reference problemdata.json
# python3 $ELIOZO_HOME/eliozo_client.py add-metadata $MATH_HOME/LV.VOL/lv-vol-2006/content_lv.md subdomain --output ./lv-vol-2006/content_lv.md --reference problemdata.json
# python3 $ELIOZO_HOME/eliozo_client.py add-metadata $MATH_HOME/LV.VOL/lv-vol-2007/content_lv.md subdomain --output ./lv-vol-2007/content_lv.md --reference problemdata.json
# python3 $ELIOZO_HOME/eliozo_client.py add-metadata $MATH_HOME/LV.VOL/lv-vol-2008/content_lv.md subdomain --output ./lv-vol-2008/content_lv.md --reference problemdata.json
# python3 $ELIOZO_HOME/eliozo_client.py add-metadata $MATH_HOME/LV.VOL/lv-vol-2009/content_lv.md subdomain --output ./lv-vol-2009/content_lv.md --reference problemdata.json
# python3 $ELIOZO_HOME/eliozo_client.py add-metadata $MATH_HOME/LV.VOL/lv-vol-2010/content_lv.md subdomain --output ./lv-vol-2010/content_lv.md --reference problemdata.json
# python3 $ELIOZO_HOME/eliozo_client.py add-metadata $MATH_HOME/LV.VOL/lv-vol-2011/content_lv.md subdomain --output ./lv-vol-2011/content_lv.md --reference problemdata.json
# python3 $ELIOZO_HOME/eliozo_client.py add-metadata $MATH_HOME/LV.VOL/lv-vol-2012/content_lv.md subdomain --output ./lv-vol-2012/content_lv.md --reference problemdata.json
python3 $ELIOZO_HOME/eliozo_client.py add-metadata $MATH_HOME/LV.VOL/lv-vol-2013/content_lv.md subdomain --output ./lv-vol-2013/content_lv.md --reference problemdata.json
python3 $ELIOZO_HOME/eliozo_client.py add-metadata $MATH_HOME/LV.VOL/lv-vol-2014/content_lv.md subdomain --output ./lv-vol-2014/content_lv.md --reference problemdata.json
python3 $ELIOZO_HOME/eliozo_client.py add-metadata $MATH_HOME/LV.VOL/lv-vol-2015/content_lv.md subdomain --output ./lv-vol-2015/content_lv.md --reference problemdata.json
python3 $ELIOZO_HOME/eliozo_client.py add-metadata $MATH_HOME/LV.VOL/lv-vol-2016/content_lv.md subdomain --output ./lv-vol-2016/content_lv.md --reference problemdata.json
python3 $ELIOZO_HOME/eliozo_client.py add-metadata $MATH_HOME/LV.VOL/lv-vol-2017/content_lv.md subdomain --output ./lv-vol-2017/content_lv.md --reference problemdata.json
python3 $ELIOZO_HOME/eliozo_client.py add-metadata $MATH_HOME/LV.VOL/lv-vol-2018/content_lv.md subdomain --output ./lv-vol-2018/content_lv.md --reference problemdata.json
python3 $ELIOZO_HOME/eliozo_client.py add-metadata $MATH_HOME/LV.VOL/lv-vol-2019/content_lv.md subdomain --output ./lv-vol-2019/content_lv.md --reference problemdata.json
python3 $ELIOZO_HOME/eliozo_client.py add-metadata $MATH_HOME/LV.VOL/lv-vol-2020/content_lv.md subdomain --output ./lv-vol-2020/content_lv.md --reference problemdata.json
python3 $ELIOZO_HOME/eliozo_client.py add-metadata $MATH_HOME/LV.VOL/lv-vol-2021/content_lv.md subdomain --output ./lv-vol-2021/content_lv.md --reference problemdata.json
python3 $ELIOZO_HOME/eliozo_client.py add-metadata $MATH_HOME/LV.VOL/lv-vol-2022/content_lv.md subdomain --output ./lv-vol-2022/content_lv.md --reference problemdata.json
python3 $ELIOZO_HOME/eliozo_client.py add-metadata $MATH_HOME/LV.VOL/lv-vol-2023/content_lv.md subdomain --output ./lv-vol-2023/content_lv.md --reference problemdata.json
python3 $ELIOZO_HOME/eliozo_client.py add-metadata $MATH_HOME/LV.VOL/lv-vol-2024/content_lv.md subdomain --output ./lv-vol-2024/content_lv.md --reference problemdata.json
python3 $ELIOZO_HOME/eliozo_client.py add-metadata $MATH_HOME/LV.VOL/lv-vol-2025/content_lv.md subdomain --output ./lv-vol-2025/content_lv.md --reference problemdata.json

echo "Done!"
