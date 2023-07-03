#Lista de Exercício 3 - Questão 1
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programação Web
#Professor: Italo Arruda
#FaÃ§a um programa que peÃ§a uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja invÃ¡lido e continue pedindo atÃ© que o usuÃ¡rio informe um valor vÃ¡lido.

nota = float(input("Digite uma nota entre zero e 10: "))

while nota > 10 or nota < 0:
    nota = float(input("Informe um valor vÃ¡lido: "))
