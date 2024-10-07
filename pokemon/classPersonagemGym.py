import pygame
from constantes import *

class Personagem:
    '''
        Classe responsável por desenhar o personagem e entregar o rect do personagem,
        e realizar sua movimentção por todo o territorio do GINASI0.
    '''
    def __init__(self) -> None:
        self.personagem = pygame.transform.scale((pygame.image.load('img/s2.png')),(30, 35))
        self.rect = self.personagem.get_rect()
        self.rect.x = 280
        self.rect.y = 300
        self.velocidade = [0, 0]
        self.pos_antiga = [0, 0]
        self.baixo = [pygame.transform.scale((pygame.image.load('img/s1.png')),(30, 35)),
                      pygame.transform.scale((pygame.image.load('img/s3.png')),(30, 35))
                      ]
        self.cima = [pygame.transform.scale((pygame.image.load('img/w2.png')),(30, 35)),
                     pygame.transform.scale((pygame.image.load('img/w3.png')),(30, 35))
            ]
        self.esquerda = [
                    pygame.transform.scale((pygame.image.load('img/a2.png')),(30, 35)),
                    pygame.transform.scale((pygame.image.load('img/a3.png')),(30, 35))
                        ]
        self.direita = [
                    pygame.transform.scale((pygame.image.load('img/d2.png')),(30, 35)),
                    pygame.transform.scale((pygame.image.load('img/d3.png')),(30, 35))
                        ]
        self.parados = [
                    pygame.transform.scale((pygame.image.load('img/s2.png')),(30, 35)),
                    pygame.transform.scale((pygame.image.load('img/w1.png')),(30, 35)),
                    pygame.transform.scale((pygame.image.load('img/a1.png')),(30, 35)),
                    pygame.transform.scale((pygame.image.load('img/d1.png')),(30, 35))
        ]
        self.current_frame = 0
        self.rect_baixo = self.baixo[self.current_frame].get_rect()
        self.animation_counter = 0
        self.animation_interval = 10
        self.last_key = None

    def desenha_personagem(self, window):
        '''
            Função que desenha o personagem, imagem armazenada no init da classe.
        '''
        tecla_apertada = pygame.key.get_pressed()
        if tecla_apertada[pygame.K_s]:
            window.blit(self.baixo[self.current_frame], (self.rect.x, self.rect.y))
            self.animation_counter += 1
            if self.animation_counter == self.animation_interval:
                self.current_frame = (self.current_frame + 1) % len(self.baixo)
                self.animation_counter = 0
        elif tecla_apertada[pygame.K_w]:
            window.blit(self.cima[self.current_frame], (self.rect.x, self.rect.y))
            self.animation_counter += 1
            if self.animation_counter == self.animation_interval:
                self.current_frame = (self.current_frame + 1) % len(self.cima)
                self.animation_counter = 0
        elif tecla_apertada[pygame.K_a]:
            window.blit(self.esquerda[self.current_frame], (self.rect.x, self.rect.y))
            self.animation_counter += 1
            if self.animation_counter == self.animation_interval:
                self.current_frame = (self.current_frame + 1) % len(self.esquerda)
                self.animation_counter = 0
        elif tecla_apertada[pygame.K_d]:
            window.blit(self.direita[self.current_frame], (self.rect.x, self.rect.y))
            self.animation_counter += 1
            if self.animation_counter == self.animation_interval:
                self.current_frame = (self.current_frame + 1) % len(self.direita)
                self.animation_counter = 0
        else:
            window.blit(self.personagem, (self.rect.x, self.rect.y))


    def altera_sprite_horizontal(self):
        '''
            Função que altera o sprite do personagem para a direção horizontal.
        '''
        
        next_pos = self.rect.x + self.velocidade[0]
        self.rect.x = next_pos
    
    def altera_sprite_vertical(self):
        '''
            Função que altera o sprite do personagem para a direção vertical.
        '''
        
        next_pos = self.rect.y + self.velocidade[1]
        self.rect.y = next_pos
    
    def verifica_colisao(self, lista_paredes):
        '''
            Função que recebe uma lista de rects (paredes)
            e verifica se o rect do personagem esta colidindo
            , caso sim retorna um boleano (True para hit / False
            para nao hit).
        '''

        is_hit = False
        for parede in lista_paredes:
            if parede.colliderect(self.rect):
                is_hit = True
                break

        return is_hit