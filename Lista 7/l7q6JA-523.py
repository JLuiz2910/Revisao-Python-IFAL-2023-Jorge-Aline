#Lista de Exercício 7 - Questão 6
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programação Web
#Professor: Italo Arruda
#Exercicio 6
'''
Classe TV: FaÃ§a um programa que simule um televisor criando-o como um objeto. 
O usuÃ¡rio deve ser capaz de informar o nÃºmero do canal e aumentar ou diminuir o volume. 
Certifique-se de que o nÃºmero do canal e o nÃ­vel do volume permanecem dentro de faixas vÃ¡lidas.
'''

class TV:
    def __init__(self, canal = 0, volume = 0):
        self.canal = canal
        self.volume = volume

    def set_canal(self,canal):
        if canal > 0 and canal < 100:
            self.canal = canal
        else:
            print('Canal indisponivel')

    def aumenta_volume(self):
        if self.volume < 100:
            self.volume += 1
    
    def diminui_volume(self):
        if self.volume > 0:
            self.volume -= 1

#Teste Classe
controle = TV()
controle.set_canal(11)
controle.aumenta_volume()
controle.aumenta_volume()
controle.aumenta_volume()
controle.diminui_volume()
controle.set_canal(200)
print(f'\nCanal: {controle.canal} \nVolume: {controle.volume}')