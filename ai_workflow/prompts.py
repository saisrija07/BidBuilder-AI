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
        "executive_summary": "The full executive summary text (2-3 paragraphs)."
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
        "why_us": "A persuasive header (e.g., 'Why We Are The Right Partner')"
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
            "proposed_solution": "To achieve the goal of {project_goal}, we propose a microservices architecture using..."
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
        "scope_of_work": [
            "Phase 1: Planning & Design (e.g., Wireframes, SRS Document)",
            "Phase 2: Development (e.g., Source Code, API Integration)",
            "Phase 3: Quality Assurance (e.g., Test Plans, UAT Sign-off)",
            "Phase 4: Deployment (e.g., Cloud Setup, User Manuals, Training)"
        ]
    }}
    """
    return prompt


def generate_timeline_table_prompt(params_dict):
    client_name, client_industry, project_goal, target_audience, timeline, budget_range, tech_pref, tone = get_input(params_dict)
    prompt = f"""
       ROLE: You are a Senior Project Manager and Scrum Master.

    TASK: Create a detailed Project Timeline (Gantt Chart equivalent) for the project: "{project_goal}".

    INPUTS:
    - Total Duration: {timeline}

    INSTRUCTIONS:
    1. Break down the "{timeline}" duration into 5 logical phases:
       - Phase 1: Discovery & Planning (approx. 10%)
       - Phase 2: Design & Prototyping (approx. 20%)
       - Phase 3: Development & Integration (approx. 40%)
       - Phase 4: Testing & QA (approx. 20%)
       - Phase 5: Deployment & Handover (approx. 10%)
    2. Assign specific weeks (e.g., "Week 1-2") or dates to each phase.
    3. List 2-3 key deliverables for each phase.

    OUTPUT FORMAT (STRICT JSON ONLY):
    Return a valid JSON object with a single key: "timeline_table".
    The value must be a list of objects, where each object represents a phase.

    Example:
    {{
        "project_timeline": [
            {{
                "phase": "Phase 1: Discovery",
                "duration": "Week 1-2",
                "deliverables": "SRS Document, Project Plan"
            }},
            {{
                "phase": "Phase 2: Design",
                "duration": "Week 3-5",
                "deliverables": "Wireframes, UI Mockups"
            }},
            ...
        ]
    }}
    """
    return prompt

def generate_team_structure_prompt(params_dict):
    client_name, client_industry, project_goal, target_audience, timeline, budget_range, tech_pref, tone = get_input(params_dict)
    prompt = f"""
    ROLE: You are a Senior Resource Manager and HR Strategist for a top-tier software consultancy.

    TASK: Propose the optimal Team Structure (Staffing Plan) to deliver "{project_goal}" within the budget of "{budget_range}".

    INPUTS:
    - Budget: {budget_range}

    INSTRUCTIONS:
    1. ANALYZE the Budget:
       - If budget is Low (<$10k): Propose a "Lean Squad" (e.g., 1 Full Stack Dev, 1 Part-time PM).
       - If budget is Medium ($20k-$80k): Propose a "Standard Agile Team" (PM, UI/UX, Backend, Frontend, QA).
       - If budget is High ($100k+): Propose an "Enterprise Pod" (Product Owner, Scrum Master, Architects, DevOps, multiple Devs).
    2. List the specific roles required.
    3. focus should give the tech stack.

    OUTPUT FORMAT (STRICT JSON ONLY):
    Return a valid JSON object with a single key: "team_structure".
    The value must be a list of objects.

    Example:
    {{
        "team_structure": [
            {{
                "role": "Project Manager",
                "count": 1,
                "focus": "Client communication and sprint planning."
            }},
            {{
                "role": "Full Stack Developer",
                "count": 2,
                "focus": "Core feature implementation."
            }}
        ]
    }}
    """
    return prompt

def generate_cost_breakdown_prompt(params_dict):
    client_name, client_industry, project_goal, target_audience, timeline, budget_range, tech_pref, tone = get_input(params_dict)
    prompt = f"""
    ROLE: You are a Senior Project Estimator and Financial Analyst for a software consultancy.

    TASK: Create a detailed, line-item cost breakdown for the project: "{project_goal}".

    INPUTS:
    - Target Budget Range: {budget_range}

    INSTRUCTIONS:
    1. Analyze the "{budget_range}".
       - If it is a number range (e.g., "$10k-$20k"), aim for the midpoint.
       - If it is text (e.g., "Low Budget"), assume a total of $5,000.
    2. Break the total cost into these standard categories:
       - UI/UX Design (approx. 15%)
       - Frontend Development (approx. 30%)
       - Backend Development (approx. 30%)
       - Project Management & QA (approx. 15%)
       - Infrastructure & Deployment (approx. 10%)
    3. Add a "Contingency Buffer" (5%) for unforeseen risks.
    4. write a note for the user.

    OUTPUT FORMAT (STRICT JSON ONLY):
    Return a valid JSON object with a single key: "cost_breakdown".
    The value must be a list of objects.

    Example:
    {{
        "cost_breakdown": [
            {{
                "category": "UI/UX Design",
                "cost": "$3,000",
                "notes": "High-fidelity mockups and prototyping."
            }},
            {{
                "category": "Backend API",
                "cost": "$6,000",
                "notes": "Database setup and API endpoint creation."
            }},
            ...
            {{
                "category": "Total Estimated Cost",
                "cost": "$...",
                "notes": "Sum of all phases."
            }}
        ]
    }}
    """
    return prompt

def generate_risk_matrix_prompt(params_dict):
    client_name, client_industry, project_goal, target_audience, timeline, budget_range, tech_pref, tone = get_input(params_dict)
    prompt = f"""
    ROLE: You are a Senior Risk Analyst and Compliance Officer.

    TASK: Identify the top 5 risks for a project in the "{client_industry}" industry and create a Risk Mitigation Matrix.

    INPUTS:
    - Industry: {client_industry}
    - Project Goal: {project_goal}

    INSTRUCTIONS:
    1. Identify 5 specific risks relevant to "{client_industry}".
       - Example for Fintech: "Data Breach", "Regulatory Change".
       - Example for Healthcare: "HIPAA Non-compliance", "Patient Data Loss".
       - Example for E-commerce: "Payment Gateway Failure", "Inventory Sync Error".
    2. Assign a "Probability" (Low/Medium/High) and "Impact" (Low/Medium/High) to each.
    3. Provide a concrete "Mitigation Strategy" (How to fix it).

    OUTPUT FORMAT (STRICT JSON ONLY):
    Return a valid JSON object with a single key: "risk_management".
    The value must be a list of objects.
    in the output don't add probability.

    Example:
    {{
        "risk_management": [
            {{
                "risk": "Data Breach",
                "impact": "High",
                "mitigation": "Implement 2FA and encrypt database at rest."
            }},
            {{
                "risk": "API Rate Limiting",
                "impact": "Medium",
                "mitigation": "Implement exponential backoff and caching."
            }}
        ]
    }}
    """
    return prompt

def generate_qa_plan_prompt(params_dict):
    client_name, client_industry, project_goal, target_audience, timeline, budget_range, tech_pref, tone = get_input(params_dict)
    prompt = f"""
    ROLE: You are a strict Quality Assurance Lead and Technical Architect.

    TASK: Define the non-negotiable Quality Assurance (QA) standards for the project: "{project_goal}".

    INPUTS:
    - Tech Stack: {tech_pref}

    INSTRUCTIONS:
    1. Generate a list of 4-6 specific technical commitments.
    2. Include metrics where possible (e.g., ">80% code coverage", "Load testing for 10k users").
    3. Tailor the list to the tech stack:
       - If {tech_pref} includes Python/JS, mention "Linting (PEP8/ESLint)".
       - If {tech_pref} involves APIs, mention "Automated Integration Testing".
       - If {tech_pref} involves Mobile, mention "Device Compatibility Testing".
    4. Ensure the tone is contractual and professional.

    OUTPUT FORMAT (STRICT JSON ONLY):
    Return a valid JSON object with a single key: "quality_assurance".
    The value must be a list of strings.

    Example:
    {{
        "quality_assurance": [
            "Automated Unit Testing (>80% code coverage) using PyTest/Jest",
            "End-to-End (E2E) Testing for critical user flows",
            "Performance Testing to support 5,000 concurrent users",
            "Security Scan (OWASP Top 10) prior to deployment"
        ]
    }}
    """
    return prompt

def generate_tech_stack_list_prompt(params_dict):
    client_name, client_industry, project_goal, target_audience, timeline, budget_range, tech_pref, tone = get_input(params_dict)
    prompt = f"""
    ROLE: You are a Chief Technology Officer (CTO) and Cloud Architect.

    TASK: Generate a definitive list of the specific tools and technologies required to build the project: "{project_goal}".

    INPUTS:
    - User Preferences: {tech_pref}

    INSTRUCTIONS:
    1. Start with the user's preferences ({tech_pref}).
    2. FILL IN THE GAPS to create a complete production stack.
       - If they didn't mention a database, choose the best one (e.g., PostgreSQL for data, MongoDB for flexibility).
       - If they didn't mention DevOps, add "Docker" and "CI/CD (GitHub Actions)".
       - If they didn't mention Caching, add "Redis".
    3. Return a clean list of 5-8 technologies. Do not explain them, just list the names.

    OUTPUT FORMAT (STRICT JSON ONLY):
    Return a valid JSON object with a single key: "tech_stack".
    The value must be a list of strings.

    Example:
    {{
        "tech_stack": [
            "React.js (Frontend)",
            "Node.js (Backend)",
            "PostgreSQL (Database)",
            "AWS Lambda (Serverless)",
            "Docker (Containerization)",
            "Redis (Caching)",
            "Terraform (IaC)"
        ]
    }}
    """
    return prompt

def generate_case_study_prompt(params_dict):
    client_name, client_industry, project_goal, target_audience, timeline, budget_range, tech_pref, tone = get_input(params_dict)
    prompt = f"""
    ROLE: You are a Senior Portfolio Manager and Case Study Writer.

    TASK: Create a compelling, industry-specific Case Study that demonstrates our past success in the "{client_industry}" sector.

    INPUTS:
    - Industry: {client_industry}
    - Client Goal: {project_goal}

    INSTRUCTIONS:
    1. Invent a realistic success story relevant to "{client_industry}".
       - If Industry is 'Healthcare': Title it something like "Modernizing Patient Records for [Hospital Name]".
       - If Industry is 'Fintech': Title it something like "Scaling [Bank Name] to 1M Users".
       - If Industry is 'Retail': Title it something like "Boosting E-commerce Conversion for [Brand]".
    2. Define the "Challenge" clearly (e.g., "Legacy systems were slow").
    3. Define the "Outcome" with metrics (e.g., "30% faster load times", "2x revenue").

    OUTPUT FORMAT (STRICT JSON ONLY):
    Return a valid JSON object with a single key: "case_study".
    The value must be an object with "title", "challenge", and "outcome" keys.

    Example:
    {{
        "case_study": {{
            "title": "Scaling NeoBank to 1M Users",
            "challenge": "Legacy on-premise servers were crashing during payday traffic spikes, causing 40% user churn.",
            "outcome": "We migrated them to AWS Serverless architecture, resulting in 99.99% uptime during peak loads and a 40% reduction in operational infrastructure costs."
        }}
    }}
    """
    return prompt

def generate_next_steps_prompt(params_dict):
    client_name, client_industry, project_goal, target_audience, timeline, budget_range, tech_pref, tone = get_input(params_dict)
    prompt = f"""
    ROLE: You are a Senior Sales Director and Deal Closer.

    TASK: Write the final "Call to Action" paragraph for a proposal regarding "{project_goal}".

    INPUTS:
    - Desired Tone: {tone}

    INSTRUCTIONS:
    1. Write a single, professional paragraph (2-3 sentences).
    2. Explicitly tell the client what to do next to start the project.
       - Mention "Signing the Statement of Work (SOW)".
       - Mention "Scheduling a Kickoff/Discovery Workshop".
    3. Adopt the "{tone}" tone:
       - If 'Aggressive', imply that our schedule is filling up.
       - If 'Formal', be polite and contractual.

    OUTPUT FORMAT (STRICT JSON ONLY):
    Return a valid JSON object with a single key: "next_steps".
    The value must be a single string.

    Example:
    {{
        "next_steps": "To initiate this partnership, we recommend a Technical Discovery Workshop. Please review the attached Statement of Work (SOW) and return a signed copy to lock in the proposed timeline."
    }}
    """
    return prompt