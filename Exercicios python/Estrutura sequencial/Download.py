#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps). 
#Calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
tamanho_arquivo = float(input("Informe o tamnho em MB: "))
velocidade_internet = float(input("Informe a velocidade da internet em Mbps: "))
tamanho_arquivo = tamanho_arquivo * 8
tempo = tamanho_arquivo / velocidade_internet
tempo = tempo / 60
print('O tempo de download sera de aproximadamente %.2f minutos' %tempo)