#Lista de Exercício 3 - Questão 35
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programação Web
#Professor: Italo Arruda
numero = int(input("\nDigite um nÃºmero: "))
lista = []

for i in range(numero + 1):
    if i % 2 == 1 and i != 2:
        lista.append(i)

print("NÃºmeros primos: ", lista)
