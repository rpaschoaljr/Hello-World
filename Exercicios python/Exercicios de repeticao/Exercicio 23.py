#   Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
#   O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
#   Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

primos = []
n = int(input("Insira um numero para fazer os calculos: "))
divisoes = 0
cont = 0
numeros = []
for i in range(1,n+1):
    numeros.append(i)
for i in range(0,n-1):
    for j in range(1,numeros[i]+1):
        teste = numeros[i] % j
        divisoes +=1
        if (teste == 0):
            cont += 1
            primos.append(i)

print(numeros)
print(cont)
print(divisoes)
print(primos)