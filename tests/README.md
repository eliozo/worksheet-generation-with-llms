# Weaviate Utils Tests

This directory contains integration tests for `scripts/weaviate_utils.py`. These tests interact with a live Weaviate instance to verify schema creation, deletion, and searching behaviors.


## Initial Setup

To set up the environment from scratch, run the following commands from the project root:

```bash
# 1. Create a virtual environment named "wsheet-env"
python3 -m venv wsheet-env

# 2. Activate the virtual environment
source wsheet-env/bin/activate

# 3. Install required libraries
pip install weaviate-client pytest python-dotenv rdflib requests
```

## Prerequisites

1.  **Virtual Environment**: Ensure you are running in a Python virtual environment.
2.  **Dependencies**: Install the required packages.
    ```bash
    pip install weaviate-client python-dotenv pytest rdflib requests
    ```
    *Note: Ensure `weaviate-client` version is compatible with the code (v4 client is used).*

3.  **Environment Variables**:
    You need a `.env` file in the project root (or ensuring environment variables are set) containing:
    ```
    WEAVIATE_URL=...
    WEAVIATE_API_KEY=...
    OPENAI_API_KEY=...
    ```

## Running the Tests

To run the tests, use `pytest` from the project root directory.

### Command Line
```bash
# Run all tests in the file
pytest tests/weaviate_utils_test.py

# Run with output processing to see print statements (optional)
pytest -s tests/weaviate_utils_test.py
```
