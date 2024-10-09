import pygame

class Tela_gameover:
    def __init__(self):
        default_font_name = pygame.font.get_default_font()
        self.font = pygame.font.Font(default_font_name, 24)
        self.tela_final = pygame.transform.scale(pygame.image.load('assets/img/tela_gameover_pygame.jpeg'), (1020, 720))

    def atualiza(self, dt):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                return False
        return self
            
    def desenha(self, window, assets):
        window.fill((246,215,167))
        window.blit(self.tela_final, (0,0))