linha = input()
linha_spliatada = linha.split(" ")
a = float(linha_spliatada[0])
b = float(linha_spliatada[1])


if a > 0 and b > 0:
    print("Q1")
elif a < 0 and b > 0:
    print("Q2")
elif a < 0 and b < 0:
    print("Q3")
elif a > 0 and b < 0:
    print("Q4")
elif a == 0 and (b != 0):
    print("Eixo X")
elif (a != 0) and b == 0:
    print("Eixo Y")
else:
    print("Origem")