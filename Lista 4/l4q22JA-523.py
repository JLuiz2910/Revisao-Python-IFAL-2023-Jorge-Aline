#Lista de Exerc�cio 4 - Quest�o 22
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
#Exercicio 22
'''
Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
necessita da esfera;
necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:
Quantidade de mouses: 100

Situação                        Quantidade              Percentual
1- necessita da esfera                  40                     40%
2- necessita de limpeza                 30                     30%
3- necessita troca do cabo ou conector  15                     15%
4- quebrado ou inutilizado              15                     15%
'''

defeitos = ['necessita da esfera',
            'necessita de limpeza',
            'necessita troca do cabo ou conector',
            'quebrado ou inutilizado'
            ]
numeros_identificacao = []
numeros_defeitos = []
numero_identificacao = True
n_mouse = 1
while numero_identificacao != 0:
    print('\nMouse n°', n_mouse)
    numero_identificacao = int(input('Digite o número de identificação do mouse: '))
    if numero_identificacao == 0:
        break
    else:
        while numero_identificacao in numeros_identificacao:
            print('[Número repetido]')
            print('\nMouse n°', n_mouse)
            numero_identificacao = int(input('Digite o número de identificação do mouse: '))
        numero_defeito = int(input('Digite o número correspondente ao defeito: '))
        while numero_defeito > 4 or numero_defeito < 1:
            print('[Número invalido]')
            numero_defeito = int(input('Digite o número correspondente ao defeito: '))
        numeros_identificacao.append(numero_identificacao)
        numeros_defeitos.append(numero_defeito)
    n_mouse += 1
print('\nQuantidade de mouses: ', len(numeros_identificacao))
for i in range(len(defeitos)):
    print('Situação: ', defeitos[i], '/ Quantidade: ', numeros_defeitos.count(i + 1), '/ Porcentagem: ', round(100 * numeros_defeitos.count(i + 1) / len(numeros_identificacao), 2), '%')