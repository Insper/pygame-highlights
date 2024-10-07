import pygame
from constantes import *

class Desenha_ilha:
    '''
        Classe responsável por desenhar a ilha e entregar as paredes (rects) para
        realizar a colisao com as paredes.
    '''
    def __init__(self):
        self.fundo = pygame.transform.scale((pygame.image.load('img/ilha.png')),(640, 600))
        self.porta_pc = pygame.Rect(70, 310, 20, 10)
        self.porta_gym = pygame.Rect(262, 517, 20, 10)
        self.lista_paredes = [
            #Paredes gym
            pygame.Rect(167, 510, 72, 10),
            pygame.Rect(167, 400, 10, 110),
            pygame.Rect(167, 395, 180, 10),
            pygame.Rect(340, 395, 10, 115),
            pygame.Rect(305, 510, 45, 10),
            #Paredes pc
            pygame.Rect(45, 316, 12, 10),
            pygame.Rect(33, 215, 10, 100),
            pygame.Rect(33, 215, 125, 10),
            pygame.Rect(150, 215, 10, 100),
            pygame.Rect(40, 310, 10, 10),
            pygame.Rect(100, 315, 50, 10),
            #paredes avore superior esquerda
            pygame.Rect(23, 115, 8, 43),
            pygame.Rect(23, 107, 165, 8),
            pygame.Rect(180, 3, 8, 100),
            pygame.Rect(0, 150, 25, 8),
            pygame.Rect(-7, 150, 8, 270), #parede lateral esquerda colocar -9
            pygame.Rect(-7, 410, 35, 8),
            pygame.Rect(23, 410, 8, 100),
            pygame.Rect(23, 502, 35, 8),
            pygame.Rect(55, 502, 8, 40),
            pygame.Rect(63, 532, 30, 8),
            pygame.Rect(93, 537, 8, 40),
            pygame.Rect(102, 572, 300, 8),
            pygame.Rect(410, 541, 95, 8),
            pygame.Rect(409, 544, 8, 30),
            pygame.Rect(506, 515, 8, 40),
            pygame.Rect(514, 516, 80, 8),
            pygame.Rect(611, 477, 8, 40),
            pygame.Rect(578, 463, 20, 8),
            #casa lado direito gym
            pygame.Rect(520, 334, 115, 110),
            #rio
            pygame.Rect(452, 280, 180, 8),
            pygame.Rect(638, 281, 8, 20),
            pygame.Rect(371, 319, 80, 3),
            pygame.Rect(373, 252, 80, 3),
            pygame.Rect(234, 157, 115, 105),
            pygame.Rect(294, 125, 70, 8),
            pygame.Rect(374, 1, 8, 200),
            pygame.Rect(188, -5, 180, 8),

        ]
    
    def desenha_fundo(self, window):
        '''
            Função que desenha a imagem da ilha armazenada no init da classe.
        '''
        # for parede in self.lista_paredes:
        #     pygame.draw.rect(window, CIANO, parede)
        # pygame.draw.rect(window,PRETO, self.porta_gym)
        # pygame.draw.rect(window,PRETO, self.porta_pc)
        window.blit(self.fundo, (0, 0))