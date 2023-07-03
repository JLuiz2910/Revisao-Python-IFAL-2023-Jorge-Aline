#Lista de Exercício 1 - Questão 13
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programação Web
#Professor: Italo Arruda
#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fÃ³rmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

altura = float(input("Digite a altura: "))
homem = (72.7 * altura) - 58
mulher = (62.1 * altura) - 44.7

print("Homem: ", homem, "\nMulher: ", mulher)
