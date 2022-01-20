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
                # reverse i and n

        

print(myFunction(ma_liste_6))
#que constatez vous ?