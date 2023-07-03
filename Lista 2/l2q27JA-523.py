#Lista de Exerc�cio 2 - Quest�o 8
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

preco1 = float(input("Digite o primeiro preço: "))
preco2 = float(input("Digite o segundo preço: "))
preco3 = float(input("Digite o terceiro preço: "))

lista = [preco1, preco2, preco3]

print("O produto que deve ser comprado é o que custa ", min(lista))
