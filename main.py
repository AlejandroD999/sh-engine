from src.data.wiki_api import fetch_api_data 
from src.data.db import fetch_articles
from src.cli import setup_parser, parse
from src.rank import Ranker

def main():
    parser = setup_parser()
    args = parse(parser)
    
    articles = fetch_articles(args.topic)
    
    ranker = Ranker(articles, args.topic)

    data = ranker.sorted
    
    if not data:
        return

    for article in data:
        print(article['title'], article['score'])



if __name__ == "__main__":
    main()
