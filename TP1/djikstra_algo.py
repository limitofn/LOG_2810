import networkx as nx
import commande as commande

def graph_to_length (graph, source_node) :
    length, path = nx.single_source_dijkstra(graph, source_node)
    return length, path

def path_to_object (graph, path, cmd) :
    node
    panier = commande.command
    for option in path :
        objectList = [0, 0, 0]
        for noeud in option :
            objectList += graph[noeud].A
            objectList += graph[noeud].B
            objectList += graph[noeud].C
            listeDeListe += objectList
    return node

