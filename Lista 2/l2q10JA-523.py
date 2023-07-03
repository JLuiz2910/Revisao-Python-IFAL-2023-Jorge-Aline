#Lista de Exerc�cio 2 - Quest�o 19
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
'''
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
'''

import math
numero = int(input("Digite um número menor ou igual a 1000: "))
if numero <= 1000:
    centena = numero / 100
    centena2 = math.floor(float(centena))
    resto_centena = centena - centena2
    resto_multiplicado = resto_centena * 100

    dezena = resto_multiplicado / 10
    dezena2 = math.floor(float(dezena))
    unidade = dezena - dezena2
    unidade_certo = unidade * 10

    print("Centena(s): ", centena2)
    print("dezena(s): ", dezena2)
    print("Unidade(s): ", round(unidade_certo))

else:
    print("VOCÊ DIGITOU UM NÚMERO MAIOR QUE 1000")
