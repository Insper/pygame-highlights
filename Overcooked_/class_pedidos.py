import pygame
import random

class Pedidos:
    def __init__(self, dicionario, inventario, pontuacao):
        self.dicionario = dicionario
        self.lista_pedidos = ['hamburger', 'fritas', 'refri']
        self.inventario = inventario
        self.pontuacao = pontuacao
        self.timers = {} 

    def sorteia(self):
        for key, espacos in self.dicionario.items():
            if not espacos['ocupado']:
                espacos['ocupado'] = True
                random.shuffle(self.lista_pedidos)
                espacos['tipo'] = self.lista_pedidos[0]
                self.timers[key] = {'timer': None, 'last_update': None}
                break
    
    def time(self, key):
        if key in self.timers: 
            timer_info = self.timers[key]
            if timer_info['timer'] is None:
                timer_info['timer'] = 12000
                timer_info['last_update'] = pygame.time.get_ticks() 
            current_time = pygame.time.get_ticks()
            elapsed_time = current_time - timer_info['last_update']
            timer_info['last_update'] = current_time
            timer_info['timer'] -= elapsed_time
            return max(0, timer_info['timer'])
        else:
            return 0 

    def atualiza(self):
        for espacos in self.inventario.values():
            if espacos['ocupado']:
                for key, pedidos in self.dicionario.items():
                    if pedidos['ocupado']:
                        if espacos['tipo'] == pedidos['tipo']:
                            espacos['tipo'] = None
                            pedidos['tipo'] = None
                            espacos['ocupado'] = False
                            pedidos['ocupado'] = False
                            self.pontuacao += 200
                            
