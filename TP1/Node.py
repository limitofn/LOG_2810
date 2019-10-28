class Node:
    def __init__(self, nom):
        self.name = nom
        self.nbA = 0
        self.nbB = 0
        self.nbC = 0

    def setterObjects(self,numberA,numberB,numberC):
        self.nbA = numberA
        self.nbB = numberB
        self.nbC = numberC