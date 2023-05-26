import pygame
from config import *
from init_screen import init_screen
from GAMEOVER import game_over
from game_screen import game_screen

pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Highway Rush')

lvl = INIT
while lvl != QUIT:
    if lvl == INIT:
        lvl = init_screen(window)
    if lvl == GAME:
        lvl = game_screen(window)
    if lvl == OVER:
        lvl = game_over(window)

pygame.quit()