from .db import connect_to_db 
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
            text TEXT,
            score REAL)
        """)

        cur.close()

# TODO Make an execute many 
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

# Insert ranked scores
def insert_scores(scores):
    create_pages_table()

    if not scores:
        print("Scores data not provided")
        return

    query = "UPDATE pages SET score=? WHERE id=?"
    scores_data = [(score, id_) for id_, score in scores.items()]

    with connect_to_db() as conn:
        cur = conn.cursor()
        cur.executemany(query, scores_data)

        cur.close()





# Get page data and return as a dict object
def get_pages():
    create_pages_table()

    with connect_to_db() as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        cur.execute("SELECT * FROM pages")
        page_data = cur.fetchall()

        cur.close()

    return page_data

def get_titles():
    create_pages_table()

    with connect_to_db() as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        cur.execute("SELECT id, title FROM pages")

        titles = cur.fetchall()

        cur.close()

    return titles

def get_ids():
    create_pages_table()

    with connect_to_db() as conn:
        cur = conn.cursor()
        cur.execute("SELECT id FROM pages")

        ids = [row[0] for row in cur.fetchall()]

        cur.close()
    return ids







