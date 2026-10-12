import xml.etree.ElementTree as ET

ns = "{http://www.mediawiki.org/xml/export-0.11/}"

def get_pages(root, prefix):
    return root.findall(f"{prefix}page") 

tree = ET.parse("test_dumps.xml")
root = tree.getroot()

pages = get_pages(root, ns)


