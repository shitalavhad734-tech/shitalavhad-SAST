# vulnerable.py
import sqlite3

def get_user_data(username):
    # ⚠️ Unsafe query — vulnerable to SQL Injection
    query = "SELECT * FROM users WHERE name = '" + username + "';"
    print("Running query:", query)
    conn = sqlite3.connect(':memory:')
    cur = conn.cursor()
    cur.execute("CREATE TABLE users (name TEXT)")
    cur.execute(query)  # This line is vulnerable
    conn.close()

get_user_data(input("Enter username: "))
