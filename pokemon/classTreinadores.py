import pygame
class Treinador1:
    def __init__(self):
        '''
            Função que inicia todos os ataques e imagens do treinador.
        '''
        self.treinador1_img = pygame.transform.scale((pygame.image.load('img/trainer-1.png')),(30, 30))
        self.rect = pygame.Rect(35, 185, 30, 30)
        self.fire_punch = {'dano': 55, 'precisao': 100, 'tipo': 'fogo', 'nome': 'Fire Punch'}
        self.psybeam = {'dano': 65, 'precisao': 100, 'tipo': 'psiquico', 'nome': 'Psybeam'}
        self.recover = {'dano': 0, 'nome': 'Recover'}
        self.karate_chop = {'dano': 50, 'precisao': 100, 'tipo': 'lutador', 'nome': 'Karate Chop'}
        self.medicham = pygame.transform.scale((pygame.image.load('img/medicham.png')),(180,180))
        self.machop = pygame.transform.scale((pygame.image.load('img/Machop.webp')),(160,160))
    
    def desenha_treinador1(self, window, bool):
        '''
            Função que desenha o treinador.
        '''
        if not bool:
            window.blit(self.treinador1_img, (35, 185))
        
    def pokemons_treinador1(self):
        '''
            Função que comporta os pokemons do treinador.
        '''
        treinador1 = [{'vida_pokemon': 280, 'vida_max': 280, 'ataques': [self.fire_punch, self.psybeam, self.recover], 'nome': 'MEDICHAM', 'imagem': self.medicham},
                      {'vida_pokemon': 240, 'vida_max': 240, 'ataques': [self.karate_chop], 'nome': 'MACHOP', 'imagem': self.machop}]
        return treinador1

class Treinador2:
    def __init__(self):
        '''
            Função que inicia todos os ataques e imagens do treinador.
        '''
        self.trainer2_img = pygame.transform.scale((pygame.image.load('img/trainer-2.png')),(30, 30))
        self.rect = pygame.Rect(430, 492, 30, 30)
        self.tackle = {'dano': 35, 'precisao': 100, 'tipo': 'normal', 'pps': 30, 'nome': 'Tackle'}
        self.makuhita = pygame.transform.scale((pygame.image.load('img/Makuhita.webp')),(200,200))
    
    def desenha_treinador2(self, window, bool):
        '''
            Função que desenha o treinador.
        '''
        if not bool:
            window.blit(self.trainer2_img, (430, 492))
        
    def pokemons_treinador2(self):
        '''
            Função que comporta os pokemons do treinador.
        '''
        treinador2 = [{'vida_pokemon': 240, 'vida_max': 240, 'ataques': [self.tackle], 'nome': 'MAKUHITA', 'imagem': self.makuhita}]
        return treinador2

class Treinardor3:
    def __init__(self):
        '''
            Função que inicia todos os ataques e imagens do treinador.
        '''
        self.trainer3_img = pygame.transform.scale((pygame.image.load('img/trainer-2.png')),(30, 30))
        self.rect = pygame.Rect(72, 335, 30, 30)
        self.karate_chop = {'dano': 50, 'precisao': 100, 'tipo': 'lutador', 'nome': 'Karate Chop'}
        self.facade = {'dano': 50, 'precisao': 100, 'tipo': 'normal', 'nome': 'Facade'}
        self.psybeam = {'dano': 65, 'precisao': 100, 'tipo': 'psiquico', 'nome': 'Psybeam'}
        self.meditite = pygame.transform.scale((pygame.image.load('img/Meditite.webp')),(180,180))
        self.machoke = pygame.transform.scale((pygame.image.load('img/machoke.png')),(180,180))

    def desenha_treinador3(self, window, bool):
        '''
            Função que desenha o treinador.
        '''
        if not bool:
            window.blit(self.trainer3_img, (72, 335))

    def pokemons_treinador3(self):
        '''
            Função que comporta os pokemons do treinador.
        '''
        treinador3 = [{'vida_pokemon': 290, 'vida_max': 290, 'ataques': [self.karate_chop, self.facade], 'nome': 'MACHOKE', 'imagem': self.machoke},
                      {'vida_pokemon': 240, 'vida_max': 240, 'ataques': [self.psybeam], 'nome': 'MEDITITE', 'imagem': self.meditite}]
        
        return treinador3

class Treinador4:
    def __init__(self):
        '''
            Função que inicia todos os ataques e imagens do treinador.
        '''
        self.trainer4_img = pygame.transform.scale((pygame.image.load('img/trainer-2.png')),(30, 30))
        self.rect = pygame.Rect(483, 68, 30, 30)
        self.machamp = pygame.transform.scale((pygame.image.load('img/Machamp.webp')),(180,180))
        self.heracross = pygame.transform.scale((pygame.image.load('img/Heracross.webp')),(150,150))
        self.hariyama = pygame.transform.scale((pygame.image.load('img/hariyama.png')),(150,150))
        self.karate_chop = {'dano': 45, 'precisao': 100, 'tipo': 'lutador', 'nome': 'Karate Chop'}
        self.earthquake = {'dano': 75, 'precisao': 100, 'tipo': 'terra', 'nome': 'Earthquake'}
        self.megahorn = {'dano': 70, 'precisao': 100, 'tipo': 'inseto', 'nome': 'Megahorn'}
        self.cut = {'dano': 45, 'precisao': 95, 'tipo': 'normal', 'nome': 'Cut'}
        self.cross_chop = {'dano': 55, 'precisao': 100, 'tipo': 'lutador', 'nome': 'Cross Chop'}
        self.facade = {'dano': 50, 'precisao': 100, 'tipo': 'normal', 'nome': 'Facade'}
        self.fire_punch = {'dano': 65, 'precisao': 100, 'tipo': 'fogo', 'nome': 'Fire Punch'}

    def desenha_treinador4(self, window, bool):
        '''
            Função que desenha o treinador.
        '''
        if not bool:
            window.blit(self.trainer4_img, (483, 68))

    def pokemons_treinador4(self):
        '''
            Função que comporta os pokemons do treinador.
        '''
        treinador4 = [{'vida_pokemon': 260, 'vida_max': 260, 'ataques': [self.karate_chop, self.earthquake], 'nome': 'HARIYAMA', 'imagem': self.hariyama},
                      {'vida_pokemon': 330, 'vida_max': 330, 'ataques': [self.megahorn, self.cut], 'nome': 'HERACROSS', 'imagem': self.heracross},
                      {'vida_pokemon': 300, 'vida_max': 300, 'ataques': [self.fire_punch, self.cross_chop, self.facade], 'nome': 'MACHAMP', 'imagem': self.machamp}
                      ]
        return treinador4