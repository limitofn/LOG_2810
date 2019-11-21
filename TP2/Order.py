class Order:
    def __init__(self):
        self.order = []
        self.weight = 0

    def addObject(self, listObject, object):
        self.order.append(object)

        if object.type == 'A':
            self.weight += 1
        if object.type == 'B':
            self.weight += 3
        if object.type == 'C':
            self.weight += 5

        for i in listObject:
            if i == object:
                listObject.remove(i)
        return listObject

    def printOrder(self):
        if self.order == None:
            print("Désolé, votre panier est vide")
        else:
            print("Votre panier contient:")
            for i in self.order:
                print(self.order[i])
            print("Et le poid du panier est de " + str(self.weight) + "Kg")

    def removeAllObject(self, listObject):
        for object in self.order:
            listObject.append(object)
        self.order.clear()
        return listObject

    def checkOut(self, listObject):
        if self.weight >= 25:
            newInventory = self.removeAllObject(listObject)
            print("Panier trop lourd! Commande abandonnnee")
            return newInventory
        else:
            print("Commande passee! Merci d'avoir magasine chez nous!")
            self.order.clear


