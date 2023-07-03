#Lista de ExercÌcio 7 - Quest„o 14
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: ProgramaÁ„o Web
#Professor: Italo Arruda
#Exercicio 14
'''
Aprimore a classe do exerc√≠cio anterior para adicionar o m√©todo aumentarSalario (porcentualDeAumento) que aumente o sal√°rio do funcion√°rio em uma certa porcentagem.
Exemplo de uso:
   harry=funcion√°rio("Harry",25000)
   harry.aumentarSalario(10)

'''
class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = float(salario)

    def getNome(self):
        return self.nome

    def getSalario(self):
        return self.salario

    def aumentarSalario(self, percentualDeAumento):
        self.salario += self.salario * (percentualDeAumento / 100.0)
        
#Teste Classe
harry = Funcionario("Harry", 25000)
harry.aumentarSalario(10)
print (f'Nome: {harry.getNome()}')
print (f'Salario: R$ {harry.getSalario():.2f}')