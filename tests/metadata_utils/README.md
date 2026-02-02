All script tests for metadata_utils_new.py and other metadata extraction. 

To run the tests, use the following command:

```bash
pytest tests/metadata_utils/test_subdomain_classification.py
``` 

To compare before and after metadata insertion: 

```bash
export MATH_HOME="/Users/kapsitis/workspace-public/math/problembase"
diff $MATH_HOME/LV.VOL/lv-vol-2004/content_lv.md ./lv-vol-2004/content_lv.md
diff $MATH_HOME/LV.VOL/lv-vol-2005/content_lv.md ./lv-vol-2005/content_lv.md
diff $MATH_HOME/LV.VOL/lv-vol-2006/content_lv.md ./lv-vol-2006/content_lv.md
```