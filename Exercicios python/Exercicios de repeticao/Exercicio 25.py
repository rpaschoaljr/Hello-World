#   Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60;
#   e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

n_idade = int(input("Quantas pessoas tem na turma: "))
idades = []
for i in range(n_idade):
    idade = float(input("Informe as Idades: "))
    idades.append(idade)
quantidade_idades = len(idades)
soma = sum(number for number in idades)
media = soma / quantidade_idades
if (media <= 25):
    print("A turma e jovem.")
elif (media > 60):
    print("A turma e idosa.")
else:
    print("A turma e adulta")