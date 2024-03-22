import sqlite3

# Create a connection to the database
conn = sqlite3.connect('competition.db')
cursor = conn.cursor()

# Create the participants table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS participants (
        id INTEGER PRIMARY KEY,
        name TEXT,
        chickenwings INTEGER,
        hamburgers INTEGER,
        hotdogs INTEGER
    )
''')

# Insert sample data into the participants table
participants_data = [
    ("Habanero Hillary", 5, 17, 11),
    ("Big Bob", 20, 4, 11)
]

cursor.executemany('''
    INSERT INTO participants (name, chickenwings, hamburgers, hotdogs)
    VALUES (?, ?, ?, ?)
''', participants_data)

# Commit changes and close the connection
conn.commit()
conn.close()
