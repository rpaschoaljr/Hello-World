#   Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
#   Altere o programa anterior para mostrar no final a soma dos números.

primeiro_numero = int(input("Digite um numero: "))
segundo_numero = int(input("Digite outro numero: "))
contador = 0

if ((primeiro_numero+1) == segundo_numero) or ((primeiro_numero-1) == segundo_numero):
    print("Nao ha intervalo os numeros.")
elif (segundo_numero > primeiro_numero):
    for i in range((primeiro_numero+1), segundo_numero):
        print(i)
        contador = contador + 1
        a = True
elif (primeiro_numero > segundo_numero):
    for i in range((primeiro_numero-1), segundo_numero, -1):
        print(i)
        contador = contador + 1
        a = False
else:
    print("Nao ha intervalo os numeros sao iguais.")
    

# Segunda parte

numeros = []   
soma = 0
if (a == True):
    for i in range((primeiro_numero+1), segundo_numero):
        numeros.append(i)
elif (a == False):
    for i in range((primeiro_numero-1), segundo_numero, -1):
        numeros.append(i)
else:
    print("Nao a soma.")
for i in range (0 , contador):
    soma = soma + numeros[i]
print(f"A soma do intervalo e {soma}.")