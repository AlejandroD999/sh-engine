import sqlite3
from settings import DB_PATH

def create_articles_table():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()

        
        cur.execute("""
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL UNIQUE,
            description TEXT,
            excerpt TEXT
                    )
                    """)

        cur.close()

def insert_article(title, description, excerpt):
    if not title:
        raise "Article to insert must include a title"
    
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        
        try:
            cur.execute("INSERT INTO articles (title, description, excerpt) VALUES (?, ?, ?)", (title, description, excerpt)) 

        except sqlite3.IntegrityError as e:
            print(f"Database constraint integrity error: {e}")
            conn.rollback()

        cur.close()

if __name__ == "__main__":
    create_articles_table()
    
    insert_article("jupiter", "A planet of solar system", "bla bla bla")
