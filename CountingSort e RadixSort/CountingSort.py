'''
Kened Wanderson Cruz Oliveira

Algoritimo de ordenacao CountingSort produzido para a disciplina de APA
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
def CountingSort(data,n):
    aux_count = [0 for i in range(n)]               #Inicializa o auxiliar com 0

    for i in data:                                  #Verifica ocorrencia
        aux_count[i]+=1

    for i in range(1,len(aux_count)):               #Ordena o indices da auxiliar
        aux_count[i] += aux_count[i-1]

    output = [0 for i in range(len(data))]          #inicio o vetor de saia com o tamanho da
    for i in data:                                  #passa os valores ordenados para a saida
        output[aux_count[i]-1] = i
        aux_count[i]-=1
    return output
Ti = timeit.default_timer()                         #medindo tempo inicial
lista = CountingSort(lista,max(lista,key=int)+1)                     #chamada do CountingSort passando o arquivo que foi aberto
Tf = timeit.default_timer()                         #medindo tempo final
print("Tempo total: {:f}s do MergeSort".format(Tf-Ti))
# print("\n--------------------------Ordenada ----------------------------------\n ",lista)
