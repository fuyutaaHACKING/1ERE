#from pyfiglet import figlet_format

def numberCheck():
    inputData = input("Enter number")
    inputInt = int(inputData)
    if inputInt >= 0:
        print("Le chiffre rentré est positif")
    else:
        print("Le chiffre rentré n'est pas positif")

if True():
    numberCheck()