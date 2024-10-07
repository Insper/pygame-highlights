import pygame

class GameOver:
    def __init__(self):
        pass
    
    def interacoes(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        
        return True
    
    def desenha(self, window, asset, state):
        window.fill((0,0,0))

        classif = {'maior' : ['GAME OVER'],
                  'tit' : ['CRÉDITOS'], 
                  'sub' : ['Autores:', 'Agradecimentos Especiais'], 
                  'txt' : [f'Você jogou por {int((state["last_updated"]/1000)//60)} minutos e {int((state["last_updated"]/1000) - (state["last_updated"]/1000)//60*60)} segundos',
                         'E pegou um total de 0 empréstimos com o Agiota.', 'Henrique Bucci Rodrigues Netto', 'João Citino', 'Mariana de Camargo Salles Cezar']}
        
        frases = ['GAME OVER', f'Você jogou por {int((state["last_updated"]/1000)//60)} minutos e {int((state["last_updated"]/1000) - (state["last_updated"]/1000)//60*60)} segundos.',
                   'E pegou um total de 0 empréstimos com o Agiota.', 'CRÉDITOS', 'Autores:', 'Henrique Bucci Rodrigues Netto', 'João Citino', 'Agradecimentos Especiais:', 
                   'Mariana de Camargo Salles Cezar']

        dist = 80
        for i in range(len(frases)):
            if frases[i] in classif['maior']:
                font = pygame.font.Font(pygame.font.get_default_font(), 40)
                txt = font.render(frases[i], True, "#CC0000")
            elif frases[i] in classif['tit']:
                font = pygame.font.Font(pygame.font.get_default_font(), 28)
                txt = font.render(frases[i], True, (255,255,255))
            elif frases[i] in classif['sub']:
                font = pygame.font.Font(pygame.font.get_default_font(), 18)
                txt = font.render(frases[i], True, (255,255,255))
            else:
                txt = asset['def_font'].render(frases[i], True, (255,255,255))

            if frases[i-1] in classif['tit'] or frases[i-1] in classif['maior'] or frases[i-1] == 'João Citino':
                dist += 70
            elif frases[i] in classif['tit']:
                dist += 80
            else:
                dist += 30
            window.blit(txt, (asset['tam_tela'][0]/2 - txt.get_width()/2, dist))

        