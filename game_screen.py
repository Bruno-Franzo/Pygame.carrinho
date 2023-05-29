import pygame
import time
import random
from config import *
from assets import load_assets  
from classes import Jogador,Inimigo,cenario
from recorde import salvar_recordes
from recorde import carregar_recordes

def game_screen(window):

    clock = pygame.time.Clock()

    assets= load_assets()


    #criando um grupo de sprites
    all_sprites = pygame.sprite.Group()
    all_ini = pygame.sprite.Group()

    #criando background
    background = cenario(assets['background'],0)
    background2 = cenario(assets['background2'],-HEIGHT)
    all_sprites.add(background)
    all_sprites.add(background2)
    # Criando o jogador
    player= Jogador(assets['jogador_img'],assets['jogador_esquerda_img'],assets['jogador_direita_img'])
    all_sprites.add(player)

    buzina=assets['buzina']
    som_fundo= assets['som_motor']
    batida=assets['batida']
    #criando inimigos
    for i in range(4):
        cor = random.choice([assets['ini_azul'],assets['ini_vermelho'],assets['ini_verde']])
        cor2 = random.choice([assets['invrt_azul'],assets['invrt_verde'],assets['invrt_vermelho']])
        carrinho = Inimigo(cor,cor2)
        all_sprites.add(carrinho)
        all_ini.add(carrinho)
        
    #cirando sons
    #som_carro=assets['som_motor']

    #configs iniciais
    DONE= 0
    PLAYING= 1
    EXPLODING= 2
    state = PLAYING
    score = 0

    pygame.mixer.music.play(loops=-1)

    #loop principal do jogo
    while state != DONE:

        clock.tick(Fps)
        score += 2
        player.R=0
        #    olha os eventos
        for event in pygame.event.get():
            #olha as consequencias
            if event.type == pygame.QUIT:
                state = DONE
                lvl = QUIT
                return lvl
            
            #verifica se apertou teclas
            if event.type == pygame.KEYDOWN:
                # Altera a velocidade
                if event.key == pygame.K_LEFT:
                    player.R = 1
                    player.speedx -= 8
                if event.key == pygame.K_RIGHT:
                    player.R = 2
                    player.speedx += 8 
                if event.key == pygame.K_SPACE:
                    pygame.mixer.Sound.play(buzina)
                # if event.key == pygame.K_UP:
                #     background.speedy+=2.5
                #     background2.speedy+=2.5
                #     carrinho.speedy+=2.5
                # if event.key == pygame.K_DOWN:
                #     background.speedy-=2.5
                #     background2.speedy-=2.5
                #     carrinho.speedy-=2.5


            #verifica se soltou teclas
            if event.type == pygame.KEYUP:
                player.R = 3
                #altera a velocidade
                if event.key == pygame.K_LEFT:
                    player.speedx += 8
                if event.key == pygame.K_RIGHT:
                    player.speedx -= 8
                # if event.key == pygame.K_DOWN:
                #     background.speedy+=2.5
                #     background2.speedy+=2.5
                #     carrinho.speedy+=2.5
                # if event.key == pygame.K_UP:
                #     background.speedy-=2.5
                #     background2.speedy-=2.5
                #     carrinho.speedy-=2.5
        #atualizando estado do jogo#
        #atualiza todos os sprites
        all_sprites.update()

        # gera as saidas
        window.fill((255, 255, 255))  # Preenche com a cor branca
        #window.blit(background, (0, 0))
        #desenhando sprites
        all_sprites.draw(window)  

        #desenhando score
        text_surface= assets['score_font'].render("{:08d}".format(score), True, (255, 255, 0))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        window.blit(text_surface, text_rect)

        #desenhando level
        if score < 300:
            level= assets['score_font'].render('Level 1', True, (255, 255, 0))
            level_rect = level.get_rect()
            level_rect.midtop = (WIDTH / 2,  40)
            window.blit(level, level_rect)







        #atualiza o estado do jogo
        pygame.display.update()

        #Verifica colisao entre jogador e inimigo
        hits= pygame.sprite.spritecollide(player, all_ini, True, pygame.sprite.collide_mask)
        if len(hits) > 0 :
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(batida)
            #pygame.mixer.Sound.play(assets['batida'])
            time.sleep(1)
            lvl= OVER
            return lvl
        
    
