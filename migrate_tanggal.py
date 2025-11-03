import sqlite3

conn = sqlite3.connect("app.db")
cur = conn.cursor()

for col in ["tgl_periode1", "tgl_periode2", "tgl_periode3"]:
    try:
        cur.execute(f"ALTER TABLE pemeliharaan ADD COLUMN {col} TEXT;")
        print(f"✅ Kolom {col} berhasil ditambahkan")
    except sqlite3.OperationalError:
        print(f"ℹ️ Kolom {col} sudah ada, dilewati")

conn.commit()
conn.close()
print("✅ Migrasi tanggal periode selesai.")
