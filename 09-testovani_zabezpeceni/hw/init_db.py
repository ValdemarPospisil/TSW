import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()

# users tabulka
c.execute('DROP TABLE IF EXISTS users')
c.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
c.execute('INSERT INTO users (username, password) VALUES ("admin", "admin123")')
c.execute('INSERT INTO users (username, password) VALUES ("user", "user123")')

# comments tabulka
c.execute('DROP TABLE IF EXISTS comments')
c.execute('CREATE TABLE comments (id INTEGER PRIMARY KEY, text TEXT)')
c.execute('INSERT INTO comments (text) VALUES ("Hello!")')

conn.commit()
conn.close()
