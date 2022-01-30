#   Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma.
#   As turmas não podem ter mais de 40 alunos.


numero_turmas = int(input("Informe o numero de turmas: "))
qtd_alunos = []
for i in range(numero_turmas):
    alunos = int(input("Informe a quantidade de alunos na turma: "))
    print(i)
    if (alunos <= 40 and alunos >= 0):
        qtd_alunos.append(alunos)
    else:
        print("Turma muito grande.")
        while (alunos > 40):
            alunos = int(input("Informe a quantidade de alunos, tem que ser menor que 40: "))
            if (alunos <= 40 and alunos >= 0):
                qtd_alunos.append(alunos)
            else:
                print("Turma muito grande.")  
soma = sum(number for number in qtd_alunos)
media = soma / numero_turmas
print("A media de alunos por turma e %.1f" %(media))