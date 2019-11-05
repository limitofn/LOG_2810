import networkx as nx
import Robot as rob

#finds the fastest path to each node
def graph_to_length (graph, source_node):
    length, path = nx.single_source_dijkstra(graph, source_node)
    return length, path

#finds the closest node where all the command can be filled while going to her
def path_to_object (graph, path, commandAsked):
    for key in path.keys():
        nbrA = 0
        nbrB = 0
        nbrC = 0
        for nodeIndex in path[key]:
            nbrA += graph._node[nodeIndex]['nbA']
            nbrB += graph._node[nodeIndex]['nbB']
            nbrC += graph._node[nodeIndex]['nbC']
            if (nbrA >= commandAsked.nbA) & (nbrB >= commandAsked.nbB) & (nbrC >= commandAsked.nbC):
                return path[nodeIndex]

#finds all the stops needed to fulfill the command
def finds_stops (graph, pathToFinalNode, commandAsked) :
    stops = []
    for nodeIndex in pathToFinalNode:\
        #list the objects present in the node
        nbrA = graph._node[nodeIndex]['nbA']
        nbrB = graph._node[nodeIndex]['nbB']
        nbrC = graph._node[nodeIndex]['nbC']
        partialCommandFullfill(nbrA,commandAsked.nbA,stops,'A',nodeIndex)
        partialCommandFullfill(nbrB, commandAsked.nbB, stops, 'B', nodeIndex)
        partialCommandFullfill(nbrC, commandAsked.nbC, stops, 'C', nodeIndex)
    stops.reverse()
    return stops

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

def printCost (pathToFinalNode, stops, robotType,graph) :
    #requires path from 0 to final node,list of stop and objects taken, robot type
    weight = 0
    costSum = 0
    robotCarrier = rob.Robot(robotType)
    constK = robotCarrier.calculConstVitesse()

    # Calculate cost to get to final node from initial node


    for node in pathToFinalNode:
        sum = 0
        #0 etant la premiere node, on passe au deuxieme element pour avoir des paires qui se suivent jusqu'a la final node
        if node == 0:
            previousNode = 0
            continue
        sum = graph.get_edge_data(previousNode,node)['weight'] * robotCarrier.calculConstVitesse()
        costSum += sum
        print('Cost entre ' + str(previousNode) + ' et ' + str(node) +'  ' + str(sum))
        previousNode = node

    print("")
    #Starting from final node, pick up objects then calculate cost
    # to next node until first node is reached.

    #Inverse the path so that it starts at final node and ends at first node
    pathToFinalNode.reverse()

    for node in pathToFinalNode:

        #if the node where we are contains objets to be added, add them
        for stop in stops:
            if stop[0] == node:
                robotCarrier.add(stop[2],stop[1])
                print('Ajout de ' + str(stop[2]) + ' ' + stop[1] +' au noeud ' + str(node))

        sum = 0
        if node == pathToFinalNode[0]:
            previousNode = pathToFinalNode[0]
            continue
        sum = graph.get_edge_data(previousNode, node)['weight'] * robotCarrier.calculConstVitesse()
        costSum += sum
        print('Cost entre ' + str(previousNode) + ' et ' + str(node) + '  ' + str(sum))




    #print final cost


def robot_actions (pathToFinalNode, stops) :
    actionSequence = []
    endOfPath = len(pathToFinalNode)
    for nodeIndex in range (0, endOfPath-1)  :
        actionSequence.append([pathToFinalNode[nodeIndex], 'to', pathToFinalNode[nodeIndex+1]])
    pathToFinalNode.reverse()
    for nodeIndex in range(0, endOfPath - 1):
        if pathToFinalNode[nodeIndex] == stops[0][0] :
            actionSequence.append([pathToFinalNode[nodeIndex], 'get object', stops[0][1]])
            del stops[0]
        actionSequence.append([pathToFinalNode[nodeIndex], 'to', pathToFinalNode[nodeIndex + 1]])
    return actionSequence


def find_way (graph, commandAsked):
    length, path = graph_to_length(graph, 0)
    pathToFinalNode = path_to_object(graph, path, commandAsked)
    stops = finds_stops(graph, pathToFinalNode, commandAsked)
    actionSequence = robot_actions(pathToFinalNode, stops)
    return actionSequence

