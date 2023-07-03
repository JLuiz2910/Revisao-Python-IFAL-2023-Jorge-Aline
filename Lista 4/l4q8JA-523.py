#Lista de Exercício 4 - Questão 8
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programação Web
#Professor: Italo Arruda
#Exercicio 8
'''
FaÃ§a um Programa que peÃ§a a idade e a altura de 5 pessoas, armazene cada informaÃ§Ã£o no seu respectivo vetor. 
Imprima a idade e a altura na ordem inversa a ordem lida.
'''

idade = []
altura = []
n_pessoa = 1
for i in range (5):
    print('\nPessoa ', n_pessoa)
    ida = int(input('Digite a idade: '))
    alt = int(input('Digite a altura: '))
    idade.append(ida)
    altura.append(alt)
    n_pessoa += 1

idade.reverse()
altura.reverse()
print('\nIdade', idade,'\nAltura', altura)