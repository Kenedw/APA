'''
Kened Wanderson Cruz Oliveira

Algoritimo de montagem da HeapMax produzido para a disciplina de APA
'''
import math
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
    print(heap)

    max = i
    if(left < n and heap[left] > heap[i]):
        max = left
    if(right < n and heap[right] > heap[max]):
        max = right
    if(max != i):
        print("swap[] to []".format(heap[i],heap[max]))
        heap[i],heap[max] = heap[max],heap[i]
        max_heapify(heap,max)
    return heap

def Build_max_heap(data):
    for j in range(len(data)//2,-1,-1):
        data = max_heapify(data,j)
    return data


print("\n-------------------------Desordenada ------------------------------\n ",lista)
Ti = timeit.default_timer()                         #medindo tempo inicial
lista = Build_max_heap(lista)                               #chamada do HeapMax passando o arquivo que foi aberto
Tf = timeit.default_timer()                         #medindo tempo final
print("Tempo total: {:f}s do HeapMax".format(Tf-Ti))
print("\n--------------------------Ordenada ----------------------------------\n ",lista)
