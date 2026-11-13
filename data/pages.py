from db import connect_to_db 
import sqlite3

# Pages is base: no references to other table scripts (e.g links.py)

def create_pages_table():

    with connect_to_db() as conn: 
        cur = conn.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS pages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL UNIQUE,
            timestamp TEXT,
            text TEXT)
        """)

        cur.close()

def insert_page(title, timestamp, text):
    create_pages_table()
    
    if not title:
        print("Error: title not found")
        raise

    query = """INSERT INTO pages (title, timestamp, text) VALUES (?, ?, ?)"""

    with connect_to_db() as conn:
        cur = conn.cursor()
        
        try:
            cur.execute(query, (title, timestamp, text)) 

        except sqlite3.IntegrityError as e:
            print(f"Database error: {e}")
            conn.rollback()

        cur.close()

# Get page data and return as a dict object
def get_page_data():
    create_pages_table()

    with connect_to_db() as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        cur.execute("SELECT * FROM pages")
        page_data = cur.fetchall()

        cur.close()

    return page_data

def get_page_titles():
    create_pages_table()

    with connect_to_db() as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        cur.execute("SELECT id, title FROM pages")

        titles = cur.fetchall()

        cur.close()

    return titles

