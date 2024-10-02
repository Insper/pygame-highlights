import pygame
from class_game import *
from  time import sleep
from constantes import *


def inicializa ():
    """INICIO DO JOGO! CARREGAMOS TODAS AS INFORMAÇÕES NECESSÁRIAS PARA O FUNCIONAMENTO"""
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("sound/music.mp3")
    pygame.mixer.music.set_volume(0.6)
    pygame.mixer.music.play(-1)

    pygame.display.set_caption("Code Scape")
    window = pygame.display.set_mode((1152, 864))

    assets = {             #Carregamos todas as imagens necessárias para o jogo
        'player' : pygame.image.load('img/frente.png'),
        'costa' : [pygame.image.load('img/costa.png'), pygame.image.load('img/costa_anda_d.png'), pygame.image.load('img/costa_anda_e.png')],
        'frente' : [pygame.image.load('img/frente.png'), pygame.image.load('img/frente_anda_d.png'), pygame.image.load('img/frente_anda_e.png')],
        'ladod' : [pygame.image.load('img/lado_d.png'), pygame.image.load('img/lado_anda_d.png'), pygame.image.load('img/lado_anda_d2.png')],
        'ladoe' : [pygame.image.load('img/lado_e.png'), pygame.image.load('img/lado_anda_e.png'), pygame.image.load('img/lado_anda_e2.png')],
        'mapa' : [pygame.image.load('img/fase1.png'), pygame.image.load('img/menu.png'), pygame.image.load('img/fase2.png'), pygame.image.load('img/fase3.png')],
        'key' : [pygame.image.load('img/papeis.png')],
        "porta" : pygame.image.load('img/porta.png'),
        'menu_principal': pygame.image.load('img/fundo_menu.png'), 'vitoria': pygame.image.load('img/vitoria.png') , 'derrota': pygame.image.load('img/derrota.png'),
        'papel' : [pygame.image.load('img/papel.png')],
        'cama': [pygame.image.load('img/cama.png')],
        'clock': [pygame.image.load('img/clock.png')],
        'mesa1': [pygame.image.load('img/mesa1.png')],
        'bolinha de papel' : [pygame.image.load('img/bola.png')],
        'computador' : [pygame.image.load('img/computador.png'), pygame.image.load('img/computador2.png')],
        'mesa2':[pygame.image.load('img/mesa2.png')],
        'disquete':[pygame.image.load('img/disquete.png')],
        'celular':[pygame.image.load('img/celular.png')],
        'tv':[pygame.image.load('img/tv.png'), pygame.image.load('img/tv2.png')],
        'estante': [pygame.image.load('img/estante.png')],
        'interacao' : pygame.mixer.Sound('sound/item.wav'),
        'door' : pygame.mixer.Sound('sound/door.flac'),
        'tutorial': pygame.image.load('img/tutorial.png')
    }
    state = {             #Aqui criamos a lista de itens para cada fase, passando eles dentro da classe Item, a qual passamos tudo que é necessário para cada ítem, que inclui sua imagem, dica e posição.
    'jogador' : Player(360, 240),
    'lista de itens1' :[Item(assets['bolinha de papel'], (1073,696), pygame.image.load('img/dica_fase1.png')), Item(assets['cama'], (34,469), pygame.image.load('img/cama_dica.png')), Item(assets['mesa1'], (1033,463), pygame.image.load('img/mesa1_dica.png')), Item(assets['clock'], (526,13), pygame.image.load('img/clock_dica.png'))],
    'lista de itens2' :[Item(assets['papel'], (1073,700), pygame.image.load('img/dica_fase2.png')), Item(assets['computador'], (128,51), pygame.image.load('img/computador_dica.png')), Item(assets['cama'], (34,469), pygame.image.load('img/cama_dica.png')), Item(assets['mesa2'], (321,772), pygame.image.load('img/mesa1_dica.png')), Item(assets['clock'], (526,13), pygame.image.load('img/clock_dica.png')), Item(assets['disquete'], (237,633), pygame.image.load('img/disquete_dica.png'))],
    'lista de itens3' :[Item(assets['celular'], (1064,527), pygame.image.load('img/celular_dica.png')), Item(assets['tv'], (684,62), pygame.image.load('img/tv_dica.png')), Item(assets['estante'], (237,23), pygame.image.load('img/estante_dica.png')), Item(assets['computador'], (843,35), pygame.image.load('img/computador2_dica.png')), Item(assets['mesa2'], (321,772), pygame.image.load('img/copo_dica.png'))],
    'primeiro_tempo'  :0,
    'last_enter': 0,
    'troca_status_move':0,      #Variáveis usadas em condições do jogo
    'numero_trocador':0,
    'tempo_geral': 0
    }

    portas = {  #Nesse dicionário portas passamos tudo necessário às portas do jogo, como imagem, posição, texto e senha.
        'PRIMEIRA FASE' : Porta(assets['porta'], (987, 21), "A SENHA é mais facil do que parece!","Digite e tecle ENTER", "senha"),
        'SEGUNDA FASE' : Porta(assets['porta'], (987, 21), "As dicas estão por ai...","Digite e tecle ENTER", "12/01/1986"),
        'TERCEIRA FASE' : Porta(assets['porta'], (987, 21), "Vai ser na raça mesmo","Digite e tecle ENTER", "toshi"),
        'menu_principal': Porta(assets['porta'],(-500,-500), "vapo","mensagem2","no"),
        'VITORIA': Porta(assets['porta'],(-500,-500), "vapo","mensagem2","no"),
        'DERROTA':  Porta(assets['porta'],(-500,-500), "vapo","mensagem2","no")
    }

    telas = {   #Criamos a tela de cada fase, passaremos ela na classe Tela onde desenhamos as alterações
        'menu_principal': Tela(assets['menu_principal'],[],portas['menu_principal']),
        'SEGUNDA FASE' : Tela(assets['mapa'][2], state['lista de itens2'], portas['SEGUNDA FASE']),
        'PRIMEIRA FASE' : Tela(assets['mapa'][0], state['lista de itens1'], portas['PRIMEIRA FASE']),
        'TERCEIRA FASE' : Tela(assets['mapa'][3], state['lista de itens3'], portas['TERCEIRA FASE']),
        'VITORIA': Tela(assets['vitoria'],[],portas['menu_principal']),
        'DERROTA':Tela(assets['derrota'],[],portas['menu_principal'])
    }



    state['tela atual'] = telas['menu_principal']


    return window, assets, state, telas, portas

def entre_telas (state, fase) :
    """TEMPO DE ESPERA ENTRE AS FASES"""
    while state['tempo_geral']-state['last_enter']<3000 and state['jogador'].passou_menu:
        state['tempo_geral'] = pygame.time.get_ticks()
        window.fill((0,0,0))
        text_fase = BASE.render(fase, True, (255,225,255))
        window.blit(text_fase, (330,350))
        pygame.display.update()

def tutorial (state) :
    """TUTORIAL"""

    if state['tempo_geral']-state['last_enter']<8500 and state['jogador'].status == "PRIMEIRA FASE":
        state['tempo_geral'] = pygame.time.get_ticks()


        window.blit(assets['tutorial'], (326,232))
        pygame.display.update()

def desenha (window, assets, state, portas):
    """DESENHAMOS OS ÍTENS DO JOGO"""

    tempo = pygame.time.get_ticks()
    fase = state['jogador'].status # Fase recebe o nome da fase que o jogador está e isso ajuda na hora de controlar os itens e o cenário

    state['tela atual'] = telas[fase]

    state['tela atual'].img = pygame.transform.scale(state['tela atual'].img, (pygame.display.get_surface().get_size()))  # Parte de redmencionar a tela

    window.blit(state['tela atual'].img,(0,0))

    for itens in state['tela atual'].itens:   # Estrutura de for que controla a animação dos itens caso eles tenham animação.

        if itens.status:
            window.blit(itens.mensagem, (326,232))
        if len(itens.img) == 1:
            window.blit(itens.img[0], itens.ponto)

        elif tempo - state['troca_status_move'] > 1750:  #Fazer animação de alguns itens
            state['troca_status_move'] = tempo
            if state['numero_trocador'] == 0:
                state['numero_trocador'] = 1
            elif state['numero_trocador'] ==1:
                state['numero_trocador'] = 0
        if len(itens.img) == 2:
            window.blit(itens.img[state['numero_trocador']], itens.ponto)

    window.blit(portas[fase].img, portas[fase].ponto)
    tempo = pygame.time.get_ticks()

    if state['tela atual'] != telas['menu_principal'] and state['tela atual'] != telas['VITORIA'] and state['tela atual'] != telas['DERROTA']: # Controle de quais telas o jogador pode ser desenhado
        state['jogador'].desenha(window, assets)      # Desenha o jogador
        cronometro = BASE_MENOR.render(f"{(pygame.time.get_ticks()-state['primeiro_tempo'])/60000:.2f} Minutos", True, ROSA)
        window.blit(cronometro, (0,0))

        entre_telas(state, fase) # Caso o jogador tenha passado de fase é feito uma transição para outra a outra fase do jogo.
        if state['jogador'].status == 'PRIMEIRA FASE':
            tutorial(state)


    state['jogador'].passou_menu = False

    if portas[fase].esta:

        portas[fase].desenha(window, fase, portas)

    if fase == 'VITORIA':  # Verifica se o jogador venceu para assim desenhar a tela de vitória e o tempo em que resolveu os desafios
        venceu = BASE.render(state['tempo_final'], True, ROSA)
        window.blit(venceu, (259, 725))

    pygame.display.update()

def finaliza ():
    pygame.QUIT


def recebe (state, window):
    """Aqui r  recebe apenas o return da classe recebe que foi tranferida para a classe tela, já que para o game loop o recebe tem que returnar True"""
    r = state['tela atual'].recebe(state, window, assets)
    return r




def gameloop (window, assets, state):
    """Loop do jogo"""
    while recebe(state, window) :
        desenha(window, assets, state, portas)


"""Inicialização do jogo"""
window, assets, state, telas, portas = inicializa()
gameloop(window, assets, state)
finaliza()









