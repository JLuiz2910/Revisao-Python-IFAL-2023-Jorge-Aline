#Lista de Exerc�cio 2 - Quest�o 14
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
'''
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
'''

nota1 = float(input("Digite a nota1"))
nota2 = float(input("Digite a nota2"))
media = (nota1 + nota2) / 2

if media >= 0 and media <= 4:
    print("E")
elif media > 4 and media <= 6:
    print("D")
elif media > 6 and media <= 7.5:
    print("C")
elif media > 7.5 and media <= 9:
    print("B")
else:
    print("A")
