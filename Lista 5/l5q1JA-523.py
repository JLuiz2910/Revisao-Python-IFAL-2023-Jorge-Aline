#Lista de Exerc�cio 5 - Quest�o 1
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
#Lista de Exerc�cio 5 - Quest�o 1
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
#Exercicio 1
'''
Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

'''
def exercicio_1(n):
    for i in range(n):
        i += 1
        print((str(i)+"   ")*i)
n = int(input("Digite n: "))
exercicio_1(n)