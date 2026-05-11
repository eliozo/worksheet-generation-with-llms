# Metadata Utils Tests

This directory contains unit tests and integration tests for `scripts/metadata_utils_new.py` and related functionality.

## Test Files

- `test_index_loading.py`: Verifies that the subdomain CSV is loaded correctly and that the 'branch' logic works.
- `test_subdomain_alternative.py`: Verifies that subdomain classification can handle alternative values and dictionary responses, and that the markdown insertion logic works correctly.
- `test_subdomain_classification.py`: Original integration/unit tests for classification (check if it uses real OpenAI calls or mocks).

## How to Run Tests

You can run all tests in this directory using the provided shell script:

```bash
./run_all_tests.sh
```
(Make sure to make it executable: `chmod +x run_all_tests.sh`)

Running Pytest Directly from the project root:

```bash
pytest tests/metadata_utils
```

## Running command-line 

To compare before and after metadata insertion: 

```
export MATH_HOME="/Users/kapsitis/workspace-public/math/problembase"
diff $MATH_HOME/LV.VOL/lv-vol-2004/content_lv.md ./lv-vol-2004/content_lv.md
diff $MATH_HOME/LV.VOL/lv-vol-2005/content_lv.md ./lv-vol-2005/content_lv.md
diff $MATH_HOME/LV.VOL/lv-vol-2006/content_lv.md ./lv-vol-2006/content_lv.md
```