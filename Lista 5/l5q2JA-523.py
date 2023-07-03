#Lista de Exercício 5 - Questão 2
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programação Web
#Professor: Italo Arruda
#Lista de Exercício 5 - Questão 2
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programação Web
#Professor: Italo Arruda
#Exercicio 2
'''
FaÃ§a um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuÃ¡rio. Use uma funÃ§Ã£o que receba um valor n inteiro imprima atÃ© a n-Ã©sima linha.
'''

def executar(n, lista):
    for i in range(n):
         lista += str(i + 1) + "\t"     # \t Ã© igual Ã  TAB no teclado
         print(lista)
lista = ''
n = int(input("Digite n: "))
executar(n, lista)