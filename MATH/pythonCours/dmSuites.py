s=0
u=1.5
for i in range(0,5):
    u=u+3.5
    s=s+u
    print(i, "\nun:", u,"\ns:", s, "\n------------------")
print(s)