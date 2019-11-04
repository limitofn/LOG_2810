import networkx as nx
import Commande as commande

def graph_to_length (graph, source_node):
    length, path = nx.single_source_dijkstra(graph, source_node)
    return length, path

def path_to_object (graph, path, commandePasse):
    print(path)
    for list in path:
        nbreA = 0
        nbreB = 0
        nbreC = 0
        nbreA += graph.node[list]['nbA']
        nbreB += graph.node[list]['nbB']
        nbreC += graph.node[list]['nbC']
        if (nbreA >= commandePasse.nbA) & (nbreB >= commandePasse.nbB) & (nbreC >= commandePasse.nbC):
            return path[list]


