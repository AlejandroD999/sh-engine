from query.cli import setup_parser, parse
from query.query_processor import QueryProcessor
from engine import SearchEngine
from data.pages import create_pages_table
"""
parser = setup_parser()
parsed = parse(parser)

shen = SearchEngine(parsed.query)
"""

create_pages_table()
