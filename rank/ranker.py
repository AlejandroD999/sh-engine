from data.links import get_graph_conns
import networkx as nx
import matplotlib.pyplot as plt

# TODO Make demo pagerank (don't remake the wheel)
#   - When finishing, make own if needed
# demo: use pagerank class from networkx

def rank(connections):
    if not connections:
        return 

    # TODO Leave digraph blank on init. Then, add nodes from page_ids and edges from connections
    
    graph = nx.DiGraph(connections)
    return nx.pagerank(graph, alpha=0.85)

