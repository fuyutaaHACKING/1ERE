from math import sqrt

# Ecrire une fonction qui ne prend aucun paramètre, qui affiche "Hello World".
def exercice1():
    print("Hello world !")

# Ecrire une fonction qui ne prend aucun paramètre, qui renvoie l'entier 42. 
# Stockez cette valeur, dans une variable puis affichez cette variable.
def exercice2():
    number = 42
    print(number)

# Ecrivez une fonction "estPair" à 1 paramètre un entier. 
# return True si le paramètre est pair, False sinon.
def exercice3(num:int):
    booleanNum = false
    if (num % 2) == 0:
        booleanNum = True
        print(booleanNum)
    else:
        booleanNum = False
        print(booleanNum)

# Ecrivez la fonction "estImpair".
def exercice4(num:int):
    booleanNum = false
    if (num % 2) == 0:
        booleanNum = False
        print(booleanNum)
    else:
        booleanNum = True
        print(booleanNum)

# Ecrivez une fonction qui prends deux params et revoie le produit.
# vérifier que les paramètres sont des int
def exercice5(num1:int, num2:int):
    result = num1 * num2
    print(result)
    
# Ecrivez une fonction qui prends une liste et un entier en param
# retourne True si l'entier appartient à la liste, False sinon.
def exercice6(userInput:int, valuesList:list):
    isInList = False
    if userInput in valuesList:
        isInList = True
        print(isInList)
    else:
        print(isInList)
    
# Exercice 7 (6bis)
# La fonction renvoie maintenant 2 paramètres :
# - True/False
# - l'index de l'entier s'il appartient à la liste, None sinon.

def exercice7(userInput:int, valuesList:list):
    isInList = False
    if userInput in valuesList:
        indexOfUserInputInRange = valuesList.index(userInput)
        isInList = True
        
        print("Valeur booléen: ",isInList ,"\nIndex dans la liste: ", indexOfUserInputInRange)
        
    else:
        print(isInList)

# Pythagore calculateur
def pythagore():
    formula = input("Choisissez un côté entre 'a' (adjacent ou opposé), 'c' (hypothénuse)")

    if formula == "c":
        side_a = int(input("Entrez la longueur du 1er côté"))
        side_b = int(input("Entrez la longueur du 2eme côté"))

        side_c = sqrt(side_a * side_a + side_b * side_b)
        
        print("La longueur de l'hypothénuse est : ")
        print(side_c)

    elif formula == "a":
        side_b = int(input("Entrez la longueur du côté non hypothénuse"))
        side_c = int(input("Entrez la longueur du côté étant l'hypothénuse"))
        
        side_a = sqrt((side_c * side_c) - (side_b * side_b))
        
        print("La longueur du côté manquant est : ")
        print(side_a)

    else:
        print("Incorrect. Choisissez un côté entre 'a' (adjacent ou opposé), 'c' (hypothénuse)")
        
#Launcher and launcher starter

def launcher():
    print("---------------------------------------------------\n        CODE LAUNCHER : \nEntrez le nombre de l'exercice que vous voulez tester         \n---------------------------------------------------")
    keyGiven = int(input("Enter the corresponding number of the function you want to start (8 = pythagore)"))
    if keyGiven == 1:
        exercice1()
        
    elif keyGiven == 2:
        exercice2()
        
    elif keyGiven == 3:
        exercice3()
        
    elif keyGiven == 4:
        exercice4()
        
    elif keyGiven == 5:
        num1 = int(input("Entrez un premier nombre"))
        num2 = int(input("Entrez un second nombre"))
        
        exercice5(num1, num2)
    
    
    elif keyGiven == 6:
        userNumber = int(input("Entrez un entier"))
        
        # Liste
        valList = []
        n = int(input("Enter number of elements : "))
         
        # itère jusqu'à la fin de la range avec pour fin = n
        for i in range(0, n):
            ele = int(input())
         
            valList.append(ele) # adding the element
            
        exercice6(userNumber, valList)
    
    elif keyGiven == 7:
        userNumber = int(input("Entrez un entier"))
        
        # Liste
        valList = []
        n = int(input("Enter number of elements : "))
         
        # itère jusqu'à la fin de la range avec pour fin = n
        for i in range(0, n):
            ele = int(input())
         
            valList.append(ele) # adding the element
            
        exercice6(userNumber, valList)
    
    elif keyGiven == 8:
        pythagore()
     
if True:
    launcher()