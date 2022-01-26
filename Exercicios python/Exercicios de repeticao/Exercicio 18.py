#   Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

numeros= []
quantidade_de_numeros = int(input("Digite quantos numeros serao informados: "))
soma = 0
for i in range(0 , quantidade_de_numeros):
    numero = int(input("Digite os numeros: "))
    numeros.append(numero)
for i in range (0 , quantidade_de_numeros):
    soma = soma + numeros[i]
media = soma / quantidade_de_numeros
list.sort(numeros)
maior = numeros[quantidade_de_numeros-1]
menor= numeros[0]
soma_mm = maior + menor
print("A soma de todos os numeros e %d e o maior e menor numero sao %d, %d e a soma do maior com o menor e %d " %(soma, maior, menor, soma_mm))