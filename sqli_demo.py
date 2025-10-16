# sqli_demo.py
import sqlite3

def vulnerable_login(username, password):
    # WARNING: intentionally insecure string formatting (SQL injection)
    query = "SELECT * FROM users WHERE username = '%s' AND password = '%s';" % (username, password)
    print("Running query:", query)
    conn = sqlite3.connect(':memory:')
    cur = conn.cursor()
    cur.execute("CREATE TABLE users (username TEXT, password TEXT)")
    cur.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin123')")
    # Vulnerable execution using concatenated/formatted SQL
    cur.execute(query)
    rows = cur.fetchall()
    print("Rows:", rows)
    conn.close()

if __name__ == "__main__":
    # Example input that would exploit naive code if DB had real users:
    vulnerable_login(input("username: "), input("password: "))
