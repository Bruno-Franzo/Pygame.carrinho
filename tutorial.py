import pygame
from config import *
from assets import load_assets

def tutorial_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets= load_assets()

    # Carrega o fundo da tela inicial
    background = assets['como jogar']
    
    window.fill((0, 0, 0))
    window.blit(background, (0,0))

    pygame.display.update()

    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(Fps)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                lvl = QUIT    
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    lvl = INIT
                    running = False

        # A cada loop, redesenha o fundo e os sprites


        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        pygame.display.update()

    return lvl

    