primeira_nota = float(input('Digite a primeira nota: '))
segunda_nota = float(input('Digite a segunda nota: '))
terceira_nota = float(input('Digite a terceira nota: '))
media = (primeira_nota + segunda_nota + terceira_nota) / 3

print("A media das notas é " + str(media))

if (media >= 6):
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")