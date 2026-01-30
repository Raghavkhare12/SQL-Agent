from sql_tools import llm, run_sql, get_schema
import re

SQL_PROMPT = """
You are a SQL assistant.

Database tables:
{schema}

Convert the user request into ONLY a valid SQLite SQL query.
Do not explain. Do not use markdown. Do not use ```.

User: {question}
SQL:
"""

def clean_sql(sql: str):
    sql = sql.strip()
    sql = re.sub(r"```.*?\n", "", sql)
    sql = sql.replace("```", "")
    return sql.strip()


def generate_sql(question):
    schema = ", ".join(get_schema())
    prompt = SQL_PROMPT.format(schema=schema, question=question)
    response = llm.invoke(prompt)
    sql = response.content.strip()
    return clean_sql(sql)

EXPLAIN_PROMPT = """
Explain this SQL query in simple words for a beginner:

{query}
"""

DESIGN_PROMPT = """
Suggest a basic database design for this requirement.
Give tables and important columns.

Requirement:
{question}
"""

def explain_sql(query):
    prompt = EXPLAIN_PROMPT.format(query=query)
    response = llm.invoke(prompt)
    return response.content.strip()

def design_database(question):
    prompt = DESIGN_PROMPT.format(question=question)
    response = llm.invoke(prompt)
    return response.content.strip()