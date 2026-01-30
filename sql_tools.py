from sqlalchemy import create_engine, text
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()


current_db = {"path": "college.db"}

def get_engine():
    return create_engine(f"sqlite:///{current_db['path']}")


llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)

def get_schema():
    engine = get_engine()
    with engine.connect() as conn:
        result = conn.execute(text(
            "SELECT name FROM sqlite_master WHERE type='table';"
        ))
        return [row[0] for row in result]

def run_sql(query):
    engine = get_engine()
    with engine.begin() as conn:
        result = conn.execute(text(query))
        try:
            return result.fetchall()
        except:
            return "Query executed successfully."

def get_schema_details():
    engine = get_engine()
    schema = {}

    with engine.connect() as conn:
        tables = conn.execute(text(
            "SELECT name FROM sqlite_master WHERE type='table';"
        )).fetchall()

        for (table,) in tables:
            cols = conn.execute(text(f"PRAGMA table_info({table});")).fetchall()
            schema[table] = [(c[1], c[2]) for c in cols]

    return schema
