
import networkx as nx
import matplotlib.pyplot as plt
import FileHandler as fl
import djikstra_algo as algoDji
import Commande as comm
import Robot as rob
import os

commandAsked = 0
G = 0
robotUtilise

switcher = {
    1: creerGraphe,
    2: afficherGraphe,
    3: PrendreCommande,
    4: AfficherCommande,
    5: TrouverChemin,
    6: Quitter
}

def menu ():
    print (" Bienvenue dans la solution du tp1" +"\n")
    choice = prendreChoix()
    while choice != 0 :
        func = switcher.get(choice, lambda : "Entrer un choix valide"+"\n")
        func()
        choice = prendreChoix()
    print ("Fin")


def creerGraphe():
    print("<--------Creer le graphe--------->"+"\n")
    if os.stat('entrepot.txt').st_size == 0:
        print ("Desole le graphe n a pas ete creer"+"\n")
    else:
        G = fl.fillGraphFromFile('entrepot.txt')

        elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 0.5]
        esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] <= 0.5]

        pos = nx.spring_layout(G)  # positions for all nodes

        # nodes
        nx.draw_networkx_nodes(G, pos, node_size=700)

        # edges
        nx.draw_networkx_edges(G, pos, edgelist=elarge,
                               width=6)
        nx.draw_networkx_edges(G, pos, edgelist=esmall,
                               width=6, alpha=0.5, edge_color='b', style='dashed')
        # labels
        nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')

        plt.axis('off')
        plt.savefig("weighted_graph.png")  # save as png
        print("Fichier lu et Graphe Creer" +"\n")


def afficherGraphe():
    print("<--------Afficher le graphe--------->"+"\n")
    if G == 0:
        print("Veuillez creer le graphique avant" + "\n")
    else:
        plt.show()  # display

def prendreCommande():
    print("<--------Prendre la commande--------->"+"\n")
    commandAsked = comm.Command()
    type = commandAsked.commandeValide()
    if type != none:
        robotUtilise = rob.Robot(type)


def afficherCommande():
    print("<--------Afficher la derniere commande--------->"+"\n")
    if (commandAsked.nbA == 0) & (commandAsked.nbB == 0) & (commandAsked.nbC == 0):
        print ("La commande est vide!" +"\n")
    else:
        commandAsked.afficherCommande()

def TrouverChemin():
    print("<--------Trouver le plus court Chemin--------->"+"\n")
    if G == 0:
        print("Veuillez creer le graphique avant" + "\n")
    else:
        length, path = algoDji.graph_to_length(G, 0)
        pathToFinalNode = algoDji.path_to_object(G, path, commandAsked)
        stops = algoDji.finds_stops(G, pathToFinalNode, commandAsked)
        cost = algoDji.printCost(pathToFinalNode, stops, commandAsked.commandeValide(), G)
        print ('Le robot utilise est le robot de type ' + commandAsked.commandeValide() + '\n')
        print ('Le robot a pris ' + cost + ' secondes' + '\n')

def prendreChoix():
    return affichageDesChoix()

def affichageDesChoix():

    print "\n"
    print ("Choisir parmi les options suivantes: " + "\n")
    print ("1 - Creer un graphe" + "\n")
    print ("2 - Afficher un graphe" + "\n")
    print ("3 - Prendre Commande" + "\n")
    print ("4 - Afficher Ordre" + "\n")
    print ("5 - Trouver le plus court chemin" + "\n")
    print ("Quitter en entrant '6'" + "\n")

    userInput = int(input('Entrez votre choix:'))

    if (userInput >= 0) & (userInput<=6):
        return userInput
    else:
        print ("Entrez un choix valide" + "\n")
        userInput = affichageDesChoix()
        return userInput
