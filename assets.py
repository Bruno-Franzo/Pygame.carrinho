import pygame
from config import *


#imagens
def load_assets():
    assets = {}
    assets['background']= pygame.image.load('assets/img/Rua.png').convert_alpha()
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
    assets['ini_vermelho']= pygame.transform.scale(assets['ini_vermelho'],(50,100))
    assets['ini_verde']= pygame.image.load('assets/img/inimigo.verde.png')
    assets['ini_verde']= pygame.transform.scale(assets['ini_verde'],(50,100))
    assets['invrt_azul']= pygame.image.load('assets/img/invertido.azul.png')
    assets['invrt_azul']= pygame.transform.scale(assets['invrt_azul'],(50,100))
    assets['invrt_vermelho']= pygame.image.load('assets/img/invertido.vermelho.png')
    assets['invrt_vermelho']= pygame.transform.scale(assets['invrt_vermelho'],(50,100))
    assets['invrt_verde']= pygame.image.load('assets/img/invertido.verde.png')
    assets['invrt_verde']= pygame.transform.scale(assets['invrt_verde'],(50,100))
    assets['score_font'] = pygame.font.Font('assets/font/PressStart2P.ttf', 28)
    assets['backdeserto']= pygame.image.load('assets/img/deserto.png').convert_alpha()
    assets['backdeserto']= pygame.transform.scale(assets['backdeserto'],(WIDTH,HEIGHT))
    assets['backdeserto2']= pygame.image.load('assets/img/deserto.png').convert_alpha()
    assets['backdeserto2']= pygame.transform.scale(assets['backdeserto'],(WIDTH,HEIGHT))
    assets['gameover']=pygame.image.load('assets/img/Game over.png')
    assets['gameover']=pygame.transform.scale(assets['gameover'],(WIDTH,HEIGHT))
    assets['inicio'] = pygame.image.load('assets/img/inicio.png').convert_alpha()
    assets['inicio'] = pygame.transform.scale(assets['inicio'],(WIDTH,HEIGHT))

    #sons
    assets['batida']=pygame.mixer.Sound('assets/audios/batida.wav')
    assets['buzina']=pygame.mixer.Sound('assets/audios/Buzina.wav')
    assets['som_motor']=pygame.mixer.music.load('assets/audios/Audio carro.wav')
    # assets['som_motor']=pygame.mixer.music.set_volume(7)
    # assets['som_motor']=pygame.mixer.music.play()

    return assets