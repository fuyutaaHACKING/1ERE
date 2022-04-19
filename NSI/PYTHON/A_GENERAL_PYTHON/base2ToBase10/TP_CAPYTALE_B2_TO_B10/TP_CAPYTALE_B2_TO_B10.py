puissance_de_2 = [] 
for index in range(8): 
    puissance_de_2.append(2**index)
    
print(puissance_de_2) #shows the content of the variable puissance_de_2

sequence = '10101010'
convert = 0

for index in range(8):
    s = sequence[index]
    se = int(s)
    convert = se * puissance_de_2[7 - index] + convert

print(convert)
