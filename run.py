from query.cli import setup_parser, parse
from query.query_processor import QueryProcessor
from engine import SearchEngine

parser = setup_parser()
parsed = parse(parser)

shen = SearchEngine(parsed.query)

