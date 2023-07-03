#Lista de Exerc�cio 6 - Quest�o 6
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
#Exercicio 6
'''
Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.

    Data de Nascimento: 29/10/1973
    Você nasceu em  29 de Outubro de 1973.
'''

import datetime

def mesPorExtenso(mes):
    meses = [(), ['janeiro', 31], ['fevereiro', 29], ['março', 31], ['abril', 30],
                 ['maio', 31], ['junho', 30], ['julho', 31], ['agosto', 31], ['setembro', 30],
                 ['outubro', 31], ['novembro', 30], ['dezembro', 31]]
    
    dia, mes, ano = int(data[0]), int(data[1]), int(data[2])
    data_hoje = datetime.datetime.now()
    ano_hoje = data_hoje.year
    
    if mes == 2:
        meses[mes][1] = anoBissexto(ano)
    if 0 < mes < 13 and 0 < dia <= meses[mes][1] and 1900 < ano < ano_hoje:
        print(f'Data de Nascimento: {dia}/{mes}/{ano}')
        print(f'Você nasceu em {dia} de {meses[mes][0]} de {ano}')
    else:
        print('[Data inválida]')

#verifica se ano é bissexto
def anoBissexto(ano):
    if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
        return 29
    else:
        return 28

data = str(input('Digite a data [DD/MM/AAAA]:')).split("/") #separando dia, mes e ano em uma lista
mesPorExtenso(data)