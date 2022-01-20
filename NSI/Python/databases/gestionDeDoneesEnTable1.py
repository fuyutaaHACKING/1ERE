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

print(input("A pour lines B pour head"))
if input == "A":
    print(lines)
elif input == "B":
    print(head)



'''
1. A quoi sert lines ? Qu'est-ce que "[]" ? Pouvez-t-on le declarer apres with... ?
    - Lines va être une liste de listes, une liste contenant chaque ligne de notre fichier séparée.
    - "[]" va servir à déclarer le type de notre variable en tant que liste
    - On ne pourrit pas le déclarer après with car woth va correspondre à une loop qui reset lines à chaque fois sinon. En +, on serait out of scope dans certaines situations.

2. Le nom de fichier est-il le bon ? Qu'est-ce que 'r' ? A quoi correspond csv ?
    - Non, il est écrit dans le script "emissions_co2-tonne.csv" au lieu du nom "countries.csv".
    - "r" correspond au mode ouverture de fichier, r correspondant alors au "read" (=lecture).
    - csv va être l'extension de notre fichier. un .csv est fichier dit "Comma-separated values", qui est un texte de valeurs délimitées par des points virgules (commas).

3. Que fait readline?
    - readline va faire, explicitement, la lecture de la ligne du fichier ouvert en tant que "csv"

4. Que fait rstrip() ?
    - rstrip permets de retirer les caractères de retour à la ligne

5. *Pourquoi affecter head a line ? Pouvait-on ecrire line = None pour simplement declarer line ?* 
    - head va contenir la ligne lue, et va passer dans rstrip, et une fois "propre" on va pouvoir affecter à line.

6. A quoi correspond le split(';') ?
    - Split va servir à séparer chaque élement lu en un élément de liste distinct dans une même liste.

QUESTION SUPPRIMÉE PAR ERREUR

9. Que fait cette ligne ?
    - on vérifie qu'il y a bien une ligne avant de faire toute opération afin d'éviter une erreur. on aurait pu sinon faire "if not line".

11. Que fait cette ligne ?
    - Cette ligne va ajouter à notre liste de listes, la ligne lue une fois formattée, où chaque élément est séparé

12. Apres execution du code *corrige*, que contient lines ? head ?
    - Lines va contenir comme prévu, une liste contenant chaque ligne du tableur en listes distinctes, dont les diverses valeurs sont séparées.
    - Head contient alors rien.
'''

for index in range(len(ma_liste)) :       #1 On va répéter la boucle jusqu'à ce que toutes les valeurs de la ligne soient lues. len retourne le nombre d'items dans une liste et on va donc boucler sur len pour passer sur chaque élément et effectuer nos opérations par la suite dessus
    print(index, ' -> ', ma_liste[index]) #2 L'index va être le nombre incrémenté à chaque bouclage de boucle et par cela, l'index de la valeur dans la liste, la position dans la liste de l'élément exprimée par index.
    if ma_liste[index] == 'trois' :       #3 On possède donc un index correspondant à la valeur ) tester, et on va aller chercher cette valeur avec ma_liste[index] puis la comparer à la valeur cherchée "trois" par l'écriture == "trois"
        print('Nous irons au bois.')      #4 Si l'index est correspondant à la valeur cherchée, alors ce message s'affiche. On suppose alors un dé jeté, et si la valeur est 3 alors ils "iront au bois".

'''

'''