def get_input(params_dict):
    client_name = params_dict['client_name']
    client_industry = params_dict['client_industry']
    project_goal = params_dict['project_goal']
    target_audience = params_dict['target_audience']
    timeline = params_dict['timeline']
    budget_range = params_dict['budget_range']
    tech_pref = params_dict['tech_pref']
    tone = params_dict['tone']
    return client_name, client_industry, project_goal, target_audience, timeline, budget_range, tech_pref, tone

def generate_exec_summary_prompt(params_dict):
    client_name, client_industry, project_goal, target_audience, timeline, budget_range, tech_pref, tone = get_input(params_dict)
    prompt = f"""
        ROLE: You are an elite RFP Response Architect with 20 years of experience winning million-dollar contracts.

    TASK: Write a compelling Executive Summary for a proposal based strictly on the input data below.

    INPUT DATA:
    - Client: {client_name}
    - Industry: {client_industry}
    - Core Goal: {project_goal}
    - Target Audience: {target_audience}
    - Timeline: {timeline}
    - Budget Constraint: {budget_range}
    - Technology Preferences: {tech_pref}
    - Desired Tone: {tone}

    WRITING INSTRUCTIONS:
    1. Adopt the '{tone}' tone immediately.
    2. Focus on VALUE. Don't just list the requirements; explain how this project solves their specific pain point ({project_goal}).
    3. If the timeline or budget is tight, frame it as a "High-Priority Acceleration" or "Cost-Effective MVP."
    4. Do NOT invent specific metrics (like "we will increase revenue by 50%") unless they are in the input.
    5. Don't make any grammmatic mistake behave like you are the english literature professor with 15+ years of experience and also a great enterprener who has great knowledge about starting a new business.

    OUTPUT FORMAT (STRICT JSON ONLY):
    You must return a valid JSON object. Do not include markdown formatting (like ```json). and you should also set word limit upto maximum 200 words
    {{
        "summary": "The full executive summary text (2-3 paragraphs)."
    }}
    """
    return prompt

def generate_why_us_prompt(params_dict):
    client_name, client_industry, project_goal, target_audience, timeline, budget_range, tech_pref, tone = get_input(params_dict)
    prompt = f"""
       ROLE: You are a Senior Brand Strategist and Proposal Writer. You specialize in persuading skeptical clients to choose our agency over competitors.

    TASK: Write a powerful "Why Us?" section for a proposal in the '{client_industry}' industry.

    INPUT DATA:
    - Industry: {client_industry}
    - Client Goal: {project_goal}
    - Desired Tone: {tone}

    INSTRUCTIONS:
    1. Adopt the '{tone}' tone.
    2. Generate 3 distinct "Selling Points" that explain why we are the best choice. 
       - If Industry is "Tech/IT", focus on Innovation, Scalability, and Clean Code.
       - If Industry is "Finance/Legal", focus on Security, Compliance, and Trust.
       - If Industry is "Creative/Marketing", focus on Engagement, ROI, and Aesthetics.
    3. Make it sound confident, not arrogant.
    4. Keep the total word count under 150 words.
    5. do not use \\n in the output.


    OUTPUT FORMAT (STRICT JSON ONLY):
    You must return a valid JSON object but with a single key. Do not include markdown formatting (like ```json). it should be in one paragraph explaining why to choose us. and limit the word count upto maximum 200.
    {{
        "title": "A persuasive header (e.g., 'Why We Are The Right Partner')"
    }}
    """
    return prompt


def generate_solution_arch_prompt(params_dict):
    client_name, client_industry, project_goal, target_audience, timeline, budget_range, tech_pref, tone = get_input(params_dict)
    prompt = f"""
       ROLE: You are a Chief Technology Officer (CTO) and System Architect.
        
        TASK: Design a high-level technical solution for the following project.
        
        INPUTS:
        - Project Goal: {project_goal}
        - Preferred Tech Stack: {tech_pref}
        
        INSTRUCTIONS:
        1. Validate the 'Preferred Tech'. If it fits the goal, use it. If it's a bad fit, suggest a better alternative.
        2. Write a single, comprehensive paragraph (approx. 150 words) describing the end-to-end architecture.
        3. Explain *how* the components connect (e.g., "The React frontend communicates with the FastAPI backend via REST...").
        4. Mention the database and deployment strategy (e.g., AWS/Docker).

        OUTPUT FORMAT (STRICT JSON ONLY):
        Return a valid JSON object with a single key: "solution_architecture".
        Do not use markdown formatting.
        
        Example:
        {{
            "solution_architecture": "To achieve the goal of {project_goal}, we propose a microservices architecture using..."
        }}
        """
    return prompt
         
def generate_scope_of_work_prompt(params_dict):
    client_name, client_industry, project_goal, target_audience, timeline, budget_range, tech_pref, tone = get_input(params_dict)
    prompt = f"""
       ROLE: You are a Senior Delivery Manager and Scrum Master.
    
    TASK: Define the comprehensive Scope of Work (SOW) and Deliverables for this project.
    
    INPUTS:
    - Project Goal: {project_goal}
    - Timeline Constraint: {timeline}
    
    INSTRUCTIONS:
    1. Write a single, cohesive paragraph outlining exactly what will be delivered to the client.
    2. You MUST include these 4 distinct categories in your narrative:
       - Phase 1: Planning & Design (e.g., Wireframes, SRS Document).
       - Phase 2: Development (e.g., Source Code, API Integration).
       - Phase 3: Quality Assurance (e.g., Test Plans, UAT Sign-off).
       - Phase 4: Deployment (e.g., Cloud Setup, User Manuals, Training).
    3. Mention that these will be delivered within the {timeline} timeline.
    4. Keep the tone professional, contractual, and precise.

    OUTPUT FORMAT (STRICT JSON ONLY):
    Return a valid JSON object with a single key: "scope_of_work".
    The value must be a list of exactly 4 items.
    Each element in the list should be a string starting with Phase 1,2... followed by the description
    
    Example:
    {{
        "scope_of_work" :[
        "Phase 1: Planning & Design (e.g., Wireframes, SRS Document)",
        "Phase 2: Development (e.g., Source Code, API Integration)",
        "Phase 3: Quality Assurance (e.g., Test Plans, UAT Sign-off)",
        "Phase 4: Deployment (e.g., Cloud Setup, User Manuals, Training)"
        ]
    }}
    """
    return prompt


def generate_scope_of_work_prompt(params_dict):
    client_name, client_industry, project_goal, target_audience, timeline, budget_range, tech_pref, tone = get_input(params_dict)
    prompt = f"""
       ROLE: You are a Senior Delivery Manager and Scrum Master.
    
    TASK: Define the comprehensive Scope of Work (SOW) and Deliverables for this project.
    
    INPUTS:
    - Project Goal: {project_goal}
    - Timeline Constraint: {timeline}
    
    INSTRUCTIONS:
    1. Write a single, cohesive paragraph outlining exactly what will be delivered to the client.
    2. You MUST include these 4 distinct categories in your narrative:
       - Phase 1: Planning & Design (e.g., Wireframes, SRS Document).
       - Phase 2: Development (e.g., Source Code, API Integration).
       - Phase 3: Quality Assurance (e.g., Test Plans, UAT Sign-off).
       - Phase 4: Deployment (e.g., Cloud Setup, User Manuals, Training).
    3. Mention that these will be delivered within the {timeline} timeline.
    4. Keep the tone professional, contractual, and precise.

    OUTPUT FORMAT (STRICT JSON ONLY):
    Return a valid JSON object with a single key: "scope_of_work".
    The value must be a list of exactly 4 items.
    Each element in the list should be a string starting with Phase 1,2... followed by the description
    
    Example:
    {{
        "scope_of_work" :[
        "Phase 1: Planning & Design (e.g., Wireframes, SRS Document)",
        "Phase 2: Development (e.g., Source Code, API Integration)",
        "Phase 3: Quality Assurance (e.g., Test Plans, UAT Sign-off)",
        "Phase 4: Deployment (e.g., Cloud Setup, User Manuals, Training)"
        ]
    }}
    """
    return prompt
