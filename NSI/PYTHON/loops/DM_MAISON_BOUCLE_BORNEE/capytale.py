# Conditions et boucles bornées

#-------------------------------------------------------------
# Affichez si une entrée utilisateur est supérieure à 0.

inputData = input("Entrez un nombre :")

inputInt = int(inputData)

if inputInt > 0:
    print("Le chiffre rentré est supérieur à 0")
else:
    print("Le chiffre rentré est inférieur ou égal à 0")
#-------------------------------------------------------------



#-------------------------------------------------------------
'''
Générez aléatoirement un ensemble de 100 nombres entre -9 et 9.
> Pour générer un nombre aléatoire entre n et m, importez la bibliothèque random et utilisez la fonction randint(n, m):

```
import random
result = random.randint(n, m)
```

Comptez le nombre de valeur inférieure et supérieur à 0
'''

import random

results = []

def createList():
    for i in range(0,100):
        randomNum = random.randint(-9, 9)
        results.append(randomNum)
    #print(results)
    analyseList()

def analyseList():
    negativeCount = 0
    positiveCount = 0
    for result in results:
        if result < 0:
            negativeCount += 1
        else:
            positiveCount += 1
    print("Pour cette liste de 100 chiffres créés aléatoirement, il y a : \n - ", negativeCount, " chiffres inférieurs à 0 \n - ", positiveCount," chiffres supérieurs à 0.")
            
if True:
    createList()
#-------------------------------------------------------------



#-------------------------------------------------------------
'''
Ecrivez un programme qui :
- demande une entrée utisateur comprise entre 0 et 100
- génère une liste aléatoire de 10000 nombres entre 0 et 100
- calule le nombre de valeur inférieure, supérieure et égale à l'entrée utilisateur
- calcule le pourcentage de valeur inférieure à l'entrée utilisateur. Si cette valeur est supérieur à 50%, affichez "gagnez", "perdu" dans le cas contraire.
'''

import random

results = []
val = input("Entrez un nombre entre 0 et 100.")
userInput = int(val)

def createList():
    for i in range(0,10000):
        randomNum = random.randint(0, 100)
        results.append(randomNum)
    #print(results)
    analyseArray()

def analyseArray():
    #sort values
    inferiorCount = 0
    superiorCount = 0
    equalsCount = 0
    for result in results:
        if result < userInput:
            inferiorCount += 1
        elif result > userInput:
            superiorCount += 1
        else:
            equalsCount += 1

    # tells the user if won or not
    totalCount = 10000
    if(inferiorCount/totalCount*100 > 50):
        print("Vous avez gagné !")
    else:
        print("Vous avez perdu...")
            
if True:
    createList()
#-------------------------------------------------------------



#-------------------------------------------------------------
'''
### Etudiez le code
Le code suivant permet d'afficher un histogramme. C'est à dire, une représentation graphique de 
la répartition d'élément par classe, par exemple les classes "moyenne par matière".
'''

import matplotlib.pyplot as plt #importation de la bibliothéque

labels = ['math', 'nsi', 'svt', 'anglais', 'art'] #'liste' des labels à afficher
data = [15,12,8,16,13] #'liste' des éléments à afficher

fig, ax = plt.subplots() #création d'un container graphique <- à prendre tel quel
ax.bar(labels, data) #création du grphique type histogramme avec en paramètre : les labels et les valeurs pour chaque classe
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor") #Parce que c'est jolie

plt.title('Moyenne par matière de ...', fontsize=10) #ajout d'un titre

plt.show() #affichage du graphique
#-------------------------------------------------------------



#-------------------------------------------------------------
'''
## Plus
En vous inspirant du code précédent, affichez un histogramme avec les trois classes calculées précédemment (inf, sup, equ à 0).
'''

import random
import matplotlib.pyplot as plt
from numpy import equal

results = []
val = input("Entrez un nombre entre 0 et 100.")
userInput = int(val)

def createList():
    for i in range(0,10000):
        randomNum = random.randint(0, 100)
        results.append(randomNum)
    #print(results)
    analyseArray()

def analyseArray():
    #sort values
    inferiorCount = 0
    superiorCount = 0
    equalsZero = 0
    for result in results:
        if result < userInput:
            inferiorCount += 1
        elif result > userInput:
            superiorCount += 1
        else:
            equalsZero += 1
    drawHistogram(inferiorCount, superiorCount, equalsZero)
            
def drawHistogram(inferiorCount, superiorCount, equalsZero):
    labels = ['inferior', 'superior', 'equals'] # labels that shows up
    data = [inferiorCount,superiorCount,equalsZero] #data of each label

    fig, ax = plt.subplots() #creating graphical container
    ax.bar(labels, data) #création du graphique type histogramme avec en paramètre : les labels et les valeurs pour chaque classe
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor") #Parce que c'est jolie

    plt.title('Moyenne par matière de ...', fontsize=10) #ajout d'un titre

    plt.show() #affichage du graphique


if True:
    createList()
#-------------------------------------------------------------

'''

▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒░░░░  ░░░░░░▒▒░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░▒▒▒▒░░░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░▒▒▒▒▒▒░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▓▓▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▓▓▒▒▒▒▒▒▓▓▓▓▒▒▒▒▓▓▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓
▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▓▓▒▒▒▒▒▒▓▓▓▓▒▒▒▒▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▓▓▒▒▒▒▓▓▓▓▓▓▒▒▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▓▓▒▒▒▒▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓██▓▓▓▓▓▓▓▓██▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▒▒▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓██▓▓██▓▓▓▓▓▓▓▓██▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒▓▓▓▓▒▒▓▓▒▒▒▒▓▓▓▓▓▓██▓▓▓▓▓▓▓▓░░░░▓▓▓▓▒▒▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓██████▓▓▓▓██▓▓██▓▓██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▒▒▓▓▓▓▓▓▓▓██▓▓██▓▓▒▒░░▒▒▒▒▓▓░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓██▓▓██▓▓▓▓██▓▓██▓▓██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒░░▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▒▒░░▒▒▓▓██▓▓▓▓▓▓▓▓▓▓▓▓██▓▓██▓▓████▓▓██▓▓██▓▓████▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒  ▒▒▓▓▓▓▓▓██████▓▓▒▒░░░░░░▒▒▓▓░░░░▓▓▓▓██▓▓▓▓▓▓▓▓▓▓██████▓▓████▓▓██▓▓██▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░▒▒  ░░▓▓▓▓▓▓██▓▓██▓▓░░░░░░░░░░▓▓░░▒▒░░▓▓▓▓▓▓▓▓▓▓▓▓████████████████████████████▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██▓▓▓▓▓▓▓▓▓▓░░░░▒▒    ▒▒▓▓▓▓██████▓▓░░░░░░░░▒▒▒▒▒▒▒▒░░░░▒▒▓▓▒▒▓▓▓▓████████████████████▓▓██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓██▓▓██▓▓▓▓▓▓░░  ░░    ▒▒▓▓████████▒▒░░░░░░░░████████████▓▓▒▒▓▓▓▓▓▓████████████████████▓▓██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓██▓▓██▓▓▓▓▓▓░░  ░░    ░░▓▓████████░░░░░░░░▒▒▒▒▒▒██▓▓██▒▒▒▒▓▓▓▓▒▒████████████████████████▓▓████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓██▓▓▓▓▓▓░░  ░░      ▒▒▓▓██████░░░░░░░░  ░░▒▒██████▒▒  ░░▒▒▓▓████████▒▒████████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓██▓▓██▓▓▓▓▓▓            ░░░░▓▓▓▓██▒▒░░░░░░  ▒▒████████▒▒  ░░▒▒▒▒  ▓▓██▓▓░░▒▒████████████████▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓██▓▓▒▒▓▓          ░░  ░░  ▓▓▓▓▓▓  ░░░░  ░░▓▓████▓▓░░  ░░▒▒    ▓▓██▓▓▒▒▒▒████████████████▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▓▓░░▓▓              ░░    ▒▒▒▒░░  ░░          ▒▒    ░░▒▒    ████▓▓░░░░██████████████▓▓▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▒▒▓▓████▓▓▓▓  ▓▓              ░░                  ░░  ░░    ░░▒▒▓▓    ▓▓██▓▓░░░░██████████████▓▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓██▓▓▓▓  ▒▒░░    ░░░░    ░░░░░░░░              ░░░░      ▒▒▓▓    ████▒▒░░░░████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▒▒░░  ░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓██████░░  ▒▒░░░░              ░░░░░░░░                ░░▒▒▓▓    ▓▓██▒▒░░▓▓████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▒▒▒▒      ▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓██▓▓▓▓░░░░░░                        ░░░░░░          ░░▒▒██    ░░██░░▓▓██████████████████████████████████████
▒▒▒▒▒▒      ▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓████▓▓                                    ░░░░░░  ░░▒▒▓▓██      ▓▓▓▓████████████████████████████████████████
▒▒▒▒▒▒▒▒    ▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓                                        ░░  ░░▒▒▓▓██░░    ▓▓██████████████████████████████████████████
▒▒▒▒▒▒▒▒░░  ░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓░░                                          ░░░░▓▓██▒▒    ▓▓██████████████████████████████████████████
▒▒▒▒▒▒▒▒▒▒    ▓▓▓▓▓▓░░░░▓▓▓▓▓▓▓▓▒▒▓▓██████▒▒                                        ░░░░  ░░██▓▓    ▒▒██████████████████████████████████████████
▒▒▒▒▒▒▒▒▒▒░░  ░░▓▓▓▓    ▓▓▓▓▓▓▓▓▒▒▓▓▓▓████▓▓                                        ░░░░    ▓▓██      ██████████████████████████████████████████
▒▒▒▒▒▒▒▒▒▒▓▓    ▓▓▓▓    ▓▓▓▓▓▓▓▓▒▒▓▓▓▓██████▒▒                                    ░░░░░░  ░░░░▓▓░░    ▓▓████████████████████████████████████████
▒▒▒▒▒▒▒▒▓▓▒▒  ░░        ▒▒▓▓▓▓▓▓▒▒▓▓▓▓██████▓▓░░                                  ░░░░░░  ░░    ░░░░  ▒▒████████████████████████████████████████
▒▒▒▒▒▒▒▒▓▓▒▒░░      ░░  ░░▓▓▓▓▓▓▒▒▒▒▒▒██████▓▓██░░                              ░░░░░░▒▒  ░░          ░░▓▓██████████████████████████████████████
▒▒▒▒▒▒▒▒▒▒░░              ▓▓▓▓▓▓▒▒▒▒▒▒▓▓██▓▓▓▓▓▓▓▓▓▓░░                          ░░░░▒▒▒▒  ░░  ░░░░░░░░    ▓▓████████████████████████████████████
▒▒▒▒▒▒▒▒▒▒    ░░░░░░  ░░  ▒▒▓▓▓▓▒▒▒▒▒▒▓▓██▓▓▒▒▒▒▒▒▓▓▓▓▒▒░░                    ░░░░▒▒░░░░░░░░              ▓▓████████████████████████████████████
▒▒▒▒▒▒▒▒░░          ░░░░  ░░▓▓▓▓▒▒▒▒▒▒▒▒▓▓██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                ░░░░░░░░░░▒▒░░              ░░▓▓████████████████████████████████████
▒▒▒▒▒▒▒▒░░          ░░░░░░  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓░░        ░░▒▒░░░░░░░░▒▒░░░░        ░░    ░░▓▓████▓▓▒▒▓▓██████████████████████████
▒▒▒▒▒▒▒▒    ░░░░░░            ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██▒▒▒▒██▒▒░░▒▒░░░░░░░░░░░░░░░░░░░░            ░░██▓▓▒▒▓▓▒▒▓▓▓▓████████████████████████
▒▒▒▒▒▒▒▒          ░░  ░░░░    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒████░░░░▒▒░░░░░░░░░░░░░░░░                ░░▓▓▒▒▓▓▒▒▒▒▒▒▒▒▓▓████▓▓██████████████▓▓
▒▒▒▒▒▒▒▒          ░░  ░░      ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▓▓████░░░░▒▒░░░░▒▒░░░░░░░░░░░░              ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▒▒▒▒▒▒▒▒  ░░░░░░░░  ░░░░      ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒██████░░░░▒▒░░▒▒░░░░░░░░░░░░    ▒▒░░      ░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▒▒▒▒▒▒▒▒░░  ░░  ░░░░░░░░      ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██████░░░░▒▒░░░░░░░░░░░░░░▒▒    ▒▒░░      ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▒▒▒▒▒▒▓▓▒▒  ░░      ░░        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ▓▓▓▓██▓▓░░░░▒▒░░▒▒░░░░░░░░░░▓▓    ░░        ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▒▒▒▒▒▒▓▓▓▓░░                ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▓▓▓▓▓▓▓▓░░▒▒░░▒▒▓▓▓▓▒▒░░░░▓▓██░░░░          ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▒▒▒▒▒▒▓▓▓▓▒▒                ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓░░▒▒░░▓▓▓▓▓▓▓▓░░▒▒▓▓██▒▒░░          ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▒▒▓▓▓▓▓▓▓▓▓▓░░            ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓░░          ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░        ░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████░░          ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████░░          ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓░░  ░░░░░░░░░░░░░░▒▒▓▓▓▓▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓██▒▒        ░░▒▒░░▒▒██▓▓▓▓▓▓▒▒▒▒▓▓▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓    ░░░░░░░░░░░░▒▒▒▒▓▓▓▓▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓██▓▓        ░░▒▒░░░░████████▒▒▓▓████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓    ░░    ░░░░▒▒▒▒██████▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▓▓▓▓▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓        ░░░░  ▒▒▒▒████████▒▒██████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▒▒        ░░░░▒▒▒▒▓▓██████▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▓▓▓▓▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▒▒░░░░░░        ▒▒▓▓████████▓▓▓▓▓▓▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓░░    ░░░░░░▒▒▓▓████████▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▒▒          ░░▓▓████████████▓▓▓▓▓▓▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓██▓▓  ░░▒▒░░▒▒▓▓██████████████▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓██████████████▓▓▓▓▓▓██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓██▓▓  ░░░░▒▒▓▓██████████████▓▓██▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓██████████████████████▓▓▓▓▓▓██████▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓████░░░░▒▒▓▓████████████████████▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓████████████████████▓▓▓▓▓▓████▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓
██████▓▓▓▓▓▓▓▓▒▒▓▓▓▓██████████████████████▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓████████████████████▓▓▓▓▓▓████▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓
▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████████████████████▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓██████████████████▓▓▓▓▓▓████▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓
████████▓▓▓▓▓▓████████████████████████████▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████████▓▓▓▓██████▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓
████████▓▓▓▓▓▓██████████████████████████▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████████████▓▓▓▓██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓
████████▓▓▓▓▓▓██████████████████████████▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████▓▓▓▓██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓
██████████▓▓▓▓██████████████████████████▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████▓▓▓▓██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓
██████████▓▓▓▓▓▓████████████████████████▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████▓▓▓▓████▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓
████████████▓▓▓▓██████████████████████████▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▓▓▒▒▒▒▓▓▒▒▒▒▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████▓▓▓▓████▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓
████████████▓▓▓▓██████████████████████████▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████████████▓▓████▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓
██████████████▓▓▓▓██████████████████████▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████████████▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓
████████████▓▓▓▓▓▓██████████████████████▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
████████████▓▓▓▓▓▓██████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▓▓▓▓██████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████████████████████████████████
████████████▓▓▓▓▓▓▓▓██████████████████████▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▓▓▓▓██████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████████████████████▓▓██████████

'''