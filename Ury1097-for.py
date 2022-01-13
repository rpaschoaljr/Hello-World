x = 7
z = 4
for i in range(1, 10, 2):
    if i > 1:
        x = x + 2
        z = z + 2
    for j in range(x, z, -1):
        print (f"I={i} J={j}")