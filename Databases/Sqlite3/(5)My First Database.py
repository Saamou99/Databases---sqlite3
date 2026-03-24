import sqlite3

try:
    conn = sqlite3.connect("students3.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        grade INTEGER
    )
    """)

    # Insert students
    c.execute("INSERT INTO students VALUES (?, ?, ?)", (1, "SAIM", 12))
    c.execute("INSERT INTO students VALUES (?, ?, ?)", (2, "Saamou", 10))
    c.execute("INSERT INTO students VALUES (?, ?, ?)", (3, "Saaza", 7))

    conn.commit()

# BONUS: duplicate insert
    c.execute("INSERT INTO students VALUES (?, ?, ?)", (1, "Duplicate", 12))


except sqlite3.IntegrityError as e:
    print("Duplicate student ID error:", e)

except sqlite3.Error as e:
    print("Database error:", e)

finally:
    if 'conn' in locals():
        conn.close()
        print("Connection closed.")