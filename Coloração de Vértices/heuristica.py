#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Em 1976, Welsh e Powell propuseram o algoritmo LF (Large First), que analisa os vértices em ordem decrescente de seus graus
[Garey e Johnson 1976].
'''
import sys
import numpy as np


#se AdjacentList iqual a -1, lista de adjacencias seram buscadas no FilePath
def heuristica_gulosa(FilePath,AdjacentList):

    if(AdjacentList != -1):
        V_E = AdjacentList
    else:
        V_E = CreateAdjList(FilePath)

    color = np.zeros(max(V_E)[0]+1)
    for i in V_E:
        color[i[0]] = 1
        for j in i[1:]:
            if(color[i[0]] == color[j]):
                color[i[0]] += 1
                # print("colorindo {} ligado a {} com {}".format(i[0],j,color[i[0]]))
    # print(color)
    # print("Numero de cores {}".format(int(max(color))))
    return color

#Cria uma lista de adjacencias, entrar com o diretorio do arquivo
def CreateAdjList(arg): #monta a lista de adjacencia
    out = []
    before = -1
    index = -1
    if (len(arg) != 2):
        arq = open("instancias/DSJC250.9.col","r")
    else:
        arq = open("instancias/" + arg[1],"r")
    for j in arq:
        if(j[0] == 'e'):
            aux = map(int,j.split()[1:])
            if(aux[0] != before):
                out.append(aux)
                before = aux[0]
                index +=1
            else:
                out[index].append(aux[1])
    arq.close()
    return out

if __name__ == "__main__":
    heuristica_gulosa(sys.argv,-1)
