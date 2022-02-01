#O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências.
# Faça um programa que implemente uma caixa registradora rudimentar.
# O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias.
# Um valor zero deve ser informado pelo operador para indicar o final da compra.
# O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco.
# Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
#           Lojas Tabajara 
#           Produto 1: R$ 2.20
#           Produto 2: R$ 5.80
#           Produto 3: R$ 0
#           Total: R$ 8.00
#           Dinheiro: R$ 20.00
#           Troco: R$ 12.00
#           ...
valores = []
a = 1
while a == 1:
    preco = float(input('Insira o preco: '))
    if preco == 0:
        total = sum(number for number in valores)
        a = 2
    else:
        valores.append(preco)
while a == 2:   
    dinheiro = float(input("Digite o valor recebido: "))
    troco = dinheiro - total
    if troco < 0:
        print("Dinheiro insulficiente!")
    else:
        tamanho = len(valores)
        a = 3
print("." *30)   
print("Lojas Tabajara")
print("." *30)
for i in range(0,tamanho):
    print("Poduto %d: R$ %.2f" %(i+1, valores[i]))
print("Total: R$ %.2f" %(total))
print("Dinheiro: R$ %.2f"%(dinheiro))
print("Troco: R$ %.2f" %(troco))
print("." *30)