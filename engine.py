from query.query_processor import QueryProcessor
from rank.ranker import rank

class SearchEngine:
    def __init__(self, query):
        self.query = query

        # Remove after testing
        self.run()

    def run(self):
        processor = QueryProcessor(self.query)

