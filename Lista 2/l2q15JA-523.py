#Lista de Exerc�cio 2 - Quest�o 23
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
'''
Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
'''

numero = float(input("Digite um número: "))

if(numero // 1 == numero):
    print("numero inteiro")
else:
    print("Numero Decimal")
