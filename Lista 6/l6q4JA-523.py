#Lista de Exercício 6 - Questão 4
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programação Web
#Professor: Italo Arruda
#Exercicio 4
'''
Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

    F
    FU
    FUL
    FULA
    FULAN
    FULANO
'''

nome = str(input('Informe o nome: '))
vazia = ''
for letra in nome:
    vazia += letra
    print(vazia)