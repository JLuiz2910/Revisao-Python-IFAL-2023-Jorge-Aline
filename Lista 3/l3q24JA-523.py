#Lista de Exerc�cio 3 - Quest�o 24
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
numero_notas = int(input("Digite o número de notas que você irá digitar: "))
count = 0
todas_notas = []

while count < numero_notas:
    notas = todas_notas.append(float(input("Digite a nota: ")))
    count += 1

media = sum(todas_notas) / numero_notas
print("A média é igual a ", media)
