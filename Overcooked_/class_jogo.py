import pygame
from tela_inicial import Tela_inicial
from tela_jogo import Tela_jogo


class Jogo:
    def __init__(self):
        pygame.init()
        self.font = pygame.font.Font("assets/font/PressStart2P.ttf", 20)
        self.altura = 720
        self.largura = 1020
        self.window = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption('Cookinsper')
        self.assets = {}

        self.tela_atual = Tela_inicial()
        self.lastupdate = 0

    def atualiza(self):
        t1 = pygame.time.get_ticks()
        delta_t = (t1 - self.lastupdate) / 1000
        self.lastupdate = t1

        self.tela_atual = self.tela_atual.atualiza(delta_t)

        if self.tela_atual is None:
            return False
        return True

    def game_loop(self):
        clock = pygame.time.Clock()
        while self.atualiza():
            clock.tick(60)
            self.tela_atual.desenha(self.window, self.assets)
            pygame.display.update()