#Soit le dictionnaire
mon_dico = {'agneau':'bébé mouton','baleineau':'bébé baleine','chiot':'bébé chien', 'dindonneau':'bébé dinde'}
#Cherchez 'chiot' et 'chaton', si la clef n'existe pas, renvoyer None, affichez le resultat

# fonction qui va prendre en param une valeur de clé pour chercher la def, et le dictionnaire en question
def searchForDefinition(keySearched:str, dic:list):
    if keySearched in dic:
        print(dic[keySearched])
    else:
        print("Aucune définition de cette clé ne figure dans le dictionnaire utilisé.")
    
print("Pour 'chiot' dans le dictionnaire:")
searchForDefinition("chiot", mon_dico)
print("------------------------")
print("Pour 'chaton' dans le dictionnaire:")
searchForDefinition("chaton", mon_dico)