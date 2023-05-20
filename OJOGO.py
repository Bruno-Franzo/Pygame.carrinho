#Inicio
#Importações
import pygame
import random


pygame.init()
pygame.mixer.init()

#gerando tela principal
WIDTH = 480
HEIGHT = 600
window = pygame.display.set_mode((600, 300))
pygame.display.set_caption('jogo do digao e brunao')


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



    #atualiza o estado do jogo
    pygame.display.update()

#Finalizacao
pygame.quit()

    