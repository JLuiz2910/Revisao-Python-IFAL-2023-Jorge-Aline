#Lista de Exerc�cio 5 - Quest�o 9
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
#Exercicio 9
#Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721

def reverso(n):
    numeroInvertido = int(str(n)[::-1])
    print(numeroInvertido)
n = int(input('Digite o número: '))
reverso(n)