#Lista de Exerc�cio 3 - Quest�o 25
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
n_pessoas = int(input("Digite o número de pessoas que ira digitar a idade: "))
lista = []

for i in range(n_pessoas):
    idade = lista.append(int(input("Digite a idade: ")))


if sum(lista) / len(lista) < 25:
    print("jovem")
elif sum(lista) / len(lista) >= 25 and sum(lista) / len(lista) < 60:
    print("adulto")
else:
    print("idosa")
