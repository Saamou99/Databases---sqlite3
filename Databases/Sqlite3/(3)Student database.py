import sqlite3

# Try to run all database operations
try:
    # Connect to database
    conn = sqlite3.connect("students.db")
    c = conn.cursor()

    # Create table
    c.execute("""
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        grade INTEGER
    )
    """)

    # Insert students using prepared statements
    c.execute("INSERT INTO students VALUES (?, ?, ?)", (1, "SAIM", 12))
    c.execute("INSERT INTO students VALUES (?, ?, ?)", (2, "Saamou", 10))
    c.execute("INSERT INTO students VALUES (?, ?, ?)", (3, "Saaza", 7))

    # Save changes
    conn.commit()

# Specific error for duplicates
except sqlite3.IntegrityError as e:
    print("Duplicate student ID error:", e)

# Other database errors
except sqlite3.Error as e:
    print("Database error:", e)

# Always close connection
finally:
    if 'conn' in locals():
        conn.close()
        print("Connection closed.")
