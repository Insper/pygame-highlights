import pygame
import sys
from class_game import *
from  time import sleep




def inicializa ():

    # pygame.mixer.music.load()
    # var = pygame.mixer.Sound()
    # var.play()
    
    pygame.init()
    pygame.mixer.init() 
    pygame.mixer.music.load("sound/music.mp3") 
    pygame.mixer.music.set_volume(0.6) 
    pygame.mixer.music.play()
    
    window = pygame.Surface((1152,864))
    pygame.display.set_caption("Code Scape")
    trueWindow = pygame.display.set_mode((1152, 864))
    
    assets = {
        'player' : pygame.image.load('img/player.png'),
        'mapa' : [pygame.image.load('img/fase1.png'), pygame.image.load('img/menu.png'), pygame.image.load('img/fase2.png'), pygame.image.load('img/fase3.png')],
        'key' : pygame.image.load('img/papeis.png'),
        "porta" : pygame.image.load('img/porta.png'),
        'menu_principal': pygame.image.load('img/fundo_menu.png'), 'vitoria': pygame.image.load('img/vitoria.png') , 'derrota': pygame.image.load('img/derrota.png'),
        'papel' : pygame.image.load('img/papel.png'),
        'cama': pygame.image.load('img/cama.png'),
        'clock': pygame.image.load('img/clock.png'),
        'mesa1': pygame.image.load('img/mesa1.png'),
        'bolinha de papel' : pygame.image.load('img/bola.png'),
        'computador' : pygame.image.load('img/computador.png'),
        'mesa2':pygame.image.load('img/mesa2.png'),
        'disquete':pygame.image.load('img/disquete.png'),
        'celular':pygame.image.load('img/celular.png'),
        'tv':pygame.image.load('img/tv.png'),
        'estante': pygame.image.load('img/estante.png')
    } 
    state = {
    'jogador' : Player(360, 240),
    'lista de itens1' :[Item(assets['bolinha de papel'], (1073,696), pygame.image.load('img/dica_fase1.png')), Item(assets['cama'], (34,469), pygame.image.load('img/cama_dica.png')), Item(assets['mesa1'], (1033,463), pygame.image.load('img/mesa1_dica.png')), Item(assets['clock'], (526,13), pygame.image.load('img/clock_dica.png'))], 
    'lista de itens2' :[Item(assets['papel'], (1073,700), pygame.image.load('img/dica_fase2.png')), Item(assets['computador'], (128,51), pygame.image.load('img/computador_dica.png')), Item(assets['cama'], (34,469), pygame.image.load('img/cama_dica.png')), Item(assets['mesa2'], (321,772), pygame.image.load('img/mesa1_dica.png')), Item(assets['clock'], (526,13), pygame.image.load('img/clock_dica.png')), Item(assets['disquete'], (237,633), pygame.image.load('img/disquete_dica.png'))], 
    'lista de itens3' :[Item(assets['celular'], (1064,527), pygame.image.load('img/celular_dica.png')), Item(assets['tv'], (684,62), pygame.image.load('img/tv_dica.png')), Item(assets['estante'], (237,23), pygame.image.load('img/estante_dica.png')), Item(assets['computador'], (843,35), pygame.image.load('img/computador2_dica.png')), Item(assets['mesa2'], (321,772), pygame.image.load('img/copo_dica.png'))],
    'primeiro_tempo'  :0,
    
    'toma': False,
    'last_enter': 0
    }
    
    portas = { 
        'PRIMEIRA FASE' : Porta(assets['porta'], (987, 21), "A SENHA é mais facil do que parece!","Digite e tecle ENTER", "senha"),  
        'SEGUNDA FASE' : Porta(assets['porta'], (987, 21), "As dicas estão por ai...","Digite e tecle ENTER", "12/01/1986"),
        'TERCEIRA FASE' : Porta(assets['porta'], (987, 21), "Vai ser na raça mesmo","Digite e tecle ENTER", "toshi"),
        'menu_principal': Porta(assets['porta'],(-500,-500), "vapo","mensagem2","no"),
        'VITORIA': Porta(assets['porta'],(-500,-500), "vapo","mensagem2","no"),
        'DERROTA':  Porta(assets['porta'],(-500,-500), "vapo","mensagem2","no")
    }

    telas = {
        'menu_principal': Tela(assets['menu_principal'],[],portas['menu_principal']),
        'SEGUNDA FASE' : Tela(assets['mapa'][2], state['lista de itens2'], portas['SEGUNDA FASE']), 
        'PRIMEIRA FASE' : Tela(assets['mapa'][0], state['lista de itens1'], portas['PRIMEIRA FASE']),
        'TERCEIRA FASE' : Tela(assets['mapa'][3], state['lista de itens3'], portas['TERCEIRA FASE']),
        'VITORIA': Tela(assets['vitoria'],[],portas['menu_principal']),
        'DERROTA':Tela(assets['derrota'],[],portas['menu_principal'])
    }
   

    
    state['tela atual'] = telas['menu_principal']


    return window, assets, state, trueWindow, telas, portas

def desenha (window, assets, state, trueWindow, portas):
    base = pygame.font.Font(None, 64)
    fase = state['jogador'].status


        

    state['tela atual'] = telas[fase]

    state['tela atual'].img = pygame.transform.scale(state['tela atual'].img, (pygame.display.get_surface().get_size()))  # Parte de redmencionar a tela
    
    window.blit(state['tela atual'].img,(0,0))

    for itens in state['tela atual'].itens:
        window.blit(itens.img, itens.ponto)
        if itens.status:
            window.blit(itens.mensagem, (326,232))




    window.blit(portas[fase].img, portas[fase].ponto)
    tempo = pygame.time.get_ticks()

    if state['tela atual'] != telas['menu_principal'] and state['tela atual'] != telas['VITORIA'] and state['tela atual'] != telas['DERROTA']:
        state['jogador'].desenha(window, assets)

    
    while tempo-state['last_enter']<3000 and state['jogador'].passou_menu:
        tempo = pygame.time.get_ticks()
        print(tempo)
        window.fill((0,0,0))
        text_fase = base.render(fase, True, (255,225,255))
        window.blit(text_fase, (330,350))
        windowScale = pygame.transform.scale(window, (pygame.display.get_surface().get_size())) # Parte de redmencionar a tela

        trueWindow.blit(windowScale, (0,0))
        pygame.display.update()

    state['jogador'].passou_menu = False

    if portas[fase].esta:
        baseFont = pygame.font.Font(None, 32)
        BLACK = (0,0,0)
        WHITE = (255,255,255)
        pygame.draw.rect(window, (0,0,139), (390,406,500,320))
        pygame.draw.rect(window, BLACK,  (400,416, 480,300))
        pygame.draw.rect(window, WHITE, (410,646,460 ,40))
        text_digite_senha = baseFont.render(portas[fase].mensagem, True, WHITE)
        text_digite_senha2=baseFont.render(portas[fase].mensagem2, True, WHITE)
        text_user = baseFont.render(portas[fase].user_text, True, BLACK)
        window.blit(text_digite_senha, (420, 450))
        window.blit(text_digite_senha2, (420, 606))
        window.blit(text_user, (420,656))
        pygame.display.flip()
    
    if fase == 'VITORIA':
        venceu = base.render(state['tempo_final'], True, (255,0,153))
        window.blit(venceu, (259, 725))
        
    windowScale = pygame.transform.scale(window, (pygame.display.get_surface().get_size())) # Parte de redmencionar a tela

    trueWindow.blit(windowScale, (0,0))
    pygame.display.update()

def finaliza ():
    pygame.QUIT


def recebe (state, window):
    
    # Aqui r  recebe apenas o return da classe recebe que fpi tranferida para a classe tela, já que para o game loop o recebe tem que returnar True
    
    r = state['tela atual'].recebe(state, window)


    
            
    return r


    

def gameloop (window, assets, state, trueWindow):
    while recebe(state, window) :




        desenha(window, assets, state, trueWindow, portas)


if __name__ == '__main__':
    window, assets, state, trueWindow, telas, portas = inicializa()
    
    gameloop(window, assets, state, trueWindow)
    finaliza()









