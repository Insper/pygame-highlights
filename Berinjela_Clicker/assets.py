# Imagens, Sons, Fontes, Entre outros

import pygame
import os
from config import largura, altura, Imagens, Botoes, Beringuela, Zedamanga
import json


# Cria as keys do dicionario

TelaI = 'Tela Inicial'
TelaJ = 'Tela Jogo'
TelaS = 'Tela Skins'
TelaC = 'Tela Como Jogar'
Voltar = 'Botão de Voltar'
Comprar = 'Botão de Comprar'
Interrogacao = 'Botão de Interrogação'
LoadGame = 'Botão de Load Game'
NewGame = 'Botão de New Game'
Selecionado = 'Botão de Selecionado'
Selecionar = 'Botão de Selecionar'
BSkins = 'Botão de Skins'
Upgrade = 'Botão de Upgrade'
Beri = 'Berinjela'
TelaIntro = 'Tela de Introdução'
TelaF = 'Tela de Fim'


def load_assets():
    # le o arquivo de saves para obter infos
    with open('skin.json', 'r') as arquivo_json:
        texto = arquivo_json.read()
    skins = json.loads(texto)

    # Pega qual skin ta selecionada
    sel1 = skins['Selecionado1']
    sel2 = skins['Selecionado2']
    sel3 = skins['Selecionado3']

    # Assets

    assets = {}

    assets[TelaI] = pygame.image.load(
        os.path.join(Imagens, 'TelaInicial.png')).convert()
    assets[TelaI] = pygame.transform.scale(assets[TelaI], (largura, altura))
    assets[TelaJ] = pygame.image.load(
        os.path.join(Imagens, 'TelaJogo.png')).convert()
    assets[TelaJ] = pygame.transform.scale(assets[TelaJ], (largura, altura))
    assets[TelaS] = pygame.image.load(
        os.path.join(Imagens, 'TelaSkins.png')).convert()
    assets[TelaS] = pygame.transform.scale(assets[TelaS], (largura, altura))
    assets[TelaC] = pygame.image.load(
        os.path.join(Imagens, 'TelaInstrucao.png')).convert()
    assets[TelaC] = pygame.transform.scale(assets[TelaC], (largura, altura))
    assets[TelaIntro] = pygame.image.load(
        os.path.join(Imagens, 'Intro.png')).convert()
    assets[TelaIntro] = pygame.transform.scale(
        assets[TelaIntro], (largura, altura))
    assets[TelaF] = pygame.image.load(
        os.path.join(Imagens, 'End.png')).convert()
    assets[TelaF] = pygame.transform.scale(assets[TelaF], (largura, altura))

    # Adicionar qual skin tiver selecionada
    if sel1 == 1:
        assets[Beri] = [pygame.image.load(os.path.join(Imagens, 'beri.png')).convert_alpha(), pygame.image.load(os.path.join(
            Imagens, 'beri_lado.png')).convert_alpha(), pygame.image.load(os.path.join(Imagens, 'beri_parada.png')).convert_alpha()]
        assets[Beri] = [pygame.transform.scale(assets[Beri][0], (200, 200)), pygame.transform.scale(
            assets[Beri][1], (200, 200)), pygame.transform.scale(assets[Beri][2], (200, 200))]
    if sel2 == 1:
        assets[Beri] = [pygame.image.load(os.path.join(Beringuela, 'beringuela.png')).convert_alpha(), pygame.image.load(os.path.join(
            Beringuela, 'beringuela_lado.png')).convert_alpha(), pygame.image.load(os.path.join(Beringuela, 'beringuela_parada.png')).convert_alpha()]
        assets[Beri] = [pygame.transform.scale(assets[Beri][0], (200, 200)), pygame.transform.scale(
            assets[Beri][1], (200, 200)), pygame.transform.scale(assets[Beri][2], (200, 200))]
    if sel3 == 1:
        assets[Beri] = [pygame.image.load(os.path.join(Zedamanga, 'zedamanga.png')).convert_alpha(), pygame.image.load(os.path.join(
            Zedamanga, 'zedamanga_lado.png')).convert_alpha(), pygame.image.load(os.path.join(Zedamanga, 'zedamanga_parado.png')).convert_alpha()]
        assets[Beri] = [pygame.transform.scale(assets[Beri][0], (200, 200)), pygame.transform.scale(
            assets[Beri][1], (200, 200)), pygame.transform.scale(assets[Beri][2], (200, 200))]

    # Botoes

    btns = {}

    btns[Comprar] = [pygame.image.load(os.path.join(Botoes, 'Comprar1.png')).convert_alpha(
    ), pygame.image.load(os.path.join(Botoes, 'Comprar2.png')).convert_alpha()]
    btns[Comprar] = [pygame.transform.scale(
        btns[Comprar][0], (200, 75)), pygame.transform.scale(btns[Comprar][1], (200, 75))]
    btns[Voltar] = [pygame.image.load(os.path.join(Botoes, 'Voltar1.png')).convert_alpha(
    ), pygame.image.load(os.path.join(Botoes, 'Voltar2.png')).convert_alpha()]
    btns[Voltar] = [pygame.transform.scale(
        btns[Voltar][0], (50, 50)), pygame.transform.scale(btns[Voltar][1], (50, 50))]
    btns[Interrogacao] = [pygame.image.load(os.path.join(Botoes, 'Interrogação1.png')).convert_alpha(
    ), pygame.image.load(os.path.join(Botoes, 'Interrogação2.png')).convert_alpha()]
    btns[Interrogacao] = [pygame.transform.scale(
        btns[Interrogacao][0], (100, 100)), pygame.transform.scale(btns[Interrogacao][1], (100, 100))]
    btns[LoadGame] = [pygame.image.load(os.path.join(Botoes, 'LoadGame1.png')).convert_alpha(
    ), pygame.image.load(os.path.join(Botoes, 'LoadGame2.png')).convert_alpha()]
    btns[LoadGame] = [pygame.transform.scale(
        btns[LoadGame][0], (100, 100)), pygame.transform.scale(btns[LoadGame][1], (100, 100))]
    btns[NewGame] = [pygame.image.load(os.path.join(Botoes, 'NewGame1.png')).convert_alpha(
    ), pygame.image.load(os.path.join(Botoes, 'NewGame2.png')).convert_alpha()]
    btns[NewGame] = [pygame.transform.scale(
        btns[NewGame][0], (100, 100)), pygame.transform.scale(btns[NewGame][1], (100, 100))]
    btns[Selecionado] = [pygame.image.load(os.path.join(Botoes, 'Selecionado1.png')).convert_alpha(
    ), pygame.image.load(os.path.join(Botoes, 'Selecionado2.png')).convert_alpha()]
    btns[Interrogacao] = [pygame.image.load(os.path.join(Botoes, 'Interrogação1.png')).convert(
    ), pygame.image.load(os.path.join(Botoes, 'Interrogação2.png')).convert_alpha()]
    btns[Interrogacao] = [pygame.transform.scale(
        btns[Interrogacao][0], (50, 50)), pygame.transform.scale(btns[Interrogacao][1], (50, 50))]
    btns[LoadGame] = [pygame.image.load(os.path.join(Botoes, 'LoadGame1.png')).convert(
    ), pygame.image.load(os.path.join(Botoes, 'LoadGame2.png')).convert_alpha()]
    btns[LoadGame] = [pygame.transform.scale(
        btns[LoadGame][0], (200, 100)), pygame.transform.scale(btns[LoadGame][1], (200, 100))]
    btns[NewGame] = [pygame.image.load(os.path.join(Botoes, 'NewGame1.png')).convert(
    ), pygame.image.load(os.path.join(Botoes, 'NewGame2.png')).convert_alpha()]
    btns[NewGame] = [pygame.transform.scale(
        btns[NewGame][0], (200, 100)), pygame.transform.scale(btns[NewGame][1], (200, 100))]
    btns[Selecionado] = [pygame.image.load(os.path.join(Botoes, 'Selecionado1.png')).convert_alpha(
    ), pygame.image.load(os.path.join(Botoes, 'Selecionado2.png')).convert_alpha()]
    btns[Selecionado] = [pygame.transform.scale(
        btns[Selecionado][0], (200, 75)), pygame.transform.scale(btns[Selecionado][1], (200, 75))]
    btns[Selecionar] = [pygame.image.load(os.path.join(Botoes, 'Selecionar1.png')).convert_alpha(
    ), pygame.image.load(os.path.join(Botoes, 'Selecionar2.png')).convert_alpha()]
    btns[Selecionar] = [pygame.transform.scale(
        btns[Selecionar][0], (200, 75)), pygame.transform.scale(btns[Selecionar][1], (200, 75))]
    btns[BSkins] = [pygame.image.load(os.path.join(Botoes, 'Skins1.png')).convert_alpha(
    ), pygame.image.load(os.path.join(Botoes, 'Skins2.png')).convert_alpha()]
    btns[BSkins] = [pygame.transform.scale(
        btns[BSkins][0], (100, 75)), pygame.transform.scale(btns[BSkins][1], (100, 75))]
    btns[Upgrade] = [pygame.image.load(os.path.join(Botoes, 'Upgrade1.png')).convert_alpha(
    ), pygame.image.load(os.path.join(Botoes, 'Upgrade2.png')).convert_alpha()]
    btns[Upgrade] = [pygame.transform.scale(
        btns[Upgrade][0], (80, 40)), pygame.transform.scale(btns[Upgrade][1], (80, 40))]

    return [assets, btns]
