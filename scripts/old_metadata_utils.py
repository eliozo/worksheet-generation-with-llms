import os
import sys
import requests
import json

class MetadataUtils:
    openai_api_key = "NA"
    client = None
    headers = dict()

    def __init__(self, openai_api_key): 
        self.openai_api_key = openai_api_key
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {openai_api_key}'
        }
        self.system_instructions = {
            "questionType" : "You are a helpful assistant designed to output JSON. JSON should contain one property named 'uzdevuma_tips'",

            "domain" : "You are a helpful assistant responding with JSON. JSON should contain one property 'uzdevuma_tips' with a single value from this list: ['Alg', 'Comb', 'Geom', NT']"
        }
        self.instructions = {
            "questionType": "Lūdzu atrodi matemātikas uzdevuma tipu: \n\n ```{problem_text_placeholder}```\n\n"
                "Iespējamie jautājumu tipi ir: "
                "'FindAll' (uzdevumi, kuros jāatrod visi atrisinājumi); "
                "'FindCount' (uzdevumi, kuros jāsaskaita cik iespēju vai atrisinājumu skaits); "
                "'FindOptimal' (uzdevumi, kuros jāatrod maksimālais vai minimālais risinājums); "
                "'FindExample' (uzdevumi, kuros jāatrod 1 piemērs vai pretpiemērs); "
                "'Prove' (uzdevumi, kuros jāpierāda apgalvojums); "
                "'ProveDisprove' (uzdevumi, kuros apgalvojums ir jāpierāda vai jāapgāž); "
                "'Algorithm' (uzdevumi, kuros jāatrod procedūra vai spēles stratēģija)."
        }

    def classify_problem(self, problem_text, problem_solution, property):
        model = "gpt-4.1"
        
        data = {
            "model": model,
            "messages": [
                {
                    "role": "system",
                    "content": self.system_instructions[property] # questionType, domain etc
                },
                {
                    "role": "user",
                    "content": self.instructions[property].format(problem_text_placeholder=problem_text)

                }
            ],
            "max_tokens": 1000, 
            "seed": 42, 
            "temperature": 1.0
        }
        
        try:
            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers=self.headers,
                json=data
            )
            response.raise_for_status()  # Raise an error for bad HTTP status codes
        except requests.RequestException as e:
            sys.stderr.write(f"API request error: {e}\n")
            return {"error": "API request failed"}

        # try:
        #     result = response.json()
        #     completion = result['choices'][0]['message']['content']
        #     data_item = json.loads(completion)
        #     # result = data_item["standart_system_message"]
        #     # print(f'result = {result}')
        #     return result
        # except (KeyError, ValueError, json.JSONDecodeError) as e:
        #     sys.stderr.write(f"Error processing API response: {e}\n")
        #     return {"error": "Invalid format in API response"}
        try:
            result = response.json()
            completion = result['choices'][0]['message']['content']
            print(f"\n🔁 Raw model output:\n{completion}\n")

            try:
                data_item = json.loads(completion)
                return data_item  # ✅ Return parsed JSON with 'uzdevuma_tips'
            except json.JSONDecodeError as e:
                sys.stderr.write(f"❌ JSON parsing error: {e}\n")
                return {"error": "Invalid JSON format", "raw": completion}

        except (KeyError, ValueError) as e:
            sys.stderr.write(f"❌ Error processing API response: {e}\n")
            return {"error": "Invalid format in API response"}

        
    def get_query_param(self, query, seed):
        model = "gpt-4.1"
        
        data = {
            "model": model,
            "messages": [
                {
                    "role": "system",
                    "content": self.system_instructions["standart_system_message"]
                },
                {
                    "role": "user",
                    "content": query
                }
            ],
            "max_tokens": 1000, 
            "seed": seed, 
            "temperature": 1.0
        }
        
        try:
            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers=self.headers,
                json=data
            )
            response.raise_for_status()  # Raise an error for bad HTTP status codes
        except requests.RequestException as e:
            sys.stderr.write(f"API request error: {e}\n")
            return {"error": "API request failed"}

        try:
            result = response.json()
            # completion = result['choices'][0]['message']['content']
            # data_item = json.loads(completion)
            # result = data_item["standart_system_message"]
            print(f'result = {result}')
            return result
        except (KeyError, ValueError, json.JSONDecodeError) as e:
            sys.stderr.write(f"Error processing API response: {e}\n")
            return {"error": "Invalid format in API response"}