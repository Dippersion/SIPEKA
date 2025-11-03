import sqlite3, os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "app.db")

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# 🔍 Cek apakah kolom updated_at sudah ada
cur.execute("PRAGMA table_info(reports)")
columns = [col[1] for col in cur.fetchall()]

if "updated_at" not in columns:
    try:
        cur.execute("ALTER TABLE reports ADD COLUMN updated_at TEXT;")
        print("Kolom 'updated_at' berhasil ditambahkan ✅")
    except Exception as e:
        print("Error saat tambah kolom:", e)
else:
    print("Kolom 'updated_at' sudah ada, skip ✅")

# ✅ Tambah index untuk optimasi query
try:
    cur.execute("CREATE INDEX IF NOT EXISTS idx_reports_user_id ON reports(user_id)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_reports_created_at ON reports(created_at)")
    print("Index berhasil dibuat ✅")
except Exception as e:
    print("Error saat buat index:", e)

conn.commit()
conn.close()
