#!/usr/bin/env python
# -*- coding: utf-8 -*-

from heuristica import CreateAdjList, heuristica_gulosa
import sys
from random import shuffle
def main(arg):

    ''' Caso inicial do construtor guloso '''
    AdjList = CreateAdjList(arg)
    Mcolor = heuristica_gulosa("",AdjList)
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
        AfterMcolor = NeighborhoodSearch(AdjList[:])
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

def  NeighborhoodSearch(AdjMat):
    shuffle(AdjMat)
    return heuristica_gulosa("",AdjMat)

if __name__ == "__main__":
    main(sys.argv)
