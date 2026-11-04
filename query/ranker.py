import networkx as nx
import matplotlib.pyplot as plt

# TODO Make demo pagerank (don't make the wheel)
#   - When finishing, make own if needed
# demo: use pagerank class from networkx

connections = [[1, 2], [2, 3], [3, 1], [4, 1], [3, 2]]

G = nx.DiGraph(connections)

page_rank = nx.pagerank(G, alpha=0.85)

for item in page_rank.items():
    print(item)

