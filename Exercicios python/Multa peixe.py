peso = float(input('Informe o peso: '))
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print(f'A multa a ser paga sera de  {"%.2f"}' %multa)
else:
    print("Nao tem multa")