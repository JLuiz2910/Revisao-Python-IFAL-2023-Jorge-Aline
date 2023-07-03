#Lista de Exerc�cio 4 - Quest�o 23
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
#Exercicio 23
'''
A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. 
Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, 
e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, 
ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":

alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125

Neste arquivo, o nome do usuário possui 15 caracteres. 
A partir deste arquivo, você deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:

ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB

O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, 
caso sejam necessários, de forma a agilizar a execução do programa. 
A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada, 
que será chamada pelo programa principal. O cálculo do percentual de uso também deverá ser feito através de uma função, 
que será chamada pelo programa principal.
'''

usuarios = []
uso_dados =[]
uso_dados_MB = []
percentual_MB = []

with open("c:/Users/Suporte/Desktop/Python study/usuarios.txt", 'r') as arquivo: #abrindo o arquivo txt do exercicio é necessario criar o arquivo
    for i in range(6):
        nome = arquivo.readline(15)
        nome = nome.replace(' ','') #remove os espaços em branco
        dados = arquivo.readline(18)
        dados = dados.replace(' ','') #remove os espaços em branco
        dados = int(dados.replace('\n','')) #remove os '\n' e transforma em inteiro
        usuarios.append(nome)
        uso_dados.append(dados)

def conversor_bytes(uso_dados):
    for i in range(len(uso_dados)):
        kilobyte = round(uso_dados[i] / 1024, 2)
        megabyte = round(kilobyte / 1024, 2)
        uso_dados_MB.append(megabyte)
            
def calc_percent(uso_dados_MB):
    for i in range(len(uso_dados_MB)):
        percentual = round(((100 * uso_dados_MB[i]) / sum(uso_dados_MB)), 2)
        percentual_MB.append(percentual)

def impressao(percentual_MB,usuarios):
    with open("c:/Users/Suporte/Desktop/Python study/relatório.txt", 'w') as arquivo: #criando o arquivo relatorio txt
        arquivo.write('ACME Inc.               Uso do espaço em disco pelos usuários\n')
        arquivo.write('-' * 72)
        arquivo.write('\n')
        arquivo.write('Nr.  Usuário        Espaço utilizado     % do uso\n')
        arquivo.write('\n')
        for i in range(len(usuarios)):
            arquivo.write(f'{i+1:<4} {usuarios[i]:<10} {uso_dados_MB[i]:>11} MB {percentual_MB[i]:>17}%\n')
        total = sum(uso_dados_MB)
        media = round(total / len(uso_dados_MB), 2)
        arquivo.write('\n')    
        arquivo.write(f'Espaço total ocupado: {total} MB\nEspaço médio ocupado: {media} MB')

conversor_bytes(uso_dados)
calc_percent(uso_dados_MB)
impressao(percentual_MB,usuarios)