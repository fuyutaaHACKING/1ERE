from math import sqrt

def pythagore():
    formula = input("Choisissez un côté entre 'a' (adjacent ou opposé), 'c' (hypothénuse)")

    if formula == "c":
        side_a = int(input("Entrez la longueur du 1er côté"))
        side_b = int(input("Entrez la longueur du 2eme côté"))

        side_c = sqrt(side_a * side_a + side_b * side_b)
        
        print("La longueur de l'hypothénuse est : ")
        print(side_c)

    elif formula == "a":
        side_b = int(input("Entrez la longueur du côté non hypothénuse"))
        side_c = int(input("Entrez la longueur du côté étant l'hypothénuse"))
        
        side_a = sqrt((side_c * side_c) - (side_b * side_b))
        
        print("La longueur du côté manquant est : ")
        print(side_a)

    else:
        print("Incorrect. Choisissez un côté entre 'a' (adjacent ou opposé), 'c' (hypothénuse)")