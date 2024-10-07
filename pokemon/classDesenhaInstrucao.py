import pygame
from constantes import *

class Instrucao():
    '''
        Classe que desenha a tela de instruções e entrega o rect do botão 'jogar'.
    '''
    def __init__(self):
        self.img_fundo = pygame.transform.scale((pygame.image.load('img/instrucoes.png')),(640, 600))
        self.rect_jogar = pygame.Rect(530, 570, 105, 23)
    
    def desenha_inicio(self, window):
        '''
            Função que desenha a tela de instruções, imagem armazenada no init da classe.
        '''
        pygame.draw.rect(window, CIANO, self.rect_jogar)
        window.blit(self.img_fundo, (0,0))

    def verifica_click_sim(self, x, y):
        '''
            Função que verifica se o botão 'jogar' foi clicado.
        '''
        if self.rect_jogar.collidepoint(x, y):
            return True