'''
Exercice 1

on place à la banque A un capital de 5000€
Chaque année, +8%. 

1) Calculer A1, A2, A3.
A1 = 5000*1.08=5400
A2 = 5400*1.08=5832
A3 = 5832*1.08=6298.56

2) Montrer que (An) est une suite géométrique dont on précisera le 1er terme et la raison.
An+1= 1.08An vnEN
Pour passer d'un terme à l'autre on multiplie par 1.08 donc (An)
est une suite géométrique de 1er terme A0=5000 et de raison q=1.08.

3) Donner sa formule explicite
An=5000*(1.08)n (n en haut)

Partie 2 : [...] B0 = 5000 [..] augmente de 500 chaque année

1) Calc B1, B2 B3.
B1 = 5000+500=5500
B2 = 5500+500=6000
B3 = 6000+500=6500

2) Montrer que (Bn) est une suite arithmétique dont on précisera le 1er terme et la raison.
Bn+1= Bn+500.
Pour passer d'un terme à l'autre on ajoute 500.
(Bn) est une suite géométrique de 1er terme B0=5000 et de raison r=500.

Partie 3:
1) Quel est le meilleur placement à 5 ans? A 10ans?
A5 = 5000*(1.08)5=7346.64
B5= 5000+500*5=7500
Placement B à 5 ans.

A5 = 5000*(1.08)10=10794.62
B5= 5000+500*10=10000
Placement A à 10 ans.

2) A partir de quelle année un placement est meilleur qu'un autre?
A6=7934.37     B6=8000
A7=8569.12     B7=85000
A partir de la 7eme année, A est plus intéressant que B.
------------------------------------------
Exercice 2:
1) Association de gymnastique:
    - 50 adhérants en 2011
    - 18 nouvelle adhésions par an
    - 85% des inscrits renouvellent leur inscription par an
    - a0 = 50

1) Calc a1, a2, a3 en arrondissant à l'entier près
a1= 50*0.85+18=60.5 arrondi à 61
a2= 60.5*0.8+18=69.42 arrondi à 69
a3= 69.42*0.85+18=77.01 arrondi à 77.

2) Exprimer an+1 en foncktion de an
an+1 = 0.85an+18

3) a0=50 et an+1=0.85an+18 (c'est pas une question, info)

4) an est arith? geo? anemo?
A1-A0=8.92 [non égal] A2-A1=7.59 (An) n'est pas une SA.

A1/A0=1.147 [non égal] A2/A1=0.90 (An) n'est pas une SG.

5) un -) un = an-120
a) Calc u0 u1
u0 = a0-120=50-120=70
u1 = a1-120=60.5-120=-59.5

b) montrer que un est geo dont on précisera 1er term et raison
un+1/un = an+1-120/an-120 = 0.85an-18-120/an-120 = 0.85an-102/an-120 = 0.85(an-(102/0.85))/an-120 = 0.85(an-120)/an-120 ON BBARRE AN-120
=0.85 vnEN donc (Un) est une SG de raison q=0.85 et de 1er terme U0=-70

c) Exprimer Un en fonction de n.
Un = -70*0.85n (n en haut)

d) En déduire an en fonction de n.
an = Un+120=-70*0.85n+120

6)Que semble faire le nombre d'adhérants de ce club de gym?
Il semble se rapprocher de 120.

Exercice 3:
La suite Un est une suite arith de 1er terme u0=4 et de raison  r=1.5

1) Exprimer le terme général Un en fonction de n
Un=4+1.5n

2) Calculer la somme u0+...+u4
S = somme de 5 termes = 5*4+10/2=35'
(U0=4 U4=10)

'''