#Lista de Exerc�cio 5 - Quest�o 8
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
#Exercicio 8
'''
Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
'''

def contador(n):
    n = str(n)
    print(len(n))

num = int(input('Digite o numero: '))
contador(num)