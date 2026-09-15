from src.data.wiki_api import fetch_articles, parse_article


jup = fetch_articles("jupiter")

parse_article(jup)

