from src.data.wiki_api import fetch_api_data, parse_article
from src.data.db import fetch_articles
from src.cli import setup_parser, parse
from src.rank import Ranker

def main():
    parser = setup_parser()
    args = parse(parser)
    
    articles = fetch_articles(args.topic)
    
    ranker = Ranker(articles)

    ranker.sort(args.topic)


if __name__ == "__main__":
    main()
