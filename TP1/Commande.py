class Command:
    def __init__(self):
        self.Setter()

    def Setter(self):
        print('Passage de Commande')
        self.nbA = int(input('Nombre objet A'))
        self.nbB = int(input('Nombre objet B'))
        self.nbC = int(input('Nombre objet C'))
        
