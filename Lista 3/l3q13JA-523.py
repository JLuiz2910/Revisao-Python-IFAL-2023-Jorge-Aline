#Lista de Exerc�cio 3 - Quest�o 13
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
#Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

base = int(input("Digite a base: "))
expoente = int(input("Digite expoente: "))
resultado = 1

for i in range(expoente):
    resultado = base * base
    resultado = base * resultado

print(resultado)
