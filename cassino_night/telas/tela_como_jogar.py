import pygame
import os
from const import explicacoes, traducao

class ComoJogar:
    def __init__(self, asset):
        self.textos = explicacoes
        self.tela = pygame.Rect(asset['tam_tela'][0]/6, asset['tam_tela'][1]/6, 4*asset['tam_tela'][0]/6, 4*asset['tam_tela'][1]/6)
        self.fechar = pygame.Rect(self.tela.x + self.tela.width - 43, self.tela.y, 43, 40)

        tam = self.tela.width - 40
        self.buttons = {}
        i = 0
        for k in self.textos.keys():
            self.buttons[k] = pygame.Rect(self.tela.x + tam//len(self.textos.keys())*i, self.tela.y, tam//len(self.textos.keys())-1, 40)
            i += 1

        self.page = 'blackjack'

    def interacoes(self, window, asset, state):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.fechar.collidepoint(pygame.mouse.get_pos()):
                    asset['mapa'].desenha(window, asset, state)
                    state['tela_jogo'] = 'menu'
                for k, button in self.buttons.items():
                    if button.collidepoint(pygame.mouse.get_pos()):
                        self.page = k
            
        return True
    
    def divide_texto(self, key, fonte):
        words = self.textos[key].split(' ')
        space = fonte.size(' ')[0]
        max_width = self.tela.width - 30
        linha, linhas = [], []
        tam_linha = 0

        for i in range(len(words)):
            if '\n' in words[i]:
                sp = words[i].split('\n')
                if words[i] in linha:
                    linhas += [' '.join(linha[:-1] + [sp[0]])]
                else:
                    linhas += [' '.join(linha + [sp[0]])]
                linha = [sp[1]]
                tam_linha = fonte.render(sp[1], True, (255, 255, 255)).get_width()
                continue
            
            if tam_linha > max_width:
                linhas += [' '.join(linha[:-1])]
                linha = [linha[-1]]
                tam_linha = fonte.render(linha[-1], True, (255, 255, 255)).get_width()
                continue

            if i == len(words)-1:
                tam_linha += fonte.render(words[i], True, (255, 255, 255)).get_width() + space
                linha += [words[i]]
                linhas += [' '.join(linha)]
                continue

            tam_linha += fonte.render(words[i], True, (255, 255, 255)).get_width() + space
            linha += [words[i]]

        return linhas

    def desenha(self, window):
        fonte_bot = pygame.font.Font(pygame.font.get_default_font(), 16)
        fonte_tit = pygame.font.Font(pygame.font.get_default_font(), 20)
        fonte_txt = pygame.font.Font(pygame.font.get_default_font(), 14)

        #desenha base da tela de instruções
        pygame.draw.rect(window, (0,0,0), self.tela)

        #desenha botões superiores
        i = 0
        for k, b in self.buttons.items():
            pygame.draw.rect(window, (0,0,0), b)
            pygame.draw.rect(window, (255,255,255), b, width=1)
            palavra = fonte_bot.render(traducao[k], True, (255,255,255))
            window.blit(palavra, (b.x + b.width/2 - palavra.get_width()/2, b.y + b.height/2 - palavra.get_height()/2))
            i += 1
        
        #desenha botão de fechar
        pygame.draw.rect(window, (0,0,0), self.fechar)
        pygame.draw.rect(window, (255,255,255), self.fechar, width=1)
        x = fonte_bot.render('x', True, (255, 255, 255))
        window.blit(x, (self.fechar.x + self.fechar.width/2 - x.get_width()/2, self.fechar.y + self.fechar.height/2 - x.get_height()/2))

        #desenha título da página atual
        palavra = fonte_tit.render(traducao[self.page], True, (255, 255, 255))
        window.blit(palavra, (self.tela.x + 20, self.tela.y + 70))

        #desenha instruções de jogo da página atual
        j = 0
        for linha in self.divide_texto(self.page, fonte_txt):
            window.blit(fonte_txt.render(linha, True, (255, 255, 255)), (self.tela.x + 20, self.tela.y + 110 + 18*j))
            j += 1
        return
    