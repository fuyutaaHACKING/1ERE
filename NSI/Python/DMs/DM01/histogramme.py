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