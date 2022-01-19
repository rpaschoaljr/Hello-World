#   Faça um Programa que leia três números e mostre o maior e o menor deles.
primeiro_numero = int(input("Digite o primeiro numero: "))
segundo_numero = int(input("Digite o segundo numero: "))
terceiro_numero = int(input("Digite o terceiro numero: "))
numeros = [primeiro_numero, segundo_numero, terceiro_numero]
list.sort(numeros)
menor = numeros[0]
maior = numeros[2]
print(f'O maior numero e {maior} e o menor numero e {menor}')