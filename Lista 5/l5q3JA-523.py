#Lista de Exercício 5 - Questão 3
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programação Web
#Professor: Italo Arruda
#Lista de Exercício 5 - Questão 3
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programação Web
#Professor: Italo Arruda
#Exercicio 3
#FaÃ§a um programa, com uma funÃ§Ã£o que necessite de trÃªs argumentos, e que forneÃ§a a soma desses trÃªs argumentos.

def somar(a,b,c):
    print('soma =',a + b + c)

val = []
for i in range(3):
    print('\nArgumento nÂ°', i + 1)
    arg = val.append(int(input('valor: ')))

somar(val[0],val[1],val[2])