import sqlite3
import re

def connect_to_db():
    return sqlite3.connect("articles.db")

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

def create_links_table():

    with connect_to_db() as conn:
        cur = conn.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS links (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source_id INTEGER NOT NULL,
            target_id INTEGER NOT NULL,
            FOREIGN KEY (source_id) REFERENCES pages(id),
            FOREIGN KEY (target_id) REFERENCES pages(id),
            UNIQUE (source_id, target_id)

        )""")
        
        # TODO Create index (below) after inserting all links (takes more space and time but efficient lookups)
        # cur.execute("CREATE INDEX IF NOT EXISTS idx_links_target ON links(target_id)")

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
    with connect_to_db() as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        cur.execute("SELECT * FROM pages")
        page_data = cur.fetchall()

        cur.close()

    return page_data

def extract_links(title, article_text: str):

    pattern = r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]'

    links = re.findall(pattern, article_text)
    
    return {title: links}


if __name__ == "__main__":
    create_links_table()    
