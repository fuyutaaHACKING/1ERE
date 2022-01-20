chiffre = 2
 
puissance = 0
 
resultats = {
        "puissance":[],
        "valeur":[]
        }
 
while puissance != 7:
    puissance += 1
    result = 2**puissance
    resultats["puissance"].append(puissance)
    resultats["valeur"].append(result)
    
print(resultats)