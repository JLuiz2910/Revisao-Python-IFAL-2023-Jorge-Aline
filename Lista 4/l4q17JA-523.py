#Lista de Exerc�cio 4 - Quest�o 17
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
#Exercicio 17
'''
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. 
O resultado do atleta será determinado pela média dos cinco valores restantes. 
Você deve fazer um programa que receba o nome e as cinco distâncias 
alcançadas pelo atleta em seus saltos e depois informe o nome,
os saltos e a média dos saltos. 
O programa deve ser encerrado quando não for informado o nome do atleta. 
A saída do programa deve ser conforme o exemplo abaixo:

    Atleta: Rodrigo Curvêllo
    
    Primeiro Salto: 6.5 m
    Segundo Salto: 6.1 m
    Terceiro Salto: 6.2 m
    Quarto Salto: 5.4 m
    Quinto Salto: 5.3 m
    
    Resultado final:
    Atleta: Rodrigo Curvêllo
    Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
    Média dos saltos: 5.9 m
'''

nome = True
contador = 1
saltos = []

while nome != 0:
    print('atleta ',contador)
    nome = str(input('Digite o nome do atleta: '))
    if nome == '':
        break
    else:
        for i in range(5):
            print(i + 1,'º Salto')
            distancia = float(input('Digite a distancia em metros do salto: '))
            saltos.append(distancia)    
    media = sum(saltos) / len(saltos)

    print('\nAtleta: ',nome,'\n')

    for i in range(5):
        print(i + 1,'º Salto:' ,saltos[i],'m')

    print('\nResultado final:')
    print('Atleta: ',nome)
    print('Saltos: ',saltos)
    print('Média dos saltos: ',media,'m')
    print('\n' * 3)
    contador += 1