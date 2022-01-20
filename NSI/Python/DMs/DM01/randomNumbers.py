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