#   Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
#   O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
#   Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

primos = []
n = int(input("as: "))
divisoes = 0
for j in range(0,n+1):
    numero = j
    cont = 0
    for i in range(1,numero+1):
        teste = numero % i
        divisoes += 1
        if (teste == 0):
            divisores.append(i) # Segunda parte
            cont += 1
    if ((numero == 1) or (cont == 2)):
        primos.append(numero)
print(primos)
print(divisoes)
    