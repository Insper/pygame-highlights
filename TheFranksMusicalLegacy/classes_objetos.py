import pygame
import math
import random

class Tiro(pygame.sprite.Sprite):
    def __init__(self, player, assets, dimen, clock):
        '''
        Função que define a classe Tiro

        parâmetro self: representa a própria classe
        parâmetro player: representa o jogador
        parâmetro dimen: representa as dimensões da tela
        parâmetro clock: representa o tempo dos frames
        paràmetro assets: dicionário com alguns valores importantes para o jogo
        '''

        self.clock = clock

        pygame.sprite.Sprite.__init__(self)

        self.assets = assets
        self.vel = 650

        tipo = random.randint(1,4)
        cor = random.randint(1,8)

        self.tiro = pygame.image.load(f"Sprites/Projectiles/{tipo}/{cor}.png")
        self.image = pygame.transform.scale_by(self.tiro, 5)
        self.rect = self.image.get_rect()

        self.largura_tela = dimen[0]
        self.altura_tela = dimen[1]

        self.player = player.rect

        center_pos = [self.player.x + (self.player.width/4), self.player.y + self.player.h/4]

        self.rect.x = center_pos[0]
        self.rect.y = center_pos[1]

        self.x_bala = float(self.rect.x)
        self.y_bala = float(self.rect.y)

        x_dist = pygame.mouse.get_pos()[0] - center_pos[0]
        y_dist = pygame.mouse.get_pos()[1] - center_pos[1]

        self.angle = math.degrees(math.atan2(y_dist, x_dist))

    def update(self):
        '''
        Função que atualiza o tiro

        parâmetro self: representa a própria classe
        '''

        self.vel_x = self.vel * math.cos(math.radians(self.angle))
        self.vel_y = self.vel * math.sin(math.radians(self.angle))

        self.x_bala = self.x_bala + self.vel_x * self.clock.get_time()/1000
        self.y_bala = self.y_bala + self.vel_y * self.clock.get_time()/1000

        self.rect.x = int(self.x_bala)
        self.rect.y = int(self.y_bala)

class Tiro_boss(pygame.sprite.Sprite):
    def __init__(self, pos, assets, dimen, clock, angle):
        '''
        Função que define a classe Tiro_boss

        parâmetro self: representa a própria classe
        parâmetro pos: representa a posição d
        parâmetro dimen: representa as dimensões da tela
        parâmetro clock: representa o tempo dos frames
        paràmetro assets: dicionário com alguns valores importantes para o jogo
        parâmetro angle: representa o ângulo de visão do boss
        '''

        pygame.sprite.Sprite.__init__(self)

        self.pos = pos
        self.assets = assets
        self.dimen = dimen
        self.clock = clock
        self.angle = angle

        self.sprite = pygame.image.load("Sprites/Projectiles/Boss/1/1.png")
        self.image = pygame.transform.scale(self.sprite, (30,30))
        
        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = self.pos

        self.vel_x = 0
        self.vel_y = 0

        self.vel = 250

        self.x_bala = float(self.rect.x)
        self.y_bala = float(self.rect.y)

    def update(self):
        '''
        Função que atualiza o Tiro_boss

        parâmetro self: representa a própria classe
        '''

        if self.rect.x > self.dimen[0] or self.rect.x < 0:
            self.kill()
        if self.rect.y > self.dimen[1] or self.rect.y < 0:
            self.kill()

        self.vel_x = self.vel * math.cos(math.radians(self.angle))
        self.vel_y = self.vel * math.sin(math.radians(self.angle))

        self.x_bala = self.x_bala + self.vel_x * self.clock.get_time()/1000
        self.y_bala = self.y_bala + self.vel_y * self.clock.get_time()/1000

        self.rect.x = int(self.x_bala)
        self.rect.y = int(self.y_bala)


class Parede(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, largura, altura, direcao):
        '''
        Função que define a classe Parede

        parâmetro self: representa a própria classe
        parâmetro pos_x: representa a posição x do nato superior esquerdo da parede
        parâmetro pos_y: representa a posição y do nato superior esquerdo da parede
        parâmetro largura: representa a largura da parede
        parâmetro altura: representa a altura da parede
        '''

        self.direcao = direcao
    
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((largura, altura)).fill((0,0,255))

        self.rect = pygame.rect.Rect(pos_x, pos_y, largura, altura)

    def colide_com_player(self, player):
        if self.rect.colliderect(player.rect):
            if self.direcao == 'direita':
                if player.vel_x > 0:
                    player.vel_x = -1
            if self.direcao == 'esquerda':
                if player.vel_x < 0:
                    player.vel_x = 1
            if self.direcao == 'baixo':
                if player.vel_y > 0:
                    player.vel_y = 1
            if self.direcao == 'cima':
                if player.vel_y < 0:
                                        player.vel_y = -1


class Hazzard(pygame.sprite.Sprite):
    def __init__(self, dimen, clock, assets):
        '''
        Função que define a classe Hazzard

        parâmetro self: representa a própria classe
        parâmetro dimen: representa as dimensões da tela
        parâmetro clock: representa o tempo dos frames
        paràmetro assets: dicionário com alguns valores importantes para o jogo
        '''

        self.largura_tela = dimen[0]
        self.altura_tela = dimen[1]
        

    def atualiza_estado(self):
        pass
    
    def desenha(self, window):
        pass

class Rythm():
    def __init__(self, clock, bpm, bin, introd, loop):

        self.clock = clock
        self.bpm = bpm
        self.bin = bin
        self.loop = loop
        self.introd = introd
        self.load = True

        self.metronomo = pygame.mixer.Sound("audio/batida_metronomo.wav")

        self.vel = -(bpm//6)

        self.tolerance = 50

        self.spacing = 100

        self.main_bar = pygame.Rect(0, 0, self.tolerance + 40, 30)

        # self.tolerance += 10

        self.bars = []

        for i, boolean in enumerate(bin):
            i += 1

            if boolean == '1':
                self.bars.append([self.tolerance*2 + (i*self.spacing), 0])

        self.end = (self.spacing * (len(bin)))

        self.second_bar = pygame.Rect(self.end - self.tolerance - 40, 0, self.tolerance + 40, 30)

        self.bpm = 0

        self.cronometro = 0

        self.p_input = 0

        self.acertou_ritmo = 0

        self.errado = False
        self.dentro_do_tempo = True

        self.start_music = False
        self.toca_uma_vez = True
        self.barra_recente = 0

    def update(self):
        '''
        Função que atualiza o rítmo

        parâmetro self: representa a própria classe
        '''

        if self.load:
            pygame.mixer.music.load(self.introd)
            self.load = False

        self.cronometro += self.clock.get_time()
        if self.cronometro >= 1000 * 60:
            self.bpm = 0
            self.cronometro = 0
            

        self.errado = False
        self.dentro_do_tempo = False
        
        self.teclas = pygame.key.get_pressed()

        if self.teclas[pygame.K_SPACE]:
            self.p_input += 1
        else:
            self.p_input = 0

        if self.bars[0][0] <= self.tolerance*2.2:
            if not self.start_music:
                pygame.mixer.music.play()
                pygame.mixer.music.queue(self.loop, "",-1)
                self.start_music = True

        for i in range(len(self.bars)):
            self.bars[i][0] = self.bars[i][0] + self.vel * self.clock.get_time()/100
            if self.bars[i][0] <= 0:
                self.bars[i][0] = self.end + self.bars[i][0]
                self.toca_uma_vez = True

            if self.bars[i][0] <= self.end - self.tolerance and self.bars[i][0] >= self.tolerance:
                self.acerta_uma_vez = True

            if self.bars[i][0] <= self.tolerance:
                if self.toca_uma_vez:
                    # self.metronomo.play()
                    self.bpm += 1
                    # self.toca_uma_vez = False
                
            if self.main_bar.collidepoint(self.bars[i]):

                self.barra_recente = i

                self.dentro_do_tempo = True
                if self.p_input == 1 and self.acerta_uma_vez:
                    self.acertou_ritmo += 1
                    self.acerta_uma_vez = False
                elif self.p_input == 1:
                    self.errado = True

            if self.second_bar.collidepoint(self.bars[i]):

                self.barra_recente = i

                self.dentro_do_tempo = True
                if self.p_input == 1 and self.acerta_uma_vez:
                    self.acertou_ritmo += 1
                    self.acerta_uma_vez = False
                elif self.p_input == 1:
                    self.errado = True
        
        if self.p_input == 1 and not self.dentro_do_tempo:
            self.errado = True
        
        if self.errado:
            self.acertou_ritmo = 0  

class UI():
    def __init__(self, player, boss, index_boss):
        '''
        Função que define a classe UI

        parâmetro self: representa a própria classe
        parâmetro player: representa o jogador
        parâmetro boss: representa o boss
        parâmetro index_boss: número do boss
        '''

        self.player = player
        self.boss = boss

        self.barra_de_vida = pygame.image.load("Sprites/UI/health_bar.png")
        self.barra_de_vida_boss = pygame.image.load(f"Sprites/UI/health_bar_boss{index_boss}.png")

        self.barra_de_vida = pygame.transform.scale_by(self.barra_de_vida, 6)
        self.barra_de_vida_boss = pygame.transform.scale_by(self.barra_de_vida_boss, 6)

        self.vida = pygame.Rect(1300, 920, 250, 35)
        self.vida_boss = pygame.Rect(604, 108, 402, 50)

    def update(self):
        '''
        Função que atualiza o UI

        parâmetro self: representa a própria classe
        '''
        self.vida.w = int(self.player.hp * 5)
        self.vida_boss.w = int(self.boss.hp * 0.4 + 2)

    def draw(self, window):
        '''
        Função que desenha o UI

        parâmetro self: representa a própria classe
        parâmetro window: representa a janlea do jogo
        '''

        pygame.draw.rect(window, (195,0,0), self.vida)
        pygame.draw.rect(window, (255,0,0), self.vida_boss)

        window.blit(self.barra_de_vida, (1275, 900))
        window.blit(self.barra_de_vida_boss, (550, 80))

class Shield(pygame.sprite.Sprite):
    def __init__(self, player, clock):
        pygame.sprite.Sprite.__init__(self)

        self.clock = clock
        self.player = player
        self.cronometro = 0

        self.current_sprite = 0
        
        self.sprites = []
        for i in range(4):
            i += 1
            sprite = pygame.image.load(f"Sprites/Shield/{i}.png")
            self.sprites.append(pygame.transform.scale_by(sprite, 6))
        
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = (player.rect.x - 25, player.rect.y - 25)

        self.ativo = True


    def update(self):
        self.cronometro += self.clock.get_time()

        self.image = self.sprites[self.current_sprite]
        self.rect.x, self.rect.y = (self.player.rect.x - 18, self.player.rect.y - 25)

        if self.current_sprite == 3 and self.ativo:
            self.cronometro = 0

        if self.current_sprite == 0 and not self.ativo:
            if self.cronometro >= 150:
                self.kill()

        if self.current_sprite != 3 and self.ativo:
            if self.cronometro >= 150:
                self.current_sprite += 1
                self.cronometro = 0
        
        if self.current_sprite != 0 and not self.ativo:
            if self.cronometro >= 150:
                self.current_sprite -= 1
                self.cronometro = 0
    
    def colide_com_tiros(self, shield, tiros):
        colisoes = pygame.sprite.groupcollide(shield, tiros, False, True)
    
class Shockwave(pygame.sprite.Sprite):
    def __init__(self, player, clock, dimen):
        pygame.sprite.Sprite.__init__(self)

        self.dimen = dimen
        self.clock = clock
        self.player = player

        self.center_player = (self.player.rect.x + self.player.rect.w//2, self.player.rect.y + self.player.rect.h//2)

        self.radius = 1

        self.sprite = pygame.image.load("Sprites/Projectiles/shockwave.png")
        self.image = pygame.transform.scale(self.sprite, (self.radius*2, self.radius*2))

        self.rect = self.image.get_rect()
        self.rect.x = self.center_player[0] - self.radius
        self.rect.y = self.center_player[1] - self.radius

        self.cronometro = 0

        self.hit = False
    
    def update(self):
        self.cronometro += self.clock.get_time()
        if self.cronometro >= 5:
            self.radius += self.radius/5 + 30
        
        self.image = pygame.transform.scale(self.sprite, (self.radius*2, self.radius*2))

        self.rect = self.image.get_rect()
        self.rect.x = self.center_player[0] - self.radius
        self.rect.y = self.center_player[1] - self.radius

        if self.radius > self.dimen[0]:
            self.kill()

    









