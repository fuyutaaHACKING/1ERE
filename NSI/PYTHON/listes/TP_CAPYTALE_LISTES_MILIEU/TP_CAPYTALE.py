'''
import random
interval = [random.randint(0, 9) for x in range(2)]
if interval[0] > interval[1]:
    interval[0], interval[1] = interval[1], interval[0]

debut = interval[0] #une valeur
fin = interval[1] #une valeur superieur au debut
milieu = (value[0] + value[1])/2 
print(milieu)
'''

def calcMiddle(liste):
    middle = int((len(liste)/2) - 0.5)
    if len(liste)%2 != 0:
        return liste[middle]
    else:
        return int((liste[middle] + liste[middle + 1])/2)

        

# réponses
print("Milieu de l'intervalle 0,4:", calcMiddle([0,4]))
print("-----------------------------------")
print("Milieu de l'intervalle 4,8:", calcMiddle([4,8]))
print("-----------------------------------")

# Pour la liste [0,5], le millieu sera 5/2 = 2.5 
# Le problème étant qu'on ne peut utiliser un index correspondant à un flottant, on va donc devoir utiliser une médiane
# issue d'une fonction qui supporte le calcul d'une médiane avec une fonction impaire