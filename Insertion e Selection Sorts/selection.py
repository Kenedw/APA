'''
Kened Wanderson Cruz Oliveira

Algoritimo de ordenação selection sort produzido para a disciplina de APA
'''

import sys
if len(sys.argv) != 2:
    arq = open("123.txt","r")
else:
    arq = open(sys.argv[1],"r")
lista = []
for linha in arq:
    lista.append(int(linha))


print("\n-------------------------Desordenada ------------------------------\n ",lista)

for i in range(len(lista)):                         #percorre toda a lista
    menor = i                                       #pega o menor indice
    for k in range(i,len(lista)):                   #procura um valor menor que o do indice anterior
        if(lista[k] < lista[menor]):                #quando achar o menor valor da lista
            menor = k                               #guarda a posição do menor
    lista[i], lista[menor] = lista[menor], lista[i] #faz um swap(troca) do menor item para o primeiro elemento ainda não ordenado

print("\n--------------------------Ordenada ----------------------------------\n ",lista)
