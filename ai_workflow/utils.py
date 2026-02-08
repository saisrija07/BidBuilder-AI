import os
import json
import sys
import asyncio
from datetime import datetime
import time
from dotenv import load_dotenv
from groq import AsyncGroq
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

MODEL = "openai/gpt-oss-20b"
MAX_RETRIES = 3

load_dotenv()

client = AsyncGroq(api_key=os.environ.get("GROK_API_KEY"))

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

async def call_ai_model(prompt):
    try:
        for i in range(MAX_RETRIES):
            try:
                response = await client.chat.completions.create(
                    model=MODEL,
                    messages=[
                        {"role": "system", "content": "You are a helpful AI assistant. Output valid JSON."},
                        {"role": "user", "content": prompt}
                    ],
                )
                usage = response.usage
                message_content = json.loads(response.choices[0].message.content)
                return {
                    "response": message_content,
                    "tokens": {
                        "total": usage.total_tokens,
                        "input": usage.prompt_tokens,
                        "output": usage.completion_tokens
                    }
                }
            except Exception as e:
                if i < MAX_RETRIES - 1:
                    await asyncio.sleep(2 ** i)
                else:
                    raise Exception("Max retries reached.")
    except Exception as e:
        return {}

async def generate_executive_summary(params_dict):
    prompt = generate_exec_summary_prompt(params_dict)
    return await call_ai_model(prompt)

async def generate_why_us(params_dict):
    prompt = generate_why_us_prompt(params_dict)
    return await call_ai_model(prompt)

async def generate_solution_arch(params_dict):
    prompt = generate_solution_arch_prompt(params_dict)
    return await call_ai_model(prompt)

async def generate_scope_of_work(params_dict):
    prompt = generate_scope_of_work_prompt(params_dict)
    return await call_ai_model(prompt)

async def generate_timeline_table(params_dict):
    prompt = generate_timeline_table_prompt(params_dict)
    return await call_ai_model(prompt)

async def generate_team_structure(params_dict):
    prompt = generate_team_structure_prompt(params_dict)
    return await call_ai_model(prompt)

async def generate_cost_breakdown(params_dict):
    prompt = generate_cost_breakdown_prompt(params_dict)
    return await call_ai_model(prompt)

async def generate_risk_matrix(params_dict):
    prompt = generate_risk_matrix_prompt(params_dict)
    return await call_ai_model(prompt)

async def generate_qa_plan(params_dict):
    prompt = generate_qa_plan_prompt(params_dict)
    return await call_ai_model(prompt)

async def generate_tech_stack_list(params_dict):
    prompt = generate_tech_stack_list_prompt(params_dict)
    return await call_ai_model(prompt)

async def generate_case_study(params_dict):
    prompt = generate_case_study_prompt(params_dict)
    return await call_ai_model(prompt)

async def generate_next_steps(params_dict):
    prompt = generate_next_steps_prompt(params_dict)
    return await call_ai_model(prompt)

async def generate_proposal_context(params_dict):
    context = {}
    
    # 1. Start the timer
    start_time = time.perf_counter()

    # 2. Create the list of coroutines (pending tasks)
    tasks = [
        generate_executive_summary(params_dict),
        generate_why_us(params_dict),
        generate_solution_arch(params_dict),
        generate_scope_of_work(params_dict),
        generate_timeline_table(params_dict),
        generate_team_structure(params_dict),
        generate_cost_breakdown(params_dict),
        generate_risk_matrix(params_dict),
        generate_qa_plan(params_dict),
        generate_tech_stack_list(params_dict),
        generate_case_study(params_dict),
        generate_next_steps(params_dict)
    ]

    # 3. Fire all tasks concurrently
    results = await asyncio.gather(*tasks)
    
    # 4. Stop the timer
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    
    token_count = 0
    input_token_count = 0
    output_token_count = 0

    # 5. Process results
    for result in results:
        # specific check to ensure we don't crash on empty/failed results
        if isinstance(result, dict) and "response" in result:
            context.update(result["response"])
            
            # safeguard for token keys matching your previous structure
            tokens = result.get("tokens", {})
            token_count += tokens.get("total", 0)
            
            # Handling potential key variations (prompt vs input)
            input_token_count += tokens.get("input", tokens.get("prompt", 0)) 
            output_token_count += tokens.get("output", tokens.get("completion", 0))

    metadata = {
        "generated_at": datetime.now().isoformat() + "Z",
        "duration_seconds": round(elapsed_time, 2),  # <--- Added here
        "token_count": token_count,
        "input_token_count": input_token_count,
        "output_token_count": output_token_count,
        "input": params_dict
    }

    final_context = {
        "metadata": metadata,
        "context": context
    }
    
    return final_context

async def main():
    final_context = await generate_proposal_context(params_dict)
    with open("output/proposal_context.json", "w") as f:
        json.dump(final_context, f, indent=4)

if __name__ == "__main__":
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())