import networkx as nx


def graph_to_length (graph, source_node):
    length, path = nx.single_source_dijkstra(graph, source_node)
    return length, path


def path_to_object (graph, path, commandePasse):
    for key in path.keys():
        nbreA = 0
        nbreB = 0
        nbreC = 0
        for noeud in path[key]:
            nbreA += graph._node[noeud]['nbA']
            nbreB += graph._node[noeud]['nbB']
            nbreC += graph._node[noeud]['nbC']
            if (nbreA >= commandePasse.nbA) & (nbreB >= commandePasse.nbB) & (nbreC >= commandePasse.nbC):
                return path[noeud]


