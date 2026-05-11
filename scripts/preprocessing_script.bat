@echo off
set PYTHONIOENCODING=utf-8
python eliozo_client.py add-metadata ../../math/problembase/LV.VOL/lv-vol-2019/content_lv.md hasSolutionStructure --mode text --provider gpt-4o --output ./output/content.md --reference problemdata.json
