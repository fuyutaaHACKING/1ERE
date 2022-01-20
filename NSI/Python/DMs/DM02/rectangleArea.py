import math
import turtle as t
def formArea(typeOfForm, drawing):
    if typeOfForm == "rectangle":
        userInput1 = input("Donnez la longueur:\n>")
        userInput2 = input("Donnez la largeur:\n>")

        longueur = typeVerificator(userInput1)
        if longueur != None: # si la longueur est un int ou float
            if longueur>0:
                largeur = typeVerificator(userInput2)
                if largeur != None: # si la largueur est un int ou float
                    if largeur>0:
                        rectangleArea = longueur * largeur
                        print(rectangleArea) # affichage du résultat
                        if drawing != None: # si drawing est une int ou float (ce qui correspond à Oui dans le menu)
                            drawPolygon(4, longueur, largeur)
                    else:
                        print("Erreur : La largeur est égale à 0, calcul impossible")
                        formArea("rectangle")
                else:
                    print("Erreur : La largeur est une valeur invalide.")
                    print("Largeur est de type str")
                    formArea("rectangle")
            else:
                print("Erreur : La longueur est égale à 0, calcul impossible")
        else:
            print("Erreur : La longueur est une valeur invalide.")
            print("Longueur est de type str")
            formArea("rectangle")

    else:
        print("Aucun calculateur de cette figure n'a été trouvé.")


# variable type verificator
def typeVerificator(val):
    try:
        val = float(val) # teste si la valeur est convertissable en float
        return val
    except ValueError:
        try:
            val = int(val) # teste si la valeur est convertissable en int
            return val
        except ValueError: # la valeur ne peut ni être int ou float
            return None # la valeur n'est ni int, ni float


def drawPolygon(numberOfSides, longueur, largeur):
    t.forward(longueur)
    t.right(90)
    t.forward(largeur)
    t.right(90)
    t.forward(longueur)
    t.right(90)
    t.forward(largeur)
    t.right(90)


#Menu
def menu():
    userInput = input("Choissez l'aire que vous souhaitez calculer:\n1: Rectangle\n>")
    drawing = input("Désirez vous une représentation graphique ? '1' pour oui / 'a' pour non")
    drawing = typeVerificator(drawing)
    if userInput == "1":
        typeOfForm = "rectangle"
        formArea(typeOfForm, drawing)
    else:
        print('Choix non valide, retour au menu')
        menu()
    
menu()