import sqlite3, os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "app.db")

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

try:
    cur.execute("""
    CREATE TABLE IF NOT EXISTS spo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        alat_nama TEXT NOT NULL,
        alat_merk TEXT,
        alat_tipe TEXT,
        file_path TEXT
    )
    """)
    print("✅ Tabel SPO berhasil dibuat")
except Exception as e:
    print("Error:", e)

conn.commit()
conn.close()
