import pygame
from classes_personagens import *
from classes_objetos import *

class Start:
    def __init__(self, dimen, clock, assets):

        self.fase = pygame.image.load("Sprites/Maps/first.png")

        self.largura_tela = dimen[0]
        self.altura_tela = dimen[1]

        self.fase = pygame.transform.scale(self.fase, (self.largura_tela, self.altura_tela))

        self.dimen = dimen

        self.clock = clock
        self.assets = assets

        self.sprite = pygame.sprite.Group()

        self.player = Jogador(assets, self.clock, False)

        self.sprite.add(self.player)

        self.player.rect.x, self.player.rect.y = (self.largura_tela//2 - self.player.rect.w + 13, 600)

        self.player.size = 10

        self.ritmo = Rythm(self.clock, 223, '1011001010110110', 'Sounds/introd_2.wav', 'Sounds/loop_2.wav')

    def update(self):

        for event in pygame.event.get(pygame.QUIT): # Retorna uma lista com todos os eventos que ocorreram desde a última vez que essa função foi chamada
            if event.type == pygame.QUIT: 
                return -2
            
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_ESCAPE]:
            return -1
            
        self.ritmo.update()

        self.sprite.update()

        if self.ritmo.acertou_ritmo == 4:
            self.player.vel_y = 100
            self.player.control_facing = False
            self.player.facing = 'Back'

        if self.player.rect.y > self.altura_tela:
            return 1

        return 0

    def draw(self, window):

        window.fill((0, 0, 0))

        window.blit(self.fase, (0,0))

        self.sprite.draw(window)

        # pygame.draw.rect(window, (255,255,255), self.ritmo.main_bar)
        # pygame.draw.rect(window, (255,255,255), self.ritmo.second_bar)

        # for pos in self.ritmo.bars:
        #     pygame.draw.rect(window, (255,0,0), (pos[0], pos[1], 5, 100))

        pygame.display.update()


        


class RoomBoss1:
    def __init__(self, dimen, clock, assets):
        '''
        Função que define a classe RoomBegin

        parâmetro self: representa a própria classe
        parâmetro dimen: representa as dimensões da tela
        parâmetro clock: representa o tempo dos frames
        paràmetro assets: dicionário com alguns valores importantes para o jogo
        '''

        self.largura_tela = dimen[0]
        self.altura_tela = dimen[1]

        self.dimen = dimen

        self.clock = clock
        self.assets = assets
        self.sprites = pygame.sprite.Group()
        self.tiros = pygame.sprite.Group()
        self.boss = pygame.sprite.Group()
        self.tiros_boss = pygame.sprite.Group()
        self.tiros_boss_frente = pygame.sprite.Group()
        self.tiros_boss_tras = pygame.sprite.Group()
        self.helis = pygame.sprite.Group()
        self.shield_group = pygame.sprite.Group()
        self.shockwave_group = pygame.sprite.Group()

        self.tiros_da_frente = [(95, 77.5), (73, 77.5), (51, 77.5), (51, 77.5), (29, 77.5), (7, 77.5)]

        self.personagem = Jogador(assets, clock, True)
        self.sprites.add(self.personagem)
        self.boss1 = Boss1(self.dimen, self.clock, self.assets)
        self.ui = UI(self.personagem, self.boss1, 1)
        self.boss.add(self.boss1)

        self.fire_rate = 300
        self.count_fr = 0

        self.pos_tiro_circular_i = [(100, 69), (95, 77.5), (73, 77.5), (51, 77.5), (51, 77.5), (29, 77.5), (7, 77.5), (0, 69), (0, 69)]
        self.pos_tiro_circular_j = [(100, 69), (100, 69), (95, 60), (73, 60), (51, 60), (51, 60), (29, 60), (7, 60), (0, 69)]

        self.fase = pygame.image.load("Sprites/Maps/1.png")
        self.fase = pygame.transform.scale(self.fase, (self.largura_tela, self.altura_tela))

        self.helis_pos = []

        self.tiro_circular = {}
        for i in range(9):

            k = i

            j = i

            i += 1
            i *= 20

            j *= 20

            self.tiro_circular[i] = self.pos_tiro_circular_i[k]
            self.tiro_circular[j * (-1)] = self.pos_tiro_circular_j[k]

        self.tiro_horizontal = []
        for i in range (6):
            i += 1
            if i != 1:
                self.tiro_horizontal.append(int((self.altura_tela/5)* i))
                self.helis_pos.append(int((self.altura_tela/5)* i))

        for pos_y in self.helis_pos:
            pos_y -= 120
            heli = Heli(self.clock, (10, pos_y))
            self.helis.add(heli)

        self.ritmo = Rythm(self.clock, 224, '10100110', 'Sounds/introd.wav', 'Sounds/loop.wav')

        self.paredes = [(87,200,25,1000), (1490,200,25,1000), (87,130,1500,30), (87,self.altura_tela,1500,30)]
        self.paredes_info = ['esquerda', 'direita', 'cima', 'baixo']
        self.paredes_sprite = []

        for parede, info in zip(self.paredes, self.paredes_info):
            self.paredes_sprite.append(Parede(parede[0], parede[1], parede[2], parede[3], info))


    def update(self):
        '''
        Função que atualiza a tela do RoomBegin

        parâmetro self: representa a própria classe
        '''

        self.ritmo.update()

        self.helis.update()

        for event in pygame.event.get(pygame.QUIT): # Retorna uma lista com todos os eventos que ocorreram desde a última vez que essa função foi chamada
            if event.type == pygame.QUIT: 
                return -2
            
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_ESCAPE]:
            return -1
            
        if not self.personagem.update():
            return -1

        if pygame.mouse.get_pressed()[0]:
            if self.count_fr == 0:
                self.tiros.add(Tiro(self.personagem, self.assets, self.dimen, self.clock))
            self.count_fr += self.clock.get_time()
            if self.count_fr >= self.fire_rate:
                self.count_fr = 0
        else:
            self.count_fr = 0

        self.tiros.update()

        self.boss.update()

        if not self.boss1.vivo:
            # return 1
            pass

        self.boss1.colide_com_tiros(self.boss, self.tiros)

        if self.boss1.tiro[0]:
            for angle, pos in self.tiro_circular.items():

                tiro = Tiro_boss((self.boss1.rect.x + self.boss1.rect.w/100 * pos[0], self.boss1.rect.y + self.boss1.rect.h/100 * pos[1]), self.assets, self.dimen, self.clock, angle)

                self.tiros_boss.add(tiro)

                if pos in self.tiros_da_frente:
                    self.tiros_boss_frente.add(tiro)
                else:
                    self.tiros_boss_tras.add(tiro)

        if self.boss1.tiro[1]:
            for pos_y in self.tiro_horizontal:

                pos_y -= 80

                tiro = Tiro_boss((90, pos_y), self.assets, self.dimen, self.clock, 0)
                self.tiros_boss_frente.add(tiro)
                self.tiros_boss.add(tiro)

        self.personagem.colide_com_tiros(self.tiros_boss)

        self.ui.update()

        self.tiros_boss.update()

        if self.ritmo.acertou_ritmo == 4 and len(self.shield_group.sprites()) == 0:
            self.shield = Shield(self.personagem, self.clock)
            self.shield_group.add(self.shield)

        if self.ritmo.acertou_ritmo > 4 and self.ritmo.acertou_ritmo % 4 == 0:
            self.shockwave = Shockwave(self.personagem, self.clock, self.dimen)
            self.shockwave_group.add(self.shockwave)
            self.ritmo.acertou_ritmo = 4

        if self.ritmo.acertou_ritmo < 4 and len(self.shield_group.sprites()) != 0:
            self.shield.ativo = False
        
        if len(self.shield_group.sprites()) == 1:     
            self.shield_group.update()
            self.shield.colide_com_tiros(self.shield_group, self.tiros_boss)

        self.shockwave_group.update()

        for parede in self.paredes_sprite:
            parede.colide_com_player(self.personagem)
        
        if len(self.shockwave_group.sprites()) > 0:
            self.boss1.colide_com_shockwave(self.shockwave)

        return 1

    
    def draw(self, window):
        '''
        Função que desenha a tela do jogo

        parâmetro self: representa a própria classe
        parâmetro window: representa a janlea do jogo
        '''

        window.fill((0, 0, 0)) # Prrenche a janela do jogo com a cor preta

        window.blit(self.fase, (0,0))

        self.helis.draw(window)
        self.tiros.draw(window)
        self.sprites.draw(window)
        if len(self.shield_group.sprites()) == 1:     
            self.shield_group.draw(window)
        self.tiros_boss_tras.draw(window)
        self.boss.draw(window)
        self.tiros_boss_frente.draw(window)

        # pygame.draw.rect(window, (255,255,255), self.ritmo.main_bar)
        # pygame.draw.rect(window, (255,255,255), self.ritmo.second_bar)

        # for pos in self.ritmo.bars:
        #     pygame.draw.rect(window, (255,0,0), (pos[0], pos[1], 5, 100))

        pygame.draw.rect(window, (255,255,255), self.boss1.teste)

        self.shockwave_group.draw(window)

        self.ui.draw(window)

        pygame.display.update() # Atualiza a janela do jogo


# class RoomBoss1:
#     def __init__(self, dimen, clock, assets):
#         self.largura_tela = dimen[0]
#         self.altura_tela = dimen[1]
#         self.fundo = pygame.image.load(f"Sprites/Maps/1.png")

#         self.paredes =  pygame.sprite.Group()
#         self.paredes.add(Parede(self.largura_tela // 10, self.altura_tela // 4, self.largura_tela - self.largura_tela // 5, 5))
#         self.paredes.add(Parede(self.largura_tela // 10, self.altura_tela - 1, self.largura_tela - self.largura_tela // 5, 1))
#         self.paredes.add(Parede(self.largura_tela // 10, self.altura_tela // 4, 5, self.altura_tela - self.altura_tela // 4))
#         self.paredes.add(Parede(self.largura_tela - self.largura_tela // 10 - 5, self.altura_tela // 4, 5, self.altura_tela - self.altura_tela // 4))
        

#     def atualiza_estado(self):
#         for event in pygame.event.get(): # Retorna uma lista com todos os eventos que ocorreram desde a última vez que essa função foi chamada
#             if event.type == pygame.QUIT: 
#                 return -1
            
#         return 1

    
#     def desenha(self, window):
#         window.fill((0, 0, 0)) # Preenche a janela do jogo com a cor preta

#         pygame.display.update() # Atualiza a janela do jogo


# class RoomBoss2:
#     def __init__(self, dimen, clock, assets):
#         self.largura_tela = dimen[0]
#         self.altura_tela = dimen[1]
#         self.paredes =  pygame.sprite.Group()
#         self.paredes.add(Parede(0, 0, self.largura_tela, 1))
#         self.paredes.add(Parede(0, self.altura_tela - 15, self.largura_tela, 15))
#         self.paredes.add(Parede(0, 0, 10, self.altura_tela))
#         self.paredes.add(Parede(self.largura_tela - 10, 0, 10, self.altura_tela))
       

#     def atualiza_estado(self):
#         for event in pygame.event.get(): # Retorna uma lista com todos os eventos que ocorreram desde a última vez que essa função foi chamada
#             if event.type == pygame.QUIT: 
#                 return -1
            
#         return 2

    
#     def desenha(self, window):
#         window.fill((0, 0, 0)) # Preenche a janela do jogo com a cor preta

#         pygame.display.update() # Atualiza a janela do jogo


# class RoomFinal:
#     def __init__(self, dimen, clock, assets):
#         self.largura_tela = dimen[0]
#         self.altura_tela = dimen[1]
#         self.fase = pygame.image.load("Sprites/Maps/3.png")
#         self.fase = pygame.transform.scale(self.fase, (self.largura_tela, self.altura_tela))
#         self.paredes =  pygame.sprite.Group()
#         self.paredes.add(Parede(0, self.altura_tela // 4, self.largura_tela, 2))
#         self.paredes.add(Parede(0, self.altura_tela - 1, self.largura_tela, 1))
#         self.paredes.add(Parede(0, self.altura_tela // 4, 1, self.altura_tela - self.altura_tela // 4))
#         self.paredes.add(Parede(self.largura_tela - 1, self.altura_tela // 4, 1, self.altura_tela - self.altura_tela // 4))
        

#     def atualiza_estado(self):
#         for event in pygame.event.get(): # Retorna uma lista com todos os eventos que ocorreram desde a última vez que essa função foi chamada
#             if event.type == pygame.QUIT: 
#                 return -1
            
#         return 3

    
#     def desenha(self, window):
#         window.fill((0, 0, 0)) # Preenche a janela do jogo com a cor preta

#         pygame.display.update() # Atualiza a janela do jogo


# class TelaFinal:
#     def __init__(self, dimen, clock, assets):
#         self.largura_tela = dimen[0]
#         self.altura_tela = dimen[1]
#         self.fonte_padrao = assests['fonte_padrao']
#         self.font_texto = pygame.font.Font(self.fonte_padrao, 20)

    
#     def atualiza_estado(self):
#         for event in pygame.event.get(): # Retorna uma lista com todos os eventos que ocorreram desde a última vez que essa função foi chamada
#             if event.type == pygame.QUIT: 
#                 return -1
        
#         return 4
            
    
#     def desenha(self, window):
#         window.fill((0, 0, 0)) # Preenche a janela do jogo com a cor preta

#         texto_final = self.font_texto.render(f'PARABÉNS! VOCÊ CONSEGIUI A DROGA LENDÄRIA', True, (0, 255, 0)) # Cria uma imagem do texto
#         window.blit(texto_final, (self.largura_tela // 2 - 125, self.altura_tela // 2)) # Desenha a imagem já carregada por pygame.image.load em window na posição (x, y).

#         pygame.display.update() # Atualiza a janela do jogo


# class TelaGameOver:
#     def __init__(self, dimen, clock, assets):
#         self.largura_tela = dimen[0]
#         self.altura_tela = dimen[1]
#         self.fonte_padrao = assests['fonte_padrao']
#         self.font_texto = pygame.font.Font(self.fonte_padrao, 20)
    

#     def atualiza_estado(self):
#         for event in pygame.event.get(): # Retorna uma lista com todos os eventos que ocorreram desde a última vez que essa função foi chamada
#             if event.type == pygame.QUIT: 
#                 return -1
            
#         return 5
        
    
#     def desenha(self, window):
#         window.fill((0, 0, 0)) # Preenche a janela do jogo com a cor preta

#         texto_morte = self.font_texto.render(f'VOCË MORREU', True, (255, 0, 0)) # Cria uma imagem do texto
#         window.blit(texto_morte, (self.largura_tela // 2 - 85, self.altura_tela // 2)) # Desenha a imagem já carregada por pygame.image.load em window na posição (x, y).

#         pygame.display.update()