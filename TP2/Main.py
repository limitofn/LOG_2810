import FileReader as file
import WordSearch as search
import Order as order

#Variable globale
listObject = file.fillArrayFromFile('inventaire.txt')
wordSearcher = search.WordSearch()
panier = order.Order()
listeObjectFound = []
print('test')

#Focntion de recherche pour trouver des objets dans une liste
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

#Fonction permettant d'ajouter un objet ou des objets de la liste de recherche dans le panier
def ajouterObjet():

    global listeObjectFound
    global listObject

    print("<--------Ajout d'un objet--------->")
    if len(listeObjectFound) == 0:
        print("Veuillez faire une recherche avant d'ajouter un objet")
    else:
        print("Voici les objets trouver ou restant dans recherche")
        i = 0
        while i < 10 and i < len(listeObjectFound):
            print(str(i) + "- " + str(listeObjectFound[i].nom) + " " + str(listeObjectFound[i].code) + " "
                  + str(listeObjectFound[i].type))
            i = i + 1
        try:
            userInput = int(input("Veuillez entre le numero de l'objet:"))
            if userInput < i:
                print("L'objet ayant le code " + str(listeObjectFound[userInput].code) + " et le type " +
                      str(listeObjectFound[userInput].type) + " a ete rajoute au panier")

                listeObjectTmp = panier.addObject(listObject, listeObjectFound[userInput])
                listeObjectFound.remove(listeObjectFound[userInput])
                listObject = listeObjectTmp
                ajouterSecondObjet()
            else:
                print("Entrez un choix valide!")
                ajouterObjet()
        except ValueError:
            print("Entrez un choix valide!")
            ajouterObjet()


#fonction permetant d'enlever tous les objets et de les remettre dans l'inventaire
def clearPanier():
    global listObject
    print("<--------Retrait de tous les objets--------->")
    if len(panier.order) == 0:
        print("Aucun objet dans le panier!")
    else:
        listObjectTmp = panier.removeAllObject(listObject)
        listObject = listObjectTmp
        print("Tous les objets ont ete retire et remis dans l'inventaire!")

#fonction permettant d'afficher la commande
def afficherCommande():
    print("<--------Affichage du panier--------->")
    if len(panier.order) == 0:
        print("Aucun objet dans le panier!")
    else:
        panier.printOrder()

#fonction permettant de checkout les objets (ceux-ci ne reviennent pas dans l'inventaire)
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

def ajouterSecondObjet():
    print("Voulez-vous ajouter un objet a votre panier?")
    print("1- Oui          2-Non")
    try:
        userInput = int(input('Entrez votre choix numerique:'))

        if userInput == 1:
            ajouterObjet()
        elif userInput == 2:
            print("Retour au menu principal")
        else:
            print("Entrez un choix valide!")
            ajouterSecondObjet()
    except ValueError:
        print("Entrez un choix valide!")
        ajouterSecondObjet()


def affichageDesChoix():
    print ("<-------- Menu principal --------->")
    print("Choisir parmi les options suivantes: ")
    print("1 - Trouver un objet")
    print("2 - Ajouter un objet au panier")
    print("3 - Retirer les objets du panier")
    print("4 - Afficher Commande")
    print("5 - Passer la commande")
    print("Quitter en entrant '6'")

    try:
        userInput = int(input('Entrez votre choix:'))

        if (userInput > 0) & (userInput < 6):
            return userInput
        elif userInput == 6:
            return 0
        else:
            print("Entrez un choix valide")
            userInput = affichageDesChoix()
            return userInput
    except ValueError:
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








