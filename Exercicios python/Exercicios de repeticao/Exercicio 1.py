#   Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
a = True

while a == True:
    nota = float(input("Digite uma nota entre 0 e 10: "))
    if (nota>=0) and (nota <= 10):
        print("Esta certo")
        a = False
    else:
        print("Nota invalidade por favor digite um valor entre 0 e 10!")