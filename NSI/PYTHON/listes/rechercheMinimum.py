# tri par selection, fonction basique
'''
def recherche_minimum(liste, debut):
    for i in range(len(liste)):
        for j in range(debut, len(liste)):
            if liste[j-1] > liste[j]:
                liste[j-1], liste[j] = liste[j], liste[j-1]
    return liste

listOfValues = [8,1,5,6,2]
print(recherche_minimum(listOfValues, 1))
'''

# Devoir demandé: fonction qui renvoie la valeur minimale de la liste

def recherche_minimum(liste, debut):
    for i in range(len(liste)):
        for j in range(debut, len(liste)):
            if liste[j-1] > liste[j]:
                liste[j-1], liste[j] = liste[j], liste[j-1]
    return liste[0]

listOfValues = [8,1,5,6,2]
print("La valeur la plus petite de la liste est:",recherche_minimum(listOfValues, 1))