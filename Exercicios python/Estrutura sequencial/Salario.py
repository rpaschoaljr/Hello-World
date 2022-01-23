horas = float(input('Digite quantas horas fez no mes: '))
salario_hora = float(input('Digite quanto ganha por hora: '))
salario_mes = horas * salario_hora
print(f'Seu salario sera de {"%.2f"}' %salario_mes)