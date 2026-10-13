from db import insert_page
import xml.etree.ElementTree as ET

ns = "{http://www.mediawiki.org/xml/export-0.11/}"

def extract_xml_data(root, prefix):
    page_data = [] 
    for page in root.findall(f"{prefix}page"):
        title = page.find(f"{prefix}title")
        
        revision = page.find(f"{prefix}revision")

        timestamp = revision.find(f"{prefix}timestamp")
        text = revision.find(f"{prefix}text")
        
        page_data.append(
                {"title": title.text, "timestamp": timestamp.text, "text": text.text}
                )
    return page_data

def index_to_db(pages):

    if len(pages) < 1:
        print("Indexing error: pages not provided")
        return

    for page in pages:

        insert_page(
                title=page['title'], 
                timestamp=page['timestamp'], 
                text=page['text']
                )
    

tree = ET.parse("test_dumps.xml")
root = tree.getroot()

pages = extract_xml_data(root, ns)

index_to_db(pages)

