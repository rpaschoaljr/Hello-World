#   Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3%,
#   e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
#   Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
#   Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.



populacao_a = int(input("Informe a quantidade de populacao do primeiro pais: "))
taxa_crescimento_a = float((input("Informe a taxa de crescimento em %: ")))
populacao_b = int(input("Informe a quantidade de populacao do segundo pais: "))
taxa_crescimento_b = float((input("Informe a taxa de crescimento em %: ")))
anos = 0
taxa_crescimento_a = taxa_crescimento_a/100
taxa_crescimento_b = taxa_crescimento_b/100
if (taxa_crescimento_b >= taxa_crescimento_a and populacao_a < populacao_b):
    print("Impossivel alcancar")
else:
    while (populacao_a <= populacao_b):
        aumento_populacao_a = populacao_a * taxa_crescimento_a
        aumento_populacao_b = populacao_b * taxa_crescimento_b
        populacao_a = populacao_a + aumento_populacao_a
        populacao_b = populacao_b + aumento_populacao_b
        anos = anos + 1
    print(f"O total de anos para o pais A para o pais B sera de {anos}")


