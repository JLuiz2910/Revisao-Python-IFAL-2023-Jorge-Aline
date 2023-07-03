#Lista de Exerc�cio 3 - Quest�o 20
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
#Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

import math
lista = []
count = 0

quant = int(input("Digite a quantiade de número que deseja digitar: "))
while quant != count:
    numero = float(input("Digite um número: "))
    while numero // 1 != numero or numero < 0 or 0 or numero < 16:
        numero = float(input("Digite um número[erro]: "))

    print("Fatorial do número digitado: ", math.factorial(numero))
    count += 1
