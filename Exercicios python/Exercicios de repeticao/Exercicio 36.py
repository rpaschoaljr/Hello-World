#   Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
#   O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
#   Tabuada de 5:
#   5 X 1 = 5
#   5 X 2 = 10
#   ...
#   5 X 10 = 50
numero = int(input('Montar a tabuada de: '))
inicio = int(input("Começar por:  "))
final = int(input("Terminar em: "))
print("")
print("")
print(f"Vou montar a tabuada de {numero} começando em {inicio} e terminando em {final}:")
for i in range(inicio,final+1):
    mult = i * numero
    print(f'{numero} X {i} = {mult}')