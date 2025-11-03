import sqlite3

conn = sqlite3.connect("app.db")
cur = conn.cursor()

for col in ["file_periode1", "file_periode2", "file_periode3"]:
    try:
        cur.execute(f"ALTER TABLE pemeliharaan ADD COLUMN {col} TEXT;")
        print(f"✅ Kolom {col} berhasil ditambahkan")
    except sqlite3.OperationalError:
        print(f"ℹ️ Kolom {col} sudah ada, dilewati")

conn.commit()
conn.close()
print("✅ Migrasi selesai.")
