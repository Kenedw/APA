'''
Kened Wanderson Cruz Oliveira

Algoritimo de ordenação QuickSort produzido para a disciplina de APA
'''

import sys
import timeit
from random import random

if len(sys.argv) != 2:
    arq = open("123.txt","r")
else:
    arq = open("../instancias-numericas/"+sys.argv[1],"r")
lista = []
for linha in arq:
    lista.append(int(linha))

print("\n-------------------------Desordenada ------------------------------\n ",lista) # DEBUG:

def quicksort(a, i, f):
    if(i<f):
        Ipivo = split(a,i,f)
        quicksort(a, i, Ipivo-1)
        quicksort(a,Ipivo+1,f)
def split(a, i, f):
    Ipivo = int(random()*(len(a)-1))
    for p in range(i,f):
        if(a[p] > a[Ipivo]]) && (a[Ipivo]] > a[f]):
            a[p], a[f] = a[f], a[p]
            f-=1
        elif(a[p] > a[Ipivo]]):
            aux = a[p]
            a.remove(aux)
            a.insert(Ipivo+1,aux)
            # a[p], a[f] = a[f], a[i+p]
        elif(a[f] < a[Ipivo]]):

    return (Ipivo)

Ti = timeit.default_timer()                         #medindo tempo inicial
quicksort(lista,0,len(lista)-1)                     #chamada do quicksort passando o arquivo que foi aberto
Tf = timeit.default_timer()                         #medindo tempo final
print("Tempo total: {:f}s do MergeSort".format(Tf-Ti))
print("\n--------------------------Ordenada ----------------------------------\n ",lista) # DEBUG:
