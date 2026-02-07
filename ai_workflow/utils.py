import os
import json
import asyncio
from dotenv import load_dotenv
from openai import AsyncOpenAI 
from ai_workflow.prompts import (
    generate_exec_summary_prompt,
    generate_why_us_prompt,
    generate_solution_arch_prompt,
    generate_scope_of_work_prompt,
    generate_timeline_table_prompt,
    generate_team_structure_prompt,
    generate_cost_breakdown_prompt,
    generate_risk_matrix_prompt,
    generate_qa_plan_prompt,
    generate_tech_stack_list_prompt,
    generate_case_study_prompt,
    generate_next_steps_prompt
    
)
from groq import Groq
MODEL = "openai/gpt-oss-20b"
# Load environment variables
load_dotenv()

# Initialize Async OpenAI Client
# client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
client = Groq(api_key = os.environ.get("GROK_API_KEY"))

params_dict = {
    "client_name": "Deloitte",
    "client_industry": "IT",
    "project_goal": "Integrate AI into our workflow",
    "target_audience": "Developers",
    "timeline": "01/02/2026 - 01/05/2026",
    "budget_range": "$10000",
    "tech_pref": ["pytorch", "automation tools"],
    "tone": "formal"
}

def generate_executive_summary(params_dict):
    try:
        prompt = generate_exec_summary_prompt(params_dict)
        
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant. Output valid JSON."},
                {"role": "user", "content": prompt}
            ],
            # response_format={"type": "json_object"},
        )
        usage = response.usage
        print(f"Exec Summary Tokens: {usage.total_tokens} (Input: {usage.prompt_tokens}, Output: {usage.completion_tokens})")
        return response.choices[0].message.content

    except Exception as e:
        print(f"Error in Exec Summary: {e}")
        return "{}"

def generate_why_us(params_dict):
    try:
        prompt = generate_why_us_prompt(params_dict)
        
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant. Output valid JSON."},
                {"role": "user", "content": prompt}
            ],
            # response_format={"type": "json_object"},
        )
        usage = response.usage
        print(f"Exec Summary Tokens: {usage.total_tokens} (Input: {usage.prompt_tokens}, Output: {usage.completion_tokens})")
        return response.choices[0].message.content

    except Exception as e:
        print(f"Error in Why Us: {e}")
        return "{}"
    
def generate_solution_arch(params_dict):
    try:
        prompt = generate_solution_arch_prompt(params_dict)
        
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant. Output valid JSON."},
                {"role": "user", "content": prompt}
            ],
            # response_format={"type": "json_object"},
        )
        usage = response.usage
        print(f"Exec Summary Tokens: {usage.total_tokens} (Input: {usage.prompt_tokens}, Output: {usage.completion_tokens})")
        return response.choices[0].message.content

    except Exception as e:
        print(f"Error in Why Us: {e}")
        return "{}"
    
def generate_scope_of_work(params_dict):
    try:
        prompt = generate_scope_of_work_prompt(params_dict)
        
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant. Output valid JSON."},
                {"role": "user", "content": prompt}
            ],
            # response_format={"type": "json_object"},
        )
        usage = response.usage
        print(f"Exec Summary Tokens: {usage.total_tokens} (Input: {usage.prompt_tokens}, Output: {usage.completion_tokens})")
        return response.choices[0].message.content

    except Exception as e:
        print(f"Error in Why Us: {e}")
        return "{}"
    
def generate_timeline_table(params_dict):
    try:
        prompt = generate_timeline_table_prompt(params_dict)
        
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant. Output valid JSON."},
                {"role": "user", "content": prompt}
            ],
            # response_format={"type": "json_object"},
        )
        usage = response.usage
        print(f"Exec Summary Tokens: {usage.total_tokens} (Input: {usage.prompt_tokens}, Output: {usage.completion_tokens})")
        return response.choices[0].message.content

    except Exception as e:
        print(f"Error in Why Us: {e}")
        return "{}"
    
def generate_team_structure(params_dict):
    try:
        prompt = generate_team_structure_prompt(params_dict)
        
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant. Output valid JSON."},
                {"role": "user", "content": prompt}
            ],
            # response_format={"type": "json_object"},
        )
        usage = response.usage
        print(f"Exec Summary Tokens: {usage.total_tokens} (Input: {usage.prompt_tokens}, Output: {usage.completion_tokens})")
        return response.choices[0].message.content

    except Exception as e:
        print(f"Error in Why Us: {e}")
        return "{}"
    
def generate_cost_breakdown(params_dict):
    try:
        prompt = generate_cost_breakdown_prompt(params_dict)
        
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant. Output valid JSON."},
                {"role": "user", "content": prompt}
            ],
            # response_format={"type": "json_object"},
        )
        usage = response.usage
        print(f"Exec Summary Tokens: {usage.total_tokens} (Input: {usage.prompt_tokens}, Output: {usage.completion_tokens})")
        return response.choices[0].message.content

    except Exception as e:
        print(f"Error in Why Us: {e}")
        return "{}"

def generate_risk_matrix(params_dict):
    try:
        prompt = generate_risk_matrix_prompt(params_dict)
        
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant. Output valid JSON."},
                {"role": "user", "content": prompt}
            ],
            # response_format={"type": "json_object"},
        )
        usage = response.usage
        print(f"Exec Summary Tokens: {usage.total_tokens} (Input: {usage.prompt_tokens}, Output: {usage.completion_tokens})")
        return response.choices[0].message.content

    except Exception as e:
        print(f"Error in Why Us: {e}")
        return "{}"
    
def generate_qa_plan(params_dict):
    try:
        prompt = generate_qa_plan_prompt(params_dict)
        
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant. Output valid JSON."},
                {"role": "user", "content": prompt}
            ],
            # response_format={"type": "json_object"},
        )
        usage = response.usage
        print(f"Exec Summary Tokens: {usage.total_tokens} (Input: {usage.prompt_tokens}, Output: {usage.completion_tokens})")
        return response.choices[0].message.content

    except Exception as e:
        print(f"Error in Why Us: {e}")
        return "{}"
    
def generate_tech_stack_list(params_dict):
    try:
        prompt = generate_tech_stack_list_prompt(params_dict)
        
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant. Output valid JSON."},
                {"role": "user", "content": prompt}
            ],
            # response_format={"type": "json_object"},
        )
        usage = response.usage
        print(f"Exec Summary Tokens: {usage.total_tokens} (Input: {usage.prompt_tokens}, Output: {usage.completion_tokens})")
        return response.choices[0].message.content

    except Exception as e:
        print(f"Error in Why Us: {e}")
        return "{}"
    

def generate_case_study(params_dict):
    try:
        prompt = generate_case_study_prompt(params_dict)
        
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant. Output valid JSON."},
                {"role": "user", "content": prompt}
            ],
            # response_format={"type": "json_object"},
        )
        usage = response.usage
        print(f"Exec Summary Tokens: {usage.total_tokens} (Input: {usage.prompt_tokens}, Output: {usage.completion_tokens})")
        return response.choices[0].message.content

    except Exception as e:
        print(f"Error in Why Us: {e}")
        return "{}"
    
def generate_next_steps(params_dict):
    try:
        prompt = generate_next_steps_prompt(params_dict)
        
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant. Output valid JSON."},
                {"role": "user", "content": prompt}
            ],
            # response_format={"type": "json_object"},
        )
        usage = response.usage
        print(f"Exec Summary Tokens: {usage.total_tokens} (Input: {usage.prompt_tokens}, Output: {usage.completion_tokens})")
        return response.choices[0].message.content

    except Exception as e:
        print(f"Error in Why Us: {e}")
        return "{}"
    
# async def main():
#     # Fan-Out: Execute both requests in parallel
#     results = await asyncio.gather(
#         generate_executive_summary(params_dict),
#         generate_why_us(params_dict)
#     )

#     exec_summary = json.loads(results[0])
#     why_us = json.loads(results[1])

#     print("--- Executive Summary ---")
#     print(json.dumps(exec_summary, indent=2))
#     print("\n--- Why Us ---")
#     print(json.dumps(why_us, indent=2))

if __name__ == "__main__":
    print(generate_next_steps(params_dict))
