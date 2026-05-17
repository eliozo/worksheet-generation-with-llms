#!/bin/bash

python eliozo_client.py add-metadata ../../math/problembase/LV.VOL/lv-vol-2019/content_lv.md hasSolutionConcept --mode text --provider gpt-4o --output ../../math/problembase/LV.VOL/lv-vol-2019/content_lv3.md --reference ../../math/problembase/LV.VOL/lv-vol-2019/problemdata.json


python eliozo_client.py add-metadata ../../math/problembase/LV.VOL/lv-vol-2019/content_lv.md hasSolutionConcept --mode text --provider gpt-4o --output ../../math/problembase/LV.VOL/lv-vol-2019/content_lv3.md --reference ../../math/problembase/LV.VOL/lv-vol-2019/problemdata.json
