#Lista de Exerc�cio 3 - Quest�o 15
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

ultimo = 1
penultimo = 1
count = 1
print(ultimo)
print(penultimo)
while count <= 9:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
        print(termo)
