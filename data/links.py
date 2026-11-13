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

def insert_link(source_id, target_id):
    create_links_table()

    if not source_id or not target_id:
        print("Error: must provide source_id and target_id")
        return

    with connect_to_db() as conn:
        cur = conn.cursor()

        cur.execute("INSERT INTO links (source_id, target_id) VALUES (?, ?)", (source_id, target_id))

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

def make_links():

    # Get page data
    pages = get_page_data() 
    titles = get_page_titles()

    # Iterate & extract links
    for page in pages:

        try:
            links = extract_links(page['text'])

        except Exception:
            print("Error while creating links")
            continue 
        
        # TODO Improve speed
        for link in links:
            # TODO Make conditional based on titles (line 58)
            # Use the cheaper route
            return
            if link:
                insert_link(page['id'], target_data[0])
            else:
                continue

if __name__ == '__main__':
    titles = get_page_titles()

    print(titles[0]['id'])
'''
    links = make_links()
    
    print((links[40]))
    '''
