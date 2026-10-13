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
                {"title": title, "timestamp": timestamp, "text": text}
                )
    return page_data


tree = ET.parse("test_dumps.xml")
root = tree.getroot()

pages = extract_xml_data(root, ns)

