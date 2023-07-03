#Lista de ExercÌcio 3 - Quest„o 2
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: ProgramaÁ„o Web
#Professor: Italo Arruda
#Fa√ßa um programa que leia um nome de usu√°rio e a sua senha e n√£o aceite a senha igual ao nome do usu√°rio, mostrando uma mensagem de erro e voltando a pedir as informa√ß√µes.

nome = input("Digite o seu nome de usuario: ")
senha = input("Digite a sua senha: ")

while senha == nome:
    print("Erro, a senha n√£o pode ser igual ao nome de usuario!")
    nome = input("Digite o seu nome de usuario: ")
    senha = input("Digite a sua senha: ")
