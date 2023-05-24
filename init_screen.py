import pygame
import random
from config import Fps, GAME,QUIT

def init_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background = pygame.image.load('assets/img/inicio.png').convert()
    background_rect = background.get_rect()

    running = True
    while running:
        print('init')

        # Ajusta a velocidade do jogo.
        clock.tick(Fps)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT    
                running = False

            if event.type == pygame.KEYUP:
                state = GAME
                running = False

        # A cada loop, redesenha o fundo e os sprites
        screen.fill((0, 0, 0))
        screen.blit(background, background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        pygame.display.update()

    return state
