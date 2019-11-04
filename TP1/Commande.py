class Command:
    def __init__(self):
        self.Setter()

    def Setter(self):
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
        print('nombre object A '+ self.nbA)
        print('nombre object B ' + self.nbB)
        print('nombre object C ' + self.nbC)

