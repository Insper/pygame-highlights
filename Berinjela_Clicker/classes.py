# Classes

# Importar as bibliotecas e arquivos
from config import largura, altura, Click
import pygame


# Cria classe dos botoes
class Button():
    
    # Cria os botões
    def __init__(self, x, y, imagem):
        self.image = imagem[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
    
    # Cria função aparecer
    def aparecer(self, screen, imagem):

        apertou = False # Não apertou o botão

        pos = pygame.mouse.get_pos() # Pega posição do mouse


        if self.rect.collidepoint(pos):
            self.image = imagem[1] # Troca imagem

            if pygame.mouse.get_pressed()[0] == True:
                apertou = True # Apertou o botão
                pygame.mixer.Channel(1).play(pygame.mixer.Sound(Click))  # Toca o som do botão
                pygame.mixer.Channel(1).set_volume(0.5)


        if self.rect.collidepoint(pos) == False:
            self.image = imagem[0] # Troca a imagem


        screen.blit(self.image, self.rect) # Coloca o botão na tela 
            

        return apertou

# Cria a classe berinjela

class Berinjela(pygame.sprite.Sprite):

    # Cria a Berinjela
    def __init__(self, img, tam):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img[0] # imagem da sprite
        self.image = pygame.transform.scale(self.image, tam) # transform da imagem
        self.rect = self.image.get_rect() # pega o retangulo da imagem
        self.rect.centerx = largura/2 # centro da imagem x
        self.rect.centery = (altura)/2-60# centro da imagem y
        self.i = 0 # variavel i
        self.last_update = 0 # pega a ultima vez que essa imagem apareceu

    # Cria a berinjela que age como botão
    def Botaoberi(self, screen, imagem, x, y):
        # Verifica o tick atual.
        now = pygame.time.get_ticks() # Pega os ticks
        elapsed_ticks = now - self.last_update # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        self.rect.x = x # retangulo x
        self.rect.y = y # retangulo y
        apertou = False # nao apertou
        soltou = True # soltou o botao

        pos = pygame.mouse.get_pos() # pega a posição do mouse

        if self.rect.collidepoint(pos) == False:
            self.image = imagem[2] # troca a imagem
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == True and elapsed_ticks >= 20 and soltou == True:
                soltou = False # nao soltou o botao
                apertou = True # apertou o botao
                self.i += 1 # aumenta 1 na variavel i
                if self.i % 2 == 1:
                    self.image = imagem[0] # troca imagem
                pygame.time.delay(50)
                if self.i % 2 == 0:
                    self.image = imagem[1] # troca imagem
                self.last_update = pygame.time.get_ticks() # muda o lastupdate
        if pygame.mouse.get_pressed()[0] == True:
            soltou = False # nao soltou o mouse
        else:
            soltou = True # soltou o mouse
        pygame.time.delay(50)
        screen.blit(self.image, self.rect)  # aparece na tela

        return apertou