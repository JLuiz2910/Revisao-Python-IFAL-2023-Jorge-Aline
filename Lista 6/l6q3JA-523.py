#Lista de Exerc�cio 6 - Quest�o 3
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
#Exercicio 3
'''
Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.

    F
    U
    L
    A
    N
    O
'''

nome = str(input('Digite o seu nome: '))
for i in range(len(nome)):
    print(nome[i].upper(), '\n')