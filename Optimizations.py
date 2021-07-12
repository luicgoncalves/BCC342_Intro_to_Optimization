import math


def bracket(x1, funcao, passo=0.000001, multiplicador=2):


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


def golden_search(f,a,b,tol=1e-6):

  gr = (1 + math.sqrt(5))/2

  c = b - (b-a)/gr
  d = a + (b-a)/gr

  while abs(b-a) > tol:
    if f(c) > f(d):
      a = c
    else:
      b = d
      
    c = b - (b-a)/gr
    d = a + (b-a)/gr

  return (b+a)/2


def quadratic_fit_search(f,a,b,tol=1e-6):

  c = b
  b = (c-a)/2

  fa = f(a)
  fb = f(b)
  fc = f(c)

  while abs(c-a) < tol:
    x = 0.5*(fa*(b**2-c**2)+fb*(c**2-a**2)+fc*(a**2-b**2))/(fa*(b-c) +fb*(c-a) +fc*(a-b))
    fx = f(x)
    print(x)
    if x > b:
      if fx > fb:
        c = x
        fc = fx
      else: 
        a = b
        fa = fb
        b = x
        fb = fx
    else:
      if fx > fb:
        a = x
        fa = fx
      else:
        c = b
        fc = fb
        b = x
        fb = fx

  return (a+c)/2

f = lambda x: (x)**2


print(bracket(1,f))





#1º Passo - Gerar uma solução inicial X
#2º Passo - Definir uma direção de busca S
#3º Passo - Dar um passo  de amanho alpha na direção de S. X = X +alpha.S
#4º Passo - Se não critério de parada ir para passo 2