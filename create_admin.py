import sqlite3, os
from werkzeug.security import generate_password_hash

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "app.db")

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

username = "admin2"
password = "admin123"   # bisa diganti sesuai keinginan
role = "admin"

# bikin hash password
password_hash = generate_password_hash(password)

try:
    cur.execute("INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)",
                (username, password_hash, role))
    conn.commit()
    print(f"Akun admin '{username}' berhasil dibuat ✅")
except Exception as e:
    print("Error:", e)

conn.close()
