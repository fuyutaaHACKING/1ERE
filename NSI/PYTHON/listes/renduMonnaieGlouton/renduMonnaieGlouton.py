to_render = 520

def renduMonnaie(to_render):
  monnaie = [200,100,50,20,10,5,2,1]
  i = 0
  while(to_render > 0):
    if(monnaie[i] > to_render):
      i = i + 1
    else:
      print("OPERATION:", to_render, "-", monnaie[i])
      to_render -= monnaie[i]

renduMonnaie(to_render)