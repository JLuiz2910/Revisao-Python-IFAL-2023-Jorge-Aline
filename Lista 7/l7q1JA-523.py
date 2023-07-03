#Lista de Exercício 7 - Questão 1
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programação Web
#Professor: Italo Arruda
#Exercicio 1
'''
Classe Bola: Crie uma classe que modele uma bola:

    a. Atributos: Cor, circunferÃªncia, material
    b. MÃ©todos: trocaCor e mostraCor
'''

class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self,cor):
        self.cor = cor

    def mostraCor(self):
        print('A cor da bola Ã©: ', self.cor)

#Teste Classe
bola_1 = Bola('Azul', 10, 'plÃ¡stico')
bola_1.trocaCor('Verde')
bola_1.mostraCor()