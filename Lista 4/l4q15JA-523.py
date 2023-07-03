#Lista de Exerc�cio 4 - Quest�o 15
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
#Exercicio 15
'''
Faça um programa que leia um número indeterminado de valores, correspondentes a notas, 
encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). 
Após esta entrada de dados, faça:
    a - Mostre a quantidade de valores que foram lidos;
    b - Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
    c - Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
    d - Calcule e mostre a soma dos valores;
    e - Calcule e mostre a média dos valores;
    f - Calcule e mostre a quantidade de valores acima da média calculada;
    g - Calcule e mostre a quantidade de valores abaixo de sete;
    h - Encerre o programa com uma mensagem;
'''

valores = []
media_alta = []
valores_7 = []
cont = 1
rep = True

while rep != 0:
    print('\nValor nº ',cont) 
    val = (int(input('\nDigite o valor: ')))
    if val == -1:
       break
    else:
       valores.append(val)
    cont += 1

print('\n' * 2)
print('Quantidade de valores: \n',len(valores))
print('Os valores: \n',valores)
valores.reverse()                #invertendo a lista
print('Os valores na ordem inversa \n',valores)
print('A soma dos valores: \n',sum(valores))

media = sum(valores) / len(valores)
valores.reverse()                #invertendo novamente para a posição original

for i in range(len(valores)):
    if valores[i] > media:
        media_alta.append(valores[i])
    if valores[i] < 7:
        valores_7.append(valores[i])

print('A média dos valores: \n',media)
print('A quantidade de valores acima da média calculada: \n',media_alta)
print('A quantidade de valores abaixo de sete: \n',valores_7)
print('\nPrograma concluido!')