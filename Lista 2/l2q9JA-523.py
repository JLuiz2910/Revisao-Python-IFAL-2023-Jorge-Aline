#Lista de Exerc�cio 2 - Quest�o 18
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
'''
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
'''

data = input("Digite a data no seguinte modelo: [11/07/2002] :")
if len(data) != 10:
    print("ERRADO")
else:
    if data[2] != '/' or data[5] != '/':
        print("ERRADO")
    else:
        numeros_data = data.split('/')
        if int(numeros_data[0]) > 31:
            print("ERRADO")
        elif int(numeros_data[1]) > 12:
            print("ERRADO")
        else:
            print("CERTO")
