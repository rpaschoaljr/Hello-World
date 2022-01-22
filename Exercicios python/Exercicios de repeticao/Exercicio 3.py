#       Faça um programa que leia e valide as seguintes informações:
#           Nome: maior que 3 caracteres;
#           Idade: entre 0 e 150;
#           Salário: maior que zero;
#           Sexo: 'f' ou 'm';
#           Estado Civil: 's', 'c', 'v', 'd';

print("Digite o nome (maior que 3 caracter).")
nome = input("Digite o nome: ")
tamanho = len(nome)
while (tamanho < 4):
    print("O nome tem que ser maior que 3 letras!")
    nome = input("Digite o nome: ")
    tamanho = len(nome)
print("Digite a idade entre 0 e 150.")
idade = int(input("Digite a idade: "))
while (idade < 0 or idade > 150):
    print("Idade invalida digite entre 0 e 150!")
    idade = int(input("Digite a idade: "))
print("Informe um salario maior que 0.")
salario = float(input("Digite o salario: "))
while (salario <= 0):
    print("Salario invalido, tem que ser maior que zero!")
    salario = float(input("Digite o salario: "))
print("Sexo femino (F) ou masculino (M).")
sexo = input()
while ((sexo != "f") and (sexo != "F") and (sexo != "m") and (sexo != "M")):
    print("Sexo invalido favor digitar F ou M!")
    sexo = input()
print("Digite o estado civil solteiro(a) (S), casado(a) (C), viuvo(a) (V), divorciado(a) (D)")
estado_civil = input()
while (estado_civil != "S" and estado_civil != "s" and estado_civil != "C" and estado_civil != "c" and estado_civil != "V" and estado_civil != "v" and estado_civil != "d" and estado_civil != "D"):
    print("Estado civil incorreto favor usar S, C, V ou D. Sendo para solteiro(a), casado(a), viuvo(a) ou divorciado(a) respectivamente")
    estado_civil = input()