#Lista de Exerc�cio 3 - Quest�o 32
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
import math
numero = int(input("\nDigite o numero que quer realizar a fatorial : "))
count = numero
fatorial = math.factorial(numero)

for i in range(numero - 1):
    print(count, end=" * ")
    count -= 1
print("1 = ", fatorial)
