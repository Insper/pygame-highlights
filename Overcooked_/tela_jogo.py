
import pygame
from class_jogador import Jogador
from class_spritesheet import SpriteSheet
from class_interacao import Interacao
from class_pedidos import Pedidos
from tela_gameover import Tela_gameover


class Tela_jogo:
    def __init__(self):
        self.fundo_pedido = pygame.transform.scale(pygame.image.load('assets/img/fundo_pedido.png'), (140,70))
        self.fundo_inventario_batata = pygame.transform.scale(pygame.image.load('assets/img/fundo_pedido.png'), (50,50))
        self.fundo_inventario_refri = pygame.transform.scale(pygame.image.load('assets/img/fundo_pedido.png'), (50,50))
        self.fundo_inventario_hamburguer = pygame.transform.scale(pygame.image.load('assets/img/fundo_pedido.png'), (50,50))
        self.player_img = pygame.transform.scale(pygame.image.load('assets/img/jogador.png'), (80,80))
        self.hamburger = pygame.transform.scale(pygame.image.load('assets/img/burger.png'), (45,45))
        self.fritas = pygame.transform.scale(pygame.image.load('assets/img/French_fries.png'),(35,35))
        self.refri = pygame.transform.scale(pygame.image.load('assets/img/Soda.png'), (35,35))
        self.fogao = pygame.transform.scale(pygame.image.load('assets/img/fogao.png'), (100,100))
        self.fogao_esquerda = pygame.transform.scale(pygame.image.load('assets/img/fogao_esquerda.png'), (60,80))
        self.fogao_direita = pygame.transform.scale(pygame.image.load('assets/img/fogao_direita.png'), (80,80))
        default_font_name = pygame.font.get_default_font()
        self.font = pygame.font.Font(default_font_name, 24)
        self.jogador = Jogador(self.player_img, 510-40, 320, 0, 0)
        self.fundo = pygame.transform.scale(pygame.image.load('assets/img/mapav2.png'), (720, 720))
        self.lastupdate = 0
        self.sprite_direita = self.player_img
        self.spriteatual = self.player_img
        self.sprite_cima = self.player_img
        self.sprite_esquerda = pygame.transform.flip(self.sprite_direita, True, False)
        self.tempo_refri = False
        self.tempo_batata = False
        self.tempo_lanche = False
        self.last = 0
        self.t3 = 6000
        self.pontuacao = 0
        self.vidas = 3
        self.t4 = 6000
        self.som_sino = pygame.mixer.Sound('assets/audios/som_sino_pygame.mp3')
        #self.musica_fundo = pygame.mixer.music.load('assets/snd/tgfcoder-FrozenJam-SeamlessLoop.ogg')

        self.espacos_pedidos = {
            'espaço1': {'lugar': (5,0), 'ocupado': False, 'tipo': None},
            'espaço2': {'lugar': (5, 110), 'ocupado': False, 'tipo': None}, 
            'espaço3': {'lugar': (5, 220), 'ocupado': False, 'tipo': None},
            'espaço4': {'lugar': (5, 330), 'ocupado': False, 'tipo': None}}
        
        self.temporizadores = {
            'temporizador1': {'tempo': None, 'iniciado': False},
            'temporizador2': {'tempo': None, 'iniciado': False},
            'temporizador3': {'tempo': None, 'iniciado': False},
            'temporizador4': {'tempo': None, 'iniciado': False},
        }
        
        self.espacos_items = {
            'espaço1': {'lugar': (885, 70), 'ocupado': False, 'tipo': None},
            'espaço2': {'lugar': (955,70), 'ocupado': False, 'tipo': None} ,
            'espaço3': {'lugar': (885, 160),'ocupado': False, 'tipo': None}, 
            'espaço4': {'lugar': (955, 160), 'ocupado': False, 'tipo': None}}
        
        self.pedidos = Pedidos(self.espacos_pedidos, self.espacos_items, self.pontuacao)

    def atualiza(self, dt):
        #DeltaT
        t1 = pygame.time.get_ticks()
        deltaT = (t1 - self.lastupdate) / 1000
        self.lastupdate = t1

        t2 = pygame.time.get_ticks()
        if self.last == 0:
            self.last = t2
            tempo = (t2 - self.last)
        else:
            tempo = (t2 - self.last)
        
        if tempo >= self.t3:
            self.t3 += self.t4
            if self.t4 >= 4000:
                self.t4 -= 500
            self.pedidos.sorteia()
            
        #Rects
        mesa_cima = pygame.Rect(250, 69, 720, 1)
        mesa_direita = pygame.Rect(820, 0, 10, 720)
        mesa_esquerda = pygame.Rect(235, 119, 1, 720)
        mesa_baixo = pygame.Rect(250, 517, 720, 1)
        jogador_rect = pygame.Rect(self.jogador.x, self.jogador.y, 80, 80)
        rect_fogao_esquerda = pygame.Rect(403, 133, 1,1)
        rect_fogao_direita = pygame.Rect(453, 133, 1,1)
        rect_fogao_cima = pygame.Rect(430, 138, 1,1)
        rect_fritadeira_esquerda = pygame.Rect(668, 133, 1,1)
        rect_fritadeira_direita = pygame.Rect(700, 133, 1,1)
        rect_fritadeira_cima = pygame.Rect(688, 138, 1,1)
        rect_fogao = pygame.Rect(430, 124, 10, 20)
        rect_refri = pygame.Rect(780, 310, 2, 20)
        rect_fritadeira = pygame.Rect(668, 124, 10, 20)
        rect_entrega = pygame.Rect(600, 490, 20, 30)

        #Event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.jogador.velx += 200
                    self.jogador.img = self.sprite_direita
                if event.key == pygame.K_LEFT:
                    self.jogador.velx -= 200
                    self.jogador.img = self.sprite_esquerda
                if event.key == pygame.K_UP:
                    self.jogador.vely -= 200
                    self.jogador.img = self.sprite_cima
                if event.key == pygame.K_DOWN:
                    self.jogador.vely += 200
                if event.key == pygame.K_z:
                    if jogador_rect.colliderect(rect_fogao):
                        if self.tempo_lanche == False:
                            self.tempo_lanche = True
                            self.hamburger_t = Interacao('hamburger', 5000)
                        if self.hamburger_t.terminou == True:
                            self.tempo_lanche = False
                            for espacos in self.espacos_items.values():
                                if espacos['ocupado'] == False:
                                    espacos['ocupado'] = True
                                    espacos['tipo'] = 'hamburger'
                                    break

                    if jogador_rect.colliderect(rect_refri):
                        if self.tempo_refri == False:
                            self.tempo_refri = True
                            self.refri_t = Interacao('refri', 3000)
                        if self.refri_t.terminou == True:
                            self.tempo_refri = False
                            for espacos in self.espacos_items.values():
                                if espacos['ocupado'] == False:
                                    espacos['ocupado'] = True
                                    espacos['tipo'] = 'refri'
                                    break

                    if jogador_rect.colliderect(rect_fritadeira):
                        if self.tempo_batata == False:
                            self.tempo_batata = True
                            self.fritas_t = Interacao('fritas', 4000)
                        if self.fritas_t.terminou == True:
                            self.tempo_batata = False
                            for espacos in self.espacos_items.values():
                                if espacos['ocupado'] == False:
                                    espacos['ocupado'] = True
                                    espacos['tipo'] = 'fritas'
                                    break
                    
                    if jogador_rect.colliderect(rect_entrega):
                        self.pedidos.atualiza()
                        sino = self.som_sino
                        sino.play()
                              
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.jogador.velx -= 200
                if event.key == pygame.K_LEFT:
                    self.jogador.velx += 200
                if event.key == pygame.K_UP:
                    self.jogador.vely += 200
                if event.key == pygame.K_DOWN:
                    self.jogador.vely -= 200
        
        if self.vidas < 1:
            return Tela_gameover()

        #Posição Jogador
        self.jogador.atualiza(deltaT)
        if jogador_rect.colliderect(mesa_cima):
            self.jogador.y = 70
        if jogador_rect.colliderect(mesa_direita):
            self.jogador.x = 735
        if jogador_rect.colliderect(mesa_esquerda):
            self.jogador.x = 236
        if jogador_rect.colliderect(mesa_baixo):
            self.jogador.y = 436
        if jogador_rect.colliderect(rect_fogao_esquerda):
            self.jogador.x = 323
        if jogador_rect.colliderect(rect_fogao_direita):
            self.jogador.x = 456
        if jogador_rect.colliderect(rect_fogao_cima):
            self.jogador.y = 139
        if jogador_rect.colliderect(rect_fritadeira_esquerda):
            self.jogador.x = 587
        if jogador_rect.colliderect(rect_fritadeira_direita):
            self.jogador.x = 702
        if jogador_rect.colliderect(rect_fritadeira_cima):
            self.jogador.y = 139
        return self


    def desenha(self, window, assets):
        
        window.fill((0, 0, 0))
        fonte_padrao = pygame.font.get_default_font()
        fonte = pygame.font.Font(fonte_padrao, 15)

        #carrega_tempo
        for i in range(5):
            window.blit(fonte.render(f'@', True, (255, 255, 255)), (350+i, 60))

        for i in range(self.tempo_batata):
            window.blit(fonte.render(f'#', True, (255, 255, 255)), (350+i, 60))

        window.blit(self.fundo, (150, 0))
        
        window.blit(self.jogador.img, (self.jogador.x, self.jogador.y))

        #Pedidos
        for key, values in self.espacos_pedidos.items():
            if values['ocupado']:
                if not values.get('temporizador'): 
                    values['temporizador'] = {'tempo': None, 'iniciado': False}
                temporizador = values['temporizador']
                if not temporizador['iniciado']:
                    temporizador['iniciado'] = True
                tempo_restante = self.pedidos.time(key)
                altura_barra = 15
                largura_b = 100
                largura_barra = int((tempo_restante / 12000) * largura_b)
                x_barra = values['lugar'][0]
                y_barra = values['lugar'][1]
                window.blit(self.fundo_pedido, (x_barra, y_barra))
                pygame.draw.rect(window, (255, 255, 255), (x_barra+ 20, y_barra, largura_barra, altura_barra))
                pygame.draw.line(window, (0, 0, 0), (x_barra+ 20, y_barra), (x_barra+ 20 + largura_barra, y_barra), 3)
                pygame.draw.line(window, (0, 0, 0), (x_barra+ 20, y_barra + altura_barra), 
                                (x_barra+ 20 + largura_barra, y_barra + altura_barra), 3)
                pygame.draw.line(window, (0, 0, 0), (x_barra+ 20, y_barra), (x_barra+ 20, y_barra + altura_barra), 3)
                pygame.draw.line(window, (0, 0, 0), (x_barra+ 20 + largura_barra, y_barra), 
                                (x_barra+ 20 + largura_barra, y_barra + altura_barra), 3)
                if tempo_restante > 0:
                    pos_x_icone = x_barra + largura_b // 2 
                    pos_y_icone = y_barra + altura_barra + 5 
                    if values['tipo'] == 'hamburger':
                        window.blit(self.hamburger, (pos_x_icone, pos_y_icone))
                    if values['tipo'] == 'fritas':
                        window.blit(self.fritas, (pos_x_icone, pos_y_icone))
                    if values['tipo'] == 'refri':
                        window.blit(self.refri, (pos_x_icone, pos_y_icone))
                else:
                    temporizador['iniciado'] = False 
                    values['ocupado'] = False
                    self.vidas -= 1

        #Barra  
        if self.tempo_lanche == True:
            self.hamburger_t.atualiza()
            pygame.draw.polygon(window, (255,255,255), ([(390,84), (390+self.hamburger_t.x,84), (390+self.hamburger_t.x, 104), (390, 104)]))
            pygame.draw.line(window, (0,0,0), (390, 84), (470, 84), 3)
            pygame.draw.line(window, (0,0,0), (390, 104), (470, 104), 3)
            pygame.draw.line(window, (0,0,0), (390, 84), (390, 104), 3)
            pygame.draw.line(window, (0,0,0), (470, 84), (470, 104), 3)
            if self.hamburger_t.x >= 79:
                window.blit(self.hamburger, (410, 105))
        
        if self.tempo_refri == True:
            self.refri_t.atualiza()
            pygame.draw.polygon(window, (255,255,255), ([(785,270), (785+self.refri_t.x,270), (785+self.refri_t.x, 285), (785, 285)]))
            pygame.draw.line(window, (0,0,0), (785, 270), (865, 270), 3)
            pygame.draw.line(window, (0,0,0), (785, 285), (865, 285), 3)
            pygame.draw.line(window, (0,0,0), (785, 270), (785, 285), 3)
            pygame.draw.line(window, (0,0,0), (865, 270), (865, 285), 3)
            if self.refri_t.x >= 80:
                window.blit(self.refri, (815, 295))

        if self.tempo_batata == True:
            self.fritas_t.atualiza()
            pygame.draw.polygon(window, (255,255,255), ([(648, 84), (648+self.fritas_t.x,84), (648+self.fritas_t.x, 104), (648, 104)]))
            pygame.draw.line(window, (0,0,0), (648, 84), (728, 84), 3)
            pygame.draw.line(window, (0,0,0), (648, 104), (728, 104), 3)
            pygame.draw.line(window, (0,0,0), (648, 84), (648, 104), 3)
            pygame.draw.line(window, (0,0,0), (728, 84), (728, 104), 3)
            if self.fritas_t.x >= 80:
                window.blit(self.fritas, (668, 104))

        
        #inventario
        for espacos in self.espacos_items.values():
            if espacos['tipo'] == 'fritas':
                window.blit(self.fundo_inventario_batata, espacos['lugar'])
                window.blit(self.fritas, (espacos['lugar'][0]+7, espacos['lugar'][1]+8))
            elif espacos['tipo'] == 'refri':
                window.blit(self.fundo_inventario_refri, espacos['lugar'])
                window.blit(self.refri, (espacos['lugar'][0]+7, espacos['lugar'][1]+7))
            elif espacos['tipo'] == 'hamburger':
                window.blit(self.fundo_inventario_hamburguer, espacos['lugar'])
                window.blit(self.hamburger, (espacos['lugar'][0]+2, espacos['lugar'][1]+4))

        #coracoes
        fonte_coracao = pygame.font.Font('assets/font/PressStart2P.ttf', 40)
        window.blit(fonte_coracao.render(chr(9829) * self.vidas, True, (255, 0, 0)), (885, 5))

        #pontuacao
        fonte_padrao = pygame.font.get_default_font()
        fonte_escrita = pygame.font.Font(fonte_padrao, 35)
        window.blit(fonte_escrita.render(f'$ {self.pedidos.pontuacao}.00', True, (0, 0, 0)), (550, 40))
        

