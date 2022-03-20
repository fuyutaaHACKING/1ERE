## Les dictionnaires Python : Une implémentations des table de hashage 

#Les dictionnaires Python sont mutable, c'est à dire modifiable.
# Le principe est de pouvoir recupérer une valeur contenu dans la variable de stockage non plus par un index (cas des listes), 
# mais par une clé. Une clé étant une valeure unique.

mon_1er_dict = {'clef_1':'valeur_1', 'clef_2':'valeur_2'}
la_valeur_1 = mon_1er_dict['clef_1']
la_valeur_2 = mon_1er_dict['clef_2']

print('valeur 1 : ', la_valeur_1)
print('valeur 2 : ', la_valeur_2)

#Les clés et valeurs peuvent être de n'importe quel type. L'important est qu'une clé doit être unique.

#Créer un dictionnaire avec les clés 'un', 'deux', 'trois' et les valeurs 1, 2, 3
#Affichez les valeurs du dictionnaire en utilisant les clés.
#Let's do it:

#Créer un dictionnaire avec les clés 1, 2, 3 et les valeurs 'un', 'deux', 'trois'
#Affichez les valeurs du dictionnaire en utilisant les clés.
#Let's do it:

mon_1er_dict = {'1':'un', '2':'deux', '3':'trois'}
print(mon_1er_dict['1'])
print(mon_1er_dict['2'])
print(mon_1er_dict['3'])

'''
Les dictionnaires sont itérables. C'est à dire que l'on peut itérer, boucler sur leurs valeurs directement comme les listes, à ceci près que les dictinnaires ont des clés et des valeurs alors que les listes n'ont que des valeurs:
###### itérer sur les clés

for clef in dictionnaire.keys():
    ...

ou simplement

for clef in dictionnaire:
    ...

###### itérer sur les valeurs

for valeur in dictionnaire.values():
    ...

###### itérer sur les deux à la fois

for clef, valeur in dictionnaire.items():
    ...
'''

mon_dict = {'a':'abeille', 'b':'biberon','c':'chataigne','d':'dolmen'}
#affichez les clefs du dictionnaire
for key in mon_dict.keys():
    print(key)
print("----------------")
#affichez les valeurs du dictionnaire
for value in mon_dict.values():
    print(value)
# OU ALORS:
print(mon_dict['a'], mon_dict['b'], mon_dict['c'], mon_dict['d'])
print("----------------")
#affichez les clefs et valeurs du dictionnaire sous la forme clef -> valeur
for item in mon_dict.items():
    print(item)

'''
Si vous utilisez une clé qui n'existe pas, Python va retourner une erreur. Hors, dans certaines applications, un annuaire par exemple, vous pourriez être ammené à chercher un nom qui peut ne pas exister (non inséré). Pour cela on peut utliser la méthode *get*
```
mon_dict.get(clef, 'valeur_de_retour_si_existe_pas')
```
'''

#Soit le dictionnaire
mon_dico = {'agneau':'bébé mouton','baleineau':'bébé baleine','chiot':'bébé chien', 'dindonneau':'bébé dinde'}
#Cherchez 'chiot' et 'chaton', si la clef n'existe pas, renvoyer None, affichez le resultat

# fonction qui va prendre en param une valeur de clé pour chercher la def, et le dictionnaire en question
def searchForDefinition(keySearched:str, dic:list):
    if keySearched in dic:
        print(dic[keySearched])
    else:
        print("Aucune définition de cette clé ne figure dans le dictionnaire utilisé.")
    
print("Pour 'chiot' dans le dictionnaire:")
searchForDefinition("chiot", mon_dico)
print("------------------------")
print("Pour 'chaton' dans le dictionnaire:")
searchForDefinition("chaton", mon_dico)

'''
Un dictionnaire est mutable, c'est-à-dire qu'il est modifiable après création.
Nous pouvons donc :
- ajouter une nouvelle valeur
- modifier une valeur existante

La syntaxe est la même:
'''
mon_dic = {'un':1, 'deux':2, 'trois':4}
mon_dic['quatre'] = 4 #Ajoute le couple clé:valeur 'quatre':4 au dictionnaire
mon_dic['trois'] = 3  #Modifie le couple clé:valeur 'trois':4 à 'trois':3 du dictionnaire

#Il n'y avait pas de dictionnaire fourni, disons alors que le dictionnaire de base est celui-ci:
mon_dic = {}
mon_dic["dindonneau"] = "bébé dinde"

#Ajoutez le couple Éléphant : éléphanteau
mon_dic["Éléphant"] = "éléphanteau"
#Modifiez le couple 'dindonneau':'bébé dinde' vers 'dindonneau':'bébé dindonneau'
mon_dic['dindonneau'] = "bébé dindonneau" 

print(mon_dic)

'''
La caractéristisque mutable du dictionnaire permet de pouvoir d'en supprimer des élements. La syntaxe est la même que pour les liste:
```
del mon_dico[clef]
```
'''

#Supprimez du dictionnaire mon_dico le couple qui vous chante ...
mon_dic = {'un':1, 'deux':2, 'trois':4}

del mon_dic['un']
print(mon_dic)





