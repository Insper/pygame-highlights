# Arquivo para as missoes

# Importa bibliotecas e arquivos
from config import largura, altura, fps, quit, jogando, skins, Roxo, Fontes
from assets import TelaI, TelaJ, TelaS, load_assets, Upgrade, Beri, BSkins
from os import path
from classes import Button, Berinjela
import pygame
import json

# Lê o save ja existente
with open('save.json', 'r') as arquivo_json:
        texto = arquivo_json.read()

# Cria o dicionario e le as variaveis
goods = json.loads(texto)
money = goods['Dinheiro']
dima = goods['Gemas']
Up1 = goods['Up1']
Up2 = goods['Up2']
Up3 = goods['Up3']
Up4 = goods['Up4']
Up5 = goods['Up5']
Up6 = goods['Up6']
clicks = goods['Clicks']
auto = goods['AcumuladoAuto']
acumulado = goods['Acumulado']

# Cria o dicionario de missões com o numero, o nome, o que eu quero checar e a quantidade
def listamissoes(Up1,Up2,Up4,Up5,clicks,auto,acumulado):
    missoes = {
    1:['Clique na Berinjela 100 vezes:', clicks, 100],
    2:['Tenha 5 Clicks:', Up1, 5],
    3:['Gere 1.000 berinjelas:', acumulado, 1000],
    4:['Clique na berinjela 200 vezes:', clicks, 200],
    5:['Tenha 5 fazendeiros:', Up2, 5],
    6:['Gere 10.000 berinjelas:', acumulado, 10000],
    7:['Gere automaticamente 1.000 berinjelas:', auto, 1000],
    8:['Clique na berinjela 1.000 vezes:', clicks, 1000],
    9:['Tenha 10 Clicks:', Up1, 10],
    10:['Tenha 10 Fazendeiros:', Up2, 10],
    11:['Clique na berinjela 1.250 vezes:', clicks, 1250],
    12:['Gere 100.000 berinjelas:', acumulado, 1000],
    13:['Compre 1 Planta Robotizada:', Up4, 1],
    14:['Gere automaticamente 50.000 berinjelas:', auto, 50000],
    15:['Tenha 22 Clicks:', clicks, 22],
    16:['Clique na berinjela 1.500 vezes:', clicks, 1500],
    17:['Tenha 3 Super Clicks:', Up5, 3],
    18:['Tenha 40 Fazendeiros:', Up2, 40],
    19:['Gere automaticamente 150.000 berinjelas:', auto, 150000],
    20:['Tenha 10 Super Clicks:', Up5, 10],
    21:['Acabou', 0,0]
    }
    return missoes
