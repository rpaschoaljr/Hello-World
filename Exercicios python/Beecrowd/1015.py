p1 = list(map(float, input().split()))
p2 = list(map(float, input().split()))
distancia = (((p2[0]-p1[0])**2) + ((p2[1]-p1[1])**2))**0.5
print(f'{distancia:.4f}')