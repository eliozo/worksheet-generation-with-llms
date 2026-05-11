$env:PYTHONIOENCODING = "utf-8"
# python eliozo_client.py add-metadata ../../math/problembase/LV.VOL/lv-vol-2018/content_lv.md hasSolutionStructure --mode text --provider gpt-4o --output ../../math/problembase/LV.VOL/lv-vol-2018/content_lv2.md --reference ../../math/problembase/LV.VOL/lv-vol-2018/problemdata.json
# python eliozo_client.py add-metadata ../../math/problembase/LV.VOL/lv-vol-2019/content_lv.md hasSolutionStructure --mode text --provider gpt-4o --output ../../math/problembase/LV.VOL/lv-vol-2019/content_lv2.md --reference ../../math/problembase/LV.VOL/lv-vol-2019/problemdata.json

python eliozo_client.py add-metadata ../../math/problembase/LV.VOL/lv-vol-2018/content_lv.md hasSolutionConcept --mode text --provider gpt-4o --output ../../math/problembase/LV.VOL/lv-vol-2018/content_lv2.md --reference ../../math/problembase/LV.VOL/lv-vol-2018/problemdata.json
python eliozo_client.py add-metadata ../../math/problembase/LV.VOL/lv-vol-2019/content_lv.md hasSolutionConcept --mode text --provider gpt-4o --output ../../math/problembase/LV.VOL/lv-vol-2019/content_lv2.md --reference ../../math/problembase/LV.VOL/lv-vol-2019/problemdata.json
