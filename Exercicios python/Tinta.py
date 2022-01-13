"""""Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total."""""
metros_cliente = float(input("Quantos metros serao pintados: "))
latas = metros_cliente // 54
resto_das_latas = metros_cliente % 54

if latas == 0:
    print('Total de latas a serem compradas = 1\nTotal a ser pago = R$80,00')
elif latas >= 1:
    if resto_das_latas != 0:
        latas = latas + 1
        total_a_pagar = latas * 80
        print(f'Total de latas a serem compradas = {"%.0f"}\nTotal a ser pago = {"%.2f"}' %(latas, total_a_pagar))
    else:
        total_a_pagar = latas * 80
        print(f'Total de latas a serem compradas = {"%.0f"}\nTotal a ser pago = {"%.2f"}' %(latas, total_a_pagar))
