import pygame
from pygame.locals import *
from sys import exit
import random

pygame.init()

x = 10 #posição inicial em X do boneco
y = 200 #posição inicial em Y do boneco
posicao = 100 #distancia em Y que o boneco pula, ao alternar de pista
acertos = 0

tela = pygame.display.set_mode((750,600))
pygame.display.set_caption('Indiana Jones: Math Run')

fonte = pygame.font.SysFont('Press Start K',50,True,False)
fonte2 = pygame.font.SysFont('Press Start K',80,True,False)
fonte3 = pygame.font.SysFont('Press Start K',30,True,False)


class Corredor(pygame.sprite.Sprite): #classe que norteia o movimento do boneco
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []

        self.sprites.append(pygame.image.load('sprites/Run__000.png'))
        self.sprites.append(pygame.image.load('sprites/Run__001.png'))
        self.sprites.append(pygame.image.load('sprites/Run__002.png'))
        self.sprites.append(pygame.image.load('sprites/Run__003.png'))
        self.sprites.append(pygame.image.load('sprites/Run__004.png'))
        self.sprites.append(pygame.image.load('sprites/Run__005.png'))
        self.sprites.append(pygame.image.load('sprites/Run__006.png'))
        self.sprites.append(pygame.image.load('sprites/Run__007.png'))
        self.sprites.append(pygame.image.load('sprites/Run__008.png'))
        self.sprites.append(pygame.image.load('sprites/Run__009.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image,(415//6,507//6))
        self.rect = self.image.get_rect()
        self.rect.topleft = x,y
    def update(self):
        self.atual= self.atual + 0.25
        if self.atual>= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (415 // 6, 507 // 6))
        self.rect.topleft = x, y


def reiniciarjogo (): #função que retoma o jogo do início
    global acertos,x,y,errou_e_ganhou
    acertos = 0
    x = 10
    y = 200
    errou_e_ganhou = False
    novasperguntas()
def opcaoerrada(): #Função que é acionada quando uma resposta é dada como errada
    global errou_e_ganhou,x,y,acertos

    errou_e_ganhou = True
    while errou_e_ganhou:
        tela.blit(imagem_derrota,(0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_r:
                    reiniciarjogo()

        pygame.display.update()


def novasperguntas (): #função responsável por gerar novas perguntas
    global  termo1,termo2,respostas,respostas_aleatorias,letraA,letraB,letraC,letraD
    termo1 = random.randint(6,20)
    termo2 = random.randint(6, 15)
    respostas = [termo1 * termo2, random.randint(10, 200), random.randint(10, 200), random.randint(10, 200)]
    respostas_aleatorias = random.sample(respostas, 4)
    letraA = fonte.render(str(respostas_aleatorias[0]), False, (255, 255, 0))
    letraB = fonte.render(str(respostas_aleatorias[1]), False, (255, 255, 0))
    letraC = fonte.render(str(respostas_aleatorias[2]), False, (255, 255, 0))
    letraD = fonte.render(str(respostas_aleatorias[3]), False, (255, 255, 0))

todas_as_sprites = pygame.sprite.Group()
corredor = Corredor()
todas_as_sprites.add(corredor)

relogio = pygame.time.Clock()

imagem_fundo = pygame.image.load('imagens/ruina.gif').convert()
imagem_fundo = pygame.transform.scale(imagem_fundo,(750,600))

termo1 = random.randint(1,20)
termo2 = random.randint(1,15)

respostas = [termo1 * termo2, random.randint(10, 200), random.randint(10, 200), random.randint(10, 200)]
respostas_aleatorias = random.sample(respostas, 4)

moldura = pygame.image.load('imagens/moldura2.png')
moldura = pygame.transform.scale(moldura, (100,60))

imagem_inicio = pygame.image.load('imagens/indiana jones background.png').convert()
imagem_inicio = pygame.transform.scale(imagem_inicio,(750,600))
imagem_vitoria = pygame.image.load('imagens/tela vitória.png').convert()
imagem_vitoria = pygame.transform.scale(imagem_vitoria,(750,600))
imagem_derrota = pygame.image.load('imagens/jones derrota.png').convert()
imagem_derrota = pygame.transform.scale(imagem_derrota,(750,600))

errou_e_ganhou = False

menu = True
musica_acertos = pygame.mixer.Sound('audio/smw_coin.wav')
musica_menu = pygame.mixer.music.load('audio/musica-do-indiana-jones.mp3')
pygame.mixer.music.play(-1)
while menu: #Laço que é acionado no início do programa, como se fosse o menu
    tela.blit(imagem_inicio, (0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                menu = False

    pygame.display.flip()
pygame.mixer.music.stop()
pygame.mixer.music.set_volume(0.08)
musica_fundo = pygame.mixer.music.load('audio/BoxCat Games - CPU Talk.mp3')
pygame.mixer.music.play(-1)


while True:
    relogio.tick(100)
    tela.fill([0,0,0])

    conta = (f'{termo1} x {termo2} = ')
    pontos = (f'Pontos: {acertos}')

    texto_formatado = fonte2.render(conta, False, (255, 255, 0))
    pontos_formatado = fonte3.render(pontos,False,(255,255,0))
    letraA = fonte.render(str(respostas_aleatorias[0]),False,(255,255,0))
    letraB = fonte.render(str(respostas_aleatorias[1]),False,(255,255,0))
    letraC = fonte.render(str(respostas_aleatorias[2]),False,(255,255,0))
    letraD = fonte.render(str(respostas_aleatorias[3]),False,(255,255,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_UP and y>=300:
                y = y - posicao #comando responsável por fazer o boneco ir a uma pista acima
            if event.key == K_DOWN and y<=400:
                y = y + posicao #comando responsável por fazer o boneco ir a uma pista abaixo
    if pygame.key.get_pressed()[K_RIGHT] and x<600:
        x = x + 2

    x = x + 1

    if x == 750:
        novasperguntas()
        x = 10

    tela.blit(imagem_fundo,(0,0))
    todas_as_sprites.draw(tela)
    todas_as_sprites.update()

    pygame.draw.line(tela,(255,255,255),(0,200),(750,200),4)
    pygame.draw.line(tela,(255,255,255),(0,300),(750,300),4)
    pygame.draw.line(tela,(255,255,255),(0,400),(750,400),4)
    pygame.draw.line(tela, (255, 255, 255), (0, 500), (750, 500), 4)
    tela.blit(texto_formatado, (325, 80))

    tela.blit(moldura, (635,236))
    tela.blit(moldura, (635, 336))
    tela.blit(moldura, (635, 436))
    tela.blit(moldura, (635, 536))

    if y == 200 and x == 740: #estruturas condicionais para o caso de resposta errada em cada pista
        if respostas_aleatorias[0] != (termo1 * termo2):

            opcaoerrada()

        else:
            musica_acertos.play()
            acertos+=1


    elif y == 300 and x == 740:
        if respostas_aleatorias[1] != (termo1 * termo2):

            opcaoerrada()
        else:
            musica_acertos.play()
            acertos+=1


    elif y == 400 and x == 740:
        if respostas_aleatorias[2] != (termo1 * termo2):

            opcaoerrada()
        else:
            musica_acertos.play()
            acertos+=1


    elif y == 500 and x == 740:
        if respostas_aleatorias[3] != (termo1 * termo2):

            opcaoerrada()
        else:
            musica_acertos.play()
            acertos+=1


    tela.blit(pontos_formatado,(100,80))
    if acertos == 10: #estrutura condicional que vai nortear as ações após ganhar o jogo
        pygame.mixer.music.stop()
        pygame.mixer.music.load('audio/intro-do-jogo-ao-som-de-raca-negra.mp3')
        pygame.mixer.music.play(-1)

        errou_e_ganhou = True
        while errou_e_ganhou:
            tela.blit(imagem_vitoria,(0,0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_j:
                        pygame.mixer.music.stop()
                        pygame.mixer.music.set_volume(0.08)
                        musica_fundo = pygame.mixer.music.load('audio/BoxCat Games - CPU Talk.mp3')
                        pygame.mixer.music.play(-1)
                        reiniciarjogo()
            pygame.display.update()

    tela.blit(letraA,(650,250))
    tela.blit(letraB,(650,350))
    tela.blit(letraC,(650,450))
    tela.blit(letraD,(650,550))


    pygame.display.flip()