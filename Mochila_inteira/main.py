'''Kened Wanderson Cruz Oliveira
Problema da mochila limitada 0/1
Entrada padrão, do arquivo de dados, em que se deve ter o seguinte modelo:
n M
p1 v1
p2 v2
..
pn vn
onde:
n: |O|
M : capacidade da mochila
pi : vetor de pesos dos objetos
vi : vetor de valores dos objetos
'''
import numpy as np
from operator import itemgetter
import sys

def main():
	input = sys.argv[1]
	arq = open(input, 'r')
	print("Produtos escolhidos:\n",knapSack(arq))

def knapSack(arq):
	out = []
	Obj =InputToMatriz2x2(arq) #tranforma minha str em uma lista
	n= int(Obj[0][0])
	m=int(Obj[0][1])
	del Obj[0]		#retirando a primeira linha da entrada que capturamos a cima
	Obj.sort(key=itemgetter(0)) # ordena a matriz de entrada
	mat = Init_mat(n+1,m+1) #inicia matriz com zeros

	for j in range(1,n+1):
		for k in range(1,m+1):
			if(Obj[j-1][0]>k):#se o produto cabe na mochila
				mat[j][k] = mat[j-1][k]
			else:
				mat[j][k] = max(int(mat[j-1][k]), int(mat[j-1][abs(k-Obj[j-1][0])]) + Obj[j-1][1])
	aux=n
	while (mat[aux][m] >0):#procurando o que foi colocado na mochila e adicionando em out
		if (mat[aux][m] != mat[aux-1][m]):
			out.append(Obj[aux-1]) 
			m = m - Obj[aux-1][0]
			aux = n 
		aux-=1
	print("valor maximo: ",max(mat[n]))
	return(out)
	
def Init_mat(lines,columns):#Inicia uma matriz de tamanho linesXcolumns, com zeros
	mat = np.zeros((lines,columns),dtype=int) 
	return mat
		
def InputToMatriz2x2(arq): #converte  a entrada em str padrão, em inteiro, em uma matriz 2x2 
	mat = []
	lista = list(map(int,arq.read().split( ))) #tranforma minha str em uma lista
	for j in range(2,len(lista)+2,2): #Transforma a Lista em matrizes 2x2
		mat.append(lista[j-2:j])
	return mat
	
'''RECICLAGEM -- RECYCLING
def Val(mat,value): #busca o valor na matriz, de acordo com seu peso
	i, j = np.where(mat==value) #retorna o indice que esta o value
	if (len(i)>0):
		value = mat[int(i[0])][1]
	return value
'''
if __name__ == "__main__":
    main()