h = float(input('Digite a altura em metros: '))
peso_homens = (72.7*h) - 58
peso_mulher = (62.1*h) - 44.7
print(f'O peso ideal para homens e {"%.2f"} e o peso ideal para mulher e {"%.2f"}' %(peso_homens, peso_mulher))