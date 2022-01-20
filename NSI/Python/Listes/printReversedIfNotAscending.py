import random

def returnAscendingList(li):
    if(li[0] > li[1]):
        li.reverse()
        return li
    else:
        return li

ma_liste_5 = [random.randint(0,9) for i in range(2)]
print(returnAscendingList(ma_liste_5))