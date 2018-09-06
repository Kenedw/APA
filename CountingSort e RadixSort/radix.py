import sys
import timeit

if len(sys.argv) != 2:
    arq = open("123.txt","r")
else:
    arq = open("../instancias-numericas/"+sys.argv[1],"r")
lista = []

for linha in arq:
    lista.append(int(linha))

print("\n-------------------------Desordenada ------------------------------\n ",lista)
def CountingSort(data,digit):
    aux_count = [0 for i in range(10)]               #Inicializa o auxiliar com 0
    max_nDigit = 0                                  #tamanho maximo de digitos em um numero
    #digit = 0                                           #posição do digito

    for i in data:                                  #Verifica ocorrencia
        least = list(map(int,str(i)))
        # max_nDigit = max_nDigit  if max_nDigit>len(least) else len(least)    #manter o max sempre atualizado
        # print("i:{}".format(i))
        least = digit < len(least) and 0 or least[digit-1]             #pega zero se não ouver outro mais significativo
        aux_count[least]+=1
        # print("data:{}".format(data))
        # print("aux_count:{}".format(aux_count))
        # print(max_nDigit)

    for i in range(1,len(aux_count)):               #Ordena o indices da auxiliar
        aux_count[i] += aux_count[i-1]

    output = [0 for i in range(len(data))]          #inicio o vetor de saia com o tamanho de data
    for i in data:                                  #passa os valores ordenados para a saida
        least = list(map(int,str(i)))
        least = digit < len(least) and 0 or least[digit-1]             #pega zero se não ouver outro mais significativo
        print("least:{}".format(least))
        print("aux_count:{}".format(aux_count))
        output[aux_count[least]-1] = i
        aux_count[least]-=1
    return output
def radixSort(data,C):
    print("C:{}".format(C))
    for digit in range(C):
        print("digit:{}".format(digit))
        print(data)
        data = CountingSort(data,digit)
    return data




Ti = timeit.default_timer()                         #medindo tempo inicial
lista = radixSort(lista,len(list(map(int,str(max(lista))))))            #chamada do CountingSort passando o arquivo que foi aberto
Tf = timeit.default_timer()                         #medindo tempo final
print("Tempo total: {:f}s do RadixSort".format(Tf-Ti))
print("\n--------------------------Ordenada ----------------------------------\n ",lista)
