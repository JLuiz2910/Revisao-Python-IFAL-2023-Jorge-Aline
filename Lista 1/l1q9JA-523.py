#Lista de Exerc�cio 1 - Quest�o 9
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
# Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9).
fahrenheit = float(input("Quantidade de graus Fahrenheit: "))
celsius = (fahrenheit - 32) / 9

print(fahrenheit, " graus Fahrenheit são iguais a ", celsius, " graus celsius")
