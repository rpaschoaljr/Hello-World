#   Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
#           Fatorial de: 5
#           5! =  5 . 4 . 3 . 2 . 1 = 120

fatorial = int(input("Digite o numero a se fazer o fatorial: "))
print(f"Fatorial de: {fatorial}")
print(f"{fatorial}! = ", end="")
cont = fatorial
while cont > 0:
    print(f"{cont} ", end="")
    if (cont > 1):
        print(" . ", end="")
    else:
        print(" = ", end="")
    cont -= 1
for i in range(1,fatorial):
    fatorial = fatorial * i
print(fatorial)