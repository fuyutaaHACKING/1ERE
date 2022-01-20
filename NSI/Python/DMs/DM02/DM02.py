"""""
README :

Le devoir demande de réaliser des fonctions avec userInput intégré dans la fonction de calcul.
Certes, cela fonctionne très bien, mais je tenais à offrir une amélioration du système.

Mon code fonctionnera avec un menu qui appelera en fonction de la figure à calculer, une fonction qui va se charger de prendre les paramètres, 
au lieu de les prendre directement dans le menu ou dans la fonction de calcul.
Cette fonction vérifiera si l'entrée utilisateur est valide, demandera si l'utilisatuer souhaite une représentation graphique
et affichera le résultat (avec représentation ou non grâce à une autre fonction) grâce à une fonction de calcul dédiée, ou sinon redemandera une entrée valide.
"""""

import math
import turtle as t

#formules pour chaque figure
def calcSquare(aSide):
    squareArea = aSide ** 2
    return squareArea

def calcRectangle(wSide, lSide):
    rectArea = lSide * wSide
    return rectArea

def calcTriangle(base, height):
    triangleArea = (base * height) / 2
    return triangleArea

def calcCircle(radius):
    circleArea = math.pi * radius ** 2
    return circleArea

# variable type verificator : vérifie si la variable est int/float ou autre
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

def drawPolygon(numberOfSides, sideLength, form):
    if form == "rectangle":
        t.forward(100)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(100)
        t.right(90)
        t.forward(50)
        t.right(90)
    else:
        if numberOfSides != 1: # si ce n'est pas un cercle
            f = (numberOfSides - 2) * 180 / numberOfSides
            for i in range(numberOfSides):
                t.forward(sideLength)
                t.right(180 - f)
        else:
            t.circle(sideLength)

# cette fonction reçoie un appel avec un paramètre correspondant à la figure qu'on va calculer. Elle sert à prévenir d'une valeur entrée invalide.
# J'ai préféré isoler ce système pour la propreté du code, au lieu de tout mettre dans le menu.
def areaInput(typeOfForm, drawing):
    if typeOfForm == "circle":
        userInput1 = input("Donnez le rayon du cercle:\n>")
        rayon = typeVerificator(userInput1)
        if rayon != None: # si la longueur est un int ou float
            if rayon>0:
                print(calcCircle(rayon))
                if drawing != None: # si drawing est une int ou float (ce qui correspond à Oui dans le menu)
                    drawPolygon(1, rayon, "circle")
            else:
                print("ERREUR: La longueur est égale à 0, calcul impossible")
                areaInput("circle")
        else:
            print("Erreur : La longueur est une valeur invalide.")
            print("Longueur est de type str")
            areaInput("circle")


    if typeOfForm == "rectangle":
        userInput1 = input("Donnez la longueur:\n>")
        userInput2 = input("Donnez la largeur:\n>")

        longueur = typeVerificator(userInput1)
        if longueur != None: # si la longueur est un int ou float
            if longueur>0:
                largeur = typeVerificator(userInput2)
                if largeur != None: # si la largueur est un int ou float
                    if largeur>0:
                        print(calcRectangle(largeur, longueur)) # affichage du résultat
                        if drawing != None: # si drawing est une int ou float (ce qui correspond à Oui dans le menu)
                            drawPolygon(4, longueur, "rectangle")
                    else:
                        print("Erreur : La largeur est égale à 0, calcul impossible")
                        areaInput("rectangle")
                else:
                    print("Erreur : La largeur est une valeur invalide.")
                    print("Largeur est de type str")
                    areaInput("rectangle")
            else:
                print("Erreur : La longueur est égale à 0, calcul impossible")
        else:
            print("Erreur : La longueur est une valeur invalide.")
            print("Longueur est de type str")
            areaInput("rectangle")


    elif typeOfForm == "square":
        userInput1 = input("Donnez la longueur:\n>")
        longueur = typeVerificator(userInput1)
        if longueur != None: # si la longueur est un int ou float
            if longueur>0:
                print(calcSquare(longueur))
                if drawing != None: # si drawing est une int ou float (ce qui correspond à Oui dans le menu)
                    drawPolygon(4, longueur, "square")
            else:
                print("ERREUR: La longueur est égale à 0, calcul impossible")
                areaInput("square")
        else:
            print("Erreur : La longueur est une valeur invalide.")
            print("Longueur est de type str")
            areaInput("square")
        

    elif typeOfForm == "triangle":
        userInput1 = input("Donnez la hauteur:\n>")
        userInput2 = input("Donnez la base:\n>")

        hauteur = typeVerificator(userInput1)
        if hauteur != None: # si la longueur est un int ou float
            if hauteur>0:
                base = typeVerificator(userInput2)
                if base != None: # si la largueur est un int ou float
                    if base>0:
                        print(calcTriangle(base, hauteur)) # affichage du résultat
                        if drawing != None: # si drawing est une int ou float (ce qui correspond à Oui dans le menu)
                            drawPolygon(3, 60, "triangle")
                    else:
                        print("Erreur : La base est égale à 0, calcul impossible")
                else:
                    print("Erreur : La base est une valeur invalide.")
                    print("Largeur est de type str")
                    print(calcTriangle(base, hauteur))
            else:
                print("Erreur : La hauteur est égale à 0, calcul impossible")
        else:
            print("Erreur : La hauteur est une valeur invalide.")
            print("Hauteur est de type str")
            areaInput("triangle")
    
    else:
        print("Aucune formule trouvée, retour au menu")
        menu()

def menu():
    userInput = input("Choissez l'aire que vous souhaitez calculer:\n1: cercle\n2: rectangle\n3: carré\n4: triangle\n>")
    verif = typeVerificator(userInput)

    drawing = input("Désirez vous une représentation graphique ? '1' pour oui / 'a' pour non")
    drawing = typeVerificator(drawing)

    if verif != None:

        userInput = int(userInput)

        if userInput == 1:
            typeOfForm = "circle"
            areaInput(typeOfForm, drawing)

        elif userInput == 2:  
            typeOfForm = "rectangle"
            areaInput(typeOfForm, drawing)

        elif userInput == 3:  
            typeOfForm = "square"
            areaInput(typeOfForm, drawing)

        elif userInput == 4:  
            typeOfForm = "triangle"
            areaInput(typeOfForm, drawing)

        else:
            print('Choix non valide')
    else:
        print("La valeur renseignée n'est pas correcte, veuillez rentrer un indice listé")
        menu()

menu()