#Lista de Exercício 2 - Questão 7
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programação Web
#Professor: Italo Arruda
#FaÃ§a um Programa que leia trÃªs nÃºmeros e mostre o maior e o menor deles.

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))

lista = [valor1, valor2, valor3]

print("Menor valor: ", min(lista), "\nMenor valor: ", max(lista))
