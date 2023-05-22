#Inicio
#Importações
import pygame
import random


pygame.init()
pygame.mixer.init()

#gerando tela principal
WIDTH = 700
HEIGHT = 780
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('jogo do digao e brunao')

#inicia assets
background= pygame.image.load('assets/img/Rua.png')
background = pygame.transform.scale(background,(WIDTH,HEIGHT))
jogador_img= pygame.image.load('assets/img/carro.frente.png')
jogador_direita_img= pygame.image.load('assets/img/car.Direita.png')
jogador_esquerda_img= pygame.image.load('assets/img/car.Esquerda.png')




#iniciando estrutura de dados
#Definindo classes
class Jogador(pygame.sprite.Sprite):
    def __init__(self, img):
        # Classe mae(sprite)
        pygame.sprite.Sprite.__init__(self)

        self.image= img
        self.rect= self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom= HEIGHT - 10
        self.speedx = 0

    def update(self):
        #atualiza posicao do jogador
        self.rect.x += self.speedx

        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0



#criando um grupo de sprites
all_sprites = pygame.sprite.Group()


# Criando o jogador
player= Jogador(jogador_img)
all_sprites.add(player)

    





#loop principal do jogo
game = True
while game:
    #    olha os eventos
    for event in pygame.event.get():
        #olha as consequencias
        if event.type == pygame.QUIT:
            game = False
        #verifica se apertou teclas
        if event.type == pygame.KEYDOWN:
            # Altera a velocidade
            if event.key == pygame.K_LEFT:
                player.speedx -= 8
            if event.key == pygame.K_RIGHT:
                player.speedx += 8 
        #verifica se soltou teclas
        if event.type == pygame.KEYUP:
            #altera a velocidade
            if event.key == pygame.K_LEFT:
                player.speedx += 8
            if event.key == pygame.K_RIGHT:
                player.speedx -= 8

    #atualizando estado do jogo#
    #atualiza todos os sprites
    all_sprites.update()

    # gera as saidas
    window.fill((255, 255, 255))  # Preenche com a cor branca
    window.blit(background, (0, 0))
    #desenhando sprites
    all_sprites.draw(window)    


    #atualiza o estado do jogo
    pygame.display.update()

#Finalizacao
pygame.quit()

    