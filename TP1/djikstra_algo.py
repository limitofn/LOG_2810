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
    print('Commande impossible a realiser')

def time_ellapsed (graph, path, lenght, robot, commande):

    time = 0
    time += lenght[path[-1]] * robot.vitesseRobot # A implementer pour la vitesse du robot et donne le temps pour le robot atteigne le node le plus loin

    for noeudAller in path:
        print (noeudAller + '->')

    for element in path [::-1]: # parcours la liste de facon inverser
        nbreColisADansNoeud = graph._nodes[noeud]['nbA']
        nbreColisBDansNoeud = graph._nodes[noeud]['nbA']
        nbreColisCDansNoeud = graph._nodes[noeud]['nbA']

        compteur = 0 # reset du compteur
        while robot.conteneurA != commande.nbA or compteur <= nbreColisADansNoeud:
            robot.conteneurA + 1
            time + 10
            compteur + 1
            print ('recuperation d un Colis A sur le noeud ->')

        compteur = 0 # reset du compteur
        while robot.conteneurB != commande.nbB or compteur <= nbreColisBDansNoeud:
            robot.conteneurB + 1
            time + 10
            compteur + 1
            print ('recuperation d un Colis B sur le noeud ->')

        compteur = 0 # reset du compteur
        while robot.conteneurC != commande.nbC or compteur <= nbreColisCDansNoeud:
            robot.conteneurC + 1
            time + 10
            compteur + 1
            print ('recuperation d un Colis C sur le noeud ->')

        print (path[element-1] + '->')
        distanceEntreNoeuds = graph[element][element-1]['weight']
        time +=  distanceEntreNoeuds * robot.vitesseRobot #deplacement vers la prochaine node

        if robot.conteneurA == commande.nbA & robot.conteneurB == commande.nbB & robot.conteneurC == commande.nbC & element == 0:
            print ('Le robot a accomplie la tache en ' + time + ' secondes' )

