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
        AfterMcolor = NeighborhoodSearch(AdjDict)
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

def  NeighborhoodSearch(AdjDict):
    KeyList = list(AdjDict.keys())
    shuffle(KeyList)    #embaralha as chaves
    return heuristica_gulosa("",AdjDict,KeyList)

if __name__ == "__main__":
    main(sys.argv)
