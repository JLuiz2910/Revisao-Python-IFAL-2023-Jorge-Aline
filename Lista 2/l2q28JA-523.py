#Lista de Exercício 2 - Questão 9
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programação Web
#Professor: Italo Arruda
#FaÃ§a um Programa que leia trÃªs nÃºmeros e mostre-os em ordem decrescente.

n1 = float(input("Digite o primeiro nÃºmero: "))
n2 = float(input("Digite o segundo nÃºmero: "))
n3 = float(input("Digite o terceiro nÃºmero: "))

lista = [n1, n2, n3]

lista.sort(key=float, reverse=True)

print("decrescente: ", lista)
