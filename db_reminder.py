import sqlite3

conn = sqlite3.connect('bot.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name TEXT NOT NULL,
    chat_id INTEGER NOT NULL)''')

conn.commit()
conn.close()