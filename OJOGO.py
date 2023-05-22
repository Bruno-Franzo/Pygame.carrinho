#Inicio
#Importações
import pygame
import random


pygame.init()
pygame.mixer.init()

#gerando tela principal
WIDTH = 600
HEIGHT = 700
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('jogo do digao e brunao')

#inicia assets
background= pygame.image.load('assets/img/Rua.png')
background = pygame.transform.scale(background,(WIDTH,HEIGHT))



#iniciando estrutura de dados
game = True

#loop principal do jogo
while game:
    #    olha os eventos
    for event in pygame.event.get():
        #olha as consequencias
         if event.type == pygame.QUIT:
            game = False
        

    # gera as saidas
    window.fill((255, 255, 255))  # Preenche com a cor branca
    window.blit(background, (0, 0))


    #atualiza o estado do jogo
    pygame.display.update()

#Finalizacao
pygame.quit()

    