#Lista de Exerc�cio 3 - Quest�o 33
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
n_temperaturas = int(input("Quantidade de temperaturas que irá digitar: "))
temperaturas = []
n_temperatura = 1
for i in range(n_temperaturas):
    print("Temperatura n° ", n_temperatura)
    temperatura = temperaturas.append(float(input("Digite a temperatura: ")))
    n_temperatura += 1

print("Maior temperatura = ", max(temperaturas))
print("Menor temperatura = ", min(temperaturas))
print("Média = ", round(sum(temperaturas) / len(temperaturas), 2))
