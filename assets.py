import pygame
from config import *


#imagens
def load_assets():
    assets = {}
    assets['background']= pygame.image.load('assets/img/Rua.png')
    assets['background']= pygame.transform.scale(assets['background'],(WIDTH,HEIGHT))
    assets['background2']= pygame.image.load('assets/img/Rua.png')
    assets['background2']= pygame.transform.scale(assets['background2'],(WIDTH,HEIGHT))
    assets['jogador_img']= pygame.image.load('assets/img/carro.frente.png')
    assets['jogador_direita_img']= pygame.image.load('assets/img/car.Direita.png')
    assets['jogador_esquerda_img']= pygame.image.load('assets/img/car.Esquerda.png')
    assets['pixel_das_vias']= [180, 275, 375, 470] #definido atraves de testes
    assets['ini_azul']= pygame.image.load('assets/img/inimigo.azul.png')
    assets['ini_azul']= pygame.transform.scale(assets['ini_azul'],(50,100))
    assets['ini_vermelho']= pygame.image.load('assets/img/inimigo.vermelho.png')
    ini_vermelho= pygame.transform.scale(ini_vermelho,(50,100))
    ini_verde= pygame.image.load('assets/img/inimigo.verde.png')
    ini_verde= pygame.transform.scale(ini_verde,(50,100))
    invrt_azul= pygame.image.load('assets/img/invertido.azul.png')
    invrt_azul= pygame.transform.scale(invrt_azul,(50,100))
    invrt_vermelho= pygame.image.load('assets/img/invertido.vermelho.png')
    invrt_vermelho= pygame.transform.scale(invrt_vermelho,(50,100))
    invrt_verde= pygame.image.load('assets/img/invertido.verde.png')
    invrt_verde= pygame.transform.scale(invrt_verde,(50,100))

