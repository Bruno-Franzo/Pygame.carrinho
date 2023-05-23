#Definindo classes
import random 
import pygame
from assets import *
from config import *
from OJOGO import R

class Jogador(pygame.sprite.Sprite):
    def __init__(self, img, esq, dire):
        # Classe mae(sprite)
        pygame.sprite.Sprite.__init__(self)
        self.direita= dire
        self.esquerda = esq
        self.original= img
        self.image= img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect= self.image.get_rect()
        self.rect.centerx =( WIDTH / 3.5)+100*2
        self.rect.bottom= HEIGHT - 10
        self.speedx = 0

    def update(self):
        #atualiza posicao do jogador
        self.rect.x += self.speedx
        if R == 1:
            self.image= self.esquerda
        if R == 2:
            self.image = self.direita
        if R == 3:
            self.image= self.original
        
        # Mantem dentro da tela
        if self.rect.right > WIDTH - 160:
            self.rect.right = WIDTH - 160
        if self.rect.left < 160:
            self.rect.left = 160

#classe dos carros inimigos
class Inimigo(pygame.sprite.Sprite):
    def __init__(self,img,img2):
        #classe mae(sprite)
        pygame.sprite.Sprite.__init__(self)
        self.contra = img
        self.afavor = img2
        inicio = random.choice(pixel_das_vias)
        if inicio == 180 or inicio == 275:
            self.image = self.contra
            self.rect = self.image.get_rect()
            self.rect.y = random.randint(-100, -50)
            self.rect.x = inicio
            self.speedx = 0
            self.speedy = random.randint(14, 20)
            self.mask = pygame.mask.from_surface(self.image)
        else:
            self.image= self.afavor
            self.rect = self.image.get_rect()
            self.rect.y = random.randint(-100, -50)
            self.rect.x = inicio
            self.speedx = 0
            self.speedy = random.randint(5, 9)
            self.mask = pygame.mask.from_surface(self.image)


    def update(self):
        #atulizando inimigo
        self.rect.y += self.speedy

        #caso chegue no final, volta e sorteia nova posicao
        if self.rect.top > HEIGHT:
            inicio = random.choice(pixel_das_vias)
            if inicio == 180 or inicio == 275:
                self.image= self.contra
                self.rect= self.image.get_rect()
                self.rect.y = random.randint(-100, -50)
                self.speedy = random.randint(14, 20)
                self.rect.x= inicio
            else:
                self.image= self.afavor
                self.rect= self.image.get_rect()
                self.rect.x= inicio
                self.rect.y = random.randint(-100, -50)
                self.speedx = 0
                self.speedy = random.randint(5, 9) 

class cenario(pygame.sprite.Sprite):
    def __init__(self, img, altura):
        #classe mae
        pygame.sprite.Sprite.__init__(self)

        self.image= img
        self.rect= self.image.get_rect()
        self.rect.x = 0
        self.rect.y = altura
        self.speedy= 10

    def update(self):
        #atualizando cenario
        self.rect.y += self.speedy

        #ao chegar no final, reseta
        if self.rect.top >= HEIGHT:
            self.rect.bottom = 0