dicionario = {}
textao = input().lower()
textaosplitado = textao.split(" ")
qtdCaracter = len(textaosplitado)
especiais = '".,;:!?[}[{\|/'
texto = []

#Definir a funcao
def adicona():
  return
#Removendo especiais
for k in range(qtdCaracter):
  teste = textaosplitado[k]
  testeTamanho = len(teste)
  for j in especiais:
      teste = teste.replace(j, '')
      if teste not in texto:
        texto.append(teste)
      print(texto)
     # adiciona()
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