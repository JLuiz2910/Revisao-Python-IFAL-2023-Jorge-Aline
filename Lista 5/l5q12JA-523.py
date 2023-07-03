#Lista de ExercÌcio 5 - Quest„o 12
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: ProgramaÁ„o Web
#Professor: Italo Arruda
#Lista de ExercÌcio 5 - Quest„o 12
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: ProgramaÁ„o Web
#Professor: Italo Arruda
#Exercicio 12
'''
Embaralha palavra. Construa uma fun√ß√£o que receba uma string como par√¢metro e devolva outra string com os carateres embaralhados. 
Por exemplo: se fun√ß√£o receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combina√ß√£o poss√≠vel, de forma aleat√≥ria. 
Padronize em sua fun√ß√£o que todos os caracteres ser√£o devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.
'''

import random
def embaralhar_palavra(palavra):
    palavra_embaralhada = ''.join(random.sample(palavra,len(palavra)))
    return palavra_embaralhada
palavra = str(input("Digite uma palavra: "))
print(embaralhar_palavra(palavra))