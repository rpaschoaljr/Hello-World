A,B,C,D = input().split()
int(A)
int(B)
int(C)
int(D)
if B > C:
    if D > A:
        if (D+C) > (A+B):
            if (C >= 0) and (D >= 0):
                if (A%2) == 0:
                    print("Valores aceitos")
else:
    print("Valores nao aceitos")