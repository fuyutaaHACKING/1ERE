import math
import turtle as t
def formArea(typeOfForm, drawing):
    if typeOfForm == "circle":
        userInput1 = input("Donnez le rayon du cercle:\n>")
        rayon = typeVerificator(userInput1)
        if rayon != None: # si la longueur est un int ou float
            if rayon>0:
                radius = int(rayon)
                circleArea = math.pi * radius ** 2
                print(circleArea)
                if drawing != None: # si drawing est une int ou float (ce qui correspond à Oui dans le menu)
                    drawPolygon(1, radius)
            else:
                print("ERREUR: La longueur est égale à 0, calcul impossible")
                formArea("circle")
        else:
            print("Erreur : La longueur est une valeur invalide.")
            print("Longueur est de type str")
            formArea("circle")

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
    userInput = input("Choissez l'aire que vous souhaitez calculer:\n1: Cercle\n>")
    drawing = input("Désirez vous une représentation graphique ? '1' pour oui / 'a' pour non")
    drawing = typeVerificator(drawing)
    if userInput == "1":
        typeOfForm = "circle"
        formArea(typeOfForm, drawing)
    else:
        print('Choix non valide, retour au menu')
        menu()
    
menu()