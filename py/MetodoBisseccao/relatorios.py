#imprime a iretação caso não encontre a raiz
def iterar(ctr, f, xi):
    return("Iteração {} . Xi = {} , f(xi) = {}" .format(ctr,xi,f(xi)))
def resultado(xi):
    return("O valor da Raiz é: {}" .format(xi))
def gerarArquivo(filename):
    f = open("{}.txt".format(filename), "a")
