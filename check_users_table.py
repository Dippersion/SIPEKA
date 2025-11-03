import sqlite3, os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "app.db")

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# cek struktur tabel users
cur.execute("PRAGMA table_info(users)")
columns = cur.fetchall()

for col in columns:
    print(col)

conn.close()
