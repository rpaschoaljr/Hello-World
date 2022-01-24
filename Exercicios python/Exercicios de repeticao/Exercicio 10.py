#   Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

primeiro_numero = int(input("Digite um numero: "))
segundo_numero = int(input("Digite outro numero: "))

if (primeiro_numero > segundo_numero):
    for i in range(primeiro_numero, segundo_numero, 1):
        print(i)
elif (segundo_numero > primeiro_numero):
    for i in range(segundo_numero, primeiro_numero, 1):
        print(i)
else:
    print("Nao ha intervalo os numeros sao iguais.")