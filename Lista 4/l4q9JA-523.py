#Lista de Exerc�cio 4 - Quest�o 9
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
#Exercicio 9
#Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

import math
vetor = [1,2,3,4,5,6,7,8,9,10]
raizes = []

cont = 0
for i in range(len(vetor)):
    raiz = math.sqrt(vetor[cont])
    raizes.append(raiz)
    cont += 1

print('\nRaizes:\n',raizes)
print('\nSoma:\n',sum(raizes))