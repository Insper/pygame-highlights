import pygame
import os
from telas.tela_main import Cassino
from telas.tela_menu import Menu
from telas.tela_como_jogar import ComoJogar
from telas.tela_config import Config
from telas.tela_inicio import Inicio
from telas.tela_game_over import GameOver
from minigames.blackjack import Blackjack
from minigames.roleta import Roleta
from minigames.horserace import HorseRace
from minigames.poker import Poker
from player import Player

def inicializa():
    """
    Inicializa todas as informações e objetos do jogo.
    """

    pygame.init()

    config = Config()

    asset = {
        **config.asset,
        'def_font' : pygame.font.Font(pygame.font.get_default_font(), 15),
        'leg_font' : pygame.font.Font(pygame.font.get_default_font(), 11),
        'money_font' : pygame.font.Font(pygame.font.match_font('Abel'), 30),
        'old_font' : pygame.font.Font(pygame.font.match_font('Old English Five'), 45),
        'objs' : {},
        'personagens' : {},
    }

    #Inicializa objeto das Configurações
    asset['config'] = config

    #Inicializa objeto da Tela de Como Jogar
    asset['como_jogar'] = ComoJogar(asset)

    window = pygame.display.set_mode(tuple(asset['tam_tela']), vsync=asset['vsync'], flags=pygame.SCALED)
    pygame.display.set_caption('Casino Nights')
    

    #Pega imagens da pasta de Objetos
    for img in os.listdir('images/objs'):
        asset['objs'][img[:-4]] = pygame.image.load(f'images/objs/{img}')
    

    #Pega imagens da pasta de Personagens
    for img in os.listdir('images/personagens'):
        if img.startswith('jogador'):
            asset[img[:-4]] = Player(pygame.image.load(f'images/personagens/{img}'), [asset['tam_tela'][0]/2 - 50, asset['tam_tela'][1]/2+50], (50,50))
        else:
            asset['personagens'][img[:-4]] = pygame.transform.scale(pygame.image.load(f'images/personagens/{img}'), (60,60))
    
    #Inicializa objeto Cassino
    asset['mapa'] = Cassino(asset)

    #Inicializa objeto da Tela de Início
    asset['inicio'] = Inicio(window, asset)

    state = {
        'tela_jogo' : 'inicio',
        'aviso' : None,
        'jogador' : asset['jogador'].pos,
        'vel' : [0,0],
        'last_updated' : 0,
        'dinheiro' : 2000,
        'dt' : 0,
        'minigame' : None,
    }

    return window, asset, state

def atualiza_estado(window, asset, state):
    """
    Atualiza estado do jogo, e checa ações e interações.
    """
    if state['tela_jogo'] != 'game_over':
        t_atual = pygame.time.get_ticks()
        state['dt'] = (t_atual - state['last_updated'])/1000
        state['last_updated'] = t_atual

    pygame.mixer.music.set_volume(asset['vol_musica'])
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.load('musica/jazz_fundo.mp3')
        pygame.mixer.music.play(-1, fade_ms=1500)
    
    if state['tela_jogo'] == 'inicio': #Tela inicial
        return asset['inicio'].interacoes(asset, state)
    elif state['tela_jogo'] == 'main': #Tela principal (Cassino)
        return asset['mapa'].interacoes(asset, state)
    elif state['tela_jogo'] == 'menu': #Tela Menu
        return Menu().interacoes(state)
    elif state['tela_jogo'] == 'config': #Tela Configurações
        return asset['config'].interacoes(window, asset, state)
    elif state['tela_jogo'] == 'como_jogar': #Tela Como Jogar
        return asset['como_jogar'].interacoes(window, asset, state)
    elif state['tela_jogo'] == 'blackjack': #Tela BlackJack
        if not state['minigame'].interacoes():
            state['tela_jogo'] = 'main'
    elif state['tela_jogo'] == 'roleta': #Tela Roleta
        if not state['minigame'].interacoes():
            state['tela_jogo'] = 'main'
    elif state['tela_jogo'] == 'horse_race': #Tela Corrida de Cavalo
        if not state['minigame'].interacoes():
            state['tela_jogo'] = 'main'
    elif state['tela_jogo'] == 'poker': #Tela Poker
        if not state['minigame'].interacoes():
            state['tela_jogo'] = 'main'
    elif state['tela_jogo'] == 'slot_machine': #Tela Caça Níquel (NÃO IMPLEMENTADO)
        return asset['mapa'].interacoes(asset, state)
    elif state['tela_jogo'] ==  'game_over':
        return GameOver().interacoes()
        
    return True

def game_loop(window, asset, state):
    """
    Loop principal do jogo, onde roda todas as outras funções necessárias.
    """
    game = True
    blackjack = Blackjack(window)
    blackjack_started = False
    roleta = Roleta(window)
    roleta_started = False
    horse_race = HorseRace(window)
    horse_race_started = False
    poker = Poker(window)
    poker_started = False
    while game:
        game = atualiza_estado(window, asset, state)
        if game == False:
            return
        if state['tela_jogo'] == 'inicio':
            asset['inicio'].desenha(window, asset)
        elif state['tela_jogo'] == 'main':
            asset['mapa'].desenha(window, asset, state)
            blackjack_started = False
            roleta_started = False
            horse_race_started = False
            poker_started = False
        elif state['tela_jogo'] ==  'menu':
            Menu().desenha(window, asset)
        elif state['tela_jogo'] == 'config':
                asset['config'].desenha(window, asset)
        elif state['tela_jogo'] == 'como_jogar':
                asset['como_jogar'].desenha(window)
        elif state['tela_jogo'] == 'blackjack':
            if not blackjack_started:
                blackjack = Blackjack(window)
                state['minigame'] = blackjack
                blackjack_started = True
            blackjack.desenha()
            if not blackjack.isInMenu and not blackjack.isInGameMenu:
                blackjack.finishGame()
                if blackjack.resultGame == 'win':
                    state['dinheiro'] += 100
                elif blackjack.resultGame == 'lose':
                    state['dinheiro'] -= 100
                blackjack.resultGame = None
                blackjack.desenha(True)
        elif state['tela_jogo'] == 'roleta':
            if not roleta_started:
                roleta = Roleta(window)
                state['minigame'] = roleta
                roleta_started = True
            roleta.desenha()
            if roleta.resultMenu:
                if not roleta.giveMoney:
                    state['dinheiro'] += roleta.money
                    roleta.money = 0
                    roleta.giveMoney = True
        elif state['tela_jogo'] == 'horse_race':
            if not horse_race_started:
                horse_race = HorseRace(window)
                state['minigame'] = horse_race
                horse_race_started = True
            horse_race.desenha()
            if horse_race.money != 0 and not horse_race.giveMoney:
                horse_race.giveMoney = True
                state['dinheiro'] += horse_race.money
        elif state['tela_jogo'] == 'poker':
            if not poker_started:
                poker = Poker(window)
                state['minigame'] = poker
                poker_started = True
                poker.deal_cards()
            poker.desenha()
            if poker.resultMessage != '' and not poker.giveMoney and not poker.animation:
                poker.giveMoney = True
                state['dinheiro'] += poker.bet
        elif state['tela_jogo'] == 'slot_machine': #(NÃO IMPLEMENTADO)
            asset['mapa'].desenha(window, asset, state)
        elif state['tela_jogo'] == 'game_over':
            GameOver().desenha(window, asset, state)

        if state['dinheiro'] > 0 and state['tela_jogo'] != 'inicio':
            window.blit(asset['money_font'].render(f'Saldo: R${state["dinheiro"]}', True, (0, 0, 0)), (10,10))
        elif state['dinheiro'] <= 0 and state['tela_jogo'] != 'inicio':
            state['tela_jogo'] = 'game_over'
        pygame.display.update()

if __name__ == '__main__':
    game_loop(*inicializa())