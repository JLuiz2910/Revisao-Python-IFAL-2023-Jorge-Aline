#Lista de Exerc�cio 7 - Quest�o 12
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
#Exercicio 12
'''
Classe Conta de Investimento: Faça uma classe contaInvestimento que seja semelhante a classe contaBancaria, com a diferença de que se adicione um atributo taxaJuros. 
Forneça um construtor que configure tanto o saldo inicial como a taxa de juros. 
Forneça um método adicioneJuros (sem parâmetro explícito) que adicione juros à conta. 
Escreva um programa que construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%. 
Depois aplique o método adicioneJuros() cinco vezes e imprime o saldo resultante.
'''

class ContaInvestimento:

    def __init__(self, numero, nomeCorrentista, taxaJuros, saldo=0.0):
        self.numero = numero
        self.alterarNome(nomeCorrentista)
        self.taxaJuros = taxaJuros
        self.saldo = saldo

    def alterarNome(self, nomeCorrentista):
        self.nomeCorrentista = nomeCorrentista

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor

    def adicionaJuros(self):
        self.saldo += (self.saldo * (self.taxaJuros / 100.0))

#Teste Classe
conta = ContaInvestimento(12345678, 'Joaquim', 10)
conta.deposito(1000)
print(f'R$ {conta.saldo:.2f}')
conta.adicionaJuros()
print(f'R$ {conta.saldo:.2f}')
conta.adicionaJuros()
print(f'R$ {conta.saldo:.2f}')
conta.adicionaJuros()
print(f'R$ {conta.saldo:.2f}')
conta.adicionaJuros()
print(f'R$ {conta.saldo:.2f}')