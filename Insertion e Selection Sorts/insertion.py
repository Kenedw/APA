import sys

if len(sys.argv) != 2:
    arq = open("num.1000.1.in","r")
else:
    arq = open(sys.argv[1],"r")
lista = []
for linha in arq:
    lista.append(int(linha))


print("\n-------------------------Desordenada ------------------------------\n ",lista)

for i in range(1,len(lista)):
    escolha = lista[i]                     #pega o segundo elemento da lista
    k = i                                  #pega o tamanho do interador a ser percorrido
    while k > 0 and escolha < lista[k-1]:  #vefica se o escolhido é menor que o numero anterior da lista
        lista[k] = lista[k - 1]            #se sim, move os anteriores ate ele ser meior ou ser o primeiro
        k -= 1                             #e decrementa o iterado
    lista[k] = escolha                     #insere o escolhido na posição de ordenação

print("\n--------------------------Ordenada ----------------------------------\n ",lista)
