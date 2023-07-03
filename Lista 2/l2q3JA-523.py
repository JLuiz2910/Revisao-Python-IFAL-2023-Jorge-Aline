#Lista de ExercÌcio 2 - Quest„o 12
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: ProgramaÁ„o Web
#Professor: Italo Arruda
#Lista de ExercÌcio 2 - Quest„o 12
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: ProgramaÁ„o Web
#Professor: Italo Arruda
#Lista de ExercÌcio 2 - Quest„o 12
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: ProgramaÁ„o Web
#Professor: Italo Arruda
#Lista de ExercÌcio 2 - Quest„o 12
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: ProgramaÁ„o Web
#Professor: Italo Arruda
'''
Fa√ßa um programa para o c√°lculo de uma folha de pagamento, sabendo que os descontos s√£o do Imposto de Renda, que depende do sal√°rio bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Sal√°rio Bruto, mas n√£o √© descontado (√© a empresa que deposita). O Sal√°rio L√≠quido corresponde ao Sal√°rio Bruto menos os descontos. O programa dever√° pedir ao usu√°rio o valor da sua hora e a quantidade de horas trabalhadas no m√™s.
Desconto do IR:
Sal√°rio Bruto at√© 900 (inclusive) - isento
Sal√°rio Bruto at√© 1500 (inclusive) - desconto de 5%
Sal√°rio Bruto at√© 2500 (inclusive) - desconto de 10%
Sal√°rio Bruto acima de 2500 - desconto de 20% Imprima na tela as informa√ß√µes, dispostas conforme o exemplo abaixo. No exemplo o valor da hora √© 5 e a quantidade de hora √© 220.
        Sal√°rio Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Sal√°rio Liquido                 : R$  935,00
'''

valor_hora = float(input("Quanto voc√™ ganha por hora? "))
horas_mes = int(input("Quantas horas voc√™ trabalha no m√™s? "))
salario_bruto = horas_mes * valor_hora

ir1500 = salario_bruto * 0.05
ir2500 = salario_bruto * 0.10
irmaior = salario_bruto * 0.20

inss = salario_bruto * 0.10
fgts = salario_bruto * 0.11

print("salario Bruto: ", salario_bruto)

if salario_bruto <= 900:
    print("Seu salario permanecer√° o mesmo")
else:
    print("INSS: ", inss, "\nFGTS: ", fgts)

if salario_bruto > 900 and salario_bruto <= 1500:
    salario_liquido = float(salario_bruto) - float(ir1500) - float(inss)
    print("IR: ", ir1500, "\nSalario Liquido: ", salario_liquido)

elif salario_bruto > 1500 and salario_bruto <= 2500:
    salario_liquido = float(salario_bruto) - float(ir2500) - float(inss)
    print("IR: ", ir2500, "\nSalario Liquido: ", salario_liquido)

else:
    salario_liquido = float(salario_bruto) - float(irmaior) - float(inss)
    print("IR: ", iralto, "\nSalario Liquido: ", salario_liquido)
