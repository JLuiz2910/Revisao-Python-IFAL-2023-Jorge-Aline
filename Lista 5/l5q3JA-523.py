#Lista de Exerc�cio 5 - Quest�o 3
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
#Lista de Exerc�cio 5 - Quest�o 3
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
#Exercicio 3
#Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def somar(a,b,c):
    print('soma =',a + b + c)

val = []
for i in range(3):
    print('\nArgumento n°', i + 1)
    arg = val.append(int(input('valor: ')))

somar(val[0],val[1],val[2])