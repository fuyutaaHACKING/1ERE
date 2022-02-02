def suite_arithmetique():
    Uvals = [5]
    U = 5
    for n in range(0, 19):
        U = 2*U+3
        Uvals.append(U)
    print(Uvals)

if True:
    suite_arithmetique()