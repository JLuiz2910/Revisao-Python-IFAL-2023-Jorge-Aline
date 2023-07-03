#Lista de Exerc�cio 4 - Quest�o 20
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
#Exercicio 20
'''
As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado durante o ano que passou. 
Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono.

Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato laboral, chegou-se a seguinte forma de cálculo:
a.Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro; 
a.O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor mínimo; 
Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos, impostos ou outras particularidades. 
Seu programa deverá permitir a digitação do salário de um número indefinido (desconhecido) de salários. Um valor de salário igual a 0 (zero) encerra a digitação. 
Após a entrada de todos os dados o programa deverá calcular o valor do abono concedido a cada colaborador, de acordo com a regra definida acima. 
Ao final, o programa deverá apresentar:
        * O salário de cada funcionário, juntamente com o valor do abono;
        * O número total de funcionário processados;
        * O valor total a ser gasto com o pagamento do abono;
        * O número de funcionário que receberá o valor mínimo de 100 reais;
        * O maior valor pago como abono; 
A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos. Os valores podem mudar a cada execução do programa.

    Projeção de Gastos com Abono
    ============================ 
    
    Salário: 1000
    Salário: 300
    Salário: 500
    Salário: 100
    Salário: 4500
    Salário: 0
    
    Salário    - Abono     
    R$ 1000.00 - R$  200.00
    R$  300.00 - R$  100.00
    R$  500.00 - R$  100.00
    R$  100.00 - R$  100.00
    R$ 4500.00 - R$  900.00
    
    Foram processados 5 colaboradores
    Total gasto com abonos: R$ 1400.00
    Valor mínimo pago a 3 colaboradores
    Maior valor de abono pago: R$ 900.00
'''

funcionario = True
salario = []
abono = []

print('Projeção de Gastos com Abono')
print('=' * 28, '\n')

while funcionario != 0:
    valor = float(input('Salario: '))
    if valor == 0:
        break
    salario.append(valor)

print('\nSalário    - Abono')

for i in range(len(salario)):
    percentual = salario[i] * 0.20
    if percentual <= 100:
        percentual = 100
    print('R${:>8.2f} - R${:>8.2f}'.format(salario[i],percentual))
    abono.append(percentual)

val_min = abono.count(100)

print(f'''
Foram processados {len(salario)} colaboradores
Total gasto com abonos: R$ {sum(abono):.2f}
Valor mínimo pago a {val_min} colaboradores
Maior valor de abono pago: R$ {max(abono):.2f}
''')