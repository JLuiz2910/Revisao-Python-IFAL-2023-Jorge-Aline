#Lista de ExercÌcio 1 - Quest„o 11
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: ProgramaÁ„o Web
#Professor: Italo Arruda
# Fa√ßa um Programa que pe√ßa 2 n√∫meros inteiros e um n√∫mero real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

inteiro1 = int(input("Digite um n√∫mero inteiro: "))
inteiro2 = int(input("Digite outro n√∫mero inteiro: "))
real = float(input("Digite um n√∫mero real"))

a = (inteiro1 * 2) + (inteiro2 / 2)
b = (inteiro1 * 3) + real
c = real ** 3

print("a : ", a, "\nb : ", b, "\nc : ", c)
