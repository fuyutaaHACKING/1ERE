# BNS 2022 - DM DE NSI
# Hugo Caldier, NS_INF_05, 1G4

#----------------------#EXERCICE 01.1#----------------------------------#

# On va chercher pour chaque lettre dans le mot si la lettre == le caractère recherché
def recherche2(caractere, mot):
    occurence = 0
    for lettre in mot:
        if lettre == caractere:
            occurence = occurence + 1
    return occurence

result = recherche2("e", "tortue")
#print(result)


# On va décomposer le mot en une liste et chercher des occurences dans cette liste, une égalité caractère == lettre dans la liste
def recherche(caractere, mot):
    occurence = 0
    motDecomposeEnListe = []
    for lettre in mot:
        motDecomposeEnListe.append(lettre)
    for lettre in motDecomposeEnListe:
        if lettre == caractere:
            occurence = occurence + 1
    return occurence

result = recherche("e", "tortue")
#print(result)



#----------------------#EXERCICE 01.2#----------------------------------#

pieces = [100,50,20,10,5,2,1]

def rendu_glouton(arendre, solution=[], i=0):
    if arendre == 0:
        return solution
    p = pieces[i]
    if p <= arendre :
        solution.append(p)
        return rendu_glouton(arendre - p, solution,i)
    else :
        return rendu_glouton(arendre, solution, i+1)

#print(rendu_glouton(175))

#----------------------#SUJET 02#----------------------------------#
#----------------------#SUJET 02#----------------------------------#
#----------------------#SUJET 02#----------------------------------#



#----------------------#EXERCICE 02.1#----------------------------------#

def moyenneAvecCoef(listeDeTuples):
    totalDesNotes = 0
    totalDesCoefs = 0
    for note in listeDeTuples:
        noteConvertie = note[0] * note[1]
        totalDesNotes = totalDesNotes + noteConvertie
        totalDesCoefs = totalDesCoefs + note[1]

    return totalDesNotes / totalDesCoefs # moyenne finale

#print(moyenneAvecCoef([(15,2),(9,1),(12,3)]))
    


#----------------------#EXERCICE 02.2#----------------------------------#

def pascal(n):
    C = [[1]]
    for k in range(1,n+1):
        Ck = [1]
        for i in range(1,k):
            Ck.append(C[k-1][i-1]+C[k-1][i])
        Ck.append(1)
        C.append(Ck)
    return C

print(pascal(5))




