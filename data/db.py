import sqlite3

def connect_to_db():
    return sqlite3.connect("pages.db")

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

def get_page_data():
    with connect_to_db() as conn:
        cur = conn.cursor()

        cur.execute("SELECT * FROM pages")
        page_data = cur.fetchall()

        cur.close()

    return page_data
            

if __name__ == "__main__":
    
    print(get_page_data())
