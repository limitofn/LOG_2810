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
        for knot in path[key]:
            nbrA += graph._node[knot]['nbA']
            nbrB += graph._node[knot]['nbB']
            nbrC += graph._node[knot]['nbC']
            if (nbrA >= commandAsked.nbA) & (nbrB >= commandAsked.nbB) & (nbrC >= commandAsked.nbC):
                return path[knot]

#finds all the stops needed to fulfill the command
def finds_stops (graph, pathToFinalNode, commandAsked) :
    stops = []
    for knot in pathToFinalNode:
        nbrA = graph._node[knot]['nbA']
        nbrB = graph._node[knot]['nbB']
        nbrC = graph._node[knot]['nbC']
        if ((nbrA != 0)&(commandAsked.nbA != 0)) :
            if nbrA == commandAsked.nbA :
                stops.append([knot, 'A', nbrA])
                commandAsked.nbA = 0
            elif nbrA < commandAsked.nbA :
                stops.append([knot, 'A', nbrA])
                commandAsked.nbA = commandAsked.nbA - nbrA
            elif nbrA > commandAsked.nbA :
                stops.append([knot, 'A', commandAsked.nbA])
                commandAsked.nbA = 0
        if ((nbrB !=0)&(commandAsked.nbB != 0)) :
            if nbrB == commandAsked.nbB :
                stops.append([knot, 'B', nbrB])
                commandAsked.nbB = 0
            elif nbrB < commandAsked.nbB :
                stops.append([knot, 'B', nbrB])
                commandAsked.nbB =commandAsked.nbB - nbrB
            elif nbrB > commandAsked.nbB :
                stops.append([knot, 'B', commandAsked.nbB])
                commandAsked.nbB = 0
        if ((nbrC != 0)&(commandAsked.nbC != 0)) :
            if nbrC == commandAsked.nbC :
                stops.append([knot, 'C', nbrC])
                commandAsked.nbC = 0
            elif nbrC < commandAsked.nbC :
                stops.append([knot, 'C', nbrC])
                commandAsked.nbC = commandAsked.nbC - nbrC
            elif nbrC > commandAsked.nbC :
                stops.append([knot, 'C', commandAsked.nbC])
                commandAsked.nbC = 0
    stops.reverse()
    return stops


def robot_actions (pathToFinalNode, stops) :
    actionSequence = []
    endOfPath = len(pathToFinalNode)
    for knot in range (0, endOfPath-1)  :
        actionSequence.append([pathToFinalNode[knot], 'to', pathToFinalNode[knot+1]])
    pathToFinalNode.reverse()
    for knot in range(0, endOfPath - 1):
        if pathToFinalNode[knot] == stops[0][0] :
            actionSequence.append([pathToFinalNode[knot], 'get object', stops[0][1]])
            del stops[0]
        actionSequence.append([pathToFinalNode[knot], 'to', pathToFinalNode[knot + 1]])
    return actionSequence


def find_way (graph, commandAsked):
    length, path = graph_to_length(graph, 0)
    pathToFinalNode = path_to_object(graph, path, commandAsked)
    stops = finds_stops(graph, pathToFinalNode, commandAsked)
    actionSequence = robot_actions(pathToFinalNode, stops)
    return actionSequence