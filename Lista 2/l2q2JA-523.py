#Lista de Exerc�cio 2 - Quest�o 11
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
#Lista de Exerc�cio 2 - Quest�o 11
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
#Lista de Exerc�cio 2 - Quest�o 11
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
#Lista de Exerc�cio 2 - Quest�o 11
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
'''

salario = float(input("Digite o seu salário"))

valor_baixo = salario * 0.20
baixo = salario * 1.20
valor_medio = salario * 0.15
medio = salario * 1.15
valor_alto = salario * 0.10
alto = salario * 1.10
valor_altissimo = salario * 0.05
altissimo = salario * 1.05

print("Antes Reajuste: ", salario)

if salario <= 280: print("Aumento: 20%\nValor: ", valor_baixo, "\nFinal: ", baixo)
elif salario > 200 and salario <= 700: print("Aumento: 15%\nValor: ", valor_medio, "\nFinal: ", medio)
elif salario > 700 and salario <= 1500: print("Aumento: 10%\nValor: ", valor_alto, "\nFinal: ", alto)
else: print("Aumento: 5%\nValor: ", valor_altissimo, "\nFinal: ", altissimo)
