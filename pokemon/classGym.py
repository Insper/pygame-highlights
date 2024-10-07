import pygame
from constantes import *

class Desenha_fundo:
    '''
        Classe responsável por desenhar o fundo e entregar as paredes (rects) para
        realizar a colisao com as paredes.
    '''
    def __init__(self):
        self.fundo = pygame.transform.scale((pygame.image.load('img/map-gym.png')),(640, 600))
        self.porta_gym = pygame.Rect(173, 594, 81, 5)
        self.lista_paredes = [
            pygame.Rect(380, 20, 233, 5),
            pygame.Rect(612, 20, 5, 90),
            pygame.Rect(575, 111, 44, 6),
            pygame.Rect(575, 111, 5, 27),
            pygame.Rect(543, 133, 37, 5),
            pygame.Rect(543, 133, 5, 110),
            pygame.Rect(307, 243, 238, 5),
            pygame.Rect(307, 155, 5, 90),
            pygame.Rect(257, 155, 50, 5),
            pygame.Rect(252, 155, 5, 127),
            pygame.Rect(252, 282, 330, 5),
            pygame.Rect(577, 285, 5, 45),
            pygame.Rect(468, 330, 116, 5),
            pygame.Rect(468, 331, 5, 197),
            pygame.Rect(419, 526, 54, 5),
            pygame.Rect(417, 484, 5, 45),
            pygame.Rect(290, 484, 127, 5),
            pygame.Rect(290, 484, 5, 65),
            pygame.Rect(253, 549, 42, 5),
            pygame.Rect(253, 549, 5, 50),
            # pygame.Rect(173, 594, 81, 5), #porta
            pygame.Rect(168, 552, 5, 47),
            pygame.Rect(130, 549, 42, 5),
            pygame.Rect(130, 507, 5, 43),
            pygame.Rect(93, 507, 37, 5),
            pygame.Rect(93, 487, 5, 20),
            pygame.Rect(57, 483, 40, 5),
            pygame.Rect(58, 416, 5, 68),
            pygame.Rect(58, 414, 55, 5),
            pygame.Rect(113, 414, 5, 23),
            pygame.Rect(113, 432, 160, 5),
            pygame.Rect(272, 394, 5, 43),
            pygame.Rect(272, 392, 53, 5),
            pygame.Rect(325, 392, 5, 45),
            pygame.Rect(325, 432, 95, 5),
            pygame.Rect(417, 332, 5, 104),
            pygame.Rect(258, 331, 162, 5),
            pygame.Rect(256, 331, 5, 64),
            pygame.Rect(170, 395, 89, 5),
            pygame.Rect(165, 310, 5, 89),
            pygame.Rect(112, 310, 54, 5),
            pygame.Rect(112, 310, 5, 65),
            pygame.Rect(58, 374, 56, 5),
            pygame.Rect(58, 264, 5, 110),
            pygame.Rect(58, 262, 110, 5),
            pygame.Rect(166, 159, 5, 107),
            pygame.Rect(75, 157, 92, 5),
            pygame.Rect(75, 157, 5, 65),
            pygame.Rect(27, 222, 52, 5),
            pygame.Rect(22, 110, 5, 112),
            pygame.Rect(22, 107, 340, 5),
            pygame.Rect(362, 107, 5, 90),
            pygame.Rect(362, 197, 90, 5),
            pygame.Rect(452, 135, 5, 64),
            pygame.Rect(417, 135, 35, 5),
            pygame.Rect(417, 113, 5, 22),
            pygame.Rect(384, 113, 35, 5),
            pygame.Rect(382, 25, 5, 87),
            pygame.Rect(42, 190, 10, 5),
            pygame.Rect(439, 498, 10, 5),
            pygame.Rect(80, 340, 10, 5),
            pygame.Rect(467, 84, 70, 5),
        ]

    def desenha_mapa(self, window):
        '''
            Função que desenha a imagem do mapa armazenada no init da classe.
        '''
        # for parede in self.lista_paredes:
        #     pygame.draw.rect(window,PRETO, parede)
        # pygame.draw.rect(window,PRETO, self.porta_gym)
        window.blit(self.fundo, (0, 0))