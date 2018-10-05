#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Kened Wanderson Cruz Oliveira
Problema da mochila limitada 0/1

Entrada padrão, do arquivo de dados, em que se deve ter o seguinte modelo:
n M
p1 v1
p2 v2
..
pn vn
onde:
n: itens a serem postos na mochila
M : capacidade da mochila
pi : vetor de pesos dos objetos
vi : vetor de valores dos objetos
'''
import sys
import timeit
import numpy as np

if len(sys.argv) != 2:
    arq = open("instancias-numericas/mochila01.txt.txt","r")
else:
    arq = open("instancias-numericas/"+sys.argv[1],"r")
mat_nx2 = []
for j in arq:
	mat_nx2.append(map(int,j.split()))

def Init_mat(lines,columns):#Inicia uma matriz de tamanho linesXcolumns, com zeros
	mat = np.zeros((lines,columns),dtype=int)
	return mat

def MaxMochila(mat_nx2):
    mat = Init_mat(mat_nx2[0][0]+1,mat_nx2[0][1]+1) # inicia matriz(nxM) com 0
    for j in range(1,mat_nx2[0][0]+1):
        for w in range(1,mat_nx2[0][1]+1):
            if(mat_nx2[j][0] > w):  #se o peso do item for maior que a atual capacidade da mochila
                mat[j][w] = mat[j-1][w]
            else:
                if (w-mat_nx2[j][0]>0):
                    col = w-mat_nx2[j][0]
                else:
                    col = 0
                mat[j][w] = max(mat[j-1][w] , mat[j-1][col] + mat_nx2[j][1])
    return(mat)

def GetMochila(mat,mat_nx2):
    col = len(mat[0])-1
    elements = []
    for row in range(len(mat)-1,-1,-1):
        if(mat[row][col] != mat[row-1][col]):
            elements.append(row)
            col = abs(col-mat_nx2[row][0])
    return(elements)

mat = MaxMochila(mat_nx2)
# print(mat)
print("Valor arrecadado na mochila:{}\nitens escolhidos:{}".format(mat[-1][-1],GetMochila(mat,mat_nx2)))
