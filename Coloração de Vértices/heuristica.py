#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Em 1976, Welsh e Powell propuseram o algoritmo LF (Large First), que analisa os
vértices em ordem decrescente de seus graus
[Garey e Johnson 1976].
'''

import sys
import numpy as np

'''
heuristica gulosa, ao qual consome os vertices por quantidade de vizinhos de
forma decrescente, verifica se um dos nó que deseja colorir tem a mesm coloração
se não tiver, aquele nó podera ser colorido.
'''
def heuristica_gulosa(FilePath,AdjacentDict):
    #se AdjacentDict == -1, dicionario de adjacencias = FilePath
    Sat_V_E = {}
    if(AdjacentDict != -1):
        V_E = AdjacentDict
    else:
        V_E = CreateAdjDict(FilePath)

    color = [-1]*(len(V_E)) # cria o array de cores transparentes
    Sat_V_E = sorted(V_E.items(), key=lambda e: len(e[1]), reverse=True)
    #heuristica gulosa por saturação de vertices
    for i in Sat_V_E:
        for j in range(0,len(V_E)+1):
            if(len([k for k in i[1] if color[k]==j]) == 0):
                # print("colorindo o {} com {}".format(i[0],j))
                color[i[0]] = j
                break
    return(color)


'''
Cria uma lista de adjacencias do tipo dicionario
"nó : [vizinhos]"
'''
def CreateAdjDict(arg):
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
