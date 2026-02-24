import sqlite3

def init_db():
    conn = sqlite3.connect("todolist.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            deadline TEXT,
            done INTEGER
        )
    """)
    conn.commit()
    conn.close()

def save_task(title, deadline, done=0):
    conn = sqlite3.connect("todolist.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title, deadline, done) VALUES (?, ?, ?)", (title, deadline, done))
    conn.commit()
    conn.close()
