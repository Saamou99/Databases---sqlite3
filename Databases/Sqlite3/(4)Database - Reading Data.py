import sqlite3

# Connect to database
conn = sqlite3.connect("students2.db")
c = conn.cursor()

  # Create table
c.execute(
    """ CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        grade INTEGER
    )""")

# Insert students using prepared statements
c.execute("INSERT INTO students VALUES (?, ?, ?)", (1, "SAIM", 7))
c.execute("INSERT INTO students VALUES (?, ?, ?)", (2, "Saamou", 11))
c.execute("INSERT INTO students VALUES (?, ?, ?)", (3, "Saaza", 10))

# Save changes
conn.commit()
conn.close()

data = c.execute('SELECT * FROM user WHERE user_id=3').fetchall()
print(data)
