# Tela de Introducao 

# Imports
from config import largura, altura, fps, quit, jogando, Roxo, skins, instru, iniciando, intro, fim
from assets import TelaI, TelaJ, TelaS, TelaC, TelaIntro, TelaF, load_assets, Voltar
from classes import Button, Berinjela
from os import path
import pygame

# Gera a tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Berigela Clicker')

# Carrega os assets
assets = load_assets()[0]
btns = load_assets()[1]

# Funcao da tela
def telafim(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial

    fundo = assets[TelaF]
    fundo_rect = fundo.get_rect()

    running = True
    keysdown = {}

    while running:

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(Roxo)
        screen.blit(fundo, fundo_rect)

        # Ajusta a velocidade do jogo.
        clock.tick(fps)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = quit
                running = False
            # Verifica se clicou para continuar
            if event.type == pygame.MOUSEBUTTONUP:
                state = jogando
                running = False
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()


    return state