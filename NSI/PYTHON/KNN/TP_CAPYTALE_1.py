## KNN - Algorithme des K plus proches voisins 

#Vous allez implémenter l'algorithme KNN sur les données iris_dataset.csv

# script deja utilise dans les TPs precedents -> cree un dictionnaire a partir d'un fichier csv
values = []
headers = []
with open('iris_dataset.csv', 'r') as csv :
    line = csv.readline().rstrip('\n')
    headers = line.split(',')
    while line != '' :
        line = csv.readline().rstrip('\n')
        if line != '' :
            values.append(line.split(','))
dataset = []
for index_val in range(len(values)) :
    line = {}
    for index_head in range(len(headers)) :
        line[headers[index_head]] = values[index_val][index_head]
    dataset.append(line)

print(dataset)

#La cellule suivante permet de créer une liste de dictionnaire. Chacun des dictionnaires contient les coordonnées des Iris d'une classe particulière : *Iris-setosa*, *Iris-versicolor*, *Iris-virginica*

x = [] #contiendra les abscisses de toutes les Iris 
y = [] #contiendra les ordonnees de toutes les Iris
cl = [] #contiendra les classes de toutes les Iris

data = [{'classe':'Iris-setosa', 'coords':[]},    #liste de dictionnaires, chaque dictionnaire contient des donnees d'un type d'iris
       {'classe':'Iris-versicolor', 'coords':[]},
       {'classe':'Iris-virginica', 'coords':[]},]
for d in dataset: #parcours toutes les donnees
    x.append(float(d['petal length (cm)'])) #ajoute les abscisses dans la liste x
    y.append(float(d['petal width (cm)']))  #ajoute les ordonnees dans la liste y
    if d['target'] == 'Iris-setosa':        #filtre les donnees sur les iris setosa
        data[0]['coords'].append((float(d['petal length (cm)']), float(d['petal width (cm)'])))
        cl.append(0)
    elif d['target'] == 'Iris-versicolor':  #filtre les donnees sur les iris versicolor
        data[1]['coords'].append((float(d['petal length (cm)']), float(d['petal width (cm)'])))
        cl.append(1)
    elif d['target'] == 'Iris-virginica':   #filtre les donnees sur les iris virginica
        data[2]['coords'].append((float(d['petal length (cm)']), float(d['petal width (cm)'])))
        cl.append(2)

print(cl)

#L'inconnue :

#unknown = (3, 1)
unknown = (1.5, 0.25)

#Le script suivant permet d'afficher les données

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
unknown = (1.5, 0.25)

ax.scatter([e for e,s in zip(x,cl) if s==0] , [e for e,s in zip(y,cl) if s==0], color='g', label='setosa')
ax.scatter([e for e,s in zip(x,cl) if s==1] , [e for e,s in zip(y,cl) if s==1], color='r', label='versicolor')
ax.scatter([e for e,s in zip(x,cl) if s==2] , [e for e,s in zip(y,cl) if s==2], color='b', label='virginica')

ax.scatter([unknown[0]] , [unknown[1]], color='k', label='unknown')

plt.legend()
plt.show()


'''
Étant donné notre représentation :


data = [{'classe':'Iris-setosa', 'coords':[(x0, y0), (x1, y1)]},
       {'classe':'Iris-versicolor', 'coords':[(x0, y0), (x1, y1)]},
       {'classe':'Iris-virginica', 'coords':[(x0, y0), (x1, y1)]}]
'''


#avec l'inconnue

'''unknown = (xu, yu)'''

#et la distance de Manhatan

'''dm = abs(xu-x) + abs(yu-y)'''

#Calculez la distance entre l'inconnue et le premier représentant des *Iris Setosa* :

#calcul de la distance entre l'inconnue et le premier représentant des Iris Setosa
#l'index d'un 1er element est zero.
#recuperer une valeur d'un dictionnaire : valeur = dico[cle]
#recuperer une valeur d'un tuple : tuple=(1, 2), tuple[0] renvoie 1

distance = abs(data[0]['coords'][0][0] - unknown[0]) + abs(data[0]['coords'][0][1] - unknown[1])

print(distance)

#print(data)


'''
D'après le code précedant calculez la moyenne des distances entre l'inconnue et tous les représentants de la classe *Iris Setosa*, 
sachant que cela correspond au 1er dictionnaire. Votre code contiendra une boucle bornée.
'''

distances = []
dictio = data[0]
coords = dictio['coords']
for coordinatesSet in coords:
    xy = coordinatesSet
    distance = abs(xy[0] - unknown[0]) + abs(xy[1] - unknown[1])
    distances.append(distance)

print(distances)

'''
D'après le code précedant calculez indépendamment la moyenne des distances entre l'inconnue et tous les représentants de chaque classe. 
Cela fera 3 moyennes à stocker dans une liste. Votre code contiendra deux boucles bornées.
'''

distancesParClasses = []

for i in data:
    distances = []
    coos = i['coords']
    for coordinatesSet in coos:
        xy = coordinatesSet
        #print(co)
        distance = abs(xy[0] - unknown[0]) + abs(xy[1] - unknown[1])
        distances.append(distance)
    distancesParClasses.append(distances)


print(distancesParClasses)

'''
Trouvez l'index de la moyenne la plus petite dans la liste précedente. À partir de cet index, affichez à quelle classe appartient l'inconnue (l'index trouvé est l'index du dictionnaire de la classe).
'''

'''
PLAN:
1. Get minimals of each list
2. get minimal of minimals
3. get that minimal its index in list
'''
minimals = []
def returnMinimalOfListOfListsAndIndex():
    for irisList in distancesParClasses:
        minimal = min(irisList)
        minimals.append(minimal)
    #print(minimals)
    minimal = min(minimals)
    #print(minimal)
    for irisList in distancesParClasses:
        for dist in irisList:
            if dist == minimal:
                indexOfDist = irisList.index(dist)
                indexOfList = distancesParClasses.index(irisList)
    if indexOfList == 0:
        theListName = "Iris-setosa"
    elif indexOfList == 1:
        theListName = "Iris-versicolor"
    else:
        theListName = "Iris-virginica"
    print("The minimal distance is from the list", theListName, "at index", indexOfDist)

returnMinimalOfListOfListsAndIndex()


