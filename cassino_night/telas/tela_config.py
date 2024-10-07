import pygame
from telas.tela_menu import *
from const import nomes_config, tamanhos_tela

class Config:
    def __init__(self):
        self.asset = {
            'tam_tela' : tamanhos_tela[0],
            'vsync' : True,
            'vol_musica' : 1,
            'vol_sons' : 1,
        }

        self.mudou_tam = [False, tamanhos_tela[0]]

        self.buttons = [*[pygame.Rect(2*self.asset['tam_tela'][0]/3 - 120, i*self.asset['tam_tela'][1]/12 + 60 + self.asset['tam_tela'][1]/6, 240, 30) for i in range(len(self.asset.keys()))],
                        pygame.Rect(self.asset['tam_tela'][0]/2 - 210, 5*self.asset['tam_tela'][1]/6 - 80, 180, 30),
                        pygame.Rect(self.asset['tam_tela'][0]/2 + 30, 5*self.asset['tam_tela'][1]/6 - 80, 180, 30)]
    
    def interacoes(self, window, asset, state):
        buttons = dict(zip(list(self.asset.keys()) + ['salvar', 'cancelar'], self.buttons))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                state['tela_jogo'] = 'main'
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for key, button in buttons.items():
                    if button.collidepoint(pygame.mouse.get_pos()):
                        if key == 'tam_tela':
                            pass
                            #self.mudou_tam = [True, tamanhos_tela[0] if self.mudou_tam[1] == tamanhos_tela[1] else tamanhos_tela[1]]
                        if key == 'vsync':
                            if asset[key] == False:
                                asset[key] = True
                            else:
                                asset[key] = False
                        if key.startswith('vol'):
                            if asset[key] > 0:
                                asset[key] -= 0.05
                            else:
                                asset[key] = 1
                        if key == 'salvar':
                            if self.mudou_tam[0] == True or self.asset['vsync'] != asset['vsync']:
                                if self.mudou_tam[0]:
                                    if asset['tam_tela'] == tamanhos_tela[0]:
                                        asset['tam_tela'] = tamanhos_tela[1]
                                    else:
                                        asset['tam_tela'] = tamanhos_tela[0]
                                    self.mudou_tam[0] = False
                                window = pygame.display.set_mode(tuple(asset['tam_tela']), vsync=asset['vsync'], flags=pygame.SCALED)

                            self.asset.update({k: asset[k] for k in self.asset.keys()})
                            asset['mapa'].desenha(window, asset, state)
                            state['tela_jogo'] = 'menu'
                        if key == 'cancelar':
                            asset.update(self.asset)
                            self.mudou_tam = [False, tamanhos_tela[0] if self.asset['tam_tela'] == tamanhos_tela[0] else tamanhos_tela[1]]
                            asset['mapa'].desenha(window, asset, state)
                            state['tela_jogo'] = 'menu'
                            
        return True
    
    def desenha(self, window, asset):
        rect = pygame.Rect(self.asset['tam_tela'][0]/6, self.asset['tam_tela'][1]/6, 4*self.asset['tam_tela'][0]/6, 4*self.asset['tam_tela'][1]/6)
        pygame.draw.rect(window, (0,0,0), rect)

        buttons = self.buttons
        keys_added = list(self.asset.keys()) + ['salvar', 'cancelar']
        fonte = pygame.font.Font(pygame.font.get_default_font(), 14)
        for i in range(len(buttons)):
            if i < len(keys_added) - 2:
                pygame.draw.rect(window, (60,60,60), buttons[i]) #botões
                key = fonte.render(nomes_config[keys_added[i]], True, (255, 255, 255)) #nome da config
                window.blit(key, (self.asset['tam_tela'][0]/3 - 120, buttons[i].y + buttons[i].height/2 - key.get_height()/2)) #desenha nome da config
                if keys_added[i] != 'tam_tela':
                    if keys_added[i].startswith('vol'):
                        x = round(asset[keys_added[i]]*100)
                    else:
                        x = asset[keys_added[i]]
                    val = fonte.render(str(x), True, (255, 255, 255)) #valor da config
                else:
                    val = fonte.render(str(self.mudou_tam[1]), True, (255, 255, 255)) #valor da config
                window.blit(val, (buttons[i].x + buttons[i].width/2 - val.get_width()/2, buttons[i].y + buttons[i].height/2 - val.get_height()/2)) #desenha valor da config

                window.blit(fonte.render('>', True, (255, 255, 255)), (buttons[i].x + buttons[i].width - 20, buttons[i].y + buttons[i].height/2 - 7))
                window.blit(fonte.render('<', True, (255, 255, 255)), (buttons[i].x + 15, buttons[i].y + buttons[i].height/2 - 7))
            
            else:
                pygame.draw.rect(window, (0,0,0), buttons[i])
                pygame.draw.rect(window, (255,255,255), buttons[i], width=1)
                key = fonte.render(nomes_config[keys_added[i]], True, (255, 255, 255)) #nome da config
                window.blit(key, (buttons[i].x + buttons[i].width/2 - key.get_width()/2, buttons[i].y + buttons[i].height/2 - key.get_height()/2)) #desenha valor da config
                
        return