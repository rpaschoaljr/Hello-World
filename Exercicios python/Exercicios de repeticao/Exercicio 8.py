#   Faça um programa que leia 5 números e informe a soma e a média dos números.

numeros= []
quantidade_de_numeros = int(input("Digite quantos numeros serao informados: "))
soma = 0
for i in range(0 , quantidade_de_numeros,1):
    numero = float(input("Digite os numeros: "))
    numeros.append(numero)
for i in range (0 , quantidade_de_numeros,1):
    soma = soma + numeros[i]
media = soma / quantidade_de_numeros
print("A soma e %.2f e media da soma dos numeros e %.2f " %(soma, media))