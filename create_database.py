import sqlite3

conn = sqlite3.connect('user_data.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        email TEXT
    )
''')

test_data = [
    (1, "Alice Smith", 25, "alice.smith@example.com"),
    (2, "Bob Johnson", 30, "bob.johnson@example.com"),
    (3, "Charlie Brown", 28, "charlie.brown@example.com"),
    (4, "Diana Prince", 35, "diana.prince@example.com"),
    (5, "Ethan Hunt", 22, "ethan.hunt@example.com"),
    (6, "Fiona Green", 27, "fiona.green@example.com"),
    (7, "George Miller", 40, "george.miller@example.com"),
    (8, "Hannah Lee", 19, "hannah.lee@example.com"),
    (9, "Ian Clark", 33, "ian.clark@example.com"),
    (10, "Julia Adams", 26, "julia.adams@example.com")
]

cursor.executemany("INSERT OR IGNORE INTO users (id, name, age, email) VALUES (?, ?, ?, ?)", test_data)

conn.commit()
conn.close()