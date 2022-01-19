#   Ler vários números e quando for 0 parar de ler, E vc mostrar o maior e o menor.
numeros = []
a = 1
while a == 1:
    varios = int(input('Digite numeros menos o 0 a nao ser que queria para: '))
    if varios == 0:
        a = 2
    else:
        numeros.append(varios)
while a == 2:
    tamanho = len(numeros)
    list.sort(numeros)
    tamanho_lista = tamanho - 1
    maior = numeros[tamanho_lista]
    menor = numeros[0]
    a = 3
    
print(f'O maior e {maior} e o menor e {menor}')