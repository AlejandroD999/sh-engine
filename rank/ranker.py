from data.links import get_links
import networkx as nx
import matplotlib.pyplot as plt

# TODO Make demo pagerank (don't remake the wheel)
#   - When finishing, make own if needed
# demo: use pagerank class from networkx

def rank(connections):
    if not connections:
        return 
    
    graph = nx.DiGraph(connections)
    return nx.pagerank(graph, alpha=0.85)

