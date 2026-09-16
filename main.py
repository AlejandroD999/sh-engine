from src.data.wiki_api import fetch_api_data, parse_article
from src.data.db import fetch_articles

for i in range(10):
    article_topic = input(f"Topic {i+1}:")

    data = fetch_api_data(article_topic)
    parse_article(data)




