#Lista de Exerc�cio 3 - Quest�o 12
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
'''
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50
'''

n = int(input("digite um numero de 1 a 10: "))
cont = 1

while cont <= 10:
    tab = n * cont
    print(n, "X", cont, "=", tab)
    cont = cont + 1
