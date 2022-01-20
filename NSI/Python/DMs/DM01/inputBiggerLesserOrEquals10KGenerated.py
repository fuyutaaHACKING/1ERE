'''
1. Input a number
2. create list of 10K values between 0-100
3. Prints "won" if ther's more than 50% of the 10K values that are inferior, else "lose"

DOES NOT HANDLE TIE 5K-5K values
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