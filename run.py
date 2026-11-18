from query.query_processor import QueryProcessor
from data.links import get_graph_conns
from data.pages import get_titles
from rank.ranker import rank 

''' Query processor example
user_query = input("Query: ")

processor = QueryProcessor(user_query)
print(processor.get_processed())
'''

conns = get_graph_conns()
ranked = rank(conns)
