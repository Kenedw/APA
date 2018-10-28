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
        AfterMcolor = NeighborhoodSearch(AdjDict,Mcolor)
        after = len(set(AfterMcolor))
        # print("after:{}".format(after))
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
    ListOfreallocation = []

    bins = List2Bucket(MatColor)
    ListColors = set(MatColor)
    ListColors = list(ListColors)

    print("IN-LISTCOLORS\n{}".format(MatColor))

    #VND
    for buck in bins: #pega bucket
        for ItemColor in ListColors: #testa todas as cores
            indexColor = bins[ListColors.index(ItemColor)] #lista de nó da cor desejada
            if(buck != indexColor): #não testa a sua cor
                result=True
                for i in buck:  #testa todos os nó naquele bucket
                    ListOfreallocation = []
                    for k in indexColor: #indices da cor desejada
                        if(k not in AdjDict[i]): #se não existr um vizinho com aquela cor, podemos pintar
                            ListOfreallocation.append([k,i])
                        else:
                            result = False
                            break
                    if(not result):
                        break
                if(result):
                    for i in ListOfreallocation:
                        bins[ListColors.index(i[0])].append(i[1])
                    del bins[bins.index(buck)]
                    del ListColors[ListColors.index(ItemColor)]
                    break

    #DEBUG
    print("COLOR BUCKETS")
    for i in zip(ListColors,bins):
        print(i)

    MatColor = Bucket2List(bins)
    print("OUT-LISTCOLORS\n{}\n\n".format(MatColor))
    return MatColor

def List2Bucket(MatColor):
    bins = []
    for i in set(MatColor): #cria os buckets
        index = [j for j, val in enumerate(MatColor) if val==i]
        bins.append(index)
    return(bins)

def Bucket2List(bins):
    count = 0
    for i in bins:
        count+=len(i)
    MatColor = [0]*count
    for i in range(len(bins)):
        for j in bins[i]:
            MatColor[j-1] = i
    return(MatColor)


if __name__ == "__main__":
    main(sys.argv)
