import pygame
from tela_jogo import Tela_jogo

class Tela_inicial:
    def __init__(self):
        default_font_name = pygame.font.get_default_font()
        self.font = pygame.font.Font(default_font_name, 24)
        self.tela_inicial = pygame.transform.scale(pygame.image.load('assets/img/tela_inicial_pygame.jpeg'), (1020, 720))

    def atualiza(self, dt):
        rect_botao = pygame.Rect(360, 151, 300, 80)

        click = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if rect_botao.collidepoint(click):
                    return Tela_jogo()

            
        return self
            
    def desenha(self, window, assets):
        window.fill((246,215,167))
        window.blit(self.tela_inicial, (0,0))