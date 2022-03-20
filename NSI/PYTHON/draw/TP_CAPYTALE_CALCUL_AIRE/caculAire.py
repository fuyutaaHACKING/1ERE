'''
# Géométrie
## Calculer l'aire de formes géométriques
Dans ce devoir maison nous allons nous intéresser aux calculs d'aire de 4 formes géométriques:
- le cercle
- le rectangle
- le carré
- le triangle

**Avant toutes choses : Ecrivez vos codes sur papiers, en mode "algorithmique" -> mix mi-programme / mi-phrase en francais, 
afin de poser vos idées et que je comprenne votre démarche**
'''

#-----------------------------------------------------|-----------------------------------------------------#
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
#-----------------------------------------------------|-----------------------------------------------------#
'''
### Le cercle
Ecrivez une fonction qui prend un paramètre et qui renvoie l'aire du cercle.
* Le paramètre doit être de type entier ou flottant, sinon la fonction affiche un message d'erreur et renvoie une valeur d'erreur.
* le paramètre est forcement supérieur à zéro, sinon la fonction affiche un message d'erreur et renvoie une valeur d'erreur.

*Lorsque une fonction renvoie une valeur d'erreur, celle-ci peut-etre utilisée pour informer de l'erreur en question : 
-1 pour une valeur non permise, 
-2 pour un mauvais type, etc. La valeur d'erreur peut tout simplement être **None**.

*La valeur de retour d'une fonction peut influer sur le reste du code. Si le résultat est necessaire pour une éventuelle 
suite d'instructions, mais qu'il ne peut être calculé, l'utilisateur doit pouvoir en être informé. **D'où l'importance des valeurs de retour même en cas d'erreur**.
'''

# Il existe turtle.circle pour le cercle ^^
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



#-----------------------------------------------------|-----------------------------------------------------#
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
#-----------------------------------------------------|-----------------------------------------------------#

'''
### Le rectangle
Ecrivez une fonction qui prend deux paramètres et qui renvoie l'aire du rectangle.
* Les paramètres doivent être de type entier ou flottant, sinon la fonction affiche un message d'erreur et renvoie une valeur d'erreur.
* les paramètres sont forcement supérieurs à zéro, sinon la fonction affiche un message d'erreur et renvoie une valeur d'erreur.
'''

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



#-----------------------------------------------------|-----------------------------------------------------#
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
#-----------------------------------------------------|-----------------------------------------------------#
''''
### Le carré
Ecrivez une fonction qui prend un paramètre et qui renvoie l'aire du carré.
* Le paramètre doit être de type entier ou flottant, sinon la fonction affiche un message d'erreur et renvoie une valeur d'erreur.
* le paramètre est forcement supérieur à zéro, sinon la fonction affiche un message d'erreur et renvoie une valeur d'erreur.

*TIPS: qu'est-ce qu'un carré ?*
'''

import math
import turtle as t

def formArea(typeOfForm, drawing):
    if typeOfForm == "square":
        userInput1 = input("Donnez la longueur:\n>")
        longueur = typeVerificator(userInput1)
        if longueur != None: # si la longueur est un int ou float
            if longueur>0:
                squareArea = longueur * longueur
                print(squareArea)
                if drawing != None: # si drawing est une int ou float (ce qui correspond à Oui dans le menu)
                    drawPolygon(4, longueur)
            else:
                print("ERREUR: La longueur est égale à 0, calcul impossible")
                formArea("square")
        else:
            print("Erreur : La longueur est une valeur invalide.")
            print("Longueur est de type str")
            formArea("square")

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
    userInput = input("Choissez l'aire que vous souhaitez calculer:\n1: Carré\n>")
    drawing = input("Désirez vous une représentation graphique ? '1' pour oui / 'a' pour non")
    drawing = typeVerificator(drawing)
    if userInput == "1":
        typeOfForm = "square"
        formArea(typeOfForm, drawing)
    else:
        print('Choix non valide, retour au menu')
        menu()
    
menu()



#-----------------------------------------------------|-----------------------------------------------------#
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
#-----------------------------------------------------|-----------------------------------------------------#
'''
### Le triangle
Ecrivez une fonction qui prend deux paramètres et qui renvoie l'aire du triangle.
* Les paramètres doivent être de type entier ou flottant, sinon la fonction affiche un message d'erreur et renvoie une valeur d'erreur.
* les paramètres sont forcement supérieurs à zéro, sinon la fonction affiche un message d'erreur et renvoie une valeur d'erreur.
'''

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




#-----------------------------------------------------|-----------------------------------------------------#
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
#-----------------------------------------------------|-----------------------------------------------------#
'''
## Dessiner
La bibliothèque Tutle permet de dessiner de manière relativement simple. Vous l'avez utilisez pour dessiner un carré dans l'activité Turtle.

Modifiez les fonctions précédentes en leur ajoutant un paramètre de type booléen. Si ce paramètre est vrai (True), la fonction dessinera sa forme (cercle, rectanle ...).

**Pour le cercle :** Il sera dessiné en utilisant les instructions forward(0.5) et right avec un angle de 1°.
'''

'''
## Faire un menu
En utilisant les instructions conditionnelles faites un menu qui permet à un utilisateur de calculer l'aire 
de la forme qu'il veut, et s'il veut ou non l'affichage de la forme en question. Vous pourrez vous inspirer du code suivant:
'''

#Ce bout de code n'est qu'un exemple et n'est pas complet: par exemple, il n'y pas de test sur les opérands.
user_input = input('Choisissez une opération:\n1: addition\n2: négation\n>') # Demande un saisie utilisateur pour le choix de l'opération
user_input_int = int(user_input)                                             # Converti l'entré utilisateur de caractère à entier
if user_input_int == 1:                                                      # Condition si choix 1
    user_operand_1 = input('1ere operand: ')                                 #
    user_operand_1_int = int(user_operand_1)                                 # Choix des opérands
    user_operand_2 = input('2nd operand: ')                                  #
    user_operand_2_int = int(user_operand_2)                                 #
    result = user_operand_1_int + user_operand_2_int                         # Calcul de l'opération d'addition
    print(result)                                                            # Affiche le resultat à l'écran
elif user_input_int == 2:                                                    # Condition si choix 2
    user_operand = input('operand: ')                                        #
    user_operand_int = int(user_operand)                                     #
    result = -1 * user_operand_int                                           # Calcul de la négation
    print(result)                                                            # Affichage du résultat à l'écran
else:                                                                        # Condition par défaut
    print('Choix non valide')



#-----------------------------------+-------------------------------------



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



'''
## hors barème
Modifiez votre menu pour qu'il propose à l'utilisateur de calculer une aire *tant que ce dernier ne saisie pas le caractère 'q'* (pour quit). 
Vous aurez pour cela besoin d'utiliser une boucle **while**
'''