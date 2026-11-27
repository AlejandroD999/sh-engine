from query.cli import setup_parser, parse
from query.query_processor import QueryProcessor
from engine import SearchEngine

from data.links import get_graph_conns
from rank.ranker import rank
from data.pages import insert_scores

"""
parser = setup_parser()
parsed = parse(parser)

shen = SearchEngine(parsed.query)
"""
conns = get_graph_conns()
ranked = rank(conns)

insert_scores(ranked)