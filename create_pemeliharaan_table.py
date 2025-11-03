import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS pemeliharaan (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_alat TEXT NOT NULL,
    tanggal TEXT NOT NULL,
    status TEXT,
    keterangan TEXT,
    teknisi TEXT
)
""")

# data dummy
cur.executemany("""
INSERT INTO pemeliharaan (nama_alat, tanggal, status, keterangan, teknisi)
VALUES (?, ?, ?, ?, ?)
""", [
    ('Monitor Pasien', '2025-10-01', 'Selesai', 'Pengecekan rutin', 'Fuad'),
    ('Ventilator', '2025-10-03', 'Proses', 'Perlu penggantian filter', 'Ali'),
    ('Infus Pump', '2025-10-05', 'Selesai', 'Normal', 'Budi'),
])

conn.commit()
conn.close()

print("Tabel 'pemeliharaan' berhasil dibuat dan diisi data contoh.")
