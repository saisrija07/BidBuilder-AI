
# BidBuilder AI 🚀

**The High-Performance Automated RFP Response Architect.**

**BidBuilder AI** is an enterprise-grade application that generates comprehensive, professional business proposals in seconds. Unlike standard chatbots that generate text sequentially, BidBuilder utilizes a **Parallel Agent Architecture** to orchestrate 12 specialized AI agents simultaneously, reducing document generation time by over 70%.

---

## ⚡ Key Features

* **Parallel Orchestration:** Uses Python's `asyncio` to fire 12 independent AI prompts at once, cutting generation time from ~60s to ~15s.
* **Structured Output:** Generates a complete 12-section document including Executive Summaries, Gantt Charts, Cost Breakdowns, and Risk Matrices.
* **Strict JSON Enforcement:** AI agents are prompted to return strict JSON to ensure consistent rendering in the UI.
* **Print-Ready UI:** Custom CSS optimized for web viewing and one-click PDF export via the browser's print engine.
* **Context-Aware:** Adapts content based on Client Industry, Budget, Tech Preferences, and desired Tone.

---

## 🏗 System Architecture

The core of this project is **Parallel Execution**. We do not chain prompts (A -> B -> C). We fire them all at once (A + B + C).

![System Architecture Diagram](static/images/architecture_diagram.png)
*(Note: Add a screenshot or diagram image to your `static/images` folder)*

### The Workflow:
1.  **User Input:** The user fills out the "Hub" (Client Name, Industry, Budget, etc.).
2.  **Async Dispatch:** The Flask backend initializes the `asyncio` event loop.
3.  **The Swarm:** 12 specialized AI Agents are triggered simultaneously:
    * *Agent 1:* Writes the Executive Summary
    * *Agent 2:* Calculates the Cost Breakdown
    * *Agent 3:* Builds the Tech Stack
    * *...and 9 others.*
4.  **Aggregation:** The backend waits for all agents to return their specific JSON fragments.
5.  **Rendering:** The data is merged and injected into a Jinja2 template to create the final HTML report.

---

## 🛠 Tech Stack

* **Backend:** Python 3.10+, Flask
* **Concurrency:** `asyncio`, `aiohttp` (via Groq client)
* **AI Inference:** Groq API (Llama-3 / Mixtral models)
* **Frontend:** HTML5, CSS3, Jinja2 Templating
* **Styling:** Custom CSS with Print Media Queries

---

## 📂 Project Structure

```text
BidBuilder/
├── app.py                     # Application entry point
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables (API Keys)
├── application/
│   ├── __init__.py            # Flask App Factory
│   └── controllers.py         # Route logic and Async runners
├── ai_workflow/
│   ├── prompts.py             # Prompt engineering for 12 specific agents
│   └── utils.py               # Async engine & API handling
├── templates/
│   ├── index.html             # Input Form
│   └── proposal.html          # Final Report Template
└── output/                    # JSON logs of generated proposals

```

---

## 🚀 Getting Started

### Prerequisites

* Python 3.8 or higher
* A Groq API Key (Get one at [console.groq.com](https://console.groq.com))

### Installation

1. **Clone the repository**
```bash
git clone [https://github.com/yourusername/bidbuilder-ai.git](https://github.com/yourusername/bidbuilder-ai.git)
cd bidbuilder-ai

```


2. **Create a Virtual Environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate

```


3. **Install Dependencies**
```bash
pip install -r requirements.txt

```


4. **Configure Environment**
Create a `.env` file in the root directory and add your API Key:
```bash
GROK_API_KEY=gsk_your_actual_api_key_here

```


5. **Run the Application**
```bash
python app.py

```


6. **Access the App**
Open your browser and navigate to `http://localhost:8000`

---

## 📖 Usage Guide

1. **Fill the Hub:** Enter the client details, project goals, timeline, and budget in the input form.
2. **Select Tone:** Choose between *Formal*, *Innovative*, or *Technical* to guide the AI's writing style.
3. **Generate:** Click "Generate Proposal." The spinner indicates the backend is processing 12 streams of data.
4. **Review:** The result is a formatted HTML report.
5. **Export:** Click the "Print" button at the bottom of the page. In the print dialog, select **"Save as PDF"** to create a shareable file.

---

## 🔧 Configuration & Tuning

### Adjusting the Model

To change the AI model (e.g., to Llama-3-70b), edit `ai_workflow/utils.py`:

```python
MODEL = "llama3-70b-8192" # or "mixtral-8x7b-32768"

```

### Concurrency & Retries

If you hit rate limits with a free tier key, you can adjust the retry logic or implement a semaphore in `ai_workflow/utils.py`:

```python
MAX_RETRIES = 5

```

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

```

---

### LinkedIn Post (Bonus)

**Headline:** I built an AI that writes 12-page project proposals in 15 seconds. 🚀

We’ve all been there: The deadline is approaching, and you’re staring at a blank RFP response. It’s tedious, repetitive, and kills productivity.

So this weekend, I built **BidBuilder AI**.

It’s not just a wrapper around ChatGPT. It’s an enterprise-grade orchestration engine.

**How it works:**
1.  **The Hub:** You input the client details, industry, tech stack, and budget.
2.  **The Spokes:** The backend triggers **12 specialized AI agents** simultaneously.
3.  **The Magic:** Instead of writing one section at a time, Agent A writes the Tech Stack while Agent B calculates the Cost Breakdown and Agent C builds the Gantt Chart.

**The Tech Stack:**
* **Backend:** Flask + Python AsyncIO
* **AI:** Groq (Llama-3) for insane inference speed
* **Architecture:** Parallel execution (cut generation time by 75%)

The result? A fully formatted, print-ready proposal with strategy, timelines, and risk matrices—generated faster than you can open a new Google Doc.

Check out the code on GitHub! [Link to your repo]

#AI #Python #Flask #Automation #Productivity #Groq #SoftwareEngineering

```
