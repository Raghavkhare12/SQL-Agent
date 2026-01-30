from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///college.db")

with engine.connect() as conn:
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            marks INTEGER
        );
    """))

    conn.execute(text("""
        INSERT INTO students (name, marks) VALUES
        ('Raghav', 92),
        ('Anita', 85),
        ('Rahul', 70),
        ('Meena', 60);
    """))

    conn.commit()

print("Database created successfully.")
