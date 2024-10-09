# Configurações do jogo
from os import path
import pygame


# Infos Básicas
largura = 580
altura = 700
fps = 60


# Paths para arquivos/pastas
Imagens = path.join(path.dirname(__file__), 'assets', 'img')
Fontes = path.join(path.dirname(__file__), 'assets', 'fonts')
Botoes = path.join(path.dirname(__file__), 'assets', 'img', 'Botoes')
Beringuela = path.join(path.dirname(__file__), 'assets', 'img', 'Skins', 'beringuela')
Zedamanga = path.join(path.dirname(__file__), 'assets', 'img', 'Skins', 'zedamanga')
SomFundo = path.join(path.dirname(__file__), 'assets', 'wav', 'music_a.mp3')
Click = path.join(path.dirname(__file__), 'assets', 'wav', 'Click.mp3')

# States
quit = 0
iniciando = 1
jogando = 2
skins = 3
instru = 4
intro = 5
fim = 6

# Cores principais

Roxo = (99,46,98)

