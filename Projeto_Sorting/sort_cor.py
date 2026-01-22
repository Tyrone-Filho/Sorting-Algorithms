import math

import pygame
from sys import exit
ir_por_cor = True
def mergesort(arra,left,right,tela,distancia_quadrado,delay,processo,processo_final,reverso,fast):
    if left >= right: return
    meio = (left+right)//2
    mergesort(arra,left,meio,tela,distancia_quadrado,delay,processo,processo_final,reverso,fast)
    mergesort(arra, meio+1,right,tela,distancia_quadrado,delay,processo,processo_final,reverso,fast)
    merge(arra,left,meio,right,tela,distancia_quadrado,delay,processo,processo_final,reverso,fast)

def merge(array,esquerda_pa,meio_pa,direita_pa,tela,distancia_quadrado,delay,processo_final=False,processo=False,reverso=False,fast=False):
    sub_esquerda = array[esquerda_pa:meio_pa+1]
    sub_direita = array[meio_pa+1:direita_pa+1]
    i = j = 0
    k  = esquerda_pa
    while i < len(sub_esquerda) and j < len(sub_direita):
        if (sum(sub_esquerda[i].cor)  >=  sum(sub_direita[j].cor)) \
                if reverso else \
                (sum(sub_esquerda[i].cor) <= sum(sub_direita[j].cor)):
            array[k] = sub_esquerda[i]
            i += 1
        else:
            array[k] = sub_direita[j]
            j += 1
        array[k].x = 10+(distancia_quadrado-2) * k
        if processo and (int((math.log(len(array))*6)%3)==0 if fast else True):
            obv(tela,array,delay)
            atual_vermelho(array, tela, k)
        k += 1
    while i < len(sub_esquerda):
        array[k] = sub_esquerda[i]
        array[k].x = 10+(distancia_quadrado-2) * k
        i += 1
        if processo_final:
            obv(tela, array, delay)
            atual_vermelho(array,tela,k)
        k += 1
    while j < len(sub_direita):
        array[k] = sub_direita[j]
        array[k].x = 10+(distancia_quadrado-2) * k
        j += 1
        if processo_final:
            obv(tela, array, delay)
            atual_vermelho(array,tela,k)
        k += 1



def atual_vermelho(array,tela,index):
    array[index].draw(tela, (255, 0, 0))
    pygame.display.flip()

def obv(tela,array,delay=0):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    tela.fill((50,50,50))
    for quadrado in array:
        quadrado.draw(tela)
    if delay:
        pygame.time.delay(delay)