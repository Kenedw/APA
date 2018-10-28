#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Em 1976, Welsh e Powell propuseram o algoritmo LF (Large First), que analisa os vértices em ordem decrescente de seus graus
[Garey e Johnson 1976].
'''
import sys
import numpy as np

#se AdjacentDict iqual a -1, dicionario de adjacencias seram buscadas no FilePath
def heuristica_gulosa(FilePath,AdjacentDict):
    Sat_V_E = {}
    if(AdjacentDict != -1):
        V_E = AdjacentDict
    else:
        V_E = CreateAdjDict(FilePath)

    color = [0]*(len(V_E)+1) # cria o array de cores transparentes
    Sat_V_E = sorted(V_E.items(), key=lambda e: len(e[1]), reverse=True)
    #heuristica gulosa por saturação de vertices
    blocklist = []
    for i in Sat_V_E:
        if(i[0] not in blocklist):
            color[i[0]] = color[i[0]] + 1
            blocklist.append(i[0])
            for j in V_E[i[0]]:
                if(j not in blocklist):
                    color[j] = color[i[0]]
    # del color[0]
    return [color for _,color in sorted(zip(Sat_V_E,color))]


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
    heuristica_gulosa(sys.argv,-1)
