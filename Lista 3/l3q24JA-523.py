#Lista de Exercício 3 - Questão 24
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programação Web
#Professor: Italo Arruda
numero_notas = int(input("Digite o nÃºmero de notas que vocÃª irÃ¡ digitar: "))
count = 0
todas_notas = []

while count < numero_notas:
    notas = todas_notas.append(float(input("Digite a nota: ")))
    count += 1

media = sum(todas_notas) / numero_notas
print("A mÃ©dia Ã© igual a ", media)
