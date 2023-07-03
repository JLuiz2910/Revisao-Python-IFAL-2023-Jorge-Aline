#Lista de ExercÌcio 4 - Quest„o 7
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: ProgramaÁ„o Web
#Professor: Italo Arruda
#Exercicio 7
#Fa√ßa um Programa que leia um vetor de 5 n√∫meros inteiros, mostre a soma, a multiplica√ß√£o e os n√∫meros.

from functools import reduce
numeros = [1, 2, 3, 4, 5]
multiplicados = reduce((lambda x, y: x * y), numeros)
print("\nSoma: ", sum(numeros), "\nMultiplic√£o: ", multiplicados, "\nN√∫meros: ", numeros)