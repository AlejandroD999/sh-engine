from query.cli import setup_parser, parse
from query.query_processor import QueryProcessor

parser = setup_parser()
parsed = parse(parser)

processor = QueryProcessor(parsed.query)

print(processor.get_processed())
