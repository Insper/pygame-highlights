import pygame

class SpriteSheet:
    def __init__(self, image):
        self.sprite = image
        
    def get_image(self, largura, altura, scale, color, frame):
        image = pygame.Surface((largura, altura)).convert_alpha()
        image.blit(self.sprite, (0,0), ((frame * largura), 0, largura, altura))
        image = pygame.transform.scale(image, (largura * scale, altura * scale))
        image.set_colorkey(color)
        
        return image