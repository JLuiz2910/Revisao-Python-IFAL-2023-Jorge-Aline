#Lista de Exerc�cio 4 - Quest�o 4
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
#Exercicio 4
#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

caracteres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
vogais = ['a', 'e', 'i', 'o', 'u']
count = 0
while count < 5:
    if vogais[count] in caracteres:
        caracteres.remove(vogais[count])
    count += 1
print("\nExistem", len(caracteres), "consoantes")
print("Elas são : ", caracteres)