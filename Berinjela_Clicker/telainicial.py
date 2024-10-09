# Tela Inicial

from config import largura, altura, fps, quit, jogando, Roxo, instru, intro
from assets import TelaI, load_assets, Beri, Voltar, Interrogacao, NewGame, LoadGame
from os import path
import pygame
from classes import Button, Berinjela
import json 

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Berijela Clicker')


assets = load_assets()[0]
btns = load_assets()[1]

# criando a berinjela

beri = Berinjela(assets[Beri], (300,300))


# ----- Inicia estruturas de dados
def telainicial(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # carrega os assets e botoes
    assets = load_assets()[0]
    btns = load_assets()[1]

    # Carrega o fundo da tela inicial
    fundo = assets[TelaI]
    fundo_rect = fundo.get_rect()

    # começa a rodar o loop
    running = True

    # coloca a posição dos botões
    botaoint = Button(((largura/2)-25),600,btns[Interrogacao])
    botaonew = Button(((largura/2)-225), 470, btns[NewGame])
    botaoload = Button(((largura/2)+25), 470, btns[LoadGame])

    while running:

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(Roxo)
        screen.blit(fundo, fundo_rect)
        screen.blit(beri.image, beri.rect)

        # Desenha os botões
        int = botaoint.aparecer(screen, btns[Interrogacao])
        new = botaonew.aparecer(screen, btns[NewGame])
        load = botaoload.aparecer(screen, btns[LoadGame])

        # Ajusta a velocidade do jogo.
        clock.tick(fps)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = quit # muda o state para quit
                running = False # para de rodar

            if int:
                state = instru # muda o state para instru (instrucoes)
                running = False # para de rodar
            
            if new:
                state = intro # muda para a intro do jogo (telaintro)
                running = False # para de rodar

                # zera os saves
                save = {'Dinheiro': 0, "Soma": 1,"Gemas": 0, 'Up1': 0, 'Up2': 0, 'Up3': 0, 'Up4': 0, 'Up5': 0, 'Up6': 0, 'Auto': 0, 'Missao':1, 'Clicks': 0, 'Acumulado': 0, 'AcumuladoAuto': 0}
                skins = {'Comprado2': False, 'Comprado3': False, 'Selecionar1': 0, 'Selecionar2': 0, 'Selecionar3': 0, 'Selecionado1':1, 'Selecionado2':0, 'Selecionado3':0, 'Jacomprou1':True,'Jacomprou2':False,'Jacomprou3':False }

                # Transformando de volta para JSON (texto)
                novo_save = json.dumps(save)
                novo_skins = json.dumps(skins)
                # Salvando o arquivo
                with open('save.json', 'w') as arquivo_json:
                    arquivo_json.write(novo_save)
                with open('skin.json', 'w') as arquivo_json:
                    arquivo_json.write(novo_skins)
            if load:
                state = jogando # começa a jogar
                running = False # para de rodar

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        pygame.display.update()
        
    return state