#   Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

numeros = []
par = []
contador_par = 0
contador_impar = 0
for i in range(0 , 10):
    numero = int(input("Digite os numeros: "))
    numeros.append(numero)

for i in range(0 , 10):
    par = numeros[i] % 2
    if (par == 0):
        contador_par =  contador_par + 1
    else:
        contador_impar = contador_impar + 1
print(f'Ha {contador_impar} numeros impar e {contador_par} numeros par')