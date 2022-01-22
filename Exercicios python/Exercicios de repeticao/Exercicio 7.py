#   Faça um programa que leia 5 números e informe o maior número.
numeros= []
quantidade_de_numeros = int(input("Digite quantos numeros serao informados: "))

for i in range(0 , quantidade_de_numeros,1):
    numero = input("Digite os numeros: ")
    numeros.append(numero)
list.sort(numeros)
maior = numeros[quantidade_de_numeros-1]
print(f"O maior numeros e {maior}")