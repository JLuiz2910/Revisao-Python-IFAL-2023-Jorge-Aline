#Lista de Exerc�cio 2 - Quest�o 9
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
#Faça um Programa que leia três números e mostre-os em ordem decrescente.

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

lista = [n1, n2, n3]

lista.sort(key=float, reverse=True)

print("decrescente: ", lista)
