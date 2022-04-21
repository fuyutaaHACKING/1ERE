u = [0, 2, 4 , 6, 8]
v = [0, 1, 2, 3, 4]
w = 0 #initialise w
for i in range(w, len(u)): #boucle sur i, index de u et v
    w = w + ( u[i] * v[i] ) #mise a jour de w avec le produit entre u_i et v_i
#print(w)


u = [0, 2, 4 , 6, 8]
v = [0, 1, 2, 3, 4]
w = []
for i in range(len(v)) :#boucle sur i, index de v
    ligne = []
    for  j in range (len(u)): #boucle sur j, index de u
        resultToAdd = v[i] * u[j] #calcul le produit entre v_i et u_j
        ligne.append(resultToAdd) #ajoute le resultat a ligne -> ajouter un element a une liste
    w.append(ligne) #ajoute ligne a w -> ajouter un element a une ligne
#print(w)