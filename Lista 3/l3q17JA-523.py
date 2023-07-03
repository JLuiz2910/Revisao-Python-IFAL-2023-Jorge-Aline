#Lista de ExercÌcio 3 - Quest„o 17
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: ProgramaÁ„o Web
#Professor: Italo Arruda
#Fa√ßa um programa que calcule o fatorial de um n√∫mero inteiro fornecido pelo usu√°rio. Ex.: 5!=5.4.3.2.1=120

numero = int(input("Digite um n√∫mero: "))
count1 = 0
count = 1
while count1 < numero:
    fatorial = numero * (numero - count)
    count = count - 1
    count1 = count + 1

print(fatorial)
