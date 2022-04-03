
#---------------------------------------------------------
la_liste = [1, 3, 5, 9, 7, 11]
debut = 0
fin = len(la_liste) - 1

def calcMiddle(la_liste):
    firstValue = la_liste[0]
    lastValue = len(la_liste) - 1
    milieu = len(la_liste) / 2
    return int(milieu)

milieu = calcMiddle(la_liste)
recherche = 5 #la valeur recherchee
index = 4 #líndex de la valeur recherchee

print(milieu)
while fin >= debut : #tant que fin est superieur ou egale a debut
    if la_liste[milieu] == index: #si la valeur de la_liste au rang milieu egle la valeur recherchee
        index = la_liste[milieu]#on stock la valeur du milieu dans la variable index
        break #on a trouve l'index, on peut finir prematurement la boucle
    elif la_liste[milieu] > la_liste[index] : #sinon, on regarde si la valeur indexee par milieu est superieur a recherche
        fin = la_liste[milieu]+1 #dans ce cas, la variable fin prend pour valeur milieu plus un
    else: #sinon
        debut = la_liste[milieu] - 1 #la variable debut prend pour valeur milieu moins un

    milieu = calcMiddle(la_liste) #et on recalcul le milieu !

print('index : ', index)
print('milieu : ', milieu)
print(la_liste)
#print('loop : ', loop)