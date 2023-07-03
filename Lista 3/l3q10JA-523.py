#Lista de ExercÌcio 3 - Quest„o 10
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: ProgramaÁ„o Web
#Professor: Italo Arruda
#Fa√ßa um programa que receba dois n√∫meros inteiros e gere os n√∫meros inteiros que est√£o no intervalo compreendido por eles.

n1 = int(input("Digite um n√∫mero: "))
n2 = int(input("Digite outro n√∫mero: "))

for i in range(n1 + 1, n2):
        print(i)
for i in range(n2 + 1, n1):
        print(i)
