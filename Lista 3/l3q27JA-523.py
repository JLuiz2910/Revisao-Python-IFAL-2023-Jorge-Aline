#Lista de ExercÌcio 3 - Quest„o 27
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: ProgramaÁ„o Web
#Professor: Italo Arruda
turmas = int(input("Quantas turmas? : "))
alunos_turmas = []
turma = 1

for i in range(turmas):
    print("turma ", turma)
    alunos = int(input("Alunos da turma : "))
    while alunos > 40:
        print("turma ", turma, " [uma turma s√≥ pode ter 40 alunos]")
        alunos = int(input("Alunos da turma : "))
    turma += 1
    alunos_turmas.append(alunos)

media = sum(alunos_turmas) / len(alunos_turmas)
print("A media e igual a: ", media)
