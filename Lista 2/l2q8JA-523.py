#Lista de ExercÌcio 2 - Quest„o 17
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: ProgramaÁ„o Web
#Professor: Italo Arruda
'''
Fa√ßa um Programa que pe√ßa um n√∫mero correspondente a um determinado ano e em seguida informe se este ano √© ou n√£o bissexto.
'''

ano = int(input("Digite o ano"))

if (ano%4 == 0 and ano%100 != 0) or ano%400 == 0:
    print("Bissexto")
else:
    print("N√£o Bissexto")
