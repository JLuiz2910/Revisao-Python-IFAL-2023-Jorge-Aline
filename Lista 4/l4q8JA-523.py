#Lista de Exerc�cio 4 - Quest�o 8
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
#Exercicio 8
'''
Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. 
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