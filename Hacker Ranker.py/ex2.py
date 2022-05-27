#   https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true


if __name__ == '__main__':
    n = int(input())
    lista = list(map(int, input().split()))   
    lista.sort()
    vari1 = 1
    vari2 = 2
    vari3 = 3
    i = 0
    while i != n:
        if lista[n-vari2] != lista[n-vari1]:
            print(lista[n-vari2])
            i = n
        else:
            vari1 += 1
            vari2 += 1
            vari3 += 1