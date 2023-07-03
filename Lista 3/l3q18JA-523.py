#Lista de ExercÌcio 3 - Quest„o 18
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: ProgramaÁ„o Web
#Professor: Italo Arruda
#Fa√ßa um programa que, dado um conjunto de N n√∫meros, determine o menor valor, o maior valor e a soma dos valores.

lista = []
count = 0

quant = int(input("Digite a quantiade de n√∫mero que deseja digitar: "))
while quant != count:
    numero = lista.append(float(input("Digite um n√∫mero: ")))
    count += 1

print("Lista: ", lista, "\nMaior: ", max(lista), "\nMenor: ", min(lista))
print("Soma: ", max(lista) + min(lista))
