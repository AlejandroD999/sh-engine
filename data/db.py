import sqlite3

def create_pages_table():

    with sqlite3.connect("articles.db") as conn:
        cur = conn.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS pages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL UNIQUE,
            timestamp TEXT,
            text TEXT)
        """)

        cur.close()

if __name__ == "__main__":
    create_pages_table()


