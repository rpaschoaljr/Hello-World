#   Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles.
#   O usuário deverá informar a quantidade de CDs e o valor para em cada um.

qtd_cds = int(input("Informe a quantidade de CD que possui: "))
preco_cd = []

for i in range(qtd_cds):
    preco = float(input("Informe o preco de cada CD: "))
    preco_cd.append(preco)
soma = sum(number for number in preco_cd)
media = soma / qtd_cds
print("O total gasto na colecao e de %.2f" %(media))