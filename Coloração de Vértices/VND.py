#!/usr/bin/env python
# -*- coding: utf-8 -*-

from heuristica import CreateAdjDict, heuristica_gulosa
import sys
from random import shuffle
def main(arg):

    ''' Caso inicial do construtor guloso '''
    AdjDict = CreateAdjDict(arg)
    Mcolor = heuristica_gulosa("",AdjDict,list(AdjDict.keys()))
    Ncolor = int(max(Mcolor))
    print("------------------------------------------------------------------------")
    print(Mcolor)
    print("Numero de cores {}".format(Ncolor))
    print("------------------------------------------------------------------------")

    ''' buscando a vizinhança da heuristica '''
    before = Ncolor
    after = 0
    aux = Mcolor
    while(1):
        #busca em vizinhança
        AfterMcolor = NeighborhoodSearch(AdjDict,Mcolor)
        after = int(max(AfterMcolor))

        #VND
        if(after >= before):
            break
        else:
            after,before = before,after
            aux = AfterMcolor

    print("------------------------------------------------------------------------")
    print(aux)
    print("Novo numero de cores {}".format(before))
    print("------------------------------------------------------------------------")

'''Shack'''
# def  NeighborhoodSearch(AdjDict):
#     KeyList = list(AdjDict.keys())
#     shuffle(KeyList)    #embaralha as chaves
#     return heuristica_gulosa("",AdjDict,KeyList)
def  NeighborhoodSearch(AdjDict, MatColor):
    Ncolors = int(max(MatColor))
    result = True
    bins = []
    for i in range(1,Ncolors+1): #cria os buckers
        index = [j for j, val in enumerate(MatColor) if val==i]
        bins.append(index)
    # print(bins)
    for buck in bins: #pega bucker
        for j in range(1,Ncolors+1): #testa todas as cores
            print("TESTANDO COR : {}".format(j))
            print("TESTANDO BUCKER : {}".format(buck))
            for i in buck:  #testa todos os nó naquele bucker
                if(j != MatColor[i]): #não testa a sua cor
                    indexColor = [out for out, val in enumerate(MatColor) if val==j]
                    # print(indexColor)
                    # print(AdjDict[i])
                    for k in indexColor:
                        # print(k)
                        if(k in AdjDict[i]): #se existr um vizinho com aquela cor, não podemos pintar
                            result = False
                            break
                    print(result)
                    if(not result):
                        break
            if(result):
                for i in buck:
                    MatColor[i] = j
                # print(MatColor)
    return MatColor

if __name__ == "__main__":
    main(sys.argv)
