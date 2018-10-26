#!/usr/bin/env python
# -*- coding: utf-8 -*-

from heuristica import CreateAdjDict, heuristica_gulosa
import sys
from random import shuffle


graph_dict1 = {}

graph_dict1[0] = [1,4]
graph_dict1[1] = [0,2,4]
graph_dict1[2] = [1]
graph_dict1[3] = [4,5,6]
graph_dict1[4] = [0,1,3]
graph_dict1[5] = [3,6]
graph_dict1[6] = [3,5,7]
graph_dict1[7] = [6]

def main(arg):

    ''' Caso inicial do construtor guloso '''
    AdjDict = graph_dict1
    # AdjDict = CreateAdjDict(arg)
    Mcolor = heuristica_gulosa("",AdjDict)
    # Mcolor = heuristica_gulosa("",graph_dict1)
    # Mcolor = AdjDict.keys()
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
        bins = CreateBucketList(Mcolor)
        AfterMcolor = NeighborhoodSearch(AdjDict,Mcolor)
        after = len(set(AfterMcolor))

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
    result = True
    indexSelectColor = 0
    bins = CreateBucketList(MatColor)
    ListColors = set(MatColor)
    ListColors = list(ListColors)

    # print(ListColors)
    # print(bins)

    #VND
    for buck in bins: #pega bucket
        for ItemColor in ListColors: #testa todas as cores
            indexColor = bins[list(ListColors).index(ItemColor)] #lista de nó da cor desejada
            if(buck != indexColor): #não testa a sua cor
                result=True
                for i in buck:  #testa todos os nó naquele bucket
                    for k in indexColor: #indices da cor desejada
                        if(k in AdjDict[i]): #se existr um vizinho com aquela cor, não podemos pintar
                            result = False
                            break
                        indexSelectColor = k
                if(result):
                    for i in buck:
                        bins[indexColor.index(indexSelectColor)].append(i)
                    del bins[bins.index(buck)]
                    break
            else:
                break

    #DEBUG
    print("COLOR BUCKETS")
    for i in zip(ListColors,bins):
        print(i)

    #CreateMatColor
    colorLen = 0
    for i in bins:
        colorLen+=len(i)
    MatColor = [0]*colorLen
    for i in bins:
        for j in i:
            MatColor[j] = i[0]
    return MatColor

def CreateBucketList(MatColor):
    bins = []
    for i in set(MatColor): #cria os buckets
        index = [j for j, val in enumerate(MatColor) if val==i]
        bins.append(index)
    return(bins)


if __name__ == "__main__":
    main(sys.argv)
