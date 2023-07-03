#Lista de Exercício 3 - Questão 23
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programação Web
#Professor: Italo Arruda
numero = int(input("\nDigite um nÃºmero: "))
lista = []
divisoes = 0

for i in range(numero + 1):
    if i % 2 == 1 and i != 2:
        lista.append(i)
        divisoes += 1
    else:
        divisoes += 1
print("NÃºmeros primos: ", lista)
print("NÃºmero de divisÃµes", divisoes)
