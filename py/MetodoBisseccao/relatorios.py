#imprime a iteração caso não encontre a raiz
def iterar(ctr, f, xi):
    return("Iteração {} . Xi = {} , f(xi) = {}" .format(ctr,xi,f(xi)))

#imprime resulado na tela
def resultado(xi):
    return("O valor da Raiz é: {}" .format(xi))

#criar um arquivo para colocar as coisas
def gerarArquivo(filename):
    f = open("{}.txt".format(filename), "a")

#escreve a sessão num arquivo
#def relatar(filename):
    #estudar em https://www.w3schools.com/python/python_file_write.asp