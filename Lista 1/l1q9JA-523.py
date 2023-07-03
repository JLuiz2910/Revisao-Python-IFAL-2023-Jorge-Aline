#Lista de Exercício 1 - Questão 9
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programação Web
#Professor: Italo Arruda
# FaÃ§a um Programa que peÃ§a a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9).
fahrenheit = float(input("Quantidade de graus Fahrenheit: "))
celsius = (fahrenheit - 32) / 9

print(fahrenheit, " graus Fahrenheit sÃ£o iguais a ", celsius, " graus celsius")
