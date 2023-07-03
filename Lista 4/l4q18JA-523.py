#Lista de Exerc�cio 4 - Quest�o 18
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
#Exercicio 18
'''
Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos. Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem de programação C++. Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. Após o final da votação, o programa deverá exibir:
O total de votos computados;
Os númeos e respectivos votos de todos os jogadores que receberam votos;
O percentual de votos de cada um destes jogadores;
O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele.
Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo número do jogador. O programa deve fazer uso de arrays. O programa deverá executar o cálculo do percentual de cada jogador através de uma função. Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos. A função calculará o percentual e retornará o valor calculado. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa. Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em um arquivo texto no disco, obedecendo a mesma disposição apresentada na tela.
Enquete: Quem foi o melhor jogador?

Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 11
Número do jogador (0=fim): 10
Número do jogador (0=fim): 50
Informe um valor entre 1 e 23 ou 0 para sair!
Número do jogador (0=fim): 9
Número do jogador (0=fim): 9
Número do jogador (0=fim): 0

Resultado da votação:

Foram computados 8 votos.

Jogador Votos           %
9               4               50,0%
10              3               37,5%
11              1               12,5%
O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.
'''

votos = []
votos_jogadores_votados = []
numeros_jogadores_votados = []
voto = True
n_voto = 1
while voto != 0:
    print('Voto n°', n_voto)
    voto = int(input('Digite o número do jogador: '))
    if voto == 0:
        break
    else:
        while voto > 23 or voto < 1:
            print('[Voto inválido.]')
            print('Voto n°', n_voto)
            voto = int(input('Digite novamente: '))
        votos.append(voto)
    n_voto += 1
print('\nTotal de votos: ', len(votos))
contador = 1
for i in range(23):
    if contador not in votos:
        contador += 1
        continue
    else:
        votos_jogadores_votados.append(votos.count(contador))
        numeros_jogadores_votados.append(contador)
        print('\nVotos para o jogador camisa n°', contador, ' = ', votos.count(contador))
        print('Percentual de votos: ', round(100 * votos.count(contador) / len(votos), 2), '%')
        contador += 1
melhor = votos_jogadores_votados.index(max(votos_jogadores_votados))
print('\nO jogador mais votado foi o n°', numeros_jogadores_votados[melhor], 'com ', votos_jogadores_votados[melhor], 'votos')
print('Ganhou com', round(100 * votos_jogadores_votados[melhor] / len(votos), 2), '% dos votos')