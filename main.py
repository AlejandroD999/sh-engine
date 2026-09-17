from src.data.wiki_api import fetch_api_data, parse_article
from src.data.db import fetch_articles
from src.cli import setup_parser, parse

def main():
    parser = setup_parser()
    args = parse(parser)

    for article in fetch_articles(args.topic):
        print(article['title'])

if __name__ == "__main__":
    main()
