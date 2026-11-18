from data.links import get_graph_conns
from data.pages import get_ids
import networkx as nx
import matplotlib.pyplot as plt

# TODO Make demo pagerank (don't remake the wheel)
#   - When finishing, make own if needed
# demo: use pagerank class from networkx

def rank(connections):
    # TODO Improve ranking: all pages have same score
    if not connections:
        return 
    page_ids = get_ids()
    
    graph = nx.DiGraph()

    graph.add_nodes_from(page_ids)
    graph.add_edges_from(connections)

    return nx.pagerank(graph, alpha=0.85)

