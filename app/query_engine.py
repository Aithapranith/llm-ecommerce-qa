import sqlite3

def run_sql_query(sql_query: str):
    conn = sqlite3.connect("ecommerce.db")
    cursor = conn.cursor()

    try:
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        conn.close()
        return [dict(zip(columns, row)) for row in rows]
    except Exception as e:
        conn.close()
        return [{"error": str(e)}]
