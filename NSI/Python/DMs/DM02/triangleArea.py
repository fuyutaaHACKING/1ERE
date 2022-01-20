import math
import turtle as t

def formArea(typeOfForm, drawing):
    if typeOfForm == "triangle":
        userInput1 = input("Donnez la hauteur:\n>")
        userInput2 = input("Donnez la base:\n>")

        hauteur = typeVerificator(userInput1)
        if hauteur != None: # si la longueur est un int ou float
            if hauteur>0:
                base = typeVerificator(userInput2)
                if base != None: # si la largueur est un int ou float
                    if base>0:
                        triangleArea = (base * hauteur) / 2
                        print(triangleArea) # affichage du résultat
                        if drawing != None: # si drawing est une int ou float (ce qui correspond à Oui dans le menu)
                            drawPolygon(3, 60)
                    else:
                        print("Erreur : La base est égale à 0, calcul impossible")
                else:
                    print("Erreur : La base est une valeur invalide.")
                    print("Largeur est de type str")
                    formArea("rectangle")
            else:
                print("Erreur : La hauteur est égale à 0, calcul impossible")
        else:
            print("Erreur : La hauteur est une valeur invalide.")
            print("Hauteur est de type str")
            formArea("triangle")

    else:
        print("Aucun calculateur de cette figure n'a été trouvé.\n>")


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

def drawPolygon(numberOfSides, sideLength):
    if numberOfSides != 1: # si ce n'est pas un cercle
        f = (numberOfSides - 2) * 180 / numberOfSides
        for i in range(numberOfSides):
            t.forward(sideLength)
            t.right(180 - f)
    else:
        t.circle(sideLength)

#Menu
def menu():
    userInput = input("Choissez l'aire que vous souhaitez calculer:\n1: Triangle\n>")
    drawing = input("Désirez vous une représentation graphique ? '1' pour oui / 'a' pour non")
    drawing = typeVerificator(drawing)
    if userInput == "1":
        typeOfForm = "triangle"
        formArea(typeOfForm, drawing)
    else:
        print('Choix non valide, retour au menu')
        menu()
    
menu()