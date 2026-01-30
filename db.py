from sqlalchemy import create_engine
from langchain_community.utilities import SQLDatabase

DB_URI = "sqlite:///college.db"

engine = create_engine(DB_URI)
db = SQLDatabase(engine)

def get_db():
    return db
