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

        #VND
        if(after >= before):
            break
        else:
            after,before = before,after
            Mcolor = AfterMcolor

    print("------------------------------------------------------------------------")
    print(Mcolor)
    print("Novo numero de cores {}".format(before))
    print("------------------------------------------------------------------------")

def  NeighborhoodSearch(AdjDict, MatColor):
    # result = True
    # indexSelectColor = 0
    ListOfreallocation = []
    bins = List2Bucket(MatColor)
    ListColors = set(MatColor)
    ListColors = list(ListColors)

    print("\n\nIN-LISTCOLORS\n{}".format(MatColor))
    #VND
    for index,buck in enumerate(bins): #pega bucket
        for ItemColor in range(0,len(ListColors)): #testa todas as cores
            indexColor = bins[ItemColor] #lista de nó da cor desejada
            if(index != ItemColor): #não testa a sua cor
                ListOfreallocation = []
                result=True
                for i in buck:  #testa todos os nó naquele bucket
                    try:
                        for k in AdjDict[i]:
                            # print("------\n no:{} with AdjDict:{}\nneighborhood:{} in {} is {}".format(i,AdjDict[i],k,indexColor,k in indexColor))
                            if(k in indexColor): #seleciona o nó se não ouver vizinho da mesma cor
                                result = False
                                break
                        if(result):
                            ListOfreallocation.append([ItemColor,i])
                        else:
                            break
                    except KeyError:
                        i=i+1
                if(result):
                    for i in ListOfreallocation:
                        bins[i[0]].append(i[1])
                    del bins[index]
                    del ListColors[0]
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
    MatColor = [-1]*count
    for index, i in enumerate(bins):
        for j in i:
            MatColor[j] = index
    return(MatColor)


if __name__ == "__main__":
    main(sys.argv)
