'''
Expériences indépendantes = le résultat de la 1er expérience n'a aucune influence sur le résultat de la 2nde.

Règle d'un arbre de proba:
1. La somme des probas d'un même noeud = 1

Pa(B) = P(AnB) * P(A)

Formule des probas composées:
P(AnB) = Pa(B) * P(A)

Dire que deux évenements sont dépendants signifie que:
P(AnB) = P(A) * P(B)
La réalisation de A n'influence pas celle de B
Pa(B) = P(B)

FPT = 
P(X) = P(XnA1) + P(XnA2) +  P(XnA3)
Avec les probas conditionnelles:
P(B) = P(AnB) + P(A|nB)
'''