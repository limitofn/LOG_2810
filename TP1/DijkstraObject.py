import networkx as nx
import Commande as comm
import networkx as nx
import Commande as comm
import Robot as rob
import operator


def fonctionDjikstraObjet(graph, command):
    #On part de la node 0

    nodes = [node for node in graph.nodes if ((command.nbA > 0 and graph._node[node]["nbA"] > 0) or (command.nbB > 0 and graph._node[node]["nbB"] > 0) or (command.nbC > 0 and graph._node[node]["nbC"] > 0))]
    #calcul cout en A

    #Preparation de l'ouvrier robot
    contraintesInit = rob.Robot(command.commandeValide())
    contraintesInit.setter(command.nbA, command.nbB, command.nbC)

    costsPath = fonctionQuiUpdateLeCost(0, nodes, graph, command, contraintesInit)

    print(costsPath)

    all_costs_paths = []
    for (cost, path) in costsPath:
        return_cost, return_path = nx.single_source_dijkstra(graph, path[-1], 0)
        all_costs_paths.append((cost + return_cost, path + return_path[1:]))

    # Minimum sur le premier element du tuple pour la list (cout, chemin)
    best_cost, best_path = min(all_costs_paths, key=operator.itemgetter(0))
    print (best_cost, best_path)

    return best_cost, best_path.reverse()


def fonctionQuiUpdateLeCost(start_node, nodes, graph, command, contraintesInit):

    if len(nodes) < 1:
        return [(0, [])]

    costsPath = []

    for node in nodes:
        CostA, path =  nx.single_source_dijkstra(graph, start_node, node)

        #Calcul du cout de deplacement et objets :
        cost, updcmd = calculateCost(path, command, nodes, contraintesInit, graph)

        #On enleve les nodes maintenant vides et celles qui ne servent plus ( pas d'objet utile )
        updates_nodes = [n for n in nodes if n not in path and  ((updcmd.nbA > 0 and graph._node[n]["nbA"] > 0) or (updcmd.nbB > 0 and graph._node[n]["nbB"] > 0) or (updcmd.nbC > 0 and graph._node[n]["nbC"] > 0))]

        newnode = path[-1]
        #On recalcule les chemins afin d'avoir un dijkstra dans un dijkstra sur toutes les nodes
        next_costs_path = fonctionQuiUpdateLeCost(path[-1], updates_nodes, graph, updcmd, contraintesInit)

        costsPath += [(cost + nc, path + np[1:]) for (nc, np) in next_costs_path]

    return costsPath


def calculateCost(path, command, nodes, contraintes, graph):

    if len(path) < 2:
        return 0, command

    updatedCommand = command

    first, second = path[0], path[1]
    #On cherche un cout de deplacement avec la masse actuelle de la commande ( methode inverse)
    #On se deplace de first a second avec la masse du robot

    objectSumCost = 0
    #Posons des objets :

    if (second in nodes):
        numberA = min(command.nbA, graph._node[second]['nbA']) #Nombre d'objet A
        numberB = min(command.nbB, graph._node[second]['nbB'])  # Nombre d'objet B
        numberC = min(command.nbC, graph._node[second]['nbC'])  # Nombre d'objet C
        objectSumCost = (numberA + numberB + numberC) * 10

        updatedCommand = comm.Command(command.nbA - numberA, command.nbB - numberB, command.nbC - numberC)

    sum = graph.get_edge_data(first, second)['weight'] * contraintes.calculConstVitesse()
    sum += objectSumCost

    #Calcul recursif du cost
    s, uc = calculateCost(path[1:], updatedCommand, nodes, contraintes, graph)

    return s + sum, uc



def partialCommandFullfill(nbr,nbCommand,listOfStops,type,nodeIndex):
    #input : fills one stop with the correct order, type is a string ( A, B or C )
    if ((nbr != 0) & (nbCommand != 0)):
        if nbr == nbCommand:
            listOfStops.append([nodeIndex, type, nbr]) #object = command. put the command to 0 and append the stop
            nbCommand = 0
        elif nbr < nbCommand:
            listOfStops.append([nodeIndex, 'A', nbr])  #TODO: si la commande est plus grand on modifie la commande par le nombre de node puis on append le nombre de node ici
            nbCommand = nbCommand - nbr
        elif nbr > nbCommand:
            listOfStops.append([nodeIndex, 'A', nbCommand]) #TODO: si le nombre requis est plus grand, on append la commande
            nbCommand = 0

        nbrA = 0
        nbrB = 0
        nbrC = 0
        for nodeIndex in listPathA:
            nbrA += graph._node[nodeIndex]['nbA']
            nbrB += graph._node[nodeIndex]['nbB']
            nbrC += graph._node[nodeIndex]['nbC']
            if (nbrA >= command.nbA) & (nbrB >= command.nbB) & (nbrC >= command.nbC):
                return path[nodeIndex]