#Lista de Exercício 2 - Questão 4
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programação Web
#Professor: Italo Arruda
#FaÃ§a um Programa que verifique se uma letra digitada Ã© vogal ou consoante.

letra = input("Digite uma letra: ")
vogais = ['a', 'e', 'i', 'o', 'u']

if letra in vogais: print('VOGAL')
else: print('CONSOANTE')
