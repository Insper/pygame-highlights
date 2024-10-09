import pygame
from class_spritesheet import SpriteSheet


class Jogador(pygame.sprite.Sprite):
    def __init__(self, player_sheet, x, y, velocidadeX, velocidadeY):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.velx = velocidadeX
        self.vely = velocidadeY

        self.img = player_sheet
        self.rect = pygame.Surface.get_rect(self.img)
        
    def atualiza(self, dt):
        # boneco = pygame.transform.scale(pygame.image.load('img/luccas-neto-boneco-png-01.png'), (200,150))
        self.x = self.x + self.velx * dt
        self.y = self.y + self.vely * dt
        