import pygame

class Interacao:
    def __init__(self, comida, tempo):
        self.comida = comida
        self.timer = tempo
        self.t3 = self.timer / 200
        self.x = 0
        self.last = 0
        self.terminou = False

    def atualiza(self):
        t1 = pygame.time.get_ticks()
        if self.last == 0:
            self.last = t1
            tempo = (t1 - self.last)
        else:
            tempo = (t1 - self.last)
        if tempo >= self.t3 and tempo <= self.timer:
            self.t3 += (self.timer / 200)
            if self.comida == 'hamburger':
                self.x += 0.4
            if self.comida == 'refri':
                self.x += 0.45
            if self.comida == 'fritas':
                self.x += 0.41
        if tempo >= self.timer:
            self.terminou = True

    