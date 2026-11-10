import networkx as nx
import matplotlib.pyplot as plt

# TODO Make demo pagerank (don't make the wheel)
#   - When finishing, make own if needed
# demo: use pagerank class from networkx

# Ranking happens on its own schedule (not during query)  
'''
1. Create links table in pages.db & parse links from articles to links as connections (digraph)
    - get text from article: find all [[..]] <- links
        - if pipe ("|"): get text after pipe (it's the link)
        - insert connection into links page (source_id, target_id)

2. use links to create DiGraph
3. PageRank
4. Return sorted pages
'''
connections = [[1, 2], [2, 3], [3, 1], [4, 1], [3, 2]]

G = nx.DiGraph(connections)

page_rank = nx.pagerank(G, alpha=0.85)

for item in page_rank.items():
    print(item)

