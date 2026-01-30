from db_agent import generate_sql, explain_sql, design_database
from sql_tools import run_sql, get_schema_details
from safety import is_dangerous
from sql_tools import current_db

print("=== Database & SQL Assistant Agent ===")
print("Commands:")
print("- explain schema")
print("- explain: <SQL>")
print("- design database for <use case>")
print("- or normal database questions")
print("Type 'exit' to quit\n")

pending_sql = None

while True:
    user_input = input(">> ").strip()

    if user_input.lower() == "exit":
        break
    
    #SWITCH DATABASE
    if user_input.lower().startswith("use database"):
        db_name = user_input.split()[-1]
        if not db_name.endswith(".db"):
            db_name += ".db"
        current_db["path"] = db_name
        print(f"Switched to database: {db_name}")
        continue

    #CONFIRM MODE
    if pending_sql:
        if user_input.upper() == "CONFIRM":
            result = run_sql(pending_sql)
            print(result)
        else:
            print("Operation cancelled.")
        pending_sql = None
        continue

    #EXPLAIN SCHEMA
    if user_input.lower() == "explain schema":
        schema = get_schema_details()
        for table, cols in schema.items():
            print(f"\nTable: {table}")
            for c in cols:
                print(f"  {c[0]} ({c[1]})")
        continue

    #EXPLAIN QUERY
    if user_input.lower().startswith("explain:"):
        query = user_input.replace("explain:", "").strip()
        explanation = explain_sql(query)
        print(explanation)
        continue

    #DB DESIGN MODE
    if "design database" in user_input.lower():
        design = design_database(user_input)
        print(design)
        continue

    #NORMAL SQL MODE
    sql = generate_sql(user_input)
    print("Generated SQL:", sql)

    if is_dangerous(sql):
        print("WARNING: Destructive query detected.")
        print("Type CONFIRM to execute.")
        pending_sql = sql
    else:
        result = run_sql(sql)
        print(result)
