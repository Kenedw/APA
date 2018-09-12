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

# print("\n-------------------------Desordenada ------------------------------\n ",lista)
def CountingSort(data,digit):
    aux_count = [0 for i in range(10)]              #Inicializa o auxiliar com 0
    #------------------------VERIFICA RECORRENCIA-----------------------------
    for i in data:                                  #Verifica ocorrencia
        least = list(map(int,str(i)))
        if(digit > len(least)-1):                     #pega zero se nao ouver outro mais significativo
            least = 0
        else:
            least = least[digit-1]
        aux_count[least]+=1
    #------------------------ORDENA OS INDICES-----------------------------
    for i in range(1,len(aux_count)):               #Ordena o indices da auxiliar
        aux_count[i] += aux_count[i-1]

    #-------------POPULA A SAIDA DEACORDO COM OS INDICES---------------------
    output = [0 for i in range(len(data))]          #inicio o vetor de saia com o tamanho de data
    for i in reversed(data):                                  #passa os valores ordenados para a saida
        least = list(map(int,str(i)))
        if(digit > len(least)-1):                     #pega zero se nao ouver outro mais significativo
            least = 0
        else:
            least = least[digit-1]
        output[aux_count[least]-1] = i
        aux_count[least]-=1
    return output

def radixSort(data,C):
    for digit in range(C):
        data = CountingSort(data,digit)
    return data


Ti = timeit.default_timer()                                             #medindo tempo inicial
lista = radixSort(lista,len(list(map(int,str(max(lista))))))            #chamada do CountingSort passando o arquivo que foi aberto
Tf = timeit.default_timer()                                             #medindo tempo final
print("Tempo total: {:f}s do RadixSort".format(Tf-Ti))
# print("\n--------------------------Ordenada ----------------------------------\n ",lista)
