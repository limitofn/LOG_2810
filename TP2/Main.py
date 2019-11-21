import FileReader as file
import WordSearch as search
import Order as order

listObject = file.fillArrayFromFile('inventaire.txt')
listeObjectFound = []
print('test')


def trouverItem():
    print("<--------Searching Item--------->")
    search.getInput()
    listeObjectFound = search.Search(listObject)
    print("Les objets trouves sont:")
    i = 0
    while i <= 10 & i<= len(listeObjectFound):
        print("-" + str(listeObjectFound[i]))
        i = i + 1


def ajoutObjet():
    print("<--------Ajout d'un objet--------->")
    if listeObjectFound == None:
        print("Veuillez faire une recherche avant d'ajouter un objet")
    else:
        print("Voici les objets trouver pendant la recherche")
        i = 0
        while i <= 10 & i <= len(listeObjectFound):
            print(str(i) + "- " + str(listeObjectFound[i]))
            i = i + 1
        print("Voulez-vous ajouter un objet a votre panier?")
        print("1- Oui          2-Non")
        userInput = int(input('Entrez votre choix numerique:'))
        if userInput == 1:
            userInput = int(input("Veuillez entre le numero de l'objet:"))
            listObject = order.addObject(listeObjectFound[userInput])
            listeObjectFound.remove(listeObjectFound[i])
        else:
            print("Retour au menu principal")





def prendreChoix():
    return affichageDesChoix()


def affichageDesChoix():
    print("Choisir parmi les options suivantes: ")
    print("1 - Trouver un objet")
    print("2 - Afficher un graphe")
    print("3 - Prendre Commande")
    print("4 - Afficher Commande")
    print("5 - Trouver le plus court chemin")
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
    2: afficherGraphe,
    3: prendreCommande,
    4: afficherCommande,
    5: trouverChemin,
}

def main():
    print("Bienvenue dans la solution du tp1")
    choice = prendreChoix()
    while choice != 0:
        func = switcher.get(choice, lambda: "Entrer un choix valide")
        func()
        choice = prendreChoix()
    print("Fin")


if __name__ == '__main__':
    main()








