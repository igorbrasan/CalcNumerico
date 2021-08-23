#importar biblioteca matematica
import math
from relatorios import iterar, resultado, gerarArquivo

#definir um intervalo [a,b] e um erro [e]
a = float(2)
b = float(8)
e = float(0.001)
ctr = int(0)
#definir uma função
def f(x):
    return x ** 2 - 5

#Testando teorema de Bolzano
def test(f, a, b):
    return f(a) * f(b) < 0

if test(f, a, b):
    while (math.fabs(b - a) / 2 > e):
        ctr= ctr+1
        xi = (a+b) / 2
        if f(xi) == 0:
            break
        else:
            print(iterar(ctr, f, xi))
            if f(a) * f(xi) < 0:
                b = xi
            else:
                a = xi
    print(resultado(xi))
    gerarArquivo('teste')
else:
    print('Não há raiz nesse intervalo!')
  