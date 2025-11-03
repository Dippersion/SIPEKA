import sqlite3, os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "app.db")

def clear_data():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Hanya hapus data laporan & inventaris
    tables = ["reports", "inventory"]
    for table in tables:
        cur.execute(f"DELETE FROM {table};")

    conn.commit()
    conn.close()
    print("Data laporan & inventaris berhasil dihapus, akun tetap aman ✅")

if __name__ == "__main__":
    clear_data()
