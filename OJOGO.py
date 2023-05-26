#Inicio
#Importações
import pygame
import random
import time

print('o jogo')


pygame.init()
pygame.mixer.init()

#gerando tela principal
WIDTH = 700
HEIGHT = 780
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Highway Rush')

#inicia assets
background= pygame.image.load('assets/img/Rua.png').convert_alpha()
background= pygame.transform.scale(background,(WIDTH,HEIGHT))
background2= pygame.image.load('assets/img/Rua.png').convert_alpha()
background2= pygame.transform.scale(background2,(WIDTH,HEIGHT))
jogador_img= pygame.image.load('assets/img/carro.frente.png').convert_alpha()
jogador_direita_img= pygame.image.load('assets/img/car.Direita.png').convert_alpha()
jogador_esquerda_img= pygame.image.load('assets/img/car.Esquerda.png').convert_alpha()
pixel_das_vias= [180, 275, 375, 470] #definido atraves de testes
ini_azul= pygame.image.load('assets/img/inimigo.azul.png')
ini_azul= pygame.transform.scale(ini_azul,(50,100))
ini_vermelho= pygame.image.load('assets/img/inimigo.vermelho.png')
ini_vermelho= pygame.transform.scale(ini_vermelho,(50,100))
ini_verde= pygame.image.load('assets/img/inimigo.verde.png')
ini_verde= pygame.transform.scale(ini_verde,(50,100))
invrt_azul= pygame.image.load('assets/img/invertido.azul.png')
invrt_azul= pygame.transform.scale(invrt_azul,(50,100))
invrt_vermelho= pygame.image.load('assets/img/invertido.vermelho.png')
invrt_vermelho= pygame.transform.scale(invrt_vermelho,(50,100))
invrt_verde= pygame.image.load('assets/img/invertido.verde.png')
invrt_verde= pygame.transform.scale(invrt_verde,(50,100))
score_font = pygame.font.Font('assets/font/PressStart2P.ttf', 28)
backdeserto= pygame.image.load('assets/img/deserto.png').convert_alpha()
backdeserto= pygame.transform.scale(background,(WIDTH,HEIGHT))
backdeserto2= pygame.image.load('assets/img/deserto.png').convert_alpha()
backdeserto2= pygame.transform.scale(background,(WIDTH,HEIGHT))
gameover=pygame.image.load('assets/img/Game over.png')
gameover=pygame.transform.scale(gameover,(WIDTH,HEIGHT))

#inicia sons
batida=pygame.mixer.Sound('assets/audios/batida.wav')
buzina=pygame.mixer.Sound('assets/audios/Buzina.wav')
som_motor=pygame.mixer.music.load('assets/audios/Audio carro.wav')
som_motor=pygame.mixer.music.set_volume(7)
som_motor=pygame.mixer.music.play()


#iniciando estrutura de dados
#Definindo classes
class Jogador(pygame.sprite.Sprite):
    def __init__(self, img, esq, dire):
        # Classe mae(sprite)
        pygame.sprite.Sprite.__init__(self)
        self.direita= dire
        self.esquerda = esq
        self.original= img
        self.image= img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect= self.image.get_rect()
        self.rect.centerx =( WIDTH / 3.5)+100*2
        self.rect.bottom= HEIGHT - 150
        self.speedx = 0

    def update(self):
        #atualiza posicao do jogador
        self.rect.x += self.speedx
        if R == 1:
            self.image= self.esquerda
        if R == 2:
            self.image = self.direita
        if R == 3:
            self.image= self.original
        
        # Mantem dentro da tela
        if self.rect.right > WIDTH - 160:
            self.rect.right = WIDTH - 160
        if self.rect.left < 160:
            self.rect.left = 160

#classe dos carros inimigos
class Inimigo(pygame.sprite.Sprite):
    def __init__(self,img,img2):
        #classe mae(sprite)
        pygame.sprite.Sprite.__init__(self)
        self.contra = img
        self.afavor = img2
        inicio = random.choice(pixel_das_vias)
        if inicio == 180 or inicio == 275:
            self.image = self.contra
            self.rect = self.image.get_rect()
            self.rect.y = random.randint(-100, -50)
            self.rect.x = inicio
            self.speedx = 0
            self.speedy = random.randint(14, 20)
            self.mask = pygame.mask.from_surface(self.image)
        else:
            self.image= self.afavor
            self.rect = self.image.get_rect()
            self.rect.y = random.randint(-100, -50)
            self.rect.x = inicio
            self.speedx = 0
            self.speedy = random.randint(5, 9)
            self.mask = pygame.mask.from_surface(self.image)


    def update(self):
        #atulizando inimigo
        self.rect.y += self.speedy

        #caso chegue no final, volta e sorteia nova posicao
        if self.rect.top > HEIGHT:
            inicio = random.choice(pixel_das_vias)
            if inicio == 180 or inicio == 275:
                self.image= self.contra
                self.rect= self.image.get_rect()
                self.rect.y = random.randint(-100, -50)
                self.speedy = random.randint(14, 20)
                self.rect.x= inicio
            else:
                self.image= self.afavor
                self.rect= self.image.get_rect()
                self.rect.x= inicio
                self.rect.y = random.randint(-100, -50)
                self.speedx = 0
                self.speedy = random.randint(5, 9) 

class cenario(pygame.sprite.Sprite):
    def __init__(self, img, altura):
        #classe mae
        pygame.sprite.Sprite.__init__(self)

        self.image= img
        self.rect= self.image.get_rect()
        self.rect.x = 0
        self.rect.y = altura
        self.speedy= 10

    def update(self):
        #atualizando cenario
        self.rect.y += self.speedy

        #ao chegar no final, reseta
        if self.rect.top >= HEIGHT:
            self.rect.bottom = 0
            


# Variavel para o ajuste de framerate
clock = pygame.time.Clock()
Fps= 60

#criando um grupo de sprites
all_sprites = pygame.sprite.Group()
all_ini = pygame.sprite.Group()

#criando background
background = cenario(background,0)
background2 = cenario(background2,-HEIGHT)
all_sprites.add(background)
all_sprites.add(background2)
# Criando o jogador
player= Jogador(jogador_img,jogador_esquerda_img,jogador_direita_img)
all_sprites.add(player)

#criando inimigos
for i in range(4):
    cor = random.choice([ini_azul,ini_verde,ini_vermelho])
    cor2 = random.choice([invrt_azul,invrt_verde,invrt_vermelho])
    carrinho = Inimigo(cor,cor2)
    all_sprites.add(carrinho)
    all_ini.add(carrinho)
    


#configs iniciais
score = 0


#loop principal do jogo
game = True
while game:
    clock.tick(Fps)
    R=0
    score += 2
    #    olha os eventos
    for event in pygame.event.get():
        #olha as consequencias
        if event.type == pygame.QUIT:
            game = False
        #verifica se apertou teclas
        if event.type == pygame.KEYDOWN:
            # Altera a velocidade
            if event.key == pygame.K_LEFT:
                R=1
                player.speedx -= 8
            if event.key == pygame.K_RIGHT:
                R=2
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
            R = 3
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
    text_surface= score_font.render("{:08d}".format(score), True, (255, 255, 0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (WIDTH / 2,  10)
    window.blit(text_surface, text_rect)

    #desenhando level
    if score < 300:
        level= score_font.render('Level 1', True, (255, 255, 0))
        level_rect = level.get_rect()
        level_rect.midtop = (WIDTH / 2,  40)
        window.blit(level, level_rect)







    #atualiza o estado do jogo
    pygame.display.update()

    #Verifica colisao entre jogador e inimigo
    hits= pygame.sprite.spritecollide(player, all_ini, True, pygame.sprite.collide_mask)
    if len(hits) > 0 :
        pygame.mixer.music.pause()
        pygame.mixer.Sound.play(batida)
        score = 0
        carrinho
        # # Exibe a imagem "Game Over"
        window.blit(gameover, (0, 0))
        pygame.display.update()

        # Aguarda o jogador pressionar qualquer botão
        jogando=True
        while jogando:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                    jogando=False
                if event.type == pygame.KEYDOWN:
                    # Reinicia o jogo
                    pygame.mixer.music.unpause()
                    player.rect.centerx = (WIDTH / 3.5) + 100 * 2
                    player.rect.bottom = HEIGHT - 150
                    all_ini.empty()
                    for i in range(4):
                        cor = random.choice([ini_azul, ini_verde, ini_vermelho])
                        cor2 = random.choice([invrt_azul, invrt_verde, invrt_vermelho])
                        carrinho = Inimigo(cor, cor2)
                        all_sprites.add(carrinho)
                        all_ini.add(carrinho)
                    window.fill((255, 255, 255))
                    pygame.display.update()
                    jogando=False
        

    #Verifica colisao entre inimigos

#anotacoes pra proxima
#fase deserto
#fase inferno
#Som ambiente
#som de batida
#Sons de drift
#mecanica de drift(dois botoes pressionados ao mesmo tempo)
#tela inicial
#contador de pontos
#carro caveira(talvez)




        

#Finalizacao
pygame.quit()

    