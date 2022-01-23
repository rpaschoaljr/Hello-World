n = float(input())

qtd_nota_100 = n // 100
nota_100 = qtd_nota_100 * 100
n = n - nota_100
qtd_nota_50 = n // 50
nota_50 = qtd_nota_50 * 50
n = n - nota_50
qtd_nota_20 = n // 20
nota_20 = qtd_nota_20 * 20
n = n - nota_20
qtd_nota_10 = n // 10
nota_10 = qtd_nota_10 * 10
n = n - nota_10
qtd_nota_5 = n // 5
nota_5 = qtd_nota_5 * 5
n = n - nota_5
qtd_nota_2 = n // 2
nota = qtd_nota_2 * 2
qtd_moeda_1 = n // 1
moeda_1 = qtd_moeda_1 * 1
n = n - moeda_1
qtd_moeda_50 = n // .50
moeda_50 = qtd_moeda_50 * .5
n = n - moeda_50
qtd_moeda_25 = n // .25
moead_25 = qtd_moeda_25 * .25
n = n - moead_25
qtd_moeda_10 = n // .10
moeda_10 = qtd_moeda_10 * .10
n = n - moeda_10
qtd_moeda_5 = n // .05
moeda_5 = qtd_moeda_5 * .05
n = n - moeda_5
qtd_moeda_01 = n // .01
print("NOTAS:")
print(str(qtd_nota_100) + " nota(s) de R$ 100.00")
print(str(qtd_nota_50) + " nota(s) de R$ 50.00")
print(str(qtd_nota_20) + " nota(s) de R$ 20.00")
print(str(qtd_nota_10) + " nota(s) de R$ 10.00")
print(str(qtd_nota_5) + " nota(s) de R$ 5.00")
print(str(qtd_nota_2) + " nota(s) de R$ 2.00")
print("MOEDAS:")
print(str(qtd_moeda_1) + " moeda(s) de R$ 1.00")
print(str(qtd_moeda_50) + " moeda(s) de R$ 0.50")
print(str(qtd_moeda_25) + " moeda(s) de R$ 0.25")
print(str(qtd_moeda_10) + " moeda(s) de R$ 0.10")
print(str(qtd_moeda_5) + " moeda(s) de R$ 0.05")
print(str(qtd_moeda_01) + " moeda(s) de R$ 0.01")