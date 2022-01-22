#   Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
#   mostrando uma mensagem de erro e voltando a pedir as informações.



usuario = input("Digite o usuario: ")
senha = input("Digite a senha: ")

while (usuario == senha):
        senha = input("Erro: a senha nao pode ser a mesma que o usuario, digite outra: ")