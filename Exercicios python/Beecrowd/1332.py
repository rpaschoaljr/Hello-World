escrito = ["one", "two", "three"]
print(escrito)
for i in range(len(escrito)):
    escritoSplitado = escrito[i].split()
    print(escritoSplitado)
    for letra in escritoSplitado:
        print(letra)
        