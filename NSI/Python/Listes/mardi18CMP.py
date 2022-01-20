# SCRIPT V5 QUI REPONDS AUX DEUX EXOS

lst1 = [1, 2, 3]
lst2 = [3, 2, 1]

#####################################
# V1: if else 
'''
lst1 = lst1.sort()
lst2 = lst2.sort()

if lst1 == lst2:
    print("égales")
else:
    print("non égales")
'''
#####################################
# V2
'''
def cmpLists(lst1:list, lst2:list):
    for n in lst1:
        if n in lst2:
            countLst1 = lst1.count(n)
            countLst2 = lst2.count(n)
            if countLst1 != countLst2:
                return False
            return True
        else:
            return False

print(cmpLists(lst1,lst2))
'''
#####################################
# V3
'''
def cmpLists3():
    for number in lst1:
        for number2 in lst2:
            if number == number2:
                countLst1 = lst1.count(number)
                countLst2 = lst2.count(number)
                if countLst1 != countLst2:
                    return False
            else:
                continue

            return True
'''
######################################
# V4
''''
def hmf():
    liste1 = lst1
    liste2 = lst2
    for n in liste1:
        if n in liste2:
            if (liste1.count(n) != liste2.count(n)):
                return False
        else:
            return False
        return True

print(hmf())
'''
#######################################
# V5: Avec aide internet pour le début
def sortList(lst):
    lst.sort()
    return lst

def method_2(l1:list, l2:list):
    l1 = sortList(l1)
    l2 = sortList(l2)
    for i in range(min(len(l1), len(l2))):
        if l1[i] != l2[i]:
            return False
    return len(l1) == len(l2)

print(method_2(lst1, lst2))