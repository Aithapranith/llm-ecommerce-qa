import os
from dotenv import load_dotenv
from openai import OpenAI

# Load .env file
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("❌ GROQ_API_KEY not found in .env")

# Initialize the OpenAI-compatible client for Groq
client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

SCHEMA = """
Tables and columns:
1. ad_sales_metrics(date, item_id, ad_sales, impressions, ad_spend, clicks, units_sold)
2. eligibility_table(eligibility_datetime_utc, item_id, eligibility, message)
3. total_sales_metrics(date, item_id, total_sales, total_units_ordered)
"""

def gemini_generate_sql(question: str) -> str:
    prompt = f"""
You are an expert SQL generator. Given this schema:

{SCHEMA}

Write a SQL query for the user's question:
"{question}"

Return ONLY the SQL query.
"""

    response = client.chat.completions.create(
    model="llama3-70b-8192",
    messages=[
        {"role": "user", "content": prompt}
    ],
    temperature=0.2
)

    sql = response.choices[0].message.content
    return sql.strip().strip("```sql").strip("```")
