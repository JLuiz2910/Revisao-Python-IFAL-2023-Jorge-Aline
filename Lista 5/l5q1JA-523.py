#Lista de Exercício 5 - Questão 1
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programação Web
#Professor: Italo Arruda
#Lista de Exercício 5 - Questão 1
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programação Web
#Professor: Italo Arruda
#Exercicio 1
'''
FaÃ§a um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
para um n informado pelo usuÃ¡rio. Use uma funÃ§Ã£o que receba um valor n inteiro e imprima atÃ© a n-Ã©sima linha.

'''
def exercicio_1(n):
    for i in range(n):
        i += 1
        print((str(i)+"   ")*i)
n = int(input("Digite n: "))
exercicio_1(n)