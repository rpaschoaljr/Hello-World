#   A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.

n = int(input("Determine ate que termo ira exibir: "))
termo_1 = 0
termo_2 = 1
fibonacci = [termo_1, termo_2]
cont = 2
if(n>=3):
    while (n > cont):
        termo_3 = termo_1 + termo_2
        termo_1 = termo_2
        termo_2 = termo_3
        cont += 1
        if (termo_3 <= 500):
            fibonacci.append(termo_3)
        else:
            cont = n
print(fibonacci)