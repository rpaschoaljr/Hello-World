dicionario = {}
textao = input().lower()
textaosplitado = textao.split(" ")
qtdCaracter = len(textaosplitado)

#Definir a funcao
def adicona():
  return
#Removendo especiais
for i in range(qtdCaracter):
  teste = textaosplitado[i]
  testeTamanho = len(teste)
  for j in range(testeTamanho):
    if teste[j].isalpha():
      adiciona()
    else:
      teste = teste.replace(teste[0:testeTamanho], teste[0:testeTamanho-1])
      adiciona()
#Termino da remocao

#Transformar a parte abaixo em funcao
for i in range(qtdCaracter):
  caso = textaosplitado[i]
  if caso not in dicionario.keys():
    dicionario[caso] = 1
  else:
    dicionario[caso] += 1 
keys_ordenadas = sorted(dicionario)
for key in keys_ordenadas:
  print(f"{key} aparece {dicionario[key]} vez(es)")