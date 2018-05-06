import math
import numpy as np
def formula(l,x):
    p1 = 0
    for i in range(len(l)-1):
        p1 = p1 +  ((l[i] - x[i]) ** 2)
        # print(l[i],x[i], p1)
    squad = math.sqrt(p1)
    return squad

def ordena(base, dis):
    cop = sorted(dis)
    nova = []
    # print(cop)
    # print(dis)
    for i in range(len(cop)):
        for j in range(len(dis)):
            if cop[i] == dis[j]:
                # print("{}x{}-{}\t\t{}".format(i,j,cop[i],base[j][3]))
                nova.append(base[j])

    # print("\n\n")
    # for i in range(len(nova)):
    #     print(base[i], nova[i])
    return nova

def calcula_distancia(base,x):
    d = []
    for i in range(len(base)):
        aux = formula(base[i], x)
        d.append(aux)
    # print(d)
    return d
    # baseordena(base,d)

def ff(f,i):
    # if i == 0:
    #     return
    # print(f)
    A,B = 0,0
    for j in range(i):
        if f[j][3] == 'A':
            A += 1
        else:
            B += 1
    # print("\n")

    if A == B:
        return '?'
    elif A > B:
        return 'A'
    else:
        return 'B'



def frequencia(ord):
    aux = 0
    m = []
    for i in range(len(ord)):
        f = []
        for j in range(i+1):
            f.append(ord[j])
            # print(ord[j])
            aux = i+1
        maior = ff(f,aux)
        m.append(maior)
    # print(m)
    A,B = 0,0
    for i in range(len(m)):
        if m[i] == 'A':
            A += 1
        else:
            B += 1
    if A == B:
        return '?'
    elif A > B:
        return 'A'
    else:
        return 'B'



def main():
    base = [
    [3,7,8,'A'],
    [3,2,9,'A'],
    [0,1,1,'B'],
    [4,1,2,'A'],
    [1,3,7,'B'],
    [1,1,1,'B'],
    ]
    x = [3,7,7]
    distancia = calcula_distancia(base,x)
    ordenado = ordena(base, distancia)
    freq = frequencia(ordenado)
    # for i in range(len(ordenado)):
    #     print(base[i], ordenado[i])
    print("a classe encontrada foi {}".format(freq))
    return

main()
