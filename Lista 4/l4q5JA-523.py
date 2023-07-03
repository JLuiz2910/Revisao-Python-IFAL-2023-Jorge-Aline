#Lista de ExercÌcio 4 - Quest„o 5
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: ProgramaÁ„o Web
#Professor: Italo Arruda
#Exercicio 5
#Fa√ßa um Programa que leia 20 n√∫meros inteiros e armazene-os num vetor. 
#Armazene os n√∫meros pares no vetor PAR e os n√∫meros IMPARES no vetor impar. Imprima os tr√™s vetores.

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