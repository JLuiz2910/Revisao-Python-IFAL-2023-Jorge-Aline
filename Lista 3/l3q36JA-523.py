#Lista de Exerc�cio 3 - Quest�o 36
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
n_tabuada = int(input("\nDigite o número para fazer a tabuada: "))
n_inicial = int(input("Iniciar a tabuada no : "))
n_final = int(input("Finalizar a tabuada no : "))

caminho = n_inicial

for i in range(n_inicial, n_final + 1):
    print(n_tabuada, " X ", caminho, " = ", n_tabuada * caminho)
    caminho += 1
