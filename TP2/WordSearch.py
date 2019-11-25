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
        self.debutNom = input('Critere de Recherche Nom:')
        self.debutcode = input('Critere de Recherche Code:')
        self.type = input('Type:')

    def Search(self,listObject):
        listObjectValid = []
        for object in listObject:

            if self.debutNom == "" and self.debutcode == "" and self.type == "":  #verifier
                return listObject
            elif self.debutcode == "" and self.debutNom == "":  #verifie
                check = [
                    object.type == self.type
                ]
            elif self.debutcode == "" and self.type == "":  #verifier
                check = [
                    object.nom.startswith(self.debutNom),
                ]
            elif self.debutNom == "" and self.type == "":  #verifier
                check = [
                    object.code.startswith(self.debutcode),
                ]
            elif self.debutNom == "":  #verifie
                check = [
                    object.code.startswith(self.debutcode),
                    object.type == self.type
                ]
            elif self.debutcode == "":  #verifie
                check = [
                    object.nom.startswith(self.debutNom),
                    object.type == self.type
                ]
            elif self.type == "":  #verifie
                check = [
                    object.nom.startswith(self.debutNom),
                    object.code.startswith(self.debutcode),
                ]
            else:
                check = [
                    object.nom.startswith(self.debutNom),
                    object.code.startswith(self.debutcode),
                    object.type == self.type
                ]

            if all(check):
                listObjectValid.append(object)
        return listObjectValid


