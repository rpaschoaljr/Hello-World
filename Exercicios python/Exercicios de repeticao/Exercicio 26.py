#   Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
#   Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

candidato_1 = 1
candidato_2 = 2
candidato_3 = 3
quantidade_eleitores = int(input("Informe a quantidade de eleitores: "))
voto_candidato_1 = 0
voto_candidato_2 = 0
voto_candidato_3 = 0
voto_nulo = 0
for i in range(quantidade_eleitores):
    voto = int(input("Digite o numero do candidato(1, 2 ou 3): "))

    if (voto == 1):
        voto_candidato_1 += 1
    elif (voto == 2):
        voto_candidato_2 += 1
    elif (voto == 3):
        voto_candidato_3 += 1
    else:
        print("voto nulo")
        voto_nulo += 1
print(f"O candidato 1 teve {voto_candidato_1} votos.")
print(f"O candidato 2 teve {voto_candidato_2} votos.")
print(f"O candidato 3 teve {voto_candidato_3} votos.")
print(f"Teve {voto_nulo} votos nulos.")