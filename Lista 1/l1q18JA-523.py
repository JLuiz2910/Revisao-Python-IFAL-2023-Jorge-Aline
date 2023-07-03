#Lista de ExercÌcio 1 - Quest„o 18
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: ProgramaÁ„o Web
#Professor: Italo Arruda
#Fa√ßa um programa que pe√ßa o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
from math import ceil

tamanho = float(input("Digite o tamanho do arquivo: "))
velocidade = float(input("Digite a velocidade da internet: "))

tempo = tamanho / velocidade
minutos = ceil(tempo) / 60)

print("O arquivo levar√° ", minutos, "minutos para ficar pronto")
