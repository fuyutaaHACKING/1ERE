## Manipulation de tables
'''
Le but de ce chapitre est d'introduire la manipulation de donnees en traitant des fichiers csv.
Le fichier csv que nous allons utiliser est : **countries.csv**
'''

lines = []                                         #1 
head = None                                        #-
with open('emissions_co2-tonne.csv', 'r') as csv : #2
    head = csv.readline()                          #3
    head = head.rstrip('\n')                       #4
    line = head                                    #5
    head = head.split(';')                         #6
    while line :                                   #7
        line = csv.readline().rstrip('\n')         #8
        if line :                                  #9
            columns = line.split(';')              #10
            lines.append(columns)                  #11

#1. A quoi sert lines ? Qu'est-ce que "[]" ? Pouvez-t-on le declarer apres with... ?
'''
    - Lines va être une liste de listes, une liste contenant chaque ligne de notre fichier séparée.
    - "[]" va servir à déclarer le type de notre variable en tant que liste
    - On ne pourrit pas le déclarer après with car woth va correspondre à une loop qui reset lines à chaque fois sinon. En +, on serait out of scope dans certaines situations.
'''
#2. Le nom de fichier est-il le bon ? Qu'est-ce que 'r' ? A quoi correspond csv ?
'''
    - Non, il est écrit dans le script "emissions_co2-tonne.csv" au lieu du nom "countries.csv".
    - "r" correspond au mode ouverture de fichier, r correspondant alors au "read" (=lecture).
    - csv va être l'extension de notre fichier. un .csv est fichier dit "Comma-separated values", qui est un texte de valeurs délimitées par des points virgules (commas).
'''
#3. Que fait readline?
'''
    - readline va faire, explicitement, la lecture de la ligne du fichier ouvert en tant que "csv"
'''
#4. Que fait rstrip() ?
'''
    - rstrip permets de retirer les caractères de retour à la ligne
'''
#5. *Pourquoi affecter head a line ? Pouvait-on ecrire line = None pour simplement declarer line ?* 
'''
    - head va contenir la ligne lue, et va passer dans rstrip, et une fois "propre" on va pouvoir affecter à line.
'''
#6. A quoi correspond le split(';') ?
'''
    - Split va servir à séparer chaque élement lu en un élément de liste distinct dans une même liste.
'''
#9. Que fait cette ligne ?
'''
    - on vérifie qu'il y a bien une ligne avant de faire toute opération afin d'éviter une erreur. on aurait pu sinon faire "if not line".
'''
#11. Que fait cette ligne ?
'''
    - Cette ligne va ajouter à notre liste de listes, la ligne lue une fois formattée, où chaque élément est séparé
'''
#12. Apres execution du code *corrige*, que contient lines ? head ?
'''
    - Lines va contenir comme prévu, une liste contenant chaque ligne du tableur en listes distinctes, dont les diverses valeurs sont séparées.
    - Head contient alors rien.
'''


'''
#### Rappel
Nous pouvons acceder aux elements d'une liste python en utlisant leur index :
````
ma_liste = ['un', 'deux', 'trois']
valeur = ma_liste[1]
````
- *Que contient valeur ?*
valeur = deux
````
'''

ma_liste = ['un', 'deux', 'trois']
valeur = ma_liste[1]
print('La bonne reponse est : ', valeur)

'''
Valeur contiendra alors "deux"
'''

'''
Il arrive que nous voulions trouver l'index d'une valeur specifique. Pour cela il faut **tester chaque element** de la liste pour voir s'il correspond a la valeur chercher. **Si oui**, l'index est stocke dans une variable.

Pour tester chaque element, 
- nous pouvons iterer sur tous les elements de la liste en utilisant une boucle bornee,
- tester si la valeur de l'element correspond a la valeur cherchee en utilisant une instruction conditionnelle.
'''

for index in range(len(ma_liste)) :       #1 On va répéter la boucle jusqu'à ce que toutes les valeurs de la ligne soient lues. len retourne le nombre d'items dans une liste et on va donc boucler sur len pour passer sur chaque élément et effectuer nos opérations par la suite dessus
    print(index, ' -> ', ma_liste[index]) #2 L'index va être le nombre incrémenté à chaque bouclage de boucle et par cela, l'index de la valeur dans la liste, la position dans la liste de l'élément exprimée par index.
    if ma_liste[index] == 'trois' :       #3 On possède donc un index correspondant à la valeur ) tester, et on va aller chercher cette valeur avec ma_liste[index] puis la comparer à la valeur cherchée "trois" par l'écriture == "trois"
        print('Nous irons au bois.')      #4 Si l'index est correspondant à la valeur cherchée, alors ce message s'affiche. On suppose alors un dé jeté, et si la valeur est 3 alors ils "iront au bois".

'''
1. *Que fait cette ligne ?*
2. *A quoi correspond index ? ma_liste\[index\] ?*
3. *Que fait cette ligne ?*
'''

#**Stockez dans la variable *index_population* l'index de l'element de la liste *head* qui a pour valeur 'Population'**

lines = []                                         #1 
head = None                                        #-
index_population = 5
with open('countries.csv', 'r') as csv : 
    head = csv.readline()                          #3
    head = head.rstrip('\n')                       #4
    line = head                                    #5
    head = head.split(';')                         #6
    while line :                                   #7
        line = csv.readline().rstrip('\n')         #8
        if line :                                  #9
            columns = line.split(';')              #10
            lines.append(columns)                  #11

print(head[index_population])
print(head)

        
        

#BONUS A IGNORER
# nous n'avons pas de moyen de déduire quel champ va t-on chercher pour avoir une possible population.
# On suppose que l'on sait que c'est l'avant dernier.
# on crée un convertisseur de liste qui cherche la plus grande val

'''
lineNumber = int(input("entrez un numéro de ligne"))

numbers = []
line1 = lines[lineNumber]

for item in line1:
    try:
        numbers.append(int(item))
    except ValueError:
        pass # ignore les non-int

population = max(numbers)
print(population)
'''

'''
Une liste peut contenir des listes, c'est une liste de liste.
'''
liste_de_liste = [['un', 'deux', 'trois'], ['quatre', 'cinq', 'six'], ['sept', 'huit', 'neuf']]
valeur_1 = liste_de_liste[1]
valeur_2 = valeur_1[2]
valeur_3 = liste_de_liste[1][2]
'''
1. *Que contiennent les variables valeur_1, valeur_2 et valeur_3 ?*
    - reponse pour la valeur 1: ['quatre', 'cinq', 'six']
    - reponse pour la valeur 2: six
    - reponse pour la valeur 3:  six
2. *valeur_1 et valeur_3 sont-elles egale ?*
   Valeur_1 et valeur_3 ne sont pas égales
'''

liste_de_liste = [['un', 'deux', 'trois'], ['quatre', 'cinq', 'six'], ['sept', 'huit', 'neuf']]
valeur_1 = liste_de_liste[1]
valeur_2 = valeur_1[2]
valeur_3 = liste_de_liste[1][2]
print('reponse pour la valeur 1: ', valeur_1)
print('reponse pour la valeur 2:', valeur_2)
print('reponse pour la valeur 3: ', valeur_3)
if valeur_1 == valeur_3 :
    print('Les valeurs sont egales, ceuillons des cerises')
else:
    print('Les valeurs sont differentes')

#**Cherchez dans la liste *lines* s'il existe un pays qui a une population de *66987244* habitants. 
# Attention, les valeurs dans la liste *lines* sont toutes des chaines de caractere**

#Pour cela vous devrez iterer sur toute la liste *lines*, pour chaque element vous regarderez la valeur contenu a l'index de la valeur 'Population'

lines = []                                         #1 
head = None                                        #-
index_population = 5
with open('countries.csv', 'r') as csv : 
    head = csv.readline()                          #3
    head = head.rstrip('\n')                       #4
    line = head                                    #5
    head = head.split(';')                         #6
    while line :                                   #7
        line = csv.readline().rstrip('\n')         #8
        if line :                                  #9
            columns = line.split(';')              #10
            lines.append(columns)                  #11
            

            #works fine for any value except france'

  ###############################
 ##########SEARCHER 1.0#########
##############################  
searchedElement = "66987244"
  
res1 = any(searchedElement in sublist for sublist in lines)

print("searcher 1.0 results:")
print(str(res1))

  ###############################
 ##########SEARCHER 2.0#########
##############################
searchedElement = "66987244"
def searcher():
    for list in lines:
        for element in list:
            if element==searchedElement:
                return True

isElementInList = searcher()

print("searcher 2.0 results:")
print(isElementInList)
    


#**Stockez dans la variable *index_pays* l'index de l'element de la liste *head* qui a pour valeur 'Country'**

lines = []                                         #1 
head = None                                        #-
index_population = 5
index_pays = 2
with open('countries.csv', 'r') as csv : 
    head = csv.readline()                          #3
    head = head.rstrip('\n')                       #4
    line = head                                    #5
    head = head.split(';')                         #6
    while line :                                   #7
        line = csv.readline().rstrip('\n')         #8
        if line :                                  #9
            columns = line.split(';')              #10
            lines.append(columns)                  #11

print(head[index_population])
print(head[index_pays])
print(head)


#**Cherchez dans la liste *lines* le nom du pays qui a une population de *547030.0* habitants. Attention, les valeurs dans la liste *lines* sont toutes des chaines de caractere**

lines = []                                         #1 
head = None                                        #-
index_population = 5
index_pays = 2
with open('countries.csv', 'r') as csv : 
    head = csv.readline()                          #3
    head = head.rstrip('\n')                       #4
    line = head                                    #5
    head = head.split(';')                         #6
    while line :                                   #7
        line = csv.readline().rstrip('\n')         #8
        if line :                                  #9
            columns = line.split(';')              #10
            lines.append(columns)                  #11

print(head[index_population])
print(head[index_pays])
print(head)


'''
**Comparez les deux listes suivantes :**
une_liste = [2, 5, 1, 7, 4, 8]
une_autre_liste_pas_si_differente = sorted(une_liste)
'''

une_liste = [2, 5, 1, 7, 4, 8]
une_autre_liste_pas_si_differente = sorted(une_liste)

print(une_liste)
print(une_autre_liste_pas_si_differente)

# sorted permets de trier les valeurs dans l'ordre croissant.

'''
**En testant *sorted* sur la liste *lines*, dites sur quelle element s'applique *sorted* par defaut ?**
'''

linesSorted = sorted(lines)

print(linesSorted)

# la valeur par défaut est "numeric"
'''
***No panic*** : 
*sorted* peut s'appliquer sur d'autre elements d'une liste de liste en lui donnant pour parametre *key* une fonction :
'''
index = 4
def critere(ligne):
    return ligne[index]
resultat = sorted(lines, key=critere)

#**Sur quel critere (son nom) est affectee la liste *lines* ?**

index = 4
def critere(ligne):
    return ligne[index]
resultat = sorted(lines, key=critere)

print(lines)
print('---------------------------------------')
print(resultat)
print('---------------------------------------')
print(head)
print('---------------------------------------')

# Sur le critère area.
'''
**Que fait :**
resultat = sorted(lines, key=critere, reverse=True)
'''

index = 4
def critere(ligne):
    return ligne[index]
resultat = sorted(lines, key=critere, reverse=True)

print('---------------------------------------')
print(resultat)
print('---------------------------------------')

# reverse va inverser comme dans son nom, générer une list en ordre décroissant.

'''
**Affichez le nom des 5 pays ayant la plus grande population**
'''

lines = []                                         #1 
head = None                                        #-
index_population = 5
with open('countries.csv', 'r') as csv : 
    head = csv.readline()                          #3
    head = head.rstrip('\n')                       #4
    line = head                                    #5
    head = head.split(';')                         #6
    while line :                                   #7
        line = csv.readline().rstrip('\n')         #8
        if line :                                  #9
            columns = line.split(';')              #10
            lines.append(columns)                  #11
        
numbersConverted = []
for liste in lines:
    for element in liste:
        try:
            numbersConverted.append(int(element))
        except ValueError:
            pass # pass over non-ints


population = max(numbersConverted)

print(numbersConverted)


#**Affichez la capitale de chaque pays**

lines = []                                         #1 
head = None                                        #-
index_population = 5
with open('countries.csv', 'r') as csv : 
    head = csv.readline()                          #3
    head = head.rstrip('\n')                       #4
    line = head                                    #5
    head = head.split(';')                         #6
    while line :                                   #7
        line = csv.readline().rstrip('\n')         #8
        if line :                                  #9
            columns = line.split(';')              #10
            lines.append(columns)                  #11
            

            #works fine for any value except france'

  ###############################
 ##########CAPITAL SEEKER 1.0##
##############################  
capitalIndex = 3
capitals = []

for liste in lines:
    capitals.append(liste[capitalIndex])

print("searcher 1.0 results:")
print(capitals)

'''
**Affichez tous les pays du continent europeen en utilisant une ecriture similaire a l'ecriture suivante :**
```
 [p[index_pays] for p in lines if float(p[index_population]) > 100000000]
```
'''

#index_continent = 6
#pays =  [p[index_continent] for p in lines if float(p[index_continent]) == "EU"
#         print(pays)

'''
**Vous avez du chercher l'index de plusieurs critere dans la liste *head*, et donc reecrire plusieurs fois un code similaire. Comment pourriez-vous eviter cela ? Faites le.**
'''
