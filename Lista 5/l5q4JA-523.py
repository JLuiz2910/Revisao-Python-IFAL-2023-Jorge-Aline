#Lista de Exercício 5 - Questão 4
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programação Web
#Professor: Italo Arruda
#Lista de Exercício 5 - Questão 4
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programação Web
#Professor: Italo Arruda
#Exercicio 4
'''
FaÃ§a um programa, com uma funÃ§Ã£o que necessite de um argumento. 
A funÃ§Ã£o retorna o valor de caractere â€˜Pâ€™, se seu argumento for positivo, e â€˜Nâ€™, se seu argumento for zero ou negativo.
'''

def pos_ou_neg(n):
    if n > 0:
        print('P')
    else:
        print('N')

arg = int(input('valor: '))
pos_ou_neg(arg)