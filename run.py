from query.query_processor import QueryProcessor
from data.links import get_links 
from rank.ranker import curate_links

''' Query processor example
user_query = input("Query: ")

processor = QueryProcessor(user_query)
print(processor.get_processed())
'''

curate_links(get_links())
