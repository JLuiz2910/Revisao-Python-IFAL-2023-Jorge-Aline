#Lista de Exerc�cio 3 - Quest�o 35
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
numero = int(input("\nDigite um número: "))
lista = []

for i in range(numero + 1):
    if i % 2 == 1 and i != 2:
        lista.append(i)

print("Números primos: ", lista)
