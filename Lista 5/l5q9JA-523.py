#Lista de Exercício 5 - Questão 9
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programação Web
#Professor: Italo Arruda
#Exercicio 9
#Reverso do nÃºmero. FaÃ§a uma funÃ§Ã£o que retorne o reverso de um nÃºmero inteiro informado. Por exemplo: 127 -> 721

def reverso(n):
    numeroInvertido = int(str(n)[::-1])
    print(numeroInvertido)
n = int(input('Digite o nÃºmero: '))
reverso(n)