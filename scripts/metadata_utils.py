import os
import sys
import requests
import json
import re

class MetadataUtils:
    openai_api_key = "NA"
    headers = dict()

    def __init__(self, openai_api_key): 
        self.openai_api_key = openai_api_key
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {openai_api_key}'
        }

        # Stricter system instructions to enforce raw JSON
        self.system_instructions = {
            "questionType": (
                "You are a helpful assistant. Respond ONLY with a valid JSON object "
                "like {\"uzdevuma_tips\": \"Prove\"} and nothing else. "
                "Do not include any extra explanation or text outside the JSON."
            ),
            "domain": (
                "You are a helpful assistant responding with JSON. "
                "JSON should contain one property 'uzdevuma_tips' with a single value from this list: ['Alg', 'Comb', 'Geom', 'NT']"
            )
        }

        self.instructions = {
            "questionType": (
                "Lūdzu atrodi matemātikas uzdevuma tipu:\n\n"
                "{problem_text_placeholder}\n\n"
                "Iespējamie jautājumu tipi ir: "
                "'FindAll' (uzdevumi, kuros jāatrod visi atrisinājumi); "
                "'FindCount' (uzdevumi, kuros jāsaskaita cik iespēju vai atrisinājumu skaits); "
                "'FindOptimal' (uzdevumi, kuros jāatrod maksimālais vai minimālais risinājums); "
                "'FindExample' (uzdevumi, kuros jāatrod 1 piemērs vai pretpiemērs); "
                "'Prove' (uzdevumi, kuros jāpierāda apgalvojums); "
                "'ProveDisprove' (uzdevumi, kuros apgalvojums ir jāpierāda vai jāapgāž); "
                "'Algorithm' (uzdevumi, kuros jāatrod procedūra vai spēles stratēģija)."
            )
        }

    def classify_problem(self, problem_text, problem_solution, property):
        model = "gpt-4.1"

        user_prompt = self.instructions[property].format(problem_text_placeholder=problem_text)
        system_prompt = self.system_instructions[property]

        print("\nPreparing to send request to OpenAI...")
        print(f"Prompt Preview (first 300 chars):\n{user_prompt[:300]}...\n")

        data = {
            "model": model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            "max_tokens": 1000,
            "seed": 42,
            "temperature": 1.0
        }

        try:
            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers=self.headers,
                json=data,
                timeout=30
            )
            response.raise_for_status()
            result = response.json()

            content = result['choices'][0]['message']['content']
            print(f"GPT Raw Response:\n{content}\n")

            # Try to load entire response as JSON first
            try:
                parsed = json.loads(content)
                return parsed.get("uzdevuma_tips", "NA")
            except json.JSONDecodeError:
                # Fallback to extract JSON block using regex
                json_match = re.search(r'\{.*?\}', content, re.DOTALL)
                if json_match:
                    try:
                        parsed = json.loads(json_match.group(0))
                        return parsed.get("uzdevuma_tips", "NA")
                    except json.JSONDecodeError as json_err:
                        print(f"Could not parse extracted JSON: {json_err}")
                        return "NA"
                else:
                    print("No JSON object found in GPT response.")
                    return "NA"

        except requests.RequestException as api_err:
            sys.stderr.write(f"API request error: {api_err}\n")
            return "NA"
        except Exception as e:
            sys.stderr.write(f"Unexpected error: {e}\n")
            return "NA"

    def get_query_param(self, query, seed):
        model = "gpt-4.1"

        data = {
            "model": model,
            "messages": [
                {
                    "role": "system",
                    "content": self.system_instructions.get("standart_system_message", "")
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
            response.raise_for_status()
            result = response.json()
            print(f"get_query_param result:\n{result}")
            return result
        except requests.RequestException as e:
            sys.stderr.write(f"API request error: {e}\n")
            return {"error": "API request failed"}
        except (KeyError, ValueError, json.JSONDecodeError) as e:
            sys.stderr.write(f"Error processing API response: {e}\n")
            return {"error": "Invalid format in API response"}
