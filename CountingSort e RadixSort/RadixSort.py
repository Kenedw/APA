'''
Kened Wanderson Cruz Oliveira

Algoritimo de ordenacao RadixSort produzido para a disciplina de APA
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

def insertion(lista):
    for i in range(1,len(lista)):
        escolha = lista[i]                     #pega o segundo elemento da lista
        k = i                                  #pega o tamanho do interador a ser percorrido
        while k > 0 and escolha < lista[k-1]:  #vefica se o escolhido he menor que o numero anterior da lista
            lista[k] = lista[k - 1]            #se sim, move os anteriores ate ele ser meior ou ser o primeiro
            k -= 1                             #e decrementa o iterado
        lista[k] = escolha                     #insere o escolhido na posicao de ordenacao
    return lista

print("\n-------------------------Desordenada ------------------------------\n ",lista)
def RadixSort(data):
    lens = len(data)
    bins = [[] for i in range(10)]
    result = [[] for i in range(lens)]
    for i in data:
        least = map(int,str(i))
        least = least[0]
        bins[least].append(i)
    count = 0
    for i in bins:
        for j in i:
            result[count] = j
            count +=1
            insertion(result)
    return result

Ti = timeit.default_timer()                         #medindo tempo inicial
lista = RadixSort(lista)                            #chamada do CountingSort passando o arquivo que foi aberto
Tf = timeit.default_timer()                         #medindo tempo final
print("Tempo total: {:f}s do MergeSort".format(Tf-Ti))
print("\n--------------------------Ordenada ----------------------------------\n ",lista)
