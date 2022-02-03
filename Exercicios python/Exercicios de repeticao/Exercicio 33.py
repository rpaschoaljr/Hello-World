#   O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas,
#   e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.
temperaturas = []
a = 0
c = True
while c == True:
    while a == 0:

        print("Deseja adicionar uma temperatura? s/n")
        adicionar = input()
        if ((adicionar == "s") or (adicionar == "S")):
            a = 1
        elif ((adicionar == "n") or (adicionar == "N")):
            a = 2
        else:
            print("Opcao invalida!")
            b = True
            while b == True:
                    print("Deseja adicionar uma temperatura? s/n")
                    adicionar = input()
                    if ((adicionar == "s") or (adicionar == "S")):
                        a = 1
                        b = False
                    elif ((adicionar == "n") or (adicionar == "N")):
                        a = 2 
                        b = False
        list.sort(temperaturas)
        tamanho = len(temperaturas)            
    while a == 1:
        temp = float(input("Informe a temperatura: "))
        temperaturas.append(temp)
        a = 4
    while a == 2:
        tamanho = len(temperaturas)
        
        if tamanho == 1:
            print("Deseja sair? s/n")
            sair = input()
            if sair == "s" or sair == "S":
                c = False
                a = False
            elif sair == "n" or sair == "N":
                a = 4
        else:
            a = 4
    while a ==4:
        list.sort(temperaturas)
        tamanho = len(temperaturas)
        if (tamanho > 1):
            maior = temperaturas[tamanho - 1]
            menor = temperaturas[0]
            soma = sum(number for number in temperaturas)
            media = soma / tamanho
            print("A maior temperatura e %.1f, a menor temperatura e %.1f e a media de temperatura e %.2f" %(maior, menor, media))
            print("Deseja sair? s/n")
            sair = input()

        elif (tamanho == 1):
            print("A unica temperatura informada e %.1f"%temperaturas[0])
            print("Sem dados suficiente para comparacao.")
            print("Favor inserir mais uma temperatura para comparacao.")
            a = 0
        elif (tamanho == 0 and (adicionar == "n" or adicionar == "N")):
            print("Deseja sair? s/n")
            sair = input()
            if sair == "s" or sair == "S":
                c = False
                a = False
            elif sair == "n" or sair == "N":
                a = 0
        else:
            print("Error")
            print(a)
            print(c)
            print(tamanho)
            print(maior)
            print(menor)
            print(media)
            print(soma)
            print(temperaturas)
            print(adicionar)
print("Fechar")