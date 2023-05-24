import pygame
from assets import load_assets




def game_over(window):
    window.fill((0,0,0))
    window.blit(load_assets('gameover'),(0,0))

    pygame.display.update()

    jogando = True

    while jogando:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                return True
            elif event.type == pygame.QUIT:
                return  False       