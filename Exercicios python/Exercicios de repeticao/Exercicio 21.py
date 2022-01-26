#   Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.


numero = int(input("informe o numero: "))
cont = 1
for i in range(1,numero):
    teste = numero % i
    print(teste)
    if (teste == 0):
        cont += 1
if ((numero == 1) or (cont == 2)):
    print(f"O numero {numero} e um numero primo")
else:
    print(f"O numero {numero} nao e um numero primo")
    print(cont)
