#Lista de Exercício 4 - Questão 6
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programação Web
#Professor: Italo Arruda
#Exercicio 6
'''
FaÃ§a um Programa que peÃ§a as quatro notas de 10 alunos, 
calcule e armazene num vetor a mÃ©dia de cada aluno, 
imprima o nÃºmero de alunos com mÃ©dia maior ou igual a 7.0.
'''

notas = []
media_turma = []

cont = 1
for i in range(10):
    print('\nAluno ',cont)
    for j in range(4):
        nota = float(input('Digite a nota: '))
        notas.append(nota)
    media = sum(notas) / len(notas)
    media_turma.append(media)
    print('\nNotas:', notas,'\nMedia: %.2f'% media)
    cont += 1
    notas.clear()

print('\nMelhores Medias\n')

for i in range(10):
    if media_turma[i] >= 7:
        print('Aluno nÂº ',i + 1,'Media: ',media_turma[i])