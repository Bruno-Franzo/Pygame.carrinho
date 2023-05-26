import pygame
from assets import *

def game_over(window):
 # # Exibe a imagem "Game Over"

    assets = load_assets()
    window.blit(assets['gameover'], (0, 0))
    pygame.display.update()

        # Aguarda o jogador pressionar qualquer botão
    jogando=True
    while jogando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jogando=False
                lvl=QUIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                # Reinicia o jogo
                    jogando=False
                    lvl=GAME
    return lvl