#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = input('Digite uma letra: ')
tamanho = len(letra)

if tamanho != 1:
    print("Erro: digitou nenhuma ou mais de uma letra.")
elif letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print(f"A letra, {letra}, e uma vogal.")
elif letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
    print(f"A letra, {letra}, e uma vogal.")
elif letra.isnumeric() == True:
    print("Erro: digitou um numero.")    
else:
    print(f"A letra, {letra} e uma consoante.")
    