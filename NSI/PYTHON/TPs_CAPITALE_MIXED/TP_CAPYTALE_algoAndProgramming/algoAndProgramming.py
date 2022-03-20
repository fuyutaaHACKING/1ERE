#-----------------------------------------------------|-----------------------------------------------------#
#créer et affecter une variable *mon_entier* de type entière
#à vous
mon_entier = int()
#L'instruction suivante test votre variable
assert isinstance(mon_entier, int), "mon_entier n'est pas un entier"

#créer et affecter une variable *mon_flottant* de type flottant
#à vous
mon_flottant = float()
#L'instruction suivante test votre variable
assert isinstance(mon_entier, float), "mon_entier n'est pas un flottant"

#créer et affecter une variable *ma_chaine* de type chaine de caractere
#à vous
ma_chaine = []
#L'instruction suivante test votre variable
assert isinstance(mon_entier, str), "mon_entier n'est pas une chaine de caractère"

#d'après le test suivant, créer la variable de type attendu
#à vous
quel_type = float()
#test à analyser
assert isinstance(quel_type, float), "quel_type n'est pas un flottant"
#-----------------------------------------------------|-----------------------------------------------------#
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
#-----------------------------------------------------|-----------------------------------------------------#
#INSTRUCTIONS CONDITIONNELLES
'''
Les valeurs utilées pour la suite sont créées dans la cellule suivante. Pour y avoir accès vous devez "executer" la cellule en utilisant le bouton "run" lorsque qu'elle est active (le curseur de texte est dans cette cellule).

Vous pouvez modifier les valeurs, mais pour que la modification soit prise en compte, vous devrez ré-executer la cellule.
'''
valeur_1 = -9
valeur_2 = 7
'''
Les opérateurs de condition sont les suivants:
* égalité: ==
* différence: !=
* supériorité strict: >
* infériorité strict: <
* supériorité ou égalité: >=
* infériorité ou égalité: <=
'''

#Tester si valeur_1 est supérieur à zéro
#- afficher "valeur_1 supérieur à 0" si c'est la cas, 
#- "valeur_1 inférieur ou égale à 0" dans le cas contraire

#à vous:
valeur_1 = 5
if valeur_1 > 0:
    print("valeur_1 supérieur à 0")
else:
    print("valeur_1 inférieur ou égale à 0")

#Tester si valeur_1 est supérieur à zéro, si ce n'st pas le cas, tester si valeur_2 est supérieur à valeur_1
#- afficher "valeur_1 supérieur à 0" si c'est la cas, 
#- afficher "valeur_2 inférieur à valeur_1" si c'est la cas, 
#-"valeur_1 inférieur ou égale à 0 et valeur_2 inférieur à valeur_1" dans le cas contraire

#à vous
value_1 = 5
value_2 = 7
if value_1 > 0:
    print("valeur_1 superior to 0")
elif value_2 > value_1:
    print("value_1 is superior to 0")
else:
    print("valeur_1 is equal to 0")

'''
Les *conditions* peuvent etre composées de plusieurs opérations de condition en utlisant les mots réservés:
* and
* or
* ^ (xor)
'''

#Tester si valeur_1 est inférieure à 0 ET valeur_2 supérieure à 0
#afficher "valeur_1 inférieure à 0 et valeur_2 supérieure à 0"
#valeur_1 supérieure à 0 et/ou valeur_2 inférieure à 0, sinon

#à vous
if value_1 < 0 and value_2 > 0:
    print("value_1 inferior to 0 and value_2 superior to 0")
if value_1 > 0:
    print("value_1 superior to 0")
if value_2 < 0:
    print("value_2 inferior to 0")
#-----------------------------------------------------|-----------------------------------------------------#
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
#-----------------------------------------------------|-----------------------------------------------------#

'''
## Boucles bornées

Les boucles bornées Python sont représenté par le mot clé **for**, la structure étant:

*for* une_variable *in* séquence

* séquence peut etre "remplacé" par range(début, stop, pas)
* séquence peut etre "remplacé" par un type itérable: liste, p-uplet, chaine de caractère, dictionnaire
'''

#-------------------------------------------------
#Ecrire une boucle qui affiche les valeurs de 0 à 5
#à vous
for n in range(0, 6, 1):
    print(n)

#-------------------------------------------------
#Ecrire une boucle qui affiche les valeurs de 1 à 13 par pas de 3
#à vous
for n in range(1, 14, 3):
    print(n)

#-------------------------------------------------
#soit la liste
ma_liste = [2, 4, 6, 8]
#ecrire une boucle qui affiche les elements de ma_liste
#à vous
for element in ma_liste:
    print(element)

#-------------------------------------------------
#soit la chaine de caractères:
ma_chaine = 'abc'
#ecrire une boucle qui affiche les elements de ma_chaine
#à vous
for element in ma_chaine:
    print(element)

#soit la chaine de caractères:

ma_2nd_chaine = 'abcdefghijklmnopqrstuvwxyz'
#ecrire une boucle qui affiche de la 10eme à la 15eme lettre de l'alphabets
#à vous
for n in range(0,16,1):
    n+=1
    if(n > 9 and n <15):
        print(ma_2nd_chaine[n])



#-----------------------------------------------------|-----------------------------------------------------#
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
#-----------------------------------------------------|-----------------------------------------------------#

## Boucles non bornées ou boucles conditionnelles
'''
Les boucles conditionnelles sont représentées en *Python* par le mot clé **while**:

while *condition(s)*:

La condition ou l'ensemble de conditions sont écrits de la meme manière que pour les instructions conditionnelles.

**Attention :** Contrairement aux boucles bornées, une boucle non bornée peut *tournée* indéfiniment. Faites attention à ce que la condition d'arret soit toujours atteignable.
'''

#-------------------------------------------------
#l'algorithme suivant calcul le plus grand diviseur commun de a et b avec a > b >= 0.
#L'alorithme s'arrète lorsque b est nul. Remplacer les ... par la condition de boucle.
a = 12
b = 11
while b==None:
    a, b = b, a%b
print(a)

#-------------------------------------------------
#Soit la variable suivante :
my_variable = 10
#En utilisant une boucle conditionnelle, afficher le compte à rebours: 10, 9, 8 ..., 1, 0

print(my_variable) # print the '10' (=content)
while(my_variable != 0):
    my_variable -= 1
    print(my_variable)

