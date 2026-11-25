from query.query_processor import QueryProcessor
from rank.ranker import rank

class SearchEngine:
    def __init__(self, query):
        self.query = query

        # Remove after testing
        self.run()

    def run(self):
        processor = QueryProcessor(self.query)
        processed = processor.process()

        # TODO Grab articles based on query

        # TODO Rank articles

        # TODO Return top articles (Maybe title of top 20)


