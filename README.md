# worksheet-generation-with-llms
Master's degree project "Creating Worksheets with Large Language Models"  
Author: Elizabete Ozoliņa, University of Latvia, 2025  

Commandline tool to create math olympiad worksheets!

## Prerequisites

You need to create an .env file with this information
```
WEAVIATE_URL=...
WEAVIATE_API_KEY=...
OPENAI_API_KEY=...
FUSEKI_URL=...
FUSEKI_USER=...
FUSEKI_PASSWORD=...
```

Also you need to install Python and install necessary libraries:  
**Suggestion:** Use virtual environment instead of default Python to have less issues ;)  
```
# log in as jenkins in Linux (or your user account to create worksheets manually)
cd ~
mkdir venvs
cd venvs/
python3 --version
python3 -m venv eliozo_env
cd ..
source ~/venvs/eliozo_env/bin/activate
```

```
pip install jenkins
pip install python-dotenv
pip install rdflib
pip install requests
pip install weaviate-client
pip install pypandoc
pip install jinja2
```

## Directory structure
This repo has 3 directories:
1) **generated-worksheets**, where generated worksheets are located
2) **scripts**, where all scripts are located
3) **tests**, where all tests are located

## Main commands 
To start using this commandline tool, you need to find demo_mvp.bat file
This file contains all the necessary commands to generate worksheet:
```

```

## Resources
OpenAI function agent documentation: https://platform.openai.com/docs/guides/function-calling?api-mode=chat


