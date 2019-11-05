import networkx as nx

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
    #input : fills one stop with the correct order, type is a string
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