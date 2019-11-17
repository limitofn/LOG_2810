class WordSearch:
    def __init__(self):
        self.debutNom = None
        self.debutcode = None
        self.type = None

    def clear(self):
        self.debutNom = None
        self.debutcode = None
        self.type = None

    def getInput(self):
        self.debutNom = input('Critere de Recherche Nom')
        self.debutcode = input('Critere de Recherche Code')
        self.type = input('Type')

    def Search(self,listObject):
        listObjectValid = []
        for object in listObject:
            check = [
            object.nom.startswith(self.debutNom),
            object.code.startswith(self.debutcode),
            object.type == self.type
            ]

            if all(check):
                listObjectValid.append(object)

        return listObjectValid


