from db import connect_to_db
from pages import get_page_data
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

def extract_links(title, article_text: str):
    
    if not title or not article_text:
        return 

    pattern = r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]'
    links = re.findall(pattern, article_text)
    
    return {title: links}

def create_links():
    refs  = {}

    # Get page data
    pages = get_page_data() 

    # Iterate & extract links
    for page in pages:
        title = page['title']

        try:
            refs[page['id']] = extract_links(title, page['text'])

        except Exception:
            print("Error while creating links")

    return refs
    # Find source and target references in DB: NULL if not exists

    # Insert Links

