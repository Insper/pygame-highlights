import pygame
import webbrowser

class Menu:
    def __init__(self):
        self.rects = {}
        self.keys = ['Continuar', 'Configurações', 'Como Jogar', 'Sobre Nós']
        for i in range(4):
            self.rects[self.keys[i]] = pygame.Rect(430, 100 + 140*i, 420, 100)

    def interacoes(self, state):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                state['tela_jogo'] = 'main'
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for key, val in self.rects.items():
                    if val.collidepoint(pygame.mouse.get_pos()):
                        if key == 'Continuar':
                            state['tela_jogo'] = 'main'
                        elif key == 'Configurações':
                            state['tela_jogo'] = 'config'
                        elif key == 'Como Jogar':
                            state['tela_jogo'] = 'como_jogar'
                        elif key == 'Sobre Nós':
                            webbrowser.open('https://insper-classroom.github.io/projeto-pygame-oliva/')
                            return True

        return True

    def desenha(self, window, asset):
        i = 0
        fonte = pygame.font.Font(pygame.font.get_default_font(), 18)
        for rect in self.rects.values():
            pygame.draw.rect(window, (0,0,0), rect)
            palavra = fonte.render(Menu().keys[i], True, (255,255,255))
            window.blit(palavra, (asset['tam_tela'][0]/2 - palavra.get_width()/2, 150 + 140*i - palavra.get_height()/2))

            i+=1
        
        return