#Lista de Exerc�cio 5 - Quest�o 4
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
#Lista de Exerc�cio 5 - Quest�o 4
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
#Exercicio 4
'''
Faça um programa, com uma função que necessite de um argumento. 
A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
'''

def pos_ou_neg(n):
    if n > 0:
        print('P')
    else:
        print('N')

arg = int(input('valor: '))
pos_ou_neg(arg)