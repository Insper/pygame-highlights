import pygame
from constantes import *    

class Telahp():
    '''
        Classe responsável por desenhar a tela do computador presente no centro pokemon.
    '''
    def __init__(self):
        self.img_fundo = pygame.transform.scale((pygame.image.load('img/fundo-hp.png')),(640, 400))
        self.fonte = pygame.font.Font('imgBatalhas/fontes.ttf', 18)
        self.fonte2 = pygame.font.Font('imgBatalhas/fontes.ttf', 15)
        self.texto1 = self.fonte.render('Sair', True, PRETO)
        self.rect_sair = pygame.Rect(517, 460, 105, 28)
        self.Scizor = pygame.transform.scale((pygame.image.load('img/scizor_hp.png')),(150, 100))
        self.venusaur = pygame.transform.scale((pygame.image.load('img/venusaur_hp.png')),(150, 120))
        self.pikachu = pygame.transform.scale((pygame.image.load('img/pikachulivre.png')),(100, 70))
        self.Scizor_name = self.fonte.render('Scizor:', True, BRANCO)
        self.venusaur_name = self.fonte.render('Venusaur:', True, BRANCO)
        self.pikachu_name = self.fonte.render('Pikachu:', True, BRANCO)
        self.male_symbol = pygame.transform.scale((pygame.image.load('img/male_symbol.png')),(30, 30))
        self.max1 = self.fonte2.render('/ 250', True, BRANCO)
        self.max2 = self.fonte2.render('/ 330', True, BRANCO)
        self.max3 = self.fonte2.render('/ 290', True, BRANCO)

    def desenha(self, window):
        '''
            Função que desenha a tela do computador, imagens armazenada no init da classe.
        '''
        window.fill((188, 188, 188))
        window.blit(self.img_fundo, (-2, 100))
        window.blit(self.texto1, (548, 460))
        window.blit(self.Scizor, (395, 100))
        window.blit(self.venusaur, (80, 205))
        window.blit(self.pikachu, (415, 352))
        window.blit(self.Scizor_name, (86, 171))
        window.blit(self.venusaur_name, (397, 297))
        window.blit(self.pikachu_name, (90, 417))
        window.blit(self.male_symbol, (257, 123))
        window.blit(self.male_symbol, (562, 252))
        window.blit(self.male_symbol, (261, 369))
        window.blit(self.max1, (209, 176))
        window.blit(self.max2, (547, 302))
        window.blit(self.max3, (225, 422))

    def verifica_click_sim(self, x, y):
        '''
            Função que verifica se o botão 'sair' foi clicado.
        '''
        if self.rect_sair.collidepoint(x, y):
            return True
