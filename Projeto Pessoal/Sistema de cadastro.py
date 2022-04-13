#   Cadatrando usuarios em dicionario modelo de academia que mostra o IMC do usuario   
#   Variaveis globais
usuarios = {"Nome": {"Data de nascimento": {"CPF": {"RG": {"Peso": {"Altura"}}}}}}
#   Funcoes
def cadastro():
    

    return


#   Principal
print(usuarios)
while(True):
    print("")
    print(50 * "*")
    print("Bem vindo a academia murcha panca")
    print(50 * "*")
    print("")
    print("")
    print(50 * "*")
    print("Digite a opcao desejada:")
    print(50 * "*")
    print("")
    print("")
    print("1:" + 5 * " " + "Casdastrar novo usuario.")
    print("")
    print("2:" + 5 * " " + "Buscar usuario cadastrado.")
    print("")
    escolha = input()
    if escolha == '1':
        print("passou aqui 1")
    elif escolha == '2':
        print("passou aqui 2")
    else:      
        print("Escolha um numero valido.")