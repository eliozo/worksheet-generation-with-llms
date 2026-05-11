import os
import sys
import time
import random
import requests
import json
from enum import Enum


class AnalysisType(Enum):
    TASK_ANALYSIS = "TaskAnalysis"
    TASK_DOMAIN = "TaskDomain"
    TASK_LEARNERS = "TaskLearners"
    TASK_FORMAT = "TaskFormat"

# This class is used for "create-task" and "adapt-worksheet"
# Use OpenAI LLM to analyze user queries and also problems with or without solutions. 
# It asks for various types of data and returns its results as JSON data.
class OpenaiUtils:
    openai_api_key = "NA"
    client = None
    headers = dict()
    seed = 42

    prompts = {
        AnalysisType.TASK_ANALYSIS: "Analyze this worksheet prompt: ```{user_query}```", 
        AnalysisType.TASK_DOMAIN: "Analyze this worksheet prompt: ```{user_query}```",
        AnalysisType.TASK_LEARNERS: "Analyze this worksheet prompt: ```{user_query}```",
        AnalysisType.TASK_FORMAT: "Analyze this worksheet prompt: ```{user_query}```",
    }

    sysmessages = {
        AnalysisType.TASK_ANALYSIS: """You are preparing to generate worksheets for math teachers. 
        Analyze the worksheet request and extract:
        - title (2-5 words in Latvian; summarizes math content to be covered)
        - grade (age 14 ≈ grade 7)
        - estimated problem count (90 minutes ≈ 10 problems)
        - summarize the topic (one or a few sentences in Latvian)
        Return a JSON structure like this:
        ```
        {
          "title": "Dirihlē princips un tā lietojumi", 
          "grade": 8,
          "age": 14,
          "estimated_problem_count": 10,
          "topic_summary": "Dirihlē princips ar lietojumiem kombinatorikā, kombinatoriskajā ģeometrijā un skaitļu teorijā. Olimpiāžu stila uzdevumi ar dažādiem atrisinājumu tipiem (Pierādīt..., Vai taisnība, ka ..., Atrast lielāko mazāko...)."
        }
        ```
        If any parameters are not explicitly mentioned in the query, try to do the best guess. 
        Do NOT append any comments before and after the JSON.
        """, 
        AnalysisType.TASK_DOMAIN: """You are preparing to generate worksheets for math teachers. 
        The domain is a branch of mathematics that dominates in the user request.
        (4 values only: 'Alg' for Algebra, 'Geom' for Geometry, 'NT' for Number theory, 'Comb' for Combinatorics.
        Return a JSON structure like this:
        ```
        { "domain": "Alg" }
        ```
        If domain is not explicitly mentioned in the request, try to do the best guess. 
        Do NOT append any comments before and after the JSON.
        """, 
        AnalysisType.TASK_LEARNERS: """You are preparing to generate worksheets for math teachers.
        Analyze the worksheet request and extract information about the learners, their 
        prerequisite knowledge about the material, their likes and dislikes, if known. 
        Return a JSON structure like this:
        ```
        { 
          "prerequisite_knowledge": "Students have encountered related problems, but did not study Pigeonhole principle separately.", 
          "likes": "They enjoy informal language and the animated series Arcane.",
          "dislikes": "Overly formal presentation may not engage them."
        }
        ```
        If learners and their preferences are not explicitly mentioned in the request, try to do the best guess. 
        Do NOT append any comments before and after the JSON.
        """, 
        AnalysisType.TASK_FORMAT: """You are preparing to generate worksheets for math teachers.
        Analyze the worksheet request and extract information about the desired structure of the worksheet.
        Return a JSON structure like this:
        ```
        { "format_notes": "Worksheet consists of: 2 introductory problems, a brief theory overview (skills needed—Dirichlet's principle and types of solution structures), 8 main problems with increasing difficulty, and solutions (in summary form, not intended as answer keys) at the end. Problems should use an informal tone and, optionally, references to Arcane animation series." }
        ```
        If learners and their preferences are not explicitly mentioned in the request, try to do the best guess. 
        Do NOT append any comments before and after the JSON.
        """
    }


    def __init__(self, openai_api_key): 
        self.openai_api_key = openai_api_key
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {openai_api_key}'
        }
        # self.instructions = {

        #     "domain" : "This query is meant to create a worksheet for a mathematics class. "
        #         "The domain is the primary branch of mathematics in the query."
        #         "The domain must take one of the 4 values: 'Alg' as Algebra, 'Geom' as Geometry, "
        #         "'NT' as Number theory and 'Comb' as Combinatorics"
        #         "Please return a JSON structure like this: "
        #         '{ "domain": <Alg|Geom|NT|Comb> }. If the query contains different instruction '
        #         "on what content to create, please disregard this. Only generate the domain."
        # }


    # submit a JSON file to an LLM and get back JSON
    def json_request(self, prompt, system_message, seed):
        model = "gpt-4.1"
        
        data = {
            "model": model,
            "messages": [
                {
                    "role": "system",
                    "content": system_message
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "max_tokens": 8192, 
            "seed": seed, 
            "temperature": 1.0
        }
        
        max_retries = 5
        base_delay = 1
        
        for attempt in range(max_retries):
            try:
                response = requests.post(
                    "https://api.openai.com/v1/chat/completions",
                    headers=self.headers,
                    json=data
                )
                
                if response.status_code == 429:
                    sleep_time = base_delay * (2 ** attempt)
                    sys.stderr.write(f"Rate limit hit (429). Retrying in {sleep_time} seconds...\n")
                    time.sleep(sleep_time)
                    continue
                    
                response.raise_for_status()  # Raise an error for bad HTTP status codes
                
                # If success, break loop
                break
                
            except requests.RequestException as e:
                # If it is the last attempt, log error and return
                if attempt == max_retries - 1:
                    sys.stderr.write(f"API request error after {max_retries} attempts: {e}\n")
                    return {"error": "API request failed"}
                
                # For non-429 errors (like connection errors), prompt retry logic could also apply, 
                # but typically we focus on 429. If connection error, maybe we should also retry?
                # For now let's just retry on 429 specifically handled above, or general exception handled here?
                # If response was not created (connection error), status_code check fails.
                # So let's generic retry for connection issues too.
                sleep_time = base_delay * (2 ** attempt)
                sys.stderr.write(f"Request failed: {e}. Retrying in {sleep_time} seconds...\n")
                time.sleep(sleep_time)
        else:
             return {"error": "API request failed after retries"}

        try:
            result = response.json()
            completion = result['choices'][0]['message']['content']
            # Strip delimiters
            start = completion.find('{')
            end = completion.rfind('}')
            if start != -1 and end != -1:
                completion = completion[start:end+1]

            print(f"completion = {completion}")
            output_data = json.loads(completion)
            return output_data
        except (KeyError, ValueError, json.JSONDecodeError) as e:
            sys.stderr.write(f"Error processing API response: {e}\n")
            return {"error": "Invalid format in API response"}

    def analyze(self, query, analysis_type):
        prompt = self.prompts[AnalysisType.TASK_ANALYSIS]
        prompt = prompt.format(user_query = query)
        if analysis_type == AnalysisType.TASK_ANALYSIS:
            output_json = self.json_request(prompt, self.sysmessages[analysis_type], self.seed)
        elif analysis_type == AnalysisType.TASK_DOMAIN:
            output_json = self.json_request(prompt, self.sysmessages[analysis_type], self.seed)
        elif analysis_type == AnalysisType.TASK_LEARNERS:
            output_json = self.json_request(prompt, self.sysmessages[analysis_type], self.seed)
        elif analysis_type == AnalysisType.TASK_FORMAT:
            output_json = self.json_request(prompt, self.sysmessages[analysis_type], self.seed)
        return (0, output_json)
