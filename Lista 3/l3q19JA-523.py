#Lista de Exerc�cio 3 - Quest�o 19
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

lista = []
count = 0

quant = int(input("Digite a quantiade de número que deseja digitar: "))
while quant != count:
    numero = float(input("Digite um número: "))

    while numero > 1000 or numero < 0:
        numero = float(input("Digite um número[erro]: "))
        
    lista.append(numero)
    count += 1

print("Lista: ", lista, "\nMaior: ", max(lista), "\nMenor: ", min(lista))
print("Soma: ", max(lista) + min(lista))
