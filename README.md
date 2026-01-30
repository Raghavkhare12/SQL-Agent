
---

# 🧠 Database & SQL Assistant Agent

---

## 📌 Overview

The **Database & SQL Assistant Agent** is a CLI-based intelligent system that converts natural language instructions into valid SQL queries, executes them safely on relational databases, explains database schemas and SQL queries, and assists with basic database design.

The project focuses **exclusively** on the *Database & SQL Agent* component of a larger **multi-agent AI architecture**. It is implemented using **LangChain** with an **API-based LLM backend** and is designed for **correctness, safety, and extensibility** rather than UI complexity.

---

## 🚀 Key Capabilities

* Natural language → SQL query generation
* Schema-aware query generation
* Full CRUD operations on SQLite databases
* Database switching at runtime
* SQL query explanation for beginners
* Database schema explanation
* Conceptual database design suggestions for real-world systems
* Safety confirmation for destructive queries
* CLI-based interaction for simplicity and clarity

---

## 🔐 Safety Design

The agent includes a **query safety layer** that detects potentially destructive SQL commands such as:

* `UPDATE`
* `DELETE`
* `DROP`
* `TRUNCATE`
* `ALTER`

Any such query **requires explicit user confirmation** before execution, preventing accidental data loss and unsafe operations.

---

## 🧱 Technology Stack

* **Language:** Python
* **Database:** SQLite
* **Database Connector:** SQLAlchemy
* **LLM Backend:** Groq API (LLaMA 3.1 – 8B Instant)
* **AI Framework:** LangChain
* **Interface:** Terminal / CLI

---

## 📂 Project Structure

```
Database-SQL-Assistant-Agent/
│
├── main.py          # CLI interface and command routing

├── db_agent.py      # SQL generation, explanation, and design logic

├── sql_tools.py     # Database execution, schema inspection, LLM setup

├── safety.py        # Safety checks for destructive SQL commands

├── prompt.py        # Prompt templates and system instructions

├── db.py            # Database connection utilities
├── create_db.py     # Script to generate a sample SQLite database

├── README.md        # Project documentation
├── .gitignore       # Git ignore rules
```

> ℹ️ SQLite `.db` files are generated locally and are intentionally excluded from version control.

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install sqlalchemy langchain langchain-groq python-dotenv sqlparse
```

### 4️⃣ Configure Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Make sure `.env` is listed in `.gitignore`.

---

## ▶️ Running the Agent

```bash
python main.py
```

---

## 🧪 Supported CLI Commands

### 🔹 Database Management

```text
use database company
```

### 🔹 Create Table

```text
create table employees (id integer primary key, name text, salary integer)
```

### 🔹 Insert Data

```text
add employee id=1 name=Amit salary=50000
add employee id=2 name=Neha salary=60000
```

### 🔹 Read Data

```text
show all employees
employees with salary > 55000
```

### 🔹 Update Data (Confirmation Required)

```text
update salary of Amit to 55000
CONFIRM
```

### 🔹 Delete Data (Confirmation Required)

```text
delete employee where id = 1
CONFIRM
```

### 🔹 Explain Schema

```text
explain schema
```

### 🔹 Explain SQL Query

```text
explain: SELECT * FROM employees WHERE salary > 50000
```

### 🔹 Database Design Assistance

```text
design database for online exam system
design database for online shopping system
```

---

## 🧠 Design Philosophy

* LLM used strictly for **reasoning and SQL generation**
* Actual SQL execution handled programmatically
* Safety-first approach for destructive operations
* Model-agnostic architecture (easy to swap LLM providers)
* Human-paced CLI interaction to avoid rate-limit issues

---

## 🔮 Future Enhancements

* Integration with LangChain `SQLDatabaseToolkit`
* LangGraph-based multi-agent orchestration
* Support for PostgreSQL and MySQL
* Query optimization and performance suggestions
* Web-based interface using FastAPI

---

## 👨‍💻 Author

**Raghav Khare**
VIT Bhopal University

**Project Component:**
Multi-Agent AI System — *Database & SQL Assistant Agent*

---

