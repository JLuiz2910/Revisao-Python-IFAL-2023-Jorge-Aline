#Lista de Exerc�cio 5 - Quest�o 14
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
#Lista de Exerc�cio 5 - Quest�o 14
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
#Exercicio 14
'''
Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um
número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma. Por
exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9(sem repetição dos mesmos):
    8 3 4 
    1 5 9
    6 7 2
Elabore uma função que identifca e mostra na tela todos os quadrados mágicos com as
características acima. 
'''

from random import randint

# para geração dos números de forma aleatória entre 1 a 9, utiliza-se o randint para formação desses valores
def quadrado_magico3x3():
    linha_a = [2, 1, 3]
    linha_b = [0, 0, 1]
    linha_c = [0, 0, 0]
    soma_col1 = soma_col2 = soma_col3 = diagonal1 = diagonal2 = 0
    matriz = [linha_a, linha_b, linha_c]
    while not sum(linha_a) == sum(linha_b) == sum(
            linha_c) == soma_col1 == soma_col2 == soma_col3 == diagonal1 == diagonal2:
        linha_a.clear()
        linha_b.clear()
        linha_c.clear()
        soma_col1 = soma_col2 = soma_col3 = diagonal1 = diagonal2 = 0
        while len(linha_a) != 3:
            x = randint(1, 9)
            if x not in linha_a:
                linha_a.append(x)
        while len(linha_b) != 3:
            x = randint(1, 9)
            if x not in linha_a and x not in linha_b:
                linha_b.append(x)
        while len(linha_c) != 3:
            x = randint(1, 9)
            if x not in linha_b and x not in linha_c and x not in linha_a:
                linha_c.append(x)
        soma_col1 = linha_a[0] + linha_b[0] + linha_c[0]
        soma_col2 = linha_a[1] + linha_b[1] + linha_c[1]
        soma_col3 = linha_a[2] + linha_b[2] + linha_c[2]
        diagonal1 = linha_a[0] + linha_b[1] + linha_c[2]
        diagonal2 = linha_a[2] + linha_b[1] + linha_c[0]
   
  return matriz

# leitura da matriz formada

Matriz = quadrado_magico3x3()
for lin in range(3):
    for col in range(3):
        print(f'[{Matriz[lin][col]}]', end=' ')
    print()