from sort_cor import *
import pygame
from time import time
from sys import exit
from sorting_classes import *
from random import randint
import numpy as np
"""
Nao tao atualizado/organizado/bom quanto sorting_pygame pois esse script foi feito com a unica intecao de organizar cores
e eu fiquei com 1 pouco de preguica ent n organiza tao bom assim ele organiza por clareza nao por coloracao 
"""
def sortear_array_quadrados(array_rect):
    array_rect.clear()
    for index in range(tamanho_array):
        array_rect.append(
            Quadrado(10+(distancia_quadrado-2)*index, tela.get_height()-10 - 100,
                     int(distancia_quadrado/2), 100,cor=(randint(0,255),randint(0,255),randint(0,255)))
        )
def convertor_string(string):
    string1, string2 = string.split("\n")

    return f"{string1}\n{string2}"


tamanho_array = 595 # sample size
delay = 5 # coloque 0 para desativar
processos = [True,True]
sumario = True
ir_mais_rapido = False # precisa de processo ativado pra realmente ir mais rapido
reverso = False
distancia_quadrado = 5 # int:tamanho minimo 2: distancia entre quadrados
inicio,fim = 0,0 #temporizador
array_quadrados = []
array = []
vezes_rodadas = 1 # int: vezes que vai rodar
if vezes_rodadas <= 0:
    vezes_rodadas = 1
tempo_array = []

pygame.init()
fonte = pygame.font.SysFont('Minecraft', 50)
relogio = pygame.time.Clock()
tela = pygame.display.set_mode((1800,800))
pygame.display.set_caption("Algoritmos de Sorteacao Python")

sortear_array_quadrados(array_quadrados)
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
            inicio = time()
            mergesort(array_quadrados, 0, len(array_quadrados)-1,tela,distancia_quadrado,delay=delay,processo=processos[0],processo_final=processos[1],reverso=reverso,fast=ir_mais_rapido)
            fim = time()
            tempo_array.append(fim - inicio)
            if len(tempo_array)!=vezes_rodadas:
                sortear_array_quadrados(array_quadrados)
    if keys[pygame.K_r]:
        pygame.time.delay(150)
        sortear_array_quadrados(array_quadrados)
    if sumario and fim:
        texto = f"Achou legal veja meus outros projetos em:\nhttps://github.com/Tyrone-Filho"
        surface_texto = fonte.render(convertor_string(texto),True, (200,180,180))
        tela.blit(surface_texto, (tela.get_width() / 2 - 600, 10))
    pygame.display.flip()
    relogio.tick(60)