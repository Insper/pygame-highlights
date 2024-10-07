import pygame
from constantes import *

class Inicio():
    '''
        Classe responsável por desenhar a tela inicial e entregar o rect do botao 'continuar'.
    '''
    def __init__(self):
        self.img = pygame.transform.scale((pygame.image.load('img/inicio.png')),(640, 600))
        self.rect_continuar = pygame.Rect(242, 471, 175, 20)
    
    def desenha_inicio(self, window):
        '''
            Função que desenha a tela inicial, imagem armazenada no init da classe.
        '''
        pygame.draw.rect(window, CIANO, self.rect_continuar)
        window.blit(self.img, (0, 0))

    def verifica_click_sim(self, x, y):
        '''
            Função que verifica se o botão 'continuar' foi clicado.
        '''
        if self.rect_continuar.collidepoint(x, y):
            return True