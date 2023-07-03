#Lista de Exerc�cio 2 - Quest�o 24
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
'''
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
'''

numero1 = float(input("Digite o número 1: "))
numero2 = float(input("Digite o número 2: "))
operacao = input("Digite a operação que deseja realizar: [+, -, /, *]: ")


def checar():
    if (resultado_operacao // 1 == resultado_operacao):
        print("Inteiro")
        if resultado_operacao % 2 == 0:
            print("Par")
            if resultado_operacao > 0:
                print("Positivo")
            else:
                print("Negativo")
        else:
            print("Impar")
    else:
        print("Decimal")


if operacao == '+':
    resultado_operacao = numero1 + numero2
    print("Resultado: ", resultado_operacao)
    checar()
elif operacao == '-':
    resultado_operacao = numero1 - numero2
    print("Resultado: ", resultado_operacao)
    checar()
elif operacao == '/':
    resultado_operacao = numero1 / numero2
    print("Resultado: ", resultado_operacao)
    checar()
elif operacao == '*':
    resultado_operacao = numero1 * numero2
    print("Resultado: ", resultado_operacao)
    checar()
else:
    print("Valor Invalido")
