#Lista de Exerc�cio 3 - Quest�o 30
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
paes = int(input("Digite a quantidade de pães: "))
while paes > 50:
    produtos = int(input("Digite a quantidade de produtos[menos que 50]: "))

count = 1
preco_pao = float(input("Qual é o preço do pão? : "))

for j in range(paes):
    print(count, "= R$", round(preco_pao * count, 2))
    count += 1
