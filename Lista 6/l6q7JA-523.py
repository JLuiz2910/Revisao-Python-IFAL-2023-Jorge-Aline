#Lista de ExercÌcio 6 - Quest„o 7
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: ProgramaÁ„o Web
#Professor: Italo Arruda
#Exercicio 7
'''
Conta espa√ßos e vogais. Dado uma string com uma frase informada pelo usu√°rio (incluindo espa√ßos em branco), conte:

    a.quantos espa√ßos em branco existem na frase.
    b.quantas vezes aparecem as vogais a, e, i, o, u.
'''

frase = str(input('Digite uma frase: ')).lower()
espacos = frase.count(' ')
vogais = []
for i in range(len(frase)):
    if frase[i] in ['a', 'e', 'i', 'o', 'u']:
        vogais.append(frase[i])
    else:
        continue
print('\nExistem ', espacos, 'espa√ßos na frase.')
print('A: ', vogais.count('a'), '\nE: ', vogais.count('e'), '\nI: ', vogais.count('i'), '\nO: ', vogais.count('o'), '\nU: ', vogais.count('u'))