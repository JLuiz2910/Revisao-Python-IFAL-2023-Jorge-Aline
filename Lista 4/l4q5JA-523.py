#Lista de Exerc�cio 4 - Quest�o 5
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
#Exercicio 5
#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
#Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

import random
numeros = []
par = []
impar = []

for i in range(20):
    numero_aleatorio = numeros.append(random.randrange(0, 100))

count = 0
for i in range(20):
    if numeros[count] % 2 == 0:
        par.append(numeros[count])
    else:
        impar.append(numeros[count])
    count += 1

print("\nNumeros: ", numeros, "\nPares: ", par, "\nImpares: ", impar)