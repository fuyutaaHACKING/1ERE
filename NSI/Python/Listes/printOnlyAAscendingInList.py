#Ecrire une fonction qui affiche les valeurs de la liste tant qu'elles sont croissantes
ma_liste_3 = [0, 1, 2, 3, 4, 5, 3, 6, 7, 8]

'''
def exercice6():
    ma_liste_3 = [0, 1, 2, 3, 4, 5, 3, 6, 7, 8]
    for i in ma_liste_3:
        if i > ma_liste_3[i-1]:
            print(i)
    print("-----------------")
    print(ma_liste_3[3])
    print(ma_liste_3[3-1])
'''


def ascendingList(list):
    previous = list[0] # on définie une valeur contenant l'élément précédent
    for n in list: # pour chaque élément dans la liste:
        if n < previous: # si l'élément est inférieur à celui précédent
            ma_liste_3.remove(ma_liste_3[n]) # on retire l'élément
        previous = n
    print(list)

li = [2,4,3,5,6,8]
def returnAscendingList(li):
    return [li[0]] + [j for i, j in zip(li, li[1:]) if i < j]
    # on va créer une copie de la liste qui va contenir les mêmes valeurs mais avec un décalage de 1, prenant la prochaine valeur de la liste 1.
    # on va donc pouvoir comparer la valeur de la liste 1 et de la liste 2 donc si la valeur de la liste 2 est supérieure à la valeur de la liste 1, 
    # donc la prochaine plus sgrande que l'antécédante.

print(eliminate(li))
print("-----------------------------")
print(eliminate2(li))
print("-----------------------------")
ascendingList(ma_liste_3)