"""Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias."""

area_cliente = float(input('Informe a area a ser pintada: '))
arae_lata = 18.0*6
area_galao = 3.6 * 6
area_pintada_com_lata = area_cliente / arae_lata
area_pintada_com_galao = area_cliente / area_galao
area_mista = (area_cliente // arae_lata) + (area_cliente % arae_lata) / area_galao
print(area_pintada_com_galao)
print(area_pintada_com_lata)
print(area_mista)
print(arae_lata)
print(area_galao)