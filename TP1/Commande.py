class Command:
    def __init__(self, a=0, b=0, c=0):
        self.nbA = a
        self.nbB = b
        self.nbC = c

    def setter(self):
        print('Passage de Commande')
        self.nbA = int(input('Nombre objet A'))
        self.nbB = int(input('Nombre objet B'))
        self.nbC = int(input('Nombre objet C'))

    def commandeValide(self):
        #Verifie si le poid est valide et retourne le meilleur robot
        poid = 1*self.nbA + 3*self.nbB + 6*self.nbC
        if( poid > 25):
            print('Charge Impossible')
            return None
        elif(10 < poid <= 25):
            print('Utilisation robot Z')
            return 'Z'
        elif (5 < poid <= 10):
            print('Utilisation robot Y')
            return 'Y'
        elif (0 < poid <= 5):
            print('Utilisation robot X')
            return 'X'

    def afficherCommande(self):
        print('nombre object A: ' + str(self.nbA))
        print('nombre object B: ' + str(self.nbB))
        print('nombre object C: ' + str(self.nbC))

