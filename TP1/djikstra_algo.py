import networkx as nx
import Commande as commande

def graph_to_length (graph, source_node):
    length, path = nx.single_source_dijkstra(graph, source_node)
    return length, path

def path_to_object (graph, path, commandePasse):
    panier = commande.command
    for option in path:
        nbreA = 0
        nbreB = 0
        nbreC = 0
        for noeud in option:
            nbreA += graph.node['noeud']['nbA']
            nbreB += graph.node['noeud']['nbB']
            nbreC += graph.node['noeud']['nbC']
            if (nbreA >= panier.nbA) & (nbreB >= panier.nbB) & (nbreC >= panier.nbC):
                return path[option]


