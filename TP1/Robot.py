        class Robot:
            def __init__(self, type):
                conteneurA = 0
                conteneurB = 0
                conteneurC = 0
                type = type
                CONST_K = 0

            def setter(self, nbA, nbB, nbC):
                self.conteneurA = nbA
                self.conteneurB = nbB
                self.conteneurC = nbC

            def parcoursChemin(self, path, command, graph):
                #On prends le chemin a parcourir de node debut a node end.
                #Calcul du cout vers la node de fin
                cout = 0
                
                previous = None
                for index in path:
                    if(previous != None):
                        cout += graph[previous][index]['weight']




