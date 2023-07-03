#Lista de Exercício 3 - Questão 43
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programação Web
#Professor: Italo Arruda
codigos = [100, 101, 102, 103, 104, 105]
comidas = ['Cachorro Quente', 'Bauru Simples', 'Bauru com ovo', 'Hamburguer', 'ChesseBurguer', 'Refrigerante']
precos = [1.20, 1.30, 1.50, 1.20, 1.30, 1.0]
codigo = True
n_pedido = 1
pedido = []

while codigo != 0:
    print("\nPedido nÂ°", n_pedido)
    codigo = int(input("Digite o cÃ³digo do alimento: "))
    if codigo == 0:
        break
    else:
        while codigo not in codigos:
            print("[Este cÃ³digo nÃ£o corresponde a nenhum alimento.]")
            codigo = int(input("Digite o cÃ³digo do alimento: "))

        indice = codigos.index(codigo)
        quantidade = int(input("Digite a quantidade: "))
        valor_pedido = precos[indice] * quantidade
        pedido.append(valor_pedido)
    n_pedido += 1

pedido_nota = 0
print("\n" * 2)
for i in range(n_pedido - 1):
    print("Pedido nÂ°", pedido_nota + 1, "= R$", round(pedido[pedido_nota], 2))
    pedido_nota += 1
print("Total: R$", round(sum(pedido), 2))
