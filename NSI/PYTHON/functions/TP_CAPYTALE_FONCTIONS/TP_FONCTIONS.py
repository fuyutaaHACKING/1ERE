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
        
        print("Boolean value: ",isInList ,"\nIndex in list: ", indexOfUserInputInRange)
        
    else:
        print(isInList)

# Pythagore calculateur
def pythagore():
    formula = input("Incorrect. Choose a side between 'a' (adjacent or opposed), 'c' (hypothénuse)")


    if formula == "c":
        side_a = int(input("Enter the length of the 1st side"))
        side_b = int(input("Enter thge length of the 2nd side"))

        side_c = sqrt(side_a * side_a + side_b * side_b)
        
        print("The length of the hypothenuse is :", side_c)

    elif formula == "a":
        side_b = int(input("Enter the length of the non-hypothenuse side"))
        side_c = int(input("Enter the length of the hypothenuse side"))
        
        side_a = sqrt((side_c * side_c) - (side_b * side_b))
        
        print("The length of the missing side is: ")
        print(side_a)

    else:
        print("Incorrect. Choose a side between 'a' (adjacent or opposed), 'c' (hypothénuse)")
        
#Launcher and launcher starter

def checkUserInput(input):
    try:
        # Convert it into integer
        val = int(input)
        print("Input is an integer number. Number = ", val)
        return True
    except ValueError:
        print("error")
        return False
            
def launcher():
    print("---------------------------------------------------\n        CODE LAUNCHER : \nEnter the correspond number to the exercice you want to execute        \n---------------------------------------------------")
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
        num1 = input("Enter a first number\n>")
        num2 = input("Enter a second number\n>")
        
        verifier = checkUserInput(num1)
        
        if(verifier == True):
            pass
        else:
            return
        exercice5(num1, num2)
    
    
    elif keyGiven == 6:
        userNumber = int(input("Enter an integer.\n>"))
        
        # List
        valList = []
        n = int(input("Enter number of elements:\n>"))
         
        # iterate till the end with a for in range, the end being = n
        for i in range(0, n):
            ele = int(input())
         
            valList.append(ele) # adding the element
            
        exercice6(userNumber, valList)
    
    elif keyGiven == 7:
        userNumber = int(input("Enter an integer\n"))
        
        # Liste
        valList = []
        n = int(input("Enter number of elements:\n>"))
         
        # iterate till the end with a for in range, the end being = n
        for i in range(0, n):
            ele = int(input())
         
            valList.append(ele) # adding the element
            
        exercice6(userNumber, valList)
    
    elif keyGiven == 8:
        pythagore()
     
if True:
    launcher()