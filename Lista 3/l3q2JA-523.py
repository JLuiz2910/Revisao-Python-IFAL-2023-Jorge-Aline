#Lista de Exerc�cio 3 - Quest�o 2
#Dupla: 2011316174 - Jorge Luiz e 2019322853 - Aline Lima
#Disciplina: Programa��o Web
#Professor: Italo Arruda
#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

nome = input("Digite o seu nome de usuario: ")
senha = input("Digite a sua senha: ")

while senha == nome:
    print("Erro, a senha não pode ser igual ao nome de usuario!")
    nome = input("Digite o seu nome de usuario: ")
    senha = input("Digite a sua senha: ")
