import pygame
from constantes import *

class Cura_pokemon():
    '''
        Classe responsável por desenhar o pokemon center e entregar as paredes (rects)
        para realizar a colisão com as paredes.
    '''
    def __init__(self):
        self.img_box = pygame.transform.scale((pygame.image.load('imgBatalhas/barraVazia.png')),(640, 150))
        self.img_pc = pygame.transform.scale((pygame.image.load('img/pokemonCenter.png')),(640, 400))
        self.fonte = pygame.font.Font('imgBatalhas/fontes.ttf', 18)
        self.porta_pc = pygame.Rect(310, 460, 20, 10)
        self.balcao = pygame.Rect(185, 255, 272, 8)
        self.rect_sim = pygame.Rect(510, 488, 50, 30)
        self.rect_nao = pygame.Rect(510, 538, 50, 30)
        self.rect_pc = pygame.Rect(468, 200, 35, 5)
        self.lista_paredes = [
            pygame.Rect(185, 250, 272, 5),
            pygame.Rect(186, 179, 5, 70),
            pygame.Rect(112, 206, 50, 5),
            pygame.Rect(73, 200, 18, 5),
            pygame.Rect(36, 200, 10, 10),
            pygame.Rect(13, 233, 5, 70),
            pygame.Rect(20, 334, 60, 60),
            pygame.Rect(15, 408, 5, 35),
            pygame.Rect(28, 452, 10, 5),
            pygame.Rect(40, 470, 250, 5),
            pygame.Rect(352, 470, 250, 5),
            pygame.Rect(605, 451, 10, 5),
            pygame.Rect(620, 232, 5, 250),
            pygame.Rect(506, 366, 200, 55),
            pygame.Rect(501, 322, 70, 50),
            pygame.Rect(595, 198, 10, 10),
            pygame.Rect(507, 189, 75, 5),
            pygame.Rect(447, 181, 5, 70),
            pygame.Rect(468, 190, 35, 5),
        ]
        self.texto1 = self.fonte.render('Você gostaria de curar seus pokemons?', True, PRETO)
        self.texto_sim = self.fonte.render('SIM', True, PRETO)
        self.texto_nao = self.fonte.render('NÃO', True, PRETO)
        self.mouse = pygame.mouse.get_pos()

    def desenha_pc(self, window):
        '''
            Função que desenha a imagem do pokemon center armazenada no init da classe.
        '''
        window.fill((0, 0, 0))
        # pygame.draw.rect(window, PRETO, self.rect_pc)
        # for parede in self.lista_paredes:
        #     pygame.draw.rect(window, CIANO, parede)
        # pygame.draw.rect(window, PRETO, self.porta_pc)
        # pygame.draw.rect(window, PRETO, self.balcao)
        window.blit(self.img_pc, (0, 100))

    def desenha_box(self, window):
        '''
            Função responsavel pela interacao do personagem com a enfermeira.
        '''
        window.blit(self.img_box, (0, 450))
        window.blit(self.texto1, (30, 515))
        pygame.draw.rect(window, (188, 188, 188), self.rect_nao)
        pygame.draw.rect(window, (188, 188, 188), self.rect_sim)
        window.blit(self.texto_nao, (517, 540))
        window.blit(self.texto_sim, (517, 490))

    def verifica_click_sim(self, x, y):
        '''
            Função que verifica se o mouse esta em cima do botao de sim, entregue pela funcao 'desenha_pc
            da classe CuraPokemon'.
        '''
        if self.rect_sim.collidepoint(x, y):
            return True
        
    def verifica_click_nao(self, x, y):
        '''
            Função que verifica se o mouse esta em cima do botao de não, entregue pela funcao 'desenha_pc
            da classe CuraPokemon'.
        '''
        if self.rect_nao.collidepoint(x, y):
            return True