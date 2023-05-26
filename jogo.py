import pygame
from config import *
from init_screen import init_screen
from GAMEOVER import game_over
from game_screen import game_screen

lvl = INIT
while lvl != QUIT:
    if lvl == INIT:
        lvl = init_screen()
    if lvl == GAME:
        lvl = game_screen()
    if lvl == OVER:
        lvl = game_over()

pygame.quit()