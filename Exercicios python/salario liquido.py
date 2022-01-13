horas_mes = float(input('Digite quantas horas fez no mes: '))
salario_hora = float(input('Digite quanto ganha na hora: '))
salario_bruto = horas_mes * salario_hora
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
descontos =  ir + inss + sindicato
salario_liquido = salario_bruto - descontos
print(f'+ Salario bruto = {"%.2f"}\n- IR (11%)= {"%.2f"}\n- INSS (8%) = {"%.2f"}\n- sindicato (5%) = {"%.2f"}\n= Salario liquido = {"%.2f"}\n' %(salario_bruto, ir, inss, sindicato, salario_liquido))