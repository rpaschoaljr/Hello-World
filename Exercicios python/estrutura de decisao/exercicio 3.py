#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
sexo = input("Digite F para feminino ou M para masculino: ")
if sexo == "F" or sexo == "f":
    print("Sexo feminino")
elif sexo == "m" or sexo == "M":
    print("Sexo masculino")
else:
    print("Sexo invalido")