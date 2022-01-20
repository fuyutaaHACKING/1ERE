import turtle as t

def drawPolygon():
    n = int(input("Enter a value"))
    l = int(input("Enter a value"))
    f = (n - 2) * 180/n
    for i in range(n):
        t.forward(l)
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