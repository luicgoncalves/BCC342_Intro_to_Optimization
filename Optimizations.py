import math


def bracket(x1, funcao, passo=0.000001, multiplicador=2):

  intervalo = [x1]

  x2 = x1 + passo
  intervalo = [x1, x2]

  fx1 = funcao(x1)
  fx2 = funcao(x2)

  if fx1 >= fx2:

    troca = x2 + passo
    ftroca = funcao(troca)

    while ftroca < fx2:
      x2 = troca
      fx2 = ftroca
      passo = passo*multiplicador
      troca = troca + passo
      ftroca = funcao(troca)

      intervalo = [x1, troca]

  elif fx1 < fx2:
    troca = x1 - passo
    ftroca = funcao(troca)
    while ftroca < fx1:
      x1 = troca
      fx1 = ftroca
      passo = passo*multiplicador
      troca = troca - passo
      ftroca = funcao(troca)

      intervalo = [troca, x2]

  return intervalo


def golden_search(funcao, x1, x2, tolerancia=1e-6):

    gr = (1 + math.sqrt(5))/2

    c = x2 - (x2-x1)/gr
    d = x1 + (x2-x1)/gr

    while abs(x2-x1) > tolerancia:
        if funcao(c) > funcao(d):
            x1 = c
        else:
            x2 = d
      
        c = x2 - (x2-x1)/gr
        d = x1 + (x2-x1)/gr

    return (x2+x1)/2

f = lambda x: (x)**2


print(bracket(1,f))
print(golden_search(f,-5,10))
