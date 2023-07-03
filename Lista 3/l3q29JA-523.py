#Lista de Exercício 3 - Questão 29
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programação Web
#Professor: Italo Arruda
produtos = int(input("Digite a quantidade de produtos: "))
while produtos > 50:
    produtos = int(input("Digite a quantidade de produtos[menos que 50]: "))


precos = []
n_produto = 1
count = 0

for i in range(produtos):
    print("Produto NÂ° ", n_produto)
    preco = precos.append(float(input("Digite o preco do produto: ")))
    n_produto += 1

n_produto = 1
for j in range(produtos):
    print("Produto NÂ° ", n_produto, "= ", precos[count])
    count += 1
    n_produto += 1
