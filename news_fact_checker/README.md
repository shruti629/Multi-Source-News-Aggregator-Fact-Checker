## Multi-Source News Aggregator & Fact Checker (CrewAI)

An AI-powered multi-agent system that collects news from multiple sources, analyzes social sentiment, and fact-checks information using CrewAI agents.

It helps detect misinformation by cross-verifying claims across news APIs + social trend data + AI reasoning models.

# 🚀 Features

🔍 Multi-source news collection (NewsAPI)
📊 Social sentiment analysis (Exa AI / web signals)
🧠 AI-powered fact-checking agent
📝 Automated news report generation
🤖 Multi-agent orchestration using CrewAI
⚡ Sequential + parallel AI workflows
📡 Real-time topic-based analysis
🏗️ Project Architecture

# 📌 High-Level Flow

User Input (Topic)
        ↓
News Agent ───────┐
                  ├── Collection Crew
Social Agent ─────┘
        ↓
Collected Data
        ↓
Fact Checker Agent
        ↓
Reporter Agent
        ↓
Final Verified News Report

# 🧠 AI Agents

1. News Aggregator Agent
Fetches latest news articles
Uses NewsAPI
Filters top relevant sources

2. Social Analyst Agent
Collects public sentiment signals
Uses Exa AI search API
Extracts trending discussions

3. Fact Checker Agent
Cross-verifies claims from multiple sources
Detects inconsistencies
Assigns confidence scores

4. Reporter Agent
Generates structured news brief
Produces final summarized report
Adds confidence-based insights


# 🛠️ Tech Stack
Python 🐍
CrewAI 🤖
NewsAPI 📰
Exa AI 🔎
Pydantic (data validation)
dotenv (environment variables)


# 📁 Project Structure


news_fact_checker/
│── main.py
│── .env
│
├── src/
│   ├── agents.py
│   ├── tasks.py
│   ├── crew_setup.py
│   ├── tools.py
│
└── README.md

# ⚙️ Installation

1. Clone repo
git clone https://github.com/yourusername/news_fact_checker.git
cd news_fact_checker

2. Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

3. Install dependencies
pip install crewai newsapi-python exa-py python-dotenv pydantic

4. Setup .env file

Create .env in root directory:

GOOGLE_API_KEY=your_google_gemini_key
NEWS_API_KEY=your_newsapi_key
EXA_API_KEY=your_exa_api_key

▶️ Run Project
python main.py


