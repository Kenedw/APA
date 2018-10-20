#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Em 1976, Welsh e Powell propuseram o algoritmo LF (Large First), que analisa os vértices em ordem decrescente de seus graus
[Garey e Johnson 1976].
'''
import sys
import numpy as np


#se AdjacentDict iqual a -1, dicionario de adjacencias seram buscadas no FilePath
def heuristica_gulosa(FilePath,AdjacentDict,keys):

    if(AdjacentDict != -1 or len(keys)):
        V_E = AdjacentDict
    else:
        V_E = CreateAdjDict(FilePath)
        keys = V_E.keys()

    color = np.zeros(max(keys)+1) # cria o array de cores como transparente

    for i in keys:
        color[i] = 1
        for j in V_E[i]:
            if(color[i] == color[j]):
                color[i] += 1
                # print("colorindo {} ligado a {} com {}".format(i[0],j,color[i[0]]))
    # print(color)
    # print("Numero de cores {}".format(int(max(color))))
    return color

#Cria um dicionario de adjacencias, entrar com o diretorio do arquivo
def CreateAdjDict(arg): #monta a dicionario de adjacencia
    out = {}
    if (len(arg) != 2):
        arq = open("instancias/DSJC125.1.col","r")
    else:
        arq = open("instancias/" + arg[1],"r")
    for j in arq:
        if(j[0] == 'e'):
            aux = map(int,j.split()[1:])
            for i in range(0,2): #para analizarmos nos dois sentidos da lista [1,2] e [2,1]
                if(aux[i] in out): #se existir no dicionario
                    out[aux[i]].append(aux[int(not i)]) #adicione o novo valor
                else:
                    out[aux[i]] = [aux[int(not i)]] #crie o novo elemento
    arq.close()
    return out

if __name__ == "__main__":
    heuristica_gulosa(sys.argv,-1,[])
