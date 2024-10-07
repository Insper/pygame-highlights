import pygame

class Player():
    def __init__(self, img, pos, size):
        self.img = pygame.transform.scale(img, size)
        self.pos = pos
        self.size = size
    
    def transform(self):
        return pygame.Rect(*self.pos, *self.size)