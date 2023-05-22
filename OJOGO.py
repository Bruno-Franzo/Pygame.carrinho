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
pygame.display.set_caption('Highway Rush')

#inicia assets
background= pygame.image.load('assets/img/Rua.png')
background= pygame.transform.scale(background,(WIDTH,HEIGHT))
jogador_img= pygame.image.load('assets/img/carro.frente.png')
jogador_direita_img= pygame.image.load('assets/img/car.Direita.png')
jogador_esquerda_img= pygame.image.load('assets/img/car.Esquerda.png')
pixel_das_vias= [180, 275, 375, 470] #definido atraves de testes
ini_azul= pygame.image.load('assets/img/inimigo.azul.png')
ini_azul= pygame.transform.scale(ini_azul,(50,100))
ini_vermelho= pygame.image.load('assets/img/inimigo.vermelho.png')
ini_vermelho= pygame.transform.scale(ini_vermelho,(50,100))
ini_verde= pygame.image.load('assets/img/inimigo.verde.png')
ini_verde= pygame.transform.scale(ini_verde,(50,100))


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
        if self.rect.right > WIDTH - 160:
            self.rect.right = WIDTH - 160
        if self.rect.left < 160:
            self.rect.left = 160

#classe dos carros inimigos

class Inimigo(pygame.sprite.Sprite):
    def __init__(self,img):
        #classe mae(sprite)
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(pixel_das_vias)
        self.rect.y = random.randint(-100, -50)
        self.speedx = 0
        self.speedy = random.randint(8, 10)

    def update(self):
        #atulizando inimigo
        self.rect.y += self.speedy

        #caso chegue no final, volta e sorteia nova posicao
        if self.rect.top > HEIGHT:
            self.rect.x = random.choice(pixel_das_vias)
            self.rect.y = random.randint(-100, -50)
            self.speedy = random.randint(8, 10)



# Variavel para o ajuste de framerate
clock = pygame.time.Clock()
Fps= 30

#criando um grupo de sprites
all_sprites = pygame.sprite.Group()
all_ini = pygame.sprite.Group()

# Criando o jogador
player= Jogador(jogador_img)
all_sprites.add(player)

#criando inimigos
for i in range(4):
    cor = random.choice([ini_verde,ini_azul,ini_vermelho])
    carrinho = Inimigo(cor)
    all_sprites.add(carrinho)
    all_ini.add(carrinho)

    





#loop principal do jogo
game = True
while game:
    clock.tick(Fps)
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

    