#Lista de Exerc�cio 4 - Quest�o 14
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
#Exercicio 14   *********
'''
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
    a - 'Telefonou para a vítima?'
    b - 'Esteve no local do crime?'
    c - 'Mora perto da vítima?'
    d - 'Devia para a vítima?'
    e - 'Já trabalhou com a vítima?' 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como 'Suspeita', 
entre 3 e 4 como 'Cúmplice' e 5 como 'Assassino'. 
Caso contrário, ele será classificado como 'Inocente'.
'''

sim = 0
perhuntas = ['Telefonou para a vitima? [s/n]: ',
             'Esteve no local do crime? [s/n]: ',
             'Mora perto da vitima? [s/n]: ',
             'Devia para a vitima? [s/n]: ',
             'Já trabalhou com a vítima? [s/n]: '
             ]
for i in range(len(perhuntas)):
    resposta = input(perhuntas[i])
    if resposta == 's':
        sim += 1
if sim == 2:
    print('\nSuspeita!')
elif sim > 2 and sim <= 4:
    print('\nCumplice!')
elif sim == 5:
    print('\nAssassino!')
else:
    print('\nInocente!')