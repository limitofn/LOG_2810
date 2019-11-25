import FileReader as file
import WordSearch as search
import Order as order

listObject = file.fillArrayFromFile('inventaire.txt')
wordSearcher = search.WordSearch()
panier = order.Order()
listeObjectFound = []
print('test')


def trouverItem():

    global listeObjectFound
    global listObject

    print("<--------Searching Item--------->")
    wordSearcher.getInput()
    listeObjectFound = wordSearcher.Search(listObject)
    if len(listeObjectFound) == 0:
        print("Aucun objet trouver!")
    else:
        print("Les objets correspondants sont:")
        i = 0
        while i < 10 and i < len(listeObjectFound):
            print("-" + str(listeObjectFound[i].nom) + " " + str(listeObjectFound[i].code) + " "
                  + str(listeObjectFound[i].type))
            i = i + 1


def ajouterObjet():

    global listeObjectFound
    global listObject

    print("<--------Ajout d'un objet--------->")
    if len(listeObjectFound) == 0:
        print("Veuillez faire une recherche avant d'ajouter un objet")
    else:
        print("Voici les objets trouver ou restant dans recherche")
        i = 0
        while i <= 10 and i < len(listeObjectFound):
            print(str(i) + "- " + str(listeObjectFound[i].nom) + " " + str(listeObjectFound[i].code) + " "
                  + str(listeObjectFound[i].type))
            i = i + 1

        userInput = int(input("Veuillez entre le numero de l'objet:"))
        listeObjectTmp = panier.addObject(listObject, listeObjectFound[userInput])
        print("L'objet ayant le code " + str(listeObjectFound[userInput].code) + " a ete rajoute au panier")
        listeObjectFound.remove(listeObjectFound[userInput])
        listObject = listeObjectTmp

        print("Voulez-vous ajouter un objet a votre panier?")
        print("1- Oui          2-Non")
        userInput = int(input('Entrez votre choix numerique:'))

        if userInput == 1:
            ajouterObjet()
        else:
            print("Retour au menu principal")


def clearPanier():
    global listObject
    print("<--------Retrait de tous les objets--------->")
    if len(panier.order) == 0:
        print("Aucun objet dans le panier!")
    else:
        listObjectTmp = panier.removeAllObject(listObject)
        listObject = listObjectTmp
        print("Tous les objets ont ete retire et remis dans l'inventaire!")


def afficherCommande():
    print("<--------Affichage du panier--------->")
    if len(panier.order) == 0:
        print("Aucun objet dans le panier!")
    else:
        panier.printOrder()


def checkOut():
    global listObject
    print("<-------- Checkout --------->")
    if len(panier.order) == 0:
        print("Aucun objet dans le panier!")
    else:
        inventaire = []
        inventaire = panier.checkOut(listObject)
        if len(inventaire) > 0:
            listObject = inventaire



def prendreChoix():
    return affichageDesChoix()


def affichageDesChoix():
    print ("<-------- Menu principal --------->")
    print("Choisir parmi les options suivantes: ")
    print("1 - Trouver un objet")
    print("2 - Ajouter un objet au panier")
    print("3 - Retirer les objets du panier")
    print("4 - Afficher Commande")
    print("5 - Passer la commande")
    print("Quitter en entrant '6'")

    userInput = int(input('Entrez votre choix:'))

    if (userInput >= 0) & (userInput < 6):
        return userInput
    if userInput == 6:
        return 0
    else:
        print("Entrez un choix valide")
        userInput = affichageDesChoix()
        return userInput


switcher = {
    1: trouverItem,
    2: ajouterObjet,
    3: clearPanier,
    4: afficherCommande,
    5: checkOut
}


def main():
    print("Bienvenue dans la solution du tp2")
    choice = prendreChoix()
    while choice != 0:
        func = switcher.get(choice, lambda: "Entrer un choix valide")
        func()
        choice = prendreChoix()
    print("Fin")


if __name__ == '__main__':
    main()








