# BidBuilder AI: The Intelligent RFP Response Architect

**BidBuilder AI** is an enterprise-grade automated proposal generator. It replaces the tedious, manual process of writing Requests for Proposal (RFP) responses with a high-speed, parallel AI orchestration engine.

Instead of a generic chatbot, BidBuilder uses a **Hub-and-Spoke Architecture**. A single set of project inputs (The Hub) triggers 12 specialized, independent AI agents (The Spokes) simultaneously. These agents generate specific sections of a professional proposal—from technical architecture to cost breakdowns—which are then aggregated into a polished, printable document.

---

## 🏗️ System Architecture

The core of this project is **Parallel Execution**. We do not chain prompts (A -> B -> C). We fire them all at once (A + B + C) to reduce generation time from minutes to seconds.

```mermaid
graph TD
    User[User Input Form] -->|8 Key Variables| Backend(Flask/FastAPI Async Engine)
    
    subgraph "Parallel AI Agents (The Spokes)"
        Backend -->|Async Call| Agent1[generate_exec_summary]
        Backend -->|Async Call| Agent2[generate_tech_stack]
        Backend -->|Async Call| Agent3[generate_cost_breakdown]
        Backend -->|Async Call| Agent4[generate_risk_matrix]
        Backend -->| and 8 more | AgentN[]
    end
    
    Agent1 -->|HTML Fragment| Aggregator(Data Merger)
    Agent2 -->|HTML Fragment| Aggregator
    Agent3 -->|HTML Fragment| Aggregator
    AgentN -->|HTML Fragment| Aggregator
    
    Aggregator -->|Combined Context| Jinja(Jinja2 Template Engine)
    Jinja -->|Final Document| Browser(User Dashboard/PDF)

```

---

## 📂 Project Structure

```bash
BidBuilder/
├── app.py                 # Main Flask application & Async logic
├── prompts.py             # Contains all 12 generate_* functions
├── requirements.txt       # Dependencies (flask, openai, aiohttp, etc.)
├── .env                   # API Keys (OPENAI_API_KEY)
├── static/
│   ├── css/
│   │   └── style.css      # Styles for the document layout
│   └── js/
├── templates/
│   ├── index.html         # The Input Form (The Hub)
│   └── proposal.html      # The Final Document (The Report)
└── README.md

```

---

## ✅ Development Checklist

### Phase 1: The Foundation

* [ ] **Repo Setup:** Create GitHub repo, add `.gitignore` (python), and invite team.
* [ ] **Environment:** Create `venv`, install `flask` and `openai`/`google-generativeai`.
* [ ] **Hello World:** Create a simple route in `app.py` that renders `index.html`.

### Phase 2: The Inputs (Frontend Lead)

* [ ] **Build `index.html`:** Create a clean form with the **8 Master Inputs** (see below).
* [ ] **Validation:** Ensure all fields are required.
* [ ] **Loading State:** Add a "Generating Proposal" spinner (since it takes ~10s).

### Phase 3: The Brains (Prompt Architect)

* [ ] **Setup `prompts.py`:** Initialize the LLM client (OpenAI or Gemini).
* [ ] **Write `generate_exec_summary`:** Test that it returns valid HTML (``, `<h2>`).
* [ ] **Write `generate_tech_stack`:** Test that it returns a list (`<ul>`, `<li>`).
* [ ] **Complete all 12 functions:** Ensure they all accept the correct arguments.

### Phase 4: The Engine (Backend Lead)

* [ ] **Async Setup:** Convert `app.py` routes to `async def`.
* [ ] **Concurrency:** Use `asyncio.gather()` to call all 12 functions at once.
* [ ] **Error Handling:** If one agent fails, return a default "Data Unavailable" string instead of crashing.
* [ ] **Data Merging:** Pass the results dictionary to `render_template`.

### Phase 5: The Polish (Team)

* [ ] **Styling:** Make `proposal.html` look like a real document (A4 paper width, professional fonts).
* [ ] **Print Button:** Add a button that triggers `window.print()` for PDF export.

---

## 🔑 The 8 Master Inputs (The Hub)

These are the variables collected in `index.html` and passed to the backend.

| Variable Name | Type | Options / Description |
| --- | --- | --- |
| `client_name` | Text | e.g., "Apex Healthcare", "City of Austin" |
| `client_industry` | Dropdown | Fintech, Healthcare, E-commerce, Government, Education |
| `project_goal` | Text Area | "Migrate legacy portal to cloud", "Build iOS app" |
| `target_audience` | Dropdown | Internal Staff, B2B Customers, General Public |
| `timeline` | Dropdown | 3 Months, 6 Months, 1 Year, ASAP |
| `budget_range` | Dropdown | <$50k, $100k-$500k, $1M+, TBD |
| `tech_pref` | Dropdown | Open Source (Python/Node), Enterprise (Java/.NET), Cloud Native |
| `tone` | Dropdown | Formal & Corporate, Innovative & Bold, Technical |

---

## 🧠 The 12 Functions (The Spokes)

All functions live in `prompts.py`. Each must be `async` and return an **HTML String**.

### 1. The Hook

* **Function:** `async def generate_exec_summary(client_name, goal, industry, tone)`
* **Output:** `Executive Summary`
* **Word count:** `200 words`

### 2. The Credibility

* **Function:** `async def generate_why_us(industry, tone)`
* **Output:** `Why Choose Us?`
* **Word count:** `200 words`

### 3. The Tech Strategy

* **Function:** `async def generate_solution_arch(tech_pref, goal)`
* **Output:** `Proposed Solution`
* **Word count:** `200 words`

### 4. The Deliverables

* **Function:** `async def generate_scope_of_work(goal)`
* **Output:** `Scope of Work<ul><li>...</li></ul>`
* **Word count:** `200 words`

### 5. The Gantt Chart

* **Function:** `async def generate_timeline_table(timeline)`
* **Output:** `Project Timeline<table>...</table>`

### 6. The Staffing

* **Function:** `async def generate_team_structure(budget_range)`
* **Output:** `Team Composition<ul><li>...</li></ul>`

### 7. The Pricing

* **Function:** `async def generate_cost_breakdown(budget_range)`
* **Output:** `Estimated Investment<table>...</table>`

### 8. The Safety

* **Function:** `async def generate_risk_matrix(industry)`
* **Output:** `Risk Management<ul><li>...</li></ul>`

### 9. The Testing

* **Function:** `async def generate_qa_plan(target_audience)`
* **Output:** `Quality Assurance`

### 10. The Tools

* **Function:** `async def generate_tech_stack_list(tech_pref)`
* **Output:** `Technology Stack<div class="tags">`

### 11. The Proof

* **Function:** `async def generate_case_study(industry)`
* **Output:** `Relevant Case Study`

### 12. The Closing

* **Function:** `async def generate_next_steps(tone)`
* **Output:** `Next Steps`
* **Word count:** `200 words`