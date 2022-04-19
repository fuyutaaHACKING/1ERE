'''
Nous avons deux variables, phrase et mot.
Phrase va donc être, par déduction évidente, la phrase dont on va compter le nombre de mots.
Mais alors que va être "mot", contenant l'alphabet? Et bien, cette variable va contenir tous les caractères pouvant former un mot.
On va alors pour chaque mot détecté, vérifier si ce mot contient une des lettres de l'alphabet stockée dans "mot". Si le mot qu'on vérifie ne contient pas 
une letttre de l'alphabet, c'est alors un chiffre, une ponctuation ou autre, et on ne le comptera pas comme étant un mot.
On utilisera alors une comparaison basée sur un if else, si on trouve une lettre de l'alphabet ou non.
'''
##################################################
########    WORD COUNTER V1.0   #################
################################################

from multiprocessing.sharedctypes import Value


mot = "abcdefghijklmnopqrstuvwxyz"
phrase = ""

def wordCounterNoExceptions(phrase):
    wordCount = 0
    phrase = phrase.lower()
    extractedWords = phrase.split()
    print(extractedWords)
    for word in extractedWords:
        for letter in mot:
            if letter in word:
                wordCount = wordCount + 1
                break
    return wordCount

def menuWordCounterNoExceptions():
    while True:
        phrase = input("Entrez une phrase.\n>")
        print(wordCounterNoExceptions(phrase))


##################################################
########    WORD COUNTER V2.0   #################
################################################

# SUPPORTE L'IMPLEMENTATION D'EXCEPTIONS, EN CAS DE BESOIN

motAvecAccents = "abcdefghijklmnopqrstuvwxyz"
phrase = ""

def wordCounterWithExceptions(phrase):
    wordCount = 0
    phrase = phrase.lower()
    extractedWords = phrase.split()
    exceptions = ["exception"]
    print(extractedWords)
    for word in extractedWords:
        for letter in motAvecAccents:
            if letter in word or word in exceptions:
                wordCount = wordCount + 1
                break
    return wordCount

def menuWordCounterWithExceptions():
    while True:
        phrase = input("Entrez une phrase.\n>")
        print(wordCounterWithExceptions(phrase))


#----------MENU-----------------#
def choiceAsker():
    choice = input("Entrez le numéro correspondant à la fonction que vous voulez lancer.\n>")
    return choice

def menu():
    print("--------------------\nFONCTIONS:\n1. wordCounterNoExceptions\n2. wordCounterWithExceptions")
    looping = True
    while looping:
        choice = choiceAsker()
        
        if choice == "1":
            looping = False
            phrase = input("Entrez une phrase.\n>")
            print(wordCounterNoExceptions(phrase))

        elif choice == "2":
            looping = False
            phrase = input("Entrez une phrase.\n>")
            print(wordCounterWithExceptions(phrase))
        
        else:
            print("La valeur entrée n'est pas comprise dans le menu. Il n'y a pas de fonction à ce numéro.")


menu()
#----------MENU-----------------#
