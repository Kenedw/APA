#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Em 1976, Welsh e Powell propuseram o algoritmo LF (Large First), que analisa os vértices em ordem decrescente de seus graus
[Garey e Johnson 1976].
'''
import sys
import numpy as np

def main(arg):
    V_E = InputFile(arg)
    color = np.zeros(max(V_E)[0]+1)
    for i in V_E:
        color[i[0]] = 1
        for j in i[1:]:
            if(color[i[0]] == color[j]):
                color[i[0]] += 1
                # print("colorindo {} ligado a {} com {}".format(i[0],j,color[i[0]]))
    print(color)
    print("Numero de cores {}".format(int(max(color))))

def InputFile(arg): #monta a lista de
    out = []
    after = -1
    index = -1

    if len(arg) != 2:
        arq = open("instancias/DSJC125.1.col","r")
    else:
        arq = open("instancias/" + arg[1],"r")
    for j in arq:
        if(j[0] == 'e'):
            aux = map(int,j.split()[1:])
            if(aux[0] != after):
                out.append(aux)
                after = aux[0]
                index +=1
            else:
                out[index].append(aux[1])
    arq.close()
    return out


if __name__ == "__main__":
    main(sys.argv)
