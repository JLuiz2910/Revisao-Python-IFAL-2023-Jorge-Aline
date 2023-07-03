#Lista de Exerc�cio 7 - Quest�o 5
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
#Exercicio 5
'''
Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. 
A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. 
Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.
'''

class Conta_Corrente:
    def __init__(self, numero_da_conta, nome_do_correntista, saldo=0.0):
        self.numero_da_conta = numero_da_conta
        self.nome_do_correntista = nome_do_correntista
        self.saldo = saldo    

    def alterarNome(self,nome_do_correntista):
        self.nome_do_correntista = nome_do_correntista 
        print('\nNome alterado para: ',self.nome_do_correntista)

    def deposito(self,valor):
        self.saldo += valor
        print('\nDeposito realizado no valor de: R$',valor, '\nO saldo atual é de: R$',self.saldo)

    def saque(self,valor):
        self.saldo -= valor
        print('\nSaque realizado no valor de: R$',valor, '\nO saldo atual é de: R$',self.saldo)

#Teste Classe
conta_1 = Conta_Corrente(2323232,'João') #pode colocar saldo se quizer

conta_1.alterarNome('Jose')
conta_1.deposito(100)
conta_1.saque(10)
print('\nSaldo R$',conta_1.saldo)