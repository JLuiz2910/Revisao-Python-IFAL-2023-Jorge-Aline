#Lista de ExercÌcio 4 - Quest„o 24
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: ProgramaÁ„o Web
#Professor: Italo Arruda
#Exercicio 24
'''
Fa√ßa um programa que simule um lan√ßamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . 
Depois, mostre quantas vezes cada valor foi conseguido. 
Dica: use um vetor de contadores(1-6) e uma fun√ß√£o para gerar numeros aleat√≥rios, simulando os lan√ßamentos dos dados.
'''

import random
lancamentos = []
for i in range(100):
    lancamentos.append(random.randrange(1, 6 + 1))
for i in range(6):
    print('O n√∫mero', i + 1, 'foi gerado ', lancamentos.count(i + 1), 'vezes')