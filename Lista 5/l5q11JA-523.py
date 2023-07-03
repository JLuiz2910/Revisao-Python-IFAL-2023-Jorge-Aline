#Lista de Exercício 5 - Questão 11
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programação Web
#Professor: Italo Arruda
#Lista de Exercício 5 - Questão 11
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programação Web
#Professor: Italo Arruda
#Exercicio 11
'''
Data com mÃªs por extenso. Construa uma funÃ§Ã£o que receba uma data no formato DD/MM/AAAA 
e devolva uma string no formato D de mesPorExtenso de AAAA. 
Opcionalmente, valide a data e retorne NULL caso a data seja invÃ¡lida.
'''

import datetime

def mesPorExtenso(mes):
    meses = [(), ['janeiro', 31], ['fevereiro', 29], ['marÃ§o', 31], ['abril', 30],
                 ['maio', 31], ['junho', 30], ['julho', 31], ['agosto', 31], ['setembro', 30],
                 ['outubro', 31], ['novembro', 30], ['dezembro', 31]]
    
    dia, mes, ano = int(data[0]), int(data[1]), int(data[2])
    data_hoje = datetime.datetime.now()
    ano_hoje = data_hoje.year
    
    if mes == 2:
        meses[mes][1] = anoBissexto(ano)
    if 0 < mes < 13 and 0 < dia <= meses[mes][1] and 1900 < ano < ano_hoje:
        print(f'{dia} de {meses[mes][0]} de {ano}')
    else:
        print('NULL')

#verifica se ano Ã© bissexto
def anoBissexto(ano):
    if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
        return 29
    else:
        return 28

data = str(input('Digite a data [DD/MM/AAAA]:')).split("/") #separando dia, mes e ano em uma lista
mesPorExtenso(data)