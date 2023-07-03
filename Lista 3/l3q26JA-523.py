#Lista de Exercício 3 - Questão 26
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programação Web
#Professor: Italo Arruda
eleitores = int(input("Digite o nÃºmero de eleitores: "))
votos = []

for i in range(eleitores):
    voto = votos.append(int(input("Qual candidato deseja votar? [1, 2, 3]: ")))

print("Quantidade de votos para candidato 1: ", votos.count(1))
print("Quantidade de votos para candidato 2: ", votos.count(2))
print("Quantidade de votos para candidato 3: ", votos.count(3))
