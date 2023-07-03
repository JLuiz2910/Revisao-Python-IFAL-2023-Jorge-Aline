#Lista de Exerc�cio 3 - Quest�o 16
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
#A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.

ultimo = 1
penultimo = 1
print(ultimo)
print(penultimo)
termo = 0

while termo < 500:
    termo = ultimo + penultimo
    penultimo = ultimo
    ultimo = termo
    if termo < 500:
        print(termo)
    else:
        print("O proximo valor será maior que 500")
