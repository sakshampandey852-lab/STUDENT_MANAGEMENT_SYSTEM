import sqlite3

def create_database():
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        roll_no TEXT UNIQUE NOT NULL,
        course TEXT,
        marks INTEGER,
        attendance REAL
    )
    """)

    conn.commit()
    conn.close()

create_database()

print("Database created successfully!")   

