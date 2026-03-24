import sqlite3

# Connect to database (creates file if it doesn't exist)
conn = sqlite3.connect("test.db")

# Create cursor
c = conn.cursor()

# Create table (if not exists prevents errors on rerun)
query = """ CREATE TABLE IF NOT EXISTS user (
    user_id INTEGER PRIMARY KEY NOT NULL,
    first_name TEXT NOT NULL,
    height INTEGER
)
"""
c.execute(query)

my_data = '''INSERT INTO user(user_id, first_name, height)
            VALUES (?,?,?)'''

# Insert data
c.execute(my_data, (3, 'Saamou', '171'))

# Save changes
conn.commit()
# Close connection
conn.close()