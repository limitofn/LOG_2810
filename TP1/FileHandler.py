import Node as n
import networkx as nx

def fillGraphFromFile(fileName):
    f = open(fileName, "r")
    fileContent = f.readlines()

    #on cree le graphe
    graphEntrepot = nx.Graph()

    #On cree les listes temporaires
    nodeList = []
    secondePartie = False

    for line in fileContent:
        if(line == '\n'):
            secondePartie = True
        elif( not line):
            #Sommes nous a la fin?
            break
        elif(secondePartie == False) :
            #On lit des nodes, on s'attends a 4 chiffres
            inputNode = [int(x) for x in line.split(',')]
            graphEntrepot.add_node(inputNode[0], nbA=inputNode[1], nbB = inputNode[2],nbC=inputNode[3] )
        else:
            #On lit des Arcs, on peuple le graphe
            intputGraph = [int(x) for x in line.split(',')]
            graphEntrepot.add_edge(intputGraph[0], intputGraph[1], weight=intputGraph[2])

    f.close()
    return graphEntrepot
