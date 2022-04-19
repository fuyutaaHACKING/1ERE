import turtle as t

def drawPolygon():
    numberOfSides = int(input("Enter the number of sides."))
    sideLength = int(input("Enter a the length of a side."))
    f = (numberOfSides - 2) * 180 / numberOfSides
    for i in range(numberOfSides):
        t.forward(sideLength)
        t.right(180 - f)

if True:
    drawPolygon()

'''
ORIGINAL CODE :

import turtle           #importation de la bibliotheque turtle
turtle.hideturtle()     #cache la petite tortue

turtle.forward(15)      #dessine un trait de longueur 15
turtle.right(90)        #tourne par la droite de 90 degrés
turtle.forward(15)
turtle.right(90)
turtle.forward(15)
turtle.right(90)
turtle.forward(15)
turtle.right(90)

turtle.done()           #fin de la session de dessin
'''

'''
le code ne semble pas fonctionner dans Basthon, pourtant il fonctionne bien dans
PyCharm 2020.3.3
'''
