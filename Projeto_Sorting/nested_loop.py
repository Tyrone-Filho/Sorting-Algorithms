#sortear uma array com nested loop
import numpy as np
def insertsort(array):
    n = len(array)
    for i in range(1,n):
        chave = array[i]
        j = i-1
        while j >= 0 and array[j] < chave:
            array[j+1] = array[j]
            j-=1
        array[j+1] = chave
    return array

def seilasortear(array):
    oi = []
    while len(array) != 0:
        oi.append(min(array))
        array.remove(min(array))

def bubsort(array):
    n = len(array)
    for j in range(n):
        for i in range(n-1-i):
            chave = array[i]
            if array[i] > array[i+1]:
                array[i] = array[i+1]
                array[i+1] = chave
    return array

def mergesort(arra,left,right):
    if left >= right: return
    meio = (left+right)//2
    mergesort(arra,left,meio)
    mergesort(arra, meio+1,right)
    merge(arra,left,meio,right)

def merge(array,esquerda_pa,meio_pa,direita_pa):
    esquerda = array[esquerda_pa:meio_pa+1]
    direita = array[meio_pa+1:direita_pa+1]
    i = j = 0
    k  = esquerda_pa
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            array[k] = esquerda[i]
            i += 1
        else:
            array[k] = direita[j]
            j += 1
        k += 1
    while i < len(esquerda):
        array[k] = esquerda[i]
        i += 1
        k += 1
    while j < len(direita):
        array[k] = direita[j]
        j += 1
        k += 1

arr = []
for _ in range(10**3):
    arr.append(np.random.randint(0,1000))
mergesort(arr,0,len(arr)-1)
print(arr)

"""
tentativa 1
lut = ["raj","taj","paj"]
lutas = []
for lu1 in lut:
    for lu2 in lut:
        if lu1 != lu2 and ([lu1,lu2] and [lu2,lu1]) not in lutas:
            print(f"{lu1} vs {lu2}")
            lutas.append([lu1,lu2])
print(lutas)"""