from datetime import datetime, date 

nascimento = input("Digite a data em xx/xx/xxxx: ")
nascimentosplitado = nascimento.split("/")
nascimentosplitado[0] = int(nascimentosplitado[0])
nascimentosplitado[1] = int(nascimentosplitado[1])
nascimentosplitado[2] = int(nascimentosplitado[2])
idade = nascimentosplitado[2]