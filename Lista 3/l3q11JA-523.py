#Lista de Exerc�cio 3 - Quest�o 11
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
#Altere o programa anterior para mostrar no final a soma dos números.

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

for i in range(n1 + 1, n2):
        print(i)

for i in range(n2 + 1, n1):
        print(i)

print("Soma dos números: ", i + i)
