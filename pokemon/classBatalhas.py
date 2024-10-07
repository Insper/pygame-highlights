import pygame
import time
import random
from classAnimacoes import *
class Batalha:
    def __init__(self):
        '''
            Função que inicia todos os estados, condições, imagens, personagens e contadores da batalha.
        '''
        self.fonte = pygame.font.Font('imgBatalhas/fontes.ttf', 20)
        self.fonteMenu = pygame.font.Font('imgBatalhas/fontes.ttf', 50)
        self.fonteBatalha = pygame.font.Font('imgBatalhas/fontes.ttf', 25)
        self.lista_imagens = [
            pygame.transform.scale((pygame.image.load('img/Ataques pokemon.png')),(640, 150)),
            pygame.transform.scale((pygame.image.load('img/template.png')),(330, 60)),
            pygame.transform.scale((pygame.image.load('imgBatalhas/barraSemVida.png')),(290, 80)),
            pygame.transform.scale((pygame.image.load('imgBatalhas/seta.png')),(40, 40)),
            pygame.transform.scale((pygame.image.load('imgBatalhas/barraVazia.png')),(640, 150)),
            pygame.transform.scale((pygame.image.load('imgBatalhas/seta.png')),(20, 20)),
            pygame.transform.scale((pygame.image.load('img/pikachujogador.png')),(200,200)),
            pygame.transform.scale((pygame.image.load('img/scizor.png')),(200,200)),
            pygame.transform.scale((pygame.image.load('img/venusaur.png')),(200,200)),
        ]
        tackle = {'dano': 35, 'precisao': 100, 'tipo': 'normal', 'pps': 20, 'pps_max': 20, 'nome': 'Tackle'}
        facade = {'dano': 50, 'precisao': 100, 'tipo': 'normal', 'pps': 10, 'pps_max': 10, 'nome': 'Facade'}
        facade2 = {'dano': 50, 'precisao': 100, 'tipo': 'normal', 'pps': 10, 'pps_max': 10, 'nome': 'Facade'}
        slam = {'dano': 55, 'precisao': 90, 'tipo': 'normal', 'pps': 5, 'pps_max': 5, 'nome': 'Slam'}
        thunderbolt = {'dano': 50, 'precisao': 100, 'tipo': 'eletrico', 'pps': 5, 'pps_max': 5, 'nome': 'Thunderbolt'}
        cut = {'dano': 45, 'precisao': 95, 'tipo': 'normal', 'pps': 10, 'pps_max': 10, 'nome': 'Cut'}
        cut2 = {'dano': 45, 'precisao': 95, 'tipo': 'normal', 'pps': 10, 'pps_max': 10, 'nome': 'Cut'}
        fury_cutter = {'dano': 20, 'precisao': 100, 'tipo': 'inseto', 'pps': 15, 'pps_max': 15, 'nome': 'Fury Cutter'}
        metal_claw = {'dano': 50, 'precisao': 90, 'tipo': 'metal', 'pps': 5, 'pps_max': 5, 'nome': 'Metal Claw'}
        sludge_bomb = {'dano': 40, 'precisao': 100, 'tipo': 'veneno', 'pps': 10, 'pps_max': 10, 'nome': 'Sludge Bomb'}
        razor_leaf = {'dano': 40, 'precisao': 95, 'tipo': 'grama', 'pps': 15, 'pps_max': 15, 'nome': 'Razor Leaf'}
        earthquake = {'dano': 55, 'precisao': 100, 'tipo': 'terra', 'pps': 5, 'pps_max': 5, 'nome': 'Earthquake'}
        self.pokemons = [
            {'vida': 290, 'vida_max': 290, 'ataques': [tackle, thunderbolt, slam, facade], 'nome': 'PIKACHU'},
            {'vida': 250, 'vida_max': 250, 'ataques': [cut, fury_cutter, metal_claw, facade2], 'nome': 'SCIZOR'},
            {'vida': 330, 'vida_max': 330, 'ataques': [razor_leaf, sludge_bomb, earthquake, cut2], 'nome': 'VENUSAUR'},
        ]
        self.pokemonatual = 0
        self.botao = 1
        self.inimigo_compara = 0
        self.tela_atual = 'escolhendo'
        self.inimigo_atual = 0
        self.efetivo = ''
        self.atacou = False
        self.fury_cutter = False
        self.crit = False
        self.sludge_bol = False
        self.thunder_bol = False
        self.tackle_bol = False
        self.cut_bol = False
        self.slam_bol = False
        self.facade_bol = False
        self.earthquake_bol = False
        self.earthquake_cont = 0
        self.iearthquake_bol = False
        self.iearthquake_cont = 0
        self.leaf_bol = False
        self.metal_bol = False
        self.fcut_bol = False
        self.fcut = 20
        self.itackle_bol = False
        self.ifacade_bol = False
        self.ikarate_bol = False
        self.ipsybeam_bol = False
        self.iatacou = True
        self.fpunch = False
        self.recover = False
        self.icut_bol = False
        self.horn_bol = False
        self.dchop_bol = False
        self.enter_bol = False
        self.ataqueinimigo = []
    def desenha_batalha(self, window, dicionario):
        '''
            Função que desenha, atualiza, pausa e finaliza a batalha.
        '''
        if self.tela_atual != 'animando':
            self.inimigo_atual = 0
            if dicionario[self.inimigo_atual]['vida_pokemon'] <= 0 and len(dicionario) > 1:
                self.inimigo_atual += 1
            if dicionario[self.inimigo_atual]['vida_pokemon'] <= 0 and len(dicionario) > 2:
                self.inimigo_atual += 1
            if dicionario[self.inimigo_atual]['vida_pokemon'] <= 0 and self.tela_atual != 'batalha' and self.tela_atual != 'texto_batalha':
                self.tela_atual = 'fim'
                self.pokemons[1]['ataques'][1]['dano'] = 20
        #EVITA VIDA NEGATIVA
        if dicionario[self.inimigo_atual]['vida_pokemon'] < 0:
            dicionario[self.inimigo_atual]['vida_pokemon'] = 0
        if self.pokemons[self.pokemonatual]['vida'] < 0:
            self.pokemons[self.pokemonatual]['vida'] = 0
        #DESENHA A TELA DA BATALHA
        window.fill((188, 188, 188))
        window.blit(self.lista_imagens[1], (0, 400))
        window.blit(self.lista_imagens[1], (290, 230))
        window.blit(self.lista_imagens[6 + self.pokemonatual], (30, 300))
        window.blit(self.lista_imagens[2], (40, 90))
        window.blit(self.lista_imagens[2], (310, 290))
        window.blit(self.lista_imagens[4], (0, 450))
        #RECEBE O ATAQUE DO INIMIGO
        if dicionario[self.inimigo_atual]['vida_pokemon'] > 0 and self.iatacou == False and self.earthquake_bol != True and self.tela_atual == 'inimando':
            self.ataque_inimigo = self.inimigo_ataca(dicionario)
            self.iatacou = True
        #DESENHA A VIDA DOS POKEMONS
        blit_inimigo = self.fonte.render(f'{dicionario[self.inimigo_atual]["nome"]}: {dicionario[self.inimigo_atual]["vida_pokemon"]}/{dicionario[self.inimigo_atual]["vida_max"]}', True, (0, 0, 0))
        window.blit(blit_inimigo, (80, 115))
        blit_jogador = self.fonte.render(f'{self.pokemons[self.pokemonatual]["nome"]}: {self.pokemons[self.pokemonatual]["vida"]}/{self.pokemons[self.pokemonatual]["vida_max"]}', True, (0, 0, 0))
        window.blit(blit_jogador, (350, 310))
        #PARA DE DESENHAR O POKEMON INIMIGO SE ELE MORRER
        if dicionario[self.inimigo_atual]['vida_pokemon'] >= 0 and self.earthquake_bol != True or self.iearthquake_bol != True or self.tela_atual == 'animando':
            window.blit(dicionario[self.inimigo_atual]['imagem'], (370, 130))
        #DESENHA O ATAQUE DO JOGADO
        if self.tela_atual == 'animando':
            if self.earthquake_bol == True or self.iearthquake_bol == True:
                movimento = random.randint(-15 , 15)
                self.earthquake_cont += 1
                if self.earthquake_cont == 45:
                    if self.earthquake_bol == True and self.iearthquake_bol != True:
                        self.tela_atual = 'texto_batalha'
                        movimento = 0
                    elif self.iearthquake_bol == True and self.earthquake_bol != True:
                        self.tela_atual = 'inimigo'
                        movimento = 0
                    self.earthquake_bol = False
                    self.iearthquake_bol = False
                    self.earthquake_cont = 0
                window.fill((188, 188, 188))
                window.blit(self.lista_imagens[2], (40, 90))
                window.blit(self.lista_imagens[2], (310, 290))
                window.blit(self.lista_imagens[1], (0 + movimento, 400))
                window.blit(self.lista_imagens[1], (290 + movimento, 230))
                window.blit(self.lista_imagens[6 + self.pokemonatual], (30 + movimento, 300))
                window.blit(dicionario[self.inimigo_atual]['imagem'], (370 + movimento, 130))
                blit_inimigo = self.fonte.render(f'{dicionario[self.inimigo_atual]["nome"]}: {dicionario[self.inimigo_atual]["vida_pokemon"]}/{dicionario[self.inimigo_atual]["vida_max"]}', True, (0, 0, 0))
                window.blit(blit_inimigo, (80, 115))
                blit_jogador = self.fonte.render(f'{self.pokemons[self.pokemonatual]["nome"]}: {self.pokemons[self.pokemonatual]["vida"]}/{self.pokemons[self.pokemonatual]["vida_max"]}', True, (0, 0, 0))
                window.blit(blit_jogador, (350, 310))
                window.blit(self.lista_imagens[4], (0, 450))
        if self.tela_atual == 'inimando':
            if self.earthquake_bol == True or self.iearthquake_bol == True:
                movimento = random.randint(-15 , 15)
                self.earthquake_cont += 1
                if self.earthquake_cont == 45:
                    if self.earthquake_bol == True and self.iearthquake_bol != True:
                        self.tela_atual = 'texto_batalha'
                        movimento = 0
                    elif self.iearthquake_bol == True and self.earthquake_bol != True:
                        self.tela_atual = 'inimigo'
                        movimento = 0
                    self.earthquake_bol = False
                    self.iearthquake_bol = False
                    self.earthquake_cont = 0
                window.fill((188, 188, 188))
                window.blit(self.lista_imagens[2], (40, 90))
                window.blit(self.lista_imagens[2], (310, 290))
                window.blit(self.lista_imagens[1], (0 + movimento, 400))
                window.blit(self.lista_imagens[1], (290 + movimento, 230))
                window.blit(self.lista_imagens[6 + self.pokemonatual], (30 + movimento, 300))
                window.blit(dicionario[self.inimigo_atual]['imagem'], (370 + movimento, 130))
                blit_inimigo = self.fonte.render(f'{dicionario[self.inimigo_atual]["nome"]}: {dicionario[self.inimigo_atual]["vida_pokemon"]}/{dicionario[self.inimigo_atual]["vida_max"]}', True, (0, 0, 0))
                window.blit(blit_inimigo, (80, 115))
                blit_jogador = self.fonte.render(f'{self.pokemons[self.pokemonatual]["nome"]}: {self.pokemons[self.pokemonatual]["vida"]}/{self.pokemons[self.pokemonatual]["vida_max"]}', True, (0, 0, 0))
                window.blit(blit_jogador, (350, 310))
                window.blit(self.lista_imagens[4], (0, 450))
        #ESCREVE O TEXTO DA BATALHA
        elif self.tela_atual == 'texto_batalha':
            self.tela_atual = 'inimando'
            window.blit(self.lista_imagens[4], (0, 450))
            ataque = self.fonteBatalha.render(f"{self.pokemons[self.pokemonatual]['nome']} used {self.pokemons[self.pokemonatual]['ataques'][self.botao - 1]['nome']}!", True, (0,0,0))
            window.blit(ataque, (50, 475))
            pygame.display.update()
            time.sleep(1)
            if self.efetivo == 'super':
                window.blit(self.lista_imagens[4], (0, 450))
                efetivo = self.fonteBatalha.render(f"It's super effective!", True, (0,0,0))
                window.blit(efetivo, (50, 475))
                pygame.display.update()
                time.sleep(1)
            elif self.efetivo == 'not':
                window.blit(self.lista_imagens[4], (0, 450))
                efetivo = self.fonteBatalha.render(f"It's not very effective...", True, (0,0,0))
                window.blit(efetivo, (50, 475))
                pygame.display.update()
                time.sleep(1)
            if self.crit == True:
                window.blit(self.lista_imagens[4], (0, 450))
                crit = self.fonteBatalha.render(f"A critical hit!", True, (0,0,0))
                window.blit(crit, (50, 475))
                pygame.display.update()
                time.sleep(1)
            if dicionario[self.inimigo_atual]['vida_pokemon'] <= 0:
                self.tela_atual = 'vitória'
            #ATAQUE DO INIMIGO
        if dicionario[self.inimigo_atual]['vida_pokemon'] > 0 and self.iatacou == True and self.tela_atual == 'inimigo':
            window.blit(self.lista_imagens[4], (0, 450))
            ataque1 = self.fonteBatalha.render(f"Foe {dicionario[self.inimigo_atual]['nome']} used {self.ataque_inimigo[1]}!", True, (0,0,0))
            self.pokemons[self.pokemonatual]["vida"] -= self.ataque_inimigo[0]
            window.blit(ataque1, (50, 475))
            pygame.display.update()
            time.sleep(1)
            if self.ataque_inimigo[2] == 'super':
                window.blit(self.lista_imagens[4], (0, 450))
                efetivo = self.fonteBatalha.render(f"It's super effective!", True, (0,0,0))
                window.blit(efetivo, (50, 475))
                pygame.display.update()
                time.sleep(1)
            elif self.ataque_inimigo[2] == 'not':
                window.blit(self.lista_imagens[4], (0, 450))
                efetivo = self.fonteBatalha.render(f"It's not very effective...", True, (0,0,0))
                window.blit(efetivo, (50, 475))
                pygame.display.update()
                time.sleep(1)
            if self.ataque_inimigo[3] == True:
                window.blit(self.lista_imagens[4], (0, 450))
                crit = self.fonteBatalha.render(f"A critical hit!", True, (0,0,0))
                window.blit(crit, (50, 475))
                pygame.display.update()
                time.sleep(1)               
            #ATUALIZA A MORTE DO JOGADOR E TENTA TROCAR DE POKEMON
            if self.pokemons[self.pokemonatual]['vida'] <= 0:
                if self.pokemons[self.pokemonatual]['vida'] < 0:
                    self.pokemons[self.pokemonatual]['vida'] = 0
                window.blit(self.lista_imagens[2], (310, 290))
                window.blit(self.lista_imagens[4], (0, 450))
                morte = self.fonteBatalha.render(f"{self.pokemons[self.pokemonatual]['nome']} Fainted!", True, (0,0,0))
                window.blit(morte, (50, 475))
                blit_jogador = self.fonte.render(f'{self.pokemons[self.pokemonatual]["nome"]}: {self.pokemons[self.pokemonatual]["vida"]}/{self.pokemons[0]["vida_max"]}', True, (0, 0, 0))
                window.blit(blit_jogador, (350, 310))
                pygame.display.update()
                time.sleep(1)
                for i in range(3):
                    if self.pokemons[self.pokemonatual]['vida'] <= 0:
                        if self.pokemonatual == 2:
                            self.pokemonatual = 0
                        else:
                            self.pokemonatual += 1
            self.tela_atual = 'escolhendo'
            self.botao = 1
        #TELA DE ESCOLHA DA BATALHA
        if self.tela_atual == 'escolhendo':
            self.enter_bol = False
            if self.botao != 1 and self.botao != 2:
                self.botao = 1
            self.atacou = False
            window.blit(self.lista_imagens[4], (0, 450))
            text_menu = self.fonteMenu.render('FIGHT', True, (0, 0, 0))
            window.blit(text_menu, (80, 485))
            text_pokemon = self.fonteMenu.render('POKéMON', True, (0, 0, 0))
            window.blit(text_pokemon, (330, 485))
            if self.botao == 1:
                window.blit(self.lista_imagens[3], (40, 505))
            if self.botao == 2:
                window.blit(self.lista_imagens[3], (290, 505))
            pygame.display.update()
            #MORTE DOs POKEMONs DO JOGADOR
        if self.pokemons[0]["vida"] <= 0 and self.pokemons[1]["vida"] <= 0 and self.pokemons[2]["vida"] <= 0 and self.tela_atual != 'fim':
            dicionario[0]['vida_pokemon'] = dicionario[0]['vida_max']
            if len(dicionario) > 1:
                dicionario[1]['vida_pokemon'] = dicionario[1]['vida_max']
            if len(dicionario) > 2:
                dicionario[2]['vida_pokemon'] = dicionario[2]['vida_max']
            self.tela_atual = 'fim'
            self.inimigo_atual = 0
            self.pokemonatual = 0
            self.pokemons[1]['ataques'][1]['dano'] = 20
        #ESCREVE OS ATAQUES DO JOGADOR
        elif self.tela_atual == 'batalha':
            window.blit(self.lista_imagens[0], (0, 450))
            ataque1 = self.fonteBatalha.render(self.pokemons[self.pokemonatual]['ataques'][0]['nome'], True, (0,0,0))
            ataque2 = self.fonteBatalha.render(self.pokemons[self.pokemonatual]['ataques'][1]['nome'], True, (0,0,0))
            ataque3 = self.fonteBatalha.render(self.pokemons[self.pokemonatual]['ataques'][2]['nome'], True, (0,0,0))
            ataque4 = self.fonteBatalha.render(self.pokemons[self.pokemonatual]['ataques'][3]['nome'], True, (0,0,0))
            window.blit(ataque1, (40, 475))
            window.blit(ataque2, (220, 475))
            window.blit(ataque3, (220, 525))
            window.blit(ataque4, (40, 525))
            if self.botao == 1:
                window.blit(self.lista_imagens[5], (20, 488))
            elif self.botao == 2:
                window.blit(self.lista_imagens[5], (200, 488))
            elif self.botao == 3:
                window.blit(self.lista_imagens[5], (200, 538))
            elif self.botao == 4:
                window.blit(self.lista_imagens[5], (20, 538))
            if self.botao == 1:
                pps = self.pokemons[self.pokemonatual]['ataques'][0]['pps']
                pps = self.fonteBatalha.render(f'{pps}', True, (0,0,0))
                window.blit(pps, (520, 475))
            elif self.botao == 2:
                pps = self.pokemons[self.pokemonatual]['ataques'][1]['pps']
                pps = self.fonteBatalha.render(f'{pps}', True, (0,0,0))
                window.blit(pps, (520, 475))
            elif self.botao == 3:
                pps = self.pokemons[self.pokemonatual]['ataques'][2]['pps']
                pps = self.fonteBatalha.render(f'{pps}', True, (0,0,0))
                window.blit(pps, (520, 475))
            elif self.botao == 4:
                pps = self.pokemons[self.pokemonatual]['ataques'][3]['pps']
                pps = self.fonteBatalha.render(f'{pps}', True, (0,0,0))
                window.blit(pps, (520, 475))
        #FINALIZA A BATALHA
        if self.tela_atual == 'vitória':
            window.blit(self.lista_imagens[4], (0, 450))
            morte = self.fonteBatalha.render(f"Foe {dicionario[self.inimigo_atual]['nome']} Fainted!", True, (0,0,0))
            window.blit(morte, (50, 475))
            pygame.display.update()
            time.sleep(1)
            self.tela_atual = 'escolhendo'
        self.inimigo_compara = dicionario[self.inimigo_atual]['vida_max']

    def botoes_batalha(self, event, dicionario, window):
        '''
            Função que recebe os eventos e atualiza os estados da batalha.
        '''
        #MOVE A SETA INDICANDO O ATAQUE SELECIONADO
        if event.type == pygame.KEYDOWN and self.botao == 1 and event.key == pygame.K_RIGHT:
            self.botao = 2
        elif event.type == pygame.KEYDOWN and self.botao == 1 and event.key == pygame.K_DOWN:
            self.botao = 4
        elif event.type == pygame.KEYDOWN and self.botao == 2 and event.key == pygame.K_LEFT:
            self.botao = 1
        elif event.type == pygame.KEYDOWN and self.botao == 2 and event.key == pygame.K_DOWN:
            self.botao = 3
        elif event.type == pygame.KEYDOWN and self.botao == 3 and event.key == pygame.K_LEFT:
            self.botao = 4
        elif event.type == pygame.KEYDOWN and self.botao == 3 and event.key == pygame.K_UP:
            self.botao = 2
        elif event.type == pygame.KEYDOWN and self.botao == 4 and event.key == pygame.K_RIGHT:
            self.botao = 3
        elif event.type == pygame.KEYDOWN and self.botao == 4 and event.key == pygame.K_UP:
            self.botao = 1
        #UTILIZA O ATAQUE PRESIONADO
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and self.botao == 1 and self.pokemons[self.pokemonatual]['ataques'][0]['pps'] > 0 and self.atacou == False:
            self.jogador_ataca(dicionario, 0)
            self.animacao_ataques(0)
            self.atacou == True
            self.iatacou = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and self.botao == 2 and self.pokemons[self.pokemonatual]['ataques'][1]['pps'] > 0 and self.atacou == False:
            self.jogador_ataca(dicionario, 1)
            self.animacao_ataques(1)
            self.atacou == True
            self.iatacou = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and self.botao == 3 and self.pokemons[self.pokemonatual]['ataques'][2]['pps'] > 0 and self.atacou == False:
            self.jogador_ataca(dicionario, 2)
            self.animacao_ataques(2)
            self.atacou == True
            self.iatacou = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and self.botao == 4 and self.pokemons[self.pokemonatual]['ataques'][3]['pps'] > 0 and self.atacou == False:
            self.jogador_ataca(dicionario, 3)
            self.animacao_ataques(3)
            self.atacou == True
            self.iatacou = False
    def animacao_ataques(self, num):
            '''
                Função que atualiza o estado de qual ataque foi utilizado.
            '''
            if self.pokemons[self.pokemonatual]['ataques'][num]['nome'] == 'Sludge Bomb':
                self.sludge_bol = True
                self.tela_atual = 'animando'
            elif self.pokemons[self.pokemonatual]['ataques'][num]['nome'] == 'Thunderbolt':
                self.thunder_bol = True
                self.tela_atual = 'animando'
            elif self.pokemons[self.pokemonatual]['ataques'][num]['nome'] == 'Tackle':
                self.tackle_bol = True
                self.tela_atual = 'animando'
            elif self.pokemons[self.pokemonatual]['ataques'][num]['nome'] == 'Cut':
                self.cut_bol = True
                self.tela_atual = 'animando'
            elif self.pokemons[self.pokemonatual]['ataques'][num]['nome'] == 'Earthquake':
                self.earthquake_bol = True
                self.tela_atual = 'animando'
            elif self.pokemons[self.pokemonatual]['ataques'][num]['nome'] == 'Razor Leaf':
                self.leaf_bol = True
                self.tela_atual = 'animando'
            elif self.pokemons[self.pokemonatual]['ataques'][num]['nome'] == 'Facade':
                self.facade_bol = True
                self.tela_atual = 'animando'
            elif self.pokemons[self.pokemonatual]['ataques'][num]['nome'] == 'Slam':
                self.slam_bol = True
                self.tela_atual = 'animando'
            elif self.pokemons[self.pokemonatual]['ataques'][num]['nome'] == 'Metal Claw':
                self.metal_bol = True
                self.tela_atual = 'animando'
            elif self.pokemons[self.pokemonatual]['ataques'][num]['nome'] == 'Fury Cutter':
                self.fcut_bol = True
                self.tela_atual = 'animando'
    def inimigo_ataca(self,dicionario):
        '''
            Função que comporta a lógica de batalha dos inimigos e atualiza o estado dos danos deles.
        '''
        #LÓGICA DE BATALHA DOS INIMIGOS
        crit = False
        probab = random.random()
        efetivo = ''
        if dicionario[self.inimigo_atual]['nome'] == 'MAKUHITA':
            dano = dicionario[self.inimigo_atual]['ataques'][0]['dano']
            nome = dicionario[self.inimigo_atual]['ataques'][0]['nome']
            self.itackle_bol = True
            if self.pokemons[self.pokemonatual]['nome'] == 'SCIZOR':
                dano //= 2
                efetivo = 'not'
        elif dicionario[self.inimigo_atual]['nome'] == 'MACHOKE':
            if probab < 0.5:
                dano = dicionario[self.inimigo_atual]['ataques'][0]['dano']
                nome = dicionario[self.inimigo_atual]['ataques'][0]['nome']
                self.ikarate_bol = True
            else:
                dano = dicionario[self.inimigo_atual]['ataques'][1]['dano']
                nome = dicionario[self.inimigo_atual]['ataques'][1]['nome']
                self.ifacade_bol = True
            if self.pokemons[self.pokemonatual]['nome'] == 'SCIZOR' and nome == 'Facade':
                dano //= 2
                efetivo = 'not'
            elif self.pokemons[self.pokemonatual]['nome'] == 'VENUSAUR' and nome == 'Karate Chop':
                dano //= 2
                efetivo = 'not'
        elif dicionario[self.inimigo_atual]['nome'] == 'MEDITITE':
            dano = dicionario[self.inimigo_atual]['ataques'][0]['dano']
            nome = dicionario[self.inimigo_atual]['ataques'][0]['nome']
            self.ipsybeam_bol = True
            if self.pokemons[self.pokemonatual]['nome'] == 'SCIZOR':
                dano //= 2
                efetivo = 'not'
            elif self.pokemons[self.pokemonatual]['nome'] == 'VENUSAUR':
                dano *= 2
                efetivo = 'super'
        elif dicionario[self.inimigo_atual]['nome'] == 'MEDICHAM':
            if dicionario[self.inimigo_atual]['vida_pokemon'] < 130:
                if probab < 0.75:
                    dano = dicionario[self.inimigo_atual]['ataques'][0]['dano']
                    nome = dicionario[self.inimigo_atual]['ataques'][0]['nome']
                    self.fpunch = True
                else:
                    dano = dicionario[self.inimigo_atual]['ataques'][2]['dano']
                    nome = dicionario[self.inimigo_atual]['ataques'][2]['nome']
                    dicionario[self.inimigo_atual]['vida_pokemon'] += 140
                    self.recover = True
            else:
                if probab < 0.65:
                    dano = dicionario[self.inimigo_atual]['ataques'][0]['dano']
                    nome = dicionario[self.inimigo_atual]['ataques'][0]['nome']
                    self.fpunch = True
                else:
                    dano = dicionario[self.inimigo_atual]['ataques'][1]['dano']
                    nome = dicionario[self.inimigo_atual]['ataques'][1]['nome']
                    self.ipsybeam_bol = True
            if self.pokemons[self.pokemonatual]['nome'] == 'SCIZOR' and nome == 'Fire Punch':
                dano *= 4
                efetivo = 'super'
            elif self.pokemons[self.pokemonatual]['nome'] == 'VENUSAUR' and nome == 'Fire Punch':
                dano *= 2
                efetivo = 'super'
            elif self.pokemons[self.pokemonatual]['nome'] == 'VENUSAUR' and nome == 'Psybeam':
                dano *= 2
                efetivo = 'super'
            elif self.pokemons[self.pokemonatual]['nome'] == 'SCIZOR' and nome == 'Psybeam':
                dano //= 2
                efetivo = 'not'
        elif dicionario[self.inimigo_atual]['nome'] == 'MACHOP':
            dano = dicionario[self.inimigo_atual]['ataques'][0]['dano']
            nome = dicionario[self.inimigo_atual]['ataques'][0]['nome']
            self.ikarate_bol = True
            if self.pokemons[self.pokemonatual]['nome'] == 'VENUSAUR':
                dano //= 2
                efetivo = 'not'
        elif dicionario[self.inimigo_atual]['nome'] == 'HARIYAMA':
            if self.pokemons[self.pokemonatual]['nome'] == 'PIKACHU':
                dano = dicionario[self.inimigo_atual]['ataques'][1]['dano']
                nome = dicionario[self.inimigo_atual]['ataques'][1]['nome']
                self.iearthquake_bol = True
            elif probab < 0.45:
                dano = dicionario[self.inimigo_atual]['ataques'][0]['dano']
                nome = dicionario[self.inimigo_atual]['ataques'][0]['nome']
                self.ikarate_bol = True
            else:
                dano = dicionario[self.inimigo_atual]['ataques'][1]['dano']
                nome = dicionario[self.inimigo_atual]['ataques'][1]['nome']
                self.iearthquake_bol = True
            if self.pokemons[self.pokemonatual]['nome'] == 'PIKACHU' and nome == 'Earthquake':
                dano *= 2
                efetivo = 'super'
            elif self.pokemons[self.pokemonatual]['nome'] == 'VENUSAUR' and nome == 'Karate Chop':
                dano //= 2
                efetivo = 'not'
        elif dicionario[self.inimigo_atual]['nome'] == 'HERACROSS':
            if probab < 0.75:
                dano = dicionario[self.inimigo_atual]['ataques'][0]['dano']
                nome = dicionario[self.inimigo_atual]['ataques'][0]['nome']
                self.horn_bol = True
            else:
                dano = dicionario[self.inimigo_atual]['ataques'][1]['dano']
                nome = dicionario[self.inimigo_atual]['ataques'][1]['nome']
                self.icut_bol = True
            if self.pokemons[self.pokemonatual]['nome'] == 'SCIZOR':
                dano //= 2
                efetivo = 'not'
        elif dicionario[self.inimigo_atual]['nome'] == 'MACHAMP':
            if self.pokemons[self.pokemonatual]['nome'] == 'SCIZOR':
                dano = dicionario[self.inimigo_atual]['ataques'][0]['dano']
                nome = dicionario[self.inimigo_atual]['ataques'][0]['nome']
                self.fpunch = True
            elif probab < 0.45:   
                dano = dicionario[self.inimigo_atual]['ataques'][0]['dano']
                nome = dicionario[self.inimigo_atual]['ataques'][0]['nome']
                self.fpunch = True
            elif self.pokemons[self.pokemonatual]['nome'] != 'VENUSAUR':
                dano = dicionario[self.inimigo_atual]['ataques'][1]['dano']
                nome = dicionario[self.inimigo_atual]['ataques'][1]['nome']
                self.dchop_bol = True
            else:
                dano = dicionario[self.inimigo_atual]['ataques'][2]['dano']
                nome = dicionario[self.inimigo_atual]['ataques'][2]['nome']
                self.ifacade_bol = True
            if self.pokemons[self.pokemonatual]['nome'] == 'SCIZOR' and nome == 'Fire Punch':
                dano *= 4
                efetivo = 'super'
            elif self.pokemons[self.pokemonatual]['nome'] == 'VENUSAUR' and nome == 'Fire Punch':
                dano *= 2
                efetivo = 'super'
        crit = random.random()
        if crit <= 0.0416:
            dano *= 1.5
            crit = True
        return int(dano), nome, efetivo, crit
    
    def jogador_ataca(self, dicionario, ataque):
        '''
            Função que desenha a imagem do mapa armazenada no init da classe.
        '''
        #ALTERA O DANO DO ATAQUE SE ALGUMAS CONDIÇÕES FOREM VERDADEIRAS
        self.crit = random.random()
        qual_ataque = self.pokemons[self.pokemonatual]['ataques'][ataque]
        dano = qual_ataque['dano']
        if qual_ataque['nome'] == 'Fury Cutter':
            if self.pokemons[1]['ataques'][1]['dano'] < 160:
                self.pokemons[1]['ataques'][1]['dano'] *= 2
        else:
            self.pokemons[1]['ataques'][1]['dano'] = 20
        if qual_ataque['tipo'] == 'grama':
            if dicionario[self.inimigo_atual]['nome'] == 'HERACROSS':
                dano //= 2
                self.efetivo = 'not'
        elif qual_ataque['tipo'] == 'terra':
            if dicionario[self.inimigo_atual]['nome'] == 'HERACROSS':
                dano //= 2
                self.efetivo = 'not'
        elif qual_ataque['tipo'] == 'inseto':
            if dicionario[self.inimigo_atual]['nome'] != 'MEDITITE' and dicionario[self.inimigo_atual]['nome'] != 'MEDICHAM':
                dano //= 2
                self.efetivo = 'not'
        else:
            self.efetivo = ''
        if self.crit <= 0.0416:
            dano *= 1.5
            self.crit = True
        else:
            self.crit = False
        if self.enter_bol == False:
            dicionario[self.inimigo_atual]['vida_pokemon'] -= int(dano)
            self.pokemons[self.pokemonatual]['ataques'][ataque]['pps'] -= 1
            self.enter_bol = True