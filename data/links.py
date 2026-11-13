from db import connect_to_db
from pages import get_page_data, get_page_titles 
import sqlite3 
import re

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

def insert_links(row_data: list):
    create_links_table()

    if not row_data: 
        print("Error: must provide source_id and target_id")
        return

    with connect_to_db() as conn:
        cur = conn.cursor()
        
        try:
            cur.executemany("INSERT OR IGNORE INTO links (source_id, target_id) VALUES (?, ?)", row_data)

        except sqlite3.IntegrityError as e:
            print(f"Error during DB operation: {e}")
        cur.close()

def extract_links(article_text: str):
    links_set = set() 

    if not article_text:
        return set() 

    pattern = r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]'
    links = re.findall(pattern, article_text)

    for link in links:
        links_set.add(link)
    
    return links_set 

def form_links():

    # Get page data
    print("Getting data...")
    pages = get_page_data() 
    title_to_id = {row['title']: row['id'] for row in get_page_titles()} 

    # (source_id, target_id) rows
    rows = []
    print("Forming Links...")
    for page in pages:
        for link in extract_links(page['text']):
            target_id = title_to_id.get(link)
            if target_id and target_id != page['id']: 
                rows.append([page['id'], target_id]) 

    print("Inserting Links")
    insert_links(rows)
    print("Successfully formed links")


        

if __name__ == '__main__':
    links = form_links()


