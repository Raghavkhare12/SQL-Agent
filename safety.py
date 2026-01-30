import sqlparse

WRITE_COMMANDS = ["DELETE", "UPDATE", "DROP", "TRUNCATE", "ALTER"]

def is_dangerous(sql: str):
    parsed = sqlparse.parse(sql)
    if not parsed:
        return False

    stmt = parsed[0]
    tokens = [t.value.upper() for t in stmt.tokens]

    for cmd in WRITE_COMMANDS:
        if cmd in tokens:
            return True

    return False
