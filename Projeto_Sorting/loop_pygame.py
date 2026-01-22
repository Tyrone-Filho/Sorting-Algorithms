import math

import pygame
from sys import exit

def insertsort(array,distancia,tela,processo_final=False,processo_meio=False,delay:int=0,reverso=False,fast=False):
    n = len(array)
    for i in range(1,n):
        chave = array[i]
        j = i-1
        while j >= 0 and ((not reverso and array[j].height > chave.height) or (reverso and array[j].height < chave.height)):
            array[j+1] = array[j]
            array[j + 1].x = 10 + distancia * (j+1)
            if processo_meio and (i%15==0 if fast else True):
                obv(tela,array,delay)
                atual_vermelho(array, tela, j + 1)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
            j -= 1
        array[j+1] = chave
        array[j + 1].x = 10 + distancia * (j + 1)
        if processo_meio and (i%15==0 if fast else True):
            array[j+1].draw(tela)
        if processo_final:
            obv(tela, array, delay)
            atual_vermelho(array, tela, j+1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

def bubblesort(tamanho_array, array_quadrados,distancia_quadrado,tela,processo_meio=False,processo_final=False,reverso=False,delay:int=0,fast=False):
    for i in range(tamanho_array):
        for j in range(tamanho_array - 1-i):
            if (array_quadrados[j].height < array_quadrados[j + 1].height and reverso) or (array_quadrados[j].height > array_quadrados[j + 1].height and not reverso):
                array_quadrados[j + 1].x -= distancia_quadrado
                array_quadrados[j].x += distancia_quadrado
                array_quadrados[j + 1], array_quadrados[j] = array_quadrados[j], array_quadrados[j + 1]
            if processo_meio and (j%(2**3) == 0 if fast else True):
                obv(tela,array_quadrados,delay)
                atual_vermelho(array_quadrados, tela, j+1)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                if delay:
                    pygame.time.delay(delay)
                pygame.display.flip()

        if processo_final:
            obv(tela,array_quadrados,delay)
            atual_vermelho(array_quadrados,tela,j+1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

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
        if (sub_esquerda[i].height>=sub_direita[j].height) if reverso else (sub_esquerda[i].height <= sub_direita[j].height):
            array[k] = sub_esquerda[i]
            i += 1
        else:
            array[k] = sub_direita[j]
            j += 1
        array[k].x = 10 + distancia_quadrado * k
        if processo and (int((math.log(len(array))*6)%3)==0 if fast else True):
            obv(tela,array,delay)
            atual_vermelho(array, tela, k)
        k += 1
    while i < len(sub_esquerda):
        array[k] = sub_esquerda[i]
        array[k].x = 10 + distancia_quadrado * k
        i += 1
        if processo_final:
            obv(tela, array, delay)
            atual_vermelho(array,tela,k)
        k += 1
    while j < len(sub_direita):
        array[k] = sub_direita[j]
        array[k].x = 10 + distancia_quadrado * k
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

def checkar(array,tela,delay,reverso=False):
    n = len(array)
    delay //= 2
    tela.fill((50, 50, 50))
    r1,r2,r3 = (n-1,0,-1) if reverso else (0,n-1,1)
    for quadrado in array:
        quadrado.draw(tela)

    for i in range(r1,r2,r3):
        if reverso:
            condicao = array[i].height <= array[i-1].height
        else:
            condicao = array[i + 1].height >= array[i].height

        if condicao:
            cor = (0,255,0)
        else:
            cor = (255,0, 0)

        array[i].draw(tela,cor)
        array[i].cor = cor
        if i == (r2+1 if reverso else r2-1) and condicao:
            array[r2].draw(tela, cor)
            array[r2].cor = cor
        pygame.time.delay(delay)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
