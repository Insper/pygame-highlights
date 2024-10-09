import pygame
from classes_telas import *

class Jogo:
    def __init__(self):
        '''
        Função que define a classe Jogo

        parâmetro self: representa a própria classe
        '''

        pygame.init()

        WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        self.window_dimen = (self.screen.get_width(), self.screen.get_height())
        self.current_screen_index = 0
        self.clock = pygame.time.Clock()

        self.clock.tick(60)
        pygame.display.set_caption("The Frank's musical legacy") # Define o título da janela

        self.assets = {
            'fonte_padrao': pygame.font.get_default_font()
        }
        
        # self.telas = [RoomBegin(self.window_dimen, self.clock, self.assets), RoomBoss1(self.window_dimen, self.clock, self.assets), RoomBoss2(self.window_dimen, self.clock, self.assets), RoomBoss3(self.window_dimen, self.clock, self.assets), RoomFinal(self.window_dimen, self.clock, self.assets)]
        self.telas = [Start(self.window_dimen, self.clock, self.assets), RoomBoss1(self.window_dimen, self.clock, self.assets)]

    def game_loop(self):
        '''
        Função com o objetivo de rodar o jogo

        parâmetro self: representa a própria classe
        '''

        game = True

        tela_atual = self.telas[self.current_screen_index]

        while game:
            self.current_screen_index = tela_atual.update()

            self.clock.tick(60)

            if self.current_screen_index == -1:
                self.telas = [Start(self.window_dimen, self.clock, self.assets), RoomBoss1(self.window_dimen, self.clock, self.assets)]
                self.current_screen_index = 0
                tela_atual = self.telas[self.current_screen_index]
            if self.current_screen_index == -2:
                game = False
            else:
                tela_atual = self.telas[self.current_screen_index]
                tela_atual.draw(self.screen)