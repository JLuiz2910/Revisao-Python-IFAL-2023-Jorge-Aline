#Lista de Exerc�cio 1 - Quest�o 15
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:

#Salário Bruto : R$
#IR (11%) : R$
#INSS (8%) : R$
#Sindicato ( 5%) : R$
#Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido.

quant_hora = float(input("Quanto você ganha por hora? R: "))
horas_mes = int(input("Quantas horas você trabalha no mês? R: "))
salario = quant_hora * horas_mes

ir = salario * 0.11
inss = salario * 0.08
sindicato = salario * 0.05
salario_liquido = salario - ir - inss - sindicato

print("Salário bruto: ", salario, "\nIR: ", ir, "\nINSS: ", inss, "\nSindicato ", sindicato, "\nSalário Liquido: ", salario_liquido)
