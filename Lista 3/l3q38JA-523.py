#Lista de Exerc�cio 3 - Quest�o 38
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
salario = float(input("Dgite o salario inicial do funcionario: "))
aumento = 1.5

for i in range(1996, 2018 + 1):
    aumento = aumento * 2
    salario_atual = salario + (salario * (aumento / 100))
    print("Salario em ", i, " = ", salario_atual)
