#Lista de Exerc�cio 3 - Quest�o 21
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

numero = int(input("\nDigite um número: "))

if numero % 2 == 0 and numero != 2:
    print("não primo")
else:
    print("primo")
