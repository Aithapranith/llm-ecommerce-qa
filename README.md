# 🛒 LLM E-commerce QA

An AI-powered question-answering system for e-commerce datasets using LLMs like Groq/OpenAI/Gemini. Users can ask natural language questions (e.g., "What is the total ad spend for each item?") and get intelligent SQL-based answers backed by real data.
(https://drive.google.com/file/d/1P0oMbYyN5S2H3bs2pQgwBZk6f_wvMgQZ/view?usp=drive_link)
![1](https://github.com/user-attachments/assets/120ea16b-029e-4ec8-ad5a-d08dacd70b18)

![2](https://github.com/user-attachments/assets/7d88ab3d-fc50-45e1-aa5b-dab8053fa620)


## 📌 Features

- ✅ Ask natural language questions about your e-commerce sales and ad data
- ✅ Auto-generates SQL using Large Language Models (LLMs)
- ✅ Executes SQL against a local SQLite database
- ✅ Returns direct answers and SQL query used
- ✅ Fully local — no need to expose your database online
- ✅ Supports Groq (Mixtral), OpenAI, or Gemini as the LLM backend
- 🔄 Easily switch models with `.env` configuration
- ⚡ FastAPI backend with interactive API docs via Swagger UI

## 🚀 Tech Stack

- **FastAPI** – Web framework
- **SQLite** – Local database
- **Pandas** – CSV parsing
- **Groq/OpenAI/Gemini** – LLMs for SQL generation
- **Dotenv** – For secure environment variable management

## 📁 Project Structure

genai_ecommerce_qa/
├── app/
│ ├── main.py # FastAPI app
│ ├── llm_utils.py # LLM prompt and API logic
│ ├── query_engine.py # SQL query execution logic
│ └── init.py
├── data/ # Raw CSV files
│ ├── ad_sales.csv
│ ├── eligibility.csv
│ └── total_sales.csv
├── db/
│ └── setup_db.py # Script to build ecommerce.db from CSVs
├── ecommerce.db # Auto-generated SQLite database
├── .env # API key for LLM (NOT COMMITTED)
├── .gitignore
├── requirements.txt
└── README.md


