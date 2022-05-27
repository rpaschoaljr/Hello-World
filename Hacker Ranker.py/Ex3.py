# https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

if __name__ == '__main__':
    nomes = []
    pontos = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nomes.append(name)
        pontos.append(score)
    a = 0
    PontuacaoNotas = []
    for i in range (_+1):
        PontuacaoNotas.append({"Name": nomes[i], "Nota": pontos[i]})
    PontuacaoNotasOrganizados = sorted(PontuacaoNotas, key=lambda i: (i['Nota'], i['Name']))
    pontos.sort()
    i = 0
    n = _
    nomes.clear()
    while i != n:
        if pontos[i] != pontos[i+1]:
            SegundoMenor = pontos[i+1]            
            i = n
        elif pontos[i] == pontos[i+1]:
            i += 1
        else:
            i = n
    for i in PontuacaoNotasOrganizados: 
        if i['Nota'] != SegundoMenor:
            pass
        else:
            nomes.append(i['Name'])
    for nome in nomes:
        print(nome)