import sqlite3

# buka database yang dipakai Flask kamu
conn = sqlite3.connect('database.db')
cur = conn.cursor()

# cek semua tabel
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Daftar tabel:", cur.fetchall())

conn.close()
