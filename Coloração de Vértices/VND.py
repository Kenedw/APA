#!/usr/bin/env python
# -*- coding: utf-8 -*-

from heuristica import CreateAdjDict, heuristica_gulosa
import sys
from random import shuffle
def main(arg):

    ''' Caso inicial do construtor guloso '''
    AdjDict = CreateAdjDict(arg)
    Mcolor = heuristica_gulosa("",AdjDict)
    # Mcolor = AdjDict.keys()
    # Mcolor.insert(0,0)
    Ncolor = len(set(Mcolor))
    print("------------------------------------------------------------------------")
    print(Mcolor)
    print("Numero de cores {}".format(Ncolor))
    print("------------------------------------------------------------------------")

    ''' buscando a vizinhança da heuristica '''
    before = Ncolor
    after = 0
    aux = Mcolor
    while(1):
        #Busca em vizinhança
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
    Ncolors = len(set(MatColor))
    result = True
    bins = []

    for i in range(1,Ncolors+1): #cria os buckets
        index = [j+1 for j, val in enumerate(MatColor) if val==i]
        bins.append(index)

    ListColors = set(MatColor)
    for buck in bins: #pega bucket
        for j in ListColors: #testa todas as cores
            for i in buck:  #testa todos os nó naquele bucket
                if(j != MatColor[i-1]): #não testa a sua cor
                    indexColor = [out for out, val in enumerate(MatColor) if val==j]
                    for k in indexColor: #indices da cor desejada
                        if(k in AdjDict[i]): #se existr um vizinho com aquela cor, não podemos pintar
                            result = False
                            break
                else:
                    result = False
            print("cor: {} para a cor: {} - {}".format(j,MatColor[buck[0]],result))
            if(result):
                for i in buck:
                    print("{} = {}".format(MatColor[i-1],j))
                    MatColor[i-1] = j
                    del ListColors[ListColors.index()]

            # print(MatColor)
    return MatColor

if __name__ == "__main__":
    main(sys.argv)
