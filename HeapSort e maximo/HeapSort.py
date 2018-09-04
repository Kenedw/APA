'''
Kened Wanderson Cruz Oliveira

Algoritimo de ordenacao da HeapSort produzido para a disciplina de APA
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

def max_heapify(heap,i):
    left  = 2*i + 1
    right = left+1
    n = len(heap)
    max = i
    if(left < n and heap[left] > heap[i]):
        max = left
    if(right < n and heap[right] > heap[max]):
        max = right
    if(max != i):
        heap[i],heap[max] = heap[max],heap[i]
        max_heapify(heap,max)
    return(heap)

def Build_max_heap(data):
    for j in range(len(data)//2,-1,-1):
        max_heapify(data,j)

def HeapSort(A):
    Build_max_heap(A)
    Aux = len(A) - 1
    n = Aux
    for i in range(n,0,-1):
        A[0],A[i] = A[i],A[0]
        Aux -= 1
        A[:Aux+1] = max_heapify(A[:Aux+1],0)

print("\n-------------------------Desordenada ------------------------------\n ",lista)
Ti = timeit.default_timer()                         #medindo tempo inicial
HeapSort(lista)                       #chamada do HeapSort passando o arquivo que foi aberto
Tf = timeit.default_timer()                         #medindo tempo final
print("Tempo total: {:f}s do HeapSort".format(Tf-Ti))
print("\n--------------------------Ordenada ----------------------------------\n ",lista)
