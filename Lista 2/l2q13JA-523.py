#Lista de Exerc�cio 2 - Quest�o 21
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
'''
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
'''

import math
saque = int(input("Valor para sacar: "))
nota100 = saque / 100
nota100_certo = math.floor(nota100)
resto_nota_100 = (nota100 - nota100_certo) * 100

nota50 = resto_nota_100 / 50
nota50_certo = math.floor(nota50)
resto_nota_50 = (nota50 - nota50_certo) * 50

nota10 = resto_nota_50 / 10
nota10_certo = math.floor(nota10)
resto_nota_10 = (nota10 - nota10_certo) * 10

nota5 = resto_nota_10 / 5
nota5_certo = math.floor(nota5)
nota1 = (nota5 - nota5_certo) * 5

print("Notas 100: ", nota100_certo, "\nNotas50: ", nota50_certo, "\nNota 10: ", nota10_certo, "\nNota 1: ", round(nota1))
