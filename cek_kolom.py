import sqlite3

conn = sqlite3.connect("app.db")
c = conn.cursor()
c.execute("PRAGMA table_info(pemeliharaan)")
for col in c.fetchall():
    print(col[1])

conn.close()
