from loop_pygame import *
import pygame
from time import time
from sys import exit
from sorting_classes import *
from random import randint
import numpy as np

def sortear_array_quadrados(array_rect,valores_aleatorios):
    array_rect.clear()
    valores_aleatorios.clear()
    for index in range(tamanho_array):
        valores_aleatorios.append(randint(1,400))
        array_rect.append(
            Quadrado(10+distancia_quadrado*index, tela.get_height()-10 - valores_aleatorios[index],
                     int(distancia_quadrado/2), valores_aleatorios[index],cor=(255,255,255))
        )
def convertor_string(string):
    string1 = string.split("\n")
    larguras = []
    for x in string1:
        larguras.append(len(x))
    largura = max(larguras)
    string_longa_dms = ""
    for y in string1:
        if y == string1[1] and len(string1)==2:
            string_longa_dms += f"{y:^{largura + len(y)}}\n"
        else:
            string_longa_dms += f"{y}\n"

    return string_longa_dms

def render_texto(text,x=600):
    surface_texto = fonte.render(convertor_string(text), True, (200, 180, 180))
    tela.blit(surface_texto, (tela.get_width() / 2 - x, 10))


processos = [True,True]
array_quadrados = []
array = []
tempo_array = []

tela_inicial = True
sumario = True
pode_checar = True
ir_mais_rapido = False # precisa de processo ativado pra realmente ir mais rapido
reverso = False

distancia_quadrado = 2 # int:tamanho minimo 2: distancia entre quadrados
inicio,fim = 0,0 #temporizador
tamanho_array = 780 # sample size
x=3
delay = 0 # coloque 0 para desativar
vezes_rodadas = 1 # int: vezes que vai rodar
if vezes_rodadas <= 0:
    vezes_rodadas = 1


pygame.init()
fonte = pygame.font.SysFont('Minecraft', 50)
relogio = pygame.time.Clock()
tela = pygame.display.set_mode((1600,800))
pygame.display.set_caption("Algoritmos de Sorteacao Python")

sortear_array_quadrados(array_quadrados,array)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    tela.fill((50, 50, 50))
    for quadrado in array_quadrados:
        quadrado.draw(tela)
    keys = pygame.key.get_pressed()


    if keys[pygame.K_SPACE] and len(tempo_array)==0:
        for _ in range(vezes_rodadas):
            tela_inicial = False
            inicio = time()
            #insertsort(array_quadrados,distancia_quadrado,tela,processo_meio=processos[0],processo_final=processos[1],delay=delay,reverso=reverso,fast=ir_mais_rapido)
            mergesort(array_quadrados, 0, len(array_quadrados)-1,tela,distancia_quadrado,delay=delay,processo=processos[0],processo_final=processos[1],reverso=reverso,fast=ir_mais_rapido)
            #bubblesort(tamanho_array, array_quadrados,distancia_quadrado,tela,reverso=reverso,processo_meio=processos[0],processo_final=processos[1],delay=delay,fast=ir_mais_rapido)

            fim = time()
            if pode_checar:
                checkar(array_quadrados, tela, delay, reverso=reverso)
            tempo_array.append(fim - inicio)
            if len(tempo_array)!=vezes_rodadas:
                sortear_array_quadrados(array_quadrados,array)
    if sumario and fim and not tela_inicial:
        texto = f"demorou {sum(tempo_array):.10f} segundos para organizar\n{vezes_rodadas} listas de {tamanho_array} arquivos"
        render_texto(texto)

    if keys[pygame.K_r]:
        tela_inicial = True
        pygame.time.delay(150)
        sortear_array_quadrados(array_quadrados,array)
        tempo_array.clear()

    if tela_inicial:
        dicas = "W -> ativar/desativar Reverso\nR -> Sorteia os Numeros\nA/D -> Mudar Delay\nSetas C/B -> Muda o Tamanho da lista\nZ/X -> muda o zoom\nS -> desativa/ativa o Processo"
        render_texto(dicas,(tela.get_width()//2 - 25))
        ativo = f"Reverso : {reverso}\nDelay : {delay}\nTamanho Lista : {tamanho_array}\nZoom : {distancia_quadrado}\nProcesso : {processos[0]}"
        render_texto(ativo, -250)

    if keys[pygame.K_w]:
        if reverso:
            reverso = False
        elif not reverso:
            reverso = True
        pygame.time.delay(100)

    if keys[pygame.K_s]:
        if processos[0]:
            processos[0],processos[1] = False,False
        elif not processos[0]:
            processos[0],processos[1] = True,True
        pygame.time.delay(100)

    if keys[pygame.K_a] and delay>0:
        delay-=5
        pygame.time.delay(250)
    elif keys[pygame.K_d]:
        delay+=5
        pygame.time.delay(250)

    if keys[pygame.K_z]:
        distancia_quadrado+=2
        sortear_array_quadrados(array_quadrados, array)
        pygame.time.delay(100)

    elif keys[pygame.K_x] and distancia_quadrado>2:
        distancia_quadrado-=2
        sortear_array_quadrados(array_quadrados, array)
        pygame.time.delay(100)

    if keys[pygame.K_UP]:
        if tamanho_array >= (10 ** (x+1)):
            x += 1
        if tamanho_array>= (10**x):
            tamanho_array += (10**(x-1))
        else:
            tamanho_array += 5

        sortear_array_quadrados(array_quadrados,array)
        pygame.time.delay(100)

    elif keys[pygame.K_DOWN] and tamanho_array>5:
        if tamanho_array >= (10 ** (x+1)):
            x += 1
        if tamanho_array >= (10 ** x):
            tamanho_array += (10 ** (x - 1))
        else:
            tamanho_array -= 5
        sortear_array_quadrados(array_quadrados, array)
        pygame.time.delay(100)


    pygame.display.flip()
    relogio.tick(60)