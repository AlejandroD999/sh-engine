from query.query_processor import QueryProcessor

print("Welcome to the first version of Sh-Engine")
user_query = input("Query: ")

processor = QueryProcessor(user_query)
print(processor.get_processed())
