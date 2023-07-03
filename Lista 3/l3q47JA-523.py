#Lista de Exercício 3 - Questão 47
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programação Web
#Professor: Italo Arruda
import time
nome_atleta = True
n_atleta = 1
while nome_atleta != '':
    notas = []
    print("\n" * 5)
    print("Atleta nÂ°", n_atleta)
    nome_atleta = input("Digite o nome do atleta: ")
    if nome_atleta == '':
        break
    else:
        n_jurado = 1
        print("\n" * 3)
        for i in range(7):
            print("Jurado nÂ° ", n_jurado)
            nota = float(input("Digite a nota: "))
            notas.append(nota)
            n_jurado += 1
        print("Atleta: ", nome_atleta)
        n_jurado = 1
        count = 0
        for i in range(7):
            print(n_jurado, "Â° Jurado : ", notas[count])
            n_jurado += 1
            count += 1
        print("Resultado Final:")
        print("Nome do atleta: ", nome_atleta)
        print("Melhor nota: ", max(notas))
        print("Pior nota: ", min(notas))
        notas.remove(max(notas))
        notas.remove(min(notas))
        media = sum(notas) / len(notas)
        print("Media: ", round(media, 2))
        n_atleta += 1
        print("Reiniciando em 5 segundos")
        time.sleep(5)
