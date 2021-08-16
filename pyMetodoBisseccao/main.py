#importar biblioteca matematica
import math

#definir um intervalo [a,b] e um erro e
a = float(2)
b = float(8)
e = float(0.0000000001)
ctr = int(0)
#definir uma função
def f(x):
    return x ** 2 - 5

#imprime a iretação caso não encontre a raiz
def iterar(ctr, f, xi):
    print("Iteração {} . Xi = {} , f(xi) = {}" .format(ctr,xi,f(xi)))

#Testando teorema de Bolzano


if f(a) * f(b) < 0:
    while (math.fabs(b - a) / 2 > e):
        ctr= ctr+1
        xi = (a+b) / 2
        if f(xi) == 0:
            print("A raiz é: {}" .format(xi))
            break
        else:
            iterar(ctr, f, xi)
            if f(a) * f(xi) < 0:
                b = xi
            else:
                a = xi
    print("O valor da Raiz é: {}" .format(xi))
else:
    print('Não há raiz nesse intervalo!')
  