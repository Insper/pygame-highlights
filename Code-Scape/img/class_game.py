import pygame
from main import *

class Tela:
    def __init__(self, img, itens, porta):
        self.img = img
        self.itens = itens
        self.porta = porta
        self.pode_trocar = False
        self.olha = False
    
    def recebe(self, state, window):

        state['jogador'].anda()
        if pygame.time.get_ticks () - state['primeiro_tempo']> 15*60*1000:
            state ['jogador'].status = 'DERROTA'
            
    
        for ev in pygame.event.get() :
            if ev.type == pygame.QUIT :
                return False

            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_UP :
                    state['jogador'].up_pressed = True 
                if ev.key == pygame.K_DOWN :
                    state['jogador'].down_pressed = True
                if ev.key == pygame.K_LEFT :
                    state['jogador'].left_pressed = True 
                if ev.key == pygame.K_RIGHT :
                    state['jogador'].right_pressed = True
                if ev.key == pygame.K_KP_ENTER or ev.key==pygame.K_RETURN:
                    if state['jogador'].status == 'menu_principal':
                        state['last_enter'] = pygame.time.get_ticks()
                        state['jogador'].status = 'PRIMEIRA FASE'
                        state['jogador'].passou_menu = True
                        state['primeiro_tempo'] = pygame.time.get_ticks()
                    if state['jogador'].status == 'DERROTA' or state['jogador'].status == 'VITORIA':
                        return False
                    


                if self.porta.esta == True:
                    
                    if ev.key == pygame.K_BACKSPACE:
                         self.porta.user_text =  self.porta.user_text[0:-1]

                    else :
                        
                        self.porta.user_text += ev.unicode 
                    
                    if ev.key == pygame.K_KP_ENTER or ev.key==pygame.K_RETURN:
                        if self.porta.user_text.strip().lower() == self.porta.senha and state['jogador'].status == 'PRIMEIRA FASE' :
                            state['jogador'].status = 'SEGUNDA FASE'
                            state['last_enter'] = pygame.time.get_ticks()
                            
                            state['jogador'].passou_menu = True
                            
               
                        elif self.porta.user_text.strip().lower() == self.porta.senha and state['jogador'].status == 'SEGUNDA FASE':
                            state['jogador'].status = 'TERCEIRA FASE'
                            state['jogador'].passou_menu = True
                            # state['jogador'].passou_menu = True
                        
                        elif self.porta.user_text.strip().lower() == self.porta.senha and state['jogador'].status == 'TERCEIRA FASE':
                            state['jogador'].status = 'VITORIA'
                            state['jogador'].passou_menu = True
                            state['tempo_final'] = pygame.time.get_ticks () - state['primeiro_tempo']
                            state['tempo_final'] = str(state['tempo_final'])

                            
                        self.porta.user_text = ''
                        self.porta.esta = False
                        self.olha = True


                if ev.key == pygame.K_SPACE and state['jogador'].pode_abrir(self.porta) and (self.porta.esta == False):

                    self.porta.esta = True

                elif ev.key == pygame.K_SPACE and  state['jogador'].pode_abrir(self.porta) and (self.porta.esta == True):
                    self.porta.esta = False
                    


                for item in self.itens:


                    # if state['jogador'].pode_abrir(item) and (item.status == False):
                    #     if state['jogador'].status == 'menu':
                    #         pygame.draw.circle(window, (0,0,255), (563,400), 10)
                    #         print('entrou2')
                    #         pygame.display.update()

                


                    if ev.key == pygame.K_SPACE and state['jogador'].pode_abrir(item) and (item.status == False):
                        
                        print('entrou')
                        print(item.ponto)
                        state['jogador'].interagir = True 
                        item.status = True
                    elif ev.key == pygame.K_SPACE and state['jogador'].pode_abrir(item) and item.status:
                        item.status = False

                    else :
                        item.status = False



            if ev.type == pygame.KEYUP:
                if ev.key == pygame.K_UP :
                    state['jogador'].up_pressed = False
                if ev.key == pygame.K_DOWN :
                    state['jogador'].down_pressed = False
                if ev.key == pygame.K_LEFT :
                    state['jogador'].left_pressed = False
                if ev.key == pygame.K_RIGHT :
                    state['jogador'].right_pressed = False
        # if self.olha:
        #     if self.porta.user_text.strip() == self.porta.senha and state['jogador'].status == 'menu' :
        #         state['jogador'].status = 'tela_inicial'
        #         self.porta.esta = False
               
        #     elif self.porta.user_text.strip() == self.porta.senha and state['jogador'].status == 'tela_inicial':
        #         state['jogador'].status = 'menu'
        #         self.porta.esta = False
                
        self.olha = False

        return True

                

        
class Item :
    def __init__(self, img, ponto, dica):
        self.img = img
        self.ponto = ponto
        self.larg, self.alt = self.img.get_size()
        self.rect = pygame.Rect(ponto, (self.larg, self.alt))
        self.mensagem = dica
        self.status = False


class Porta :
    def __init__(self, img, ponto, mensagem,mensagem2, senha):
        self.mensagem = mensagem
        self.mensagem2 = mensagem2
        self.senha = senha
        self.img = img
        self.ponto = ponto 
        self.esta = False
        self.user_text = ''
        self.larg, self.alt = self.img.get_size()
        self.rect = pygame.Rect(ponto, (self.larg, self.alt+20))


    



class Player :
    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y
        self.vel = 10
        self.left_pressed = False 
        self.right_pressed = False 
        self.up_pressed = False 
        self.down_pressed = False 
        self.interagir = False
        self.status = 'TERCEIRA FASE'
        self.passou_menu = False

        larg, alt = (60,40)
        self.rect = pygame.Rect((self.pos_x,self.pos_y), (larg, alt))

    def anda (self):
        
        
        self.velx = 0
        self.vely = 0

        if self.pos_x < 0:
            self.pos_x = 0
        if self.pos_x > 1112:
            self.pos_x = 1112
        if self.pos_y < 88 :
            self.pos_y = 88 
        if self.pos_y > 804:
            self.pos_y = 804

        if self.pos_x >= 0 and self.pos_x <= 1112 and self.pos_y >= 0 and self.pos_y <= 804:
        

            if self.left_pressed and not self.right_pressed:
                self.velx = -self.vel
            if self.right_pressed and not self.left_pressed:
                self.velx = +self.vel
            if self.up_pressed and not self.down_pressed:
                self.vely = -self.vel
            if self.down_pressed and not self.up_pressed:
                self.vely = +self.vel



            self.pos_x += self.velx
            self.pos_y += self.vely
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y


                



    def desenha(self, window, assets):
        window.blit(assets['player'], (self.pos_x, self.pos_y))


    def pode_abrir (self, item):

        if pygame.Rect.colliderect(item.rect, self.rect) :
            return True
        return False
