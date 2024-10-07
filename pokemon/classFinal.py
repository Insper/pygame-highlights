import pygame
from constantes import *

class GameOver:
    def __init__(self) -> None:
        self.img_fundo = pygame.transform.scale((pygame.image.load('img/final.jpeg')),(640, 400))
        self.fonte = pygame.font.Font('imgBatalhas/fontes.ttf', 18)
        self.GameOver = self.fonte.render('Congratulations', True, BRANCO)
    def desenha(self, window):
        '''
            Função que desenha a tela do computador, imagens armazenada no init da classe.
        '''
        window.fill((188, 188, 188))
        window.blit(self.img_fundo, (-2, 100))
        window.blit(self.GameOver, (240, 40))