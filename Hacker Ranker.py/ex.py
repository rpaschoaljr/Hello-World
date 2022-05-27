# https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    listaX = []
    listaY = []
    listaZ = []
    matriz = []
    for i in range(x+1):    
        
        for j in range(y+1):
            
            for k in range(z+1):
               listaZ.append(k) 
               listaX.append(i) 
               listaY.append(j)
    combinacoes = len(listaX)
    
    lista = []
    for i in range (combinacoes):
        preMatriz = [0,0,0]
        preMatriz[0] = listaX[i]
        preMatriz[1] = listaY[i]
        preMatriz[2] = listaZ[i]
        lista = preMatriz
        if len(preMatriz) == 3:
            if sum(preMatriz) != n:
                matriz.append(lista)
                    
    print(matriz)