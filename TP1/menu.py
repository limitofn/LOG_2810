import networkx as nx
import matplotlib.pyplot as plt
import FileHandler as fl
import djikstra_algo as algoDji
import Commande as comm
import Robot as rob
import os

commandAsked = comm.Command()
G = 0
robotUtilise = rob.Robot()

def creerGraphe():
    print("<--------Creer le graphe--------->")
    if os.stat('entrepot.txt').st_size == 0:
        print("Desole le graphe n a pas ete creer")
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
        print("Fichier lu et Graphe Creer")
    print("<-------------Fin-------------->"+'\n')


def afficherGraphe():
    print("<--------Afficher le graphe--------->")
    if G == 0:
        print("Veuillez creer le graphique avant")
    else:
        plt.show()  # display
    print("<-------------Fin-------------->"+'\n')


def prendreCommande():
    print("<--------Prendre la commande--------->")
    commandAsked.setter()
    type = commandAsked.commandeValide()
    if type != 0:
        robotUtilise = rob.Robot(type)
    print("<-------------Fin-------------->"+ '\n')


def afficherCommande():
    print("<--------Afficher la derniere commande--------->")
    if (commandAsked.nbA == 0) & (commandAsked.nbB == 0) & (commandAsked.nbC == 0):
        print("La commande est vide!")
    else:
        commandAsked.afficherCommande()
    print("<-------------Fin-------------->"+ '\n')


def trouverChemin():
    print("<--------Trouver le plus court Chemin--------->")
    if G == 0 or (commandAsked.nbA == 0) & (commandAsked.nbB == 0) & (commandAsked.nbC == 0):
        print("Veuillez creer le graphique avant ou creer un commande")
    else:
        length, path = algoDji.graph_to_length(G, 0)
        pathToFinalNode = algoDji.path_to_object(G, path, commandAsked)
        stops = algoDji.finds_stops(G, pathToFinalNode, commandAsked)
        cost = algoDji.printCost(pathToFinalNode, stops, commandAsked.commandeValide(), G)
        print('Le robot utilise est le robot de type: ' + str(commandAsked.commandeValide()))
        print('Le robot a pris ' + str(cost) + ' secondes')
    print("<-------------Fin-------------->" + '\n')


def prendreChoix():
    return affichageDesChoix()


def affichageDesChoix():
    print("Choisir parmi les options suivantes: ")
    print("1 - Creer un graphe")
    print("2 - Afficher un graphe")
    print("3 - Prendre Commande")
    print("4 - Afficher Commande")
    print("5 - Trouver le plus court chemin")
    print("Quitter en entrant '6'")

    userInput = int(input('Entrez votre choix:'))

    if (userInput >= 0) & (userInput < 6):
        return userInput
    if userInput == 6:
        return 0
    else:
        print("Entrez un choix valide")
        userInput = affichageDesChoix()
        return userInput


switcher = {
    1: creerGraphe,
    2: afficherGraphe,
    3: prendreCommande,
    4: afficherCommande,
    5: trouverChemin,
}


def main():
    print("Bienvenue dans la solution du tp1")
    choice = prendreChoix()
    while choice != 0:
        func = switcher.get(choice, lambda: "Entrer un choix valide")
        func()
        choice = prendreChoix()
    print("Fin")


if __name__ == '__main__':
    main()
