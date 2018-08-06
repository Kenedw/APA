'''
Kened Wanderson Cruz Oliveira

Algoritimo de ordenação MergeSort produzido para a disciplina de APA
'''

import sys
import timeit

if len(sys.argv) != 2:
    arq = open("123.txt","r")
else:
    arq = open("../instancias-numericas/"+sys.argv[1],"r")
lista = []
for linha in arq:
    lista.append(int(linha))

# print("\n-------------------------Desordenada ------------------------------\n ",lista)

def mergesort(a, i, f):
    if(f>i):
        mergesort(a, i, int((i+f)/2))               #ordenamos a primeira metade do array
        mergesort(a, int(((i+f)/2)+1), f)           #ordenamos a segunda metade do array
        merge(a, i, f)                              #juntamos as metades ordenadas

def merge(a, i, f):
    for j in range(0,f-i):
        for k in range(0,f-i):
            if((i+k) > (f-j)):
                break
            if(a[i+k] > a[f-j]):
                a[i+k], a[f-j] = a[f-j], a[i+k]     #faz um swap(troca) do menor item para a esquerda

Ti = timeit.default_timer()                         #medindo tempo inicial
mergesort(lista,0,len(lista)-1)                     #chamada do mergesort passando o arquivo que foi aberto
Tf = timeit.default_timer()                         #medindo tempo final
print("Tempo total: {:f}s do MergeSort".format(Tf-Ti))
# print("\n--------------------------Ordenada ----------------------------------\n ",lista)
