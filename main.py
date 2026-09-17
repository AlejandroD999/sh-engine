from src.data.wiki_api import fetch_api_data, parse_article
from src.data.db import fetch_articles
from src.cli import setup_parser, parse

def main():
    parser = setup_parser()

    args = parse(parser)

    print(args.topic)


if __name__ == "__main__":
    main()
