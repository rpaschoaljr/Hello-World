#   Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.


numero = int(input("informe o numero: "))
cont = 0
divisores = []  # Segunda parte
for i in range(1,numero+1):
    teste = numero % i
    if (teste == 0):
        divisores.append(i) # Segunda parte
        cont += 1

if ((numero == 1) or (cont == 2)):
    print(f"O numero {numero} e um numero primo")
else:
    print(f"O numero {numero} nao e um numero primo e ele e dividido pelos numeros {divisores}")    # modifica para segunda parte
    
    
  
#                                                       Parte 2
#   Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

