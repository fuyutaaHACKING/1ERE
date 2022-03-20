# Les *listes* Python (tableaux dynamiques)
'''
Les listes Pythons peuvent être créées ainsi :
- ma_liste = []
- ma_liste = list()
directement initialisées :
- ma_list = [1 2, 3]
- ma_list = list((1, 2, 3)) #avec un tuple
- ma_list = list([1, 2, 3]) #avec une liste

On retrouve la valeur d'une liste au rang r par
ma_list[r]

'''

#Créez une liste de valeur 1, 2, 3, 4
#Affichez les valeurs de rang 1 et 3

myList = [1,2,3,4]
print(myList[1])
print(myList[2])



#-----------------------------------------------------|-----------------------------------------------------#
############################################################################################################
############################################################################################################
############################################################################################################
#-----------------------------------------------------|-----------------------------------------------------#
'''
Une liste Python est mutable. C'est-a-dire que l'on peut la modifier:
```
ma_liste = [1, 2]
```
- en ajoutant des éléments
```
ma_liste.append(3) ->ma_liste vaut maintenant [1, 2, 3]
```
- en modifiant des elements
```
ma_liste[2] = 4 ->ma_liste vaut maintenant [1, 2, 4]
```
- en suppriment des élements
```
del ma_liste[0] ->ma_liste vaut maintenant [2, 4]
```
'''

def exercice2():
    #Soit la liste suivante:
    ma_liste = [1, 2, 2, 3, 4, 4, 6]
    #ajouter la valeur 7
    ma_liste.append(7)
    print(ma_liste)
    #modifier la 5eme valeur en lui donnant la valeur 5
    ma_liste[5] = 5
    print(ma_liste)
    #supprimer la valeur de rang 1
    del ma_liste[1]
    print(ma_liste)

exercice2()



#-----------------------------------------------------|-----------------------------------------------------#
############################################################################################################
############################################################################################################
############################################################################################################
#-----------------------------------------------------|-----------------------------------------------------#
''''
Les listes peuvent être créée par *compréhension*.
```
ma_liste_par_comprehension = [opération for index in séquence]
ma_liste_par_comprehension = [0 for index in range(5)] #crée une liste de cinq 0
ma_liste_par_comprehension = [index for index in range(5)] #crée une liste des valeurs de 0 à 4
ma_liste_par_comprehension = [index*index for index in range(5)] #crée une liste des valeurs de 0*0 à 4*4
```

Il est possible d'utiliser des conditions
```
ma_liste_par_comprehension = [index for index in range(5) if index%2==0] #crée une liste des valeurs pair entre 0 et 4 inclu
```
'''

#Créez une liste par compréhension des puissances de 2 de 2^0 à 2^7
chiffre = 2
 
puissance = 0
 
resultats = {
        "puissance":[],
        "valeur":[]
        }
 
while puissance != 7:
    puissance += 1
    result = 2**puissance
    resultats["puissance"].append(puissance)
    resultats["valeur"].append(result)
    
print(resultats)



#-----------------------------------------------------|-----------------------------------------------------#
############################################################################################################
############################################################################################################
############################################################################################################
#-----------------------------------------------------|-----------------------------------------------------#
'''
Les listes Python sont itérable. C'est à dire que l'on peut les parcourir directement au sein d'une boucle for.
```
for valeur in ma_liste:
    print(valeur)
```
Ce n'est pas toujours la meilleure manière de faire. Il est possible de parcourir une liste par index:
```
for index in range(len(ma_liste)):
    print(ma_liste[index])
```
'''

#Créez une liste par compréhension de valeur 1 à 9
#Affichez la liste.

#Affichez seulement les valeurs paires

import random

def exercice4():
    ma_liste_2 = [random.randint(-100, 100) for v in range(100)] #créez une liste par compréhension de 100 valeurs aléatoire entre -100 et 100
    #Ecrire une fonction qui prend en paramètre la liste precedente et qui renvoie la somme des éléments
    somme = sum(ma_liste_2)
    #afficher le resultat via une variable
    print(somme)

    #Ecrire une fonction qui prend en paramètre la liste precedente et qui renvoie une liste de la somme cumulée des éléments positifs
    #somme cumulé -> [1, 2, 3, 4] -> [1, 3, 6, 10]
    #afficher le resultat via une variable
def exercice5(list):
    s = 0
    for i in list:
        if i>0:
            s+=i
            print(s)

exercice4()
print("-------------------------------------------------")
exercice5(ma_liste_2)

#Soit la liste suivante:
ma_liste_3 = [0, 1, 2, 3, 4, 5, 3, 6, 7, 8]
#Ecrire une fonction qui affiche les valeurs de la liste tant qu'elles sont croissantes


def returnAscendingList(li):
    return [li[0]] + [j for i, j in zip(li, li[1:]) if i < j]
    # on va créer une copie de la liste qui va contenir les mêmes valeurs mais avec un décalage de 1, prenant la prochaine valeur de la liste 1.
    # on va donc pouvoir comparer la valeur de la liste 1 et de la liste 2 donc si la valeur de la liste 2 est supérieure à la valeur de la liste 1, 
    # donc la prochaine plus sgrande que l'antécédante.
    
    
print(returnAscendingList(ma_liste_3))
#Supprimer l'element qui casse la croissance, et retourner sa valeur.
#à vous
print("------------------")
print(ma_liste_3)
#l'instruction ci-dessus affiche la liste precedente, que remarquez vous ?

# Le 3 en trop est toujours dans la liste? Je ne saisis pas exactement la question ^^'



#-----------------------------------------------------|-----------------------------------------------------#
############################################################################################################
############################################################################################################
############################################################################################################
#-----------------------------------------------------|-----------------------------------------------------#
''''
En Python, les types construits (liste, dictionnaires, p-uplet) sont passé par **référence**. 
Un mot babare pour dire que les modifications faites dans la fonction affecte la valeurs des ces objets en dehors de la fonctions.
'''

#Soit la liste suivante:
ma_liste_4 = [2, 1]
#Ecrire une fonction qui inverse les deux éléments
#à vous
ma_liste_4.reverse()
print(ma_liste_4)

import random # vous avez oublié d'importer la lib random, a moins que cela était volontaire

#Soit la liste suivante:
ma_liste_5 = [random.randint(0,9) for v in range(2)]
#Ecrire une fonction qui inverse les deux éléments de la liste si ceux-ci sont décroissant
#à vous
def returnAscendingList(li):
    if(li[0] > li[1]):
        li.reverse()
        return li
    else:
        return li

print(returnAscendingList(ma_liste_5))

import random

#Soit la liste suivante:
ma_liste_6 = [random.randint(0,9) for v in range(5)]
print(ma_liste_6)
#Ecrire une fonction qui *pour* chaque element de la liste, regarde s'il existe un element dans les elements qui est plus petit.
#si oui, inverse les elements et passe à l'element suivant
#sinon, passe à l'element suivant sans rien faire
#->l'algorithme contient deux boucles for imbriquée
#à vous
def myFunction(li):
    for i in li:
        for n in li:
            if i>n:
                i, n = n, i
                # reverse i and n    

print(myFunction(ma_liste_6))
#que constatez vous ?

print(ma_liste_6)
#que constatez vous ?



