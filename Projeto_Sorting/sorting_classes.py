import pygame
class Quadrado:
    def __init__(self, x,y,width,height,cor):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.cor = cor
    def draw(self,tela,cor=False):
        if cor:
            pygame.draw.rect(tela, cor, (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(tela, self.cor, (self.x,self.y,self.width,self.height))