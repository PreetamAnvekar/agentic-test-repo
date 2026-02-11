# app.py

import sqlite3

def get_user(user_input):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE id = ?"
    cursor.execute(query, (user_input,))

    result = cursor.fetchall()
    conn.close()
    return result
