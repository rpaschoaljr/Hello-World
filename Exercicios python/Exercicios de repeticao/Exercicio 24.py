#   Faça um programa que calcule o mostre a média aritmética de N notas.

n_notas = int(input("Quantas notas serao calculadas: "))
notas = []
a = 0
b = 0
c = 1
for i in range(n_notas):
    nota = float(input("Informe as notas: "))
    notas.append(nota)
quantidade_notas = len(notas)
soma = sum(number for number in notas)
media = soma / quantidade_notas
print("A media e %.2f" %(media))