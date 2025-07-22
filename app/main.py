from fastapi import FastAPI
from pydantic import BaseModel
from app.query_engine import run_sql_query
from app.llm_utils import gemini_generate_sql

app = FastAPI()

class Question(BaseModel):
    text: str

@app.post("/ask")
def ask_question(q: Question):
    try:
        print("📥 User Question:", q.text)
        sql_query = gemini_generate_sql(q.text)
        print("🧾 Generated SQL:", sql_query)

        result = run_sql_query(sql_query)
        print("✅ Result:", result)

        return {
            "question": q.text,
            "generated_sql": sql_query,
            "result": result
        }

    except Exception as e:
        print("❌ ERROR:", str(e))
        return {"error": str(e)}
