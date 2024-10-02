import pygame
from main import *
from constantes import *

class Tela:
    '''CRIAÇAO DA CLASSE DAS TELAS DO JOGO'''

    def __init__(self, img, itens, porta):
        '''PASSAMOS OS PARAMETROS BASICOS PARA A CRIACAO DAS TELAS DO JOGO'''
        self.img = img
        self.itens = itens
        self.porta = porta
        self.pode_trocar = False
        # self.olha = False
    
    def recebe(self, state, window, assets):

        '''FUNÇAO QUE RECEBE AS INTERAÇOES DO PERSONAGEM COM AS FASES DO JOGO'''

        state['jogador'].anda()
        if pygame.time.get_ticks () - state['primeiro_tempo']> 15*60*1000:
            state ['jogador'].status = 'DERROTA'
            
    
        for ev in pygame.event.get() :
            if ev.type == pygame.QUIT :
                return False

            if ev.type == pygame.KEYDOWN:  # Verifica se o usuario apertou alguma tecla e então altera o estado de movimentacao dele ou o estado de interacao com os itens da tela. 
                if ev.key == pygame.K_UP and not self.porta.esta :  
                    state['jogador'].up_pressed = True 
                    state['jogador'].img = assets['costa']
                if ev.key == pygame.K_DOWN and not self.porta.esta:
                    state['jogador'].down_pressed = True
                    state['jogador'].img = assets['frente']
                if ev.key == pygame.K_LEFT and not self.porta.esta:    # O AND em cada uma das condicoes serve para travar o personagem de se omver caso estiver interagindo com a porta
                    state['jogador'].left_pressed = True
                    state['jogador'].img = assets['ladoe']
                if ev.key == pygame.K_RIGHT and not self.porta.esta:
                    state['jogador'].right_pressed = True
                    state['jogador'].img = assets['ladod']
                if ev.key == pygame.K_KP_ENTER or ev.key==pygame.K_RETURN:
                    if state['jogador'].status == 'menu_principal': #Primeira troca de tela 
                        state['last_enter'] = pygame.time.get_ticks()
                        state['jogador'].status = 'PRIMEIRA FASE'
                        state['jogador'].passou_menu = True
                        state['primeiro_tempo'] = pygame.time.get_ticks()
                    if state['jogador'].status == 'DERROTA' or state['jogador'].status == 'VITORIA':
                        return False
                    


                if self.porta.esta == True: #Verifica se a caixa de interacao com a porta esta aberta e caso esteja reconhece as teclas do teclado e desenha, ou apaga, o texto do usário
                    
                    if ev.key == pygame.K_BACKSPACE:  # Caso o usuario queira apagar 
                         self.porta.user_text =  self.porta.user_text[0:-1]

                    else : # Caso ele queira digitar é adicionado a letra da ultima tecla apertada ao texto que representa a tentativa de senha da porta
                        
                        self.porta.user_text += ev.unicode 
                    
                    if ev.key == pygame.K_KP_ENTER or ev.key==pygame.K_RETURN: # Verifica se o jogador deu enter na senha e também se  a senha está correta, além disso, faz a mudaçca de fases para cada caso 
                        if self.porta.user_text.strip().lower() == self.porta.senha and state['jogador'].status == 'PRIMEIRA FASE' :
                            state['jogador'].status = 'SEGUNDA FASE'
                            state['last_enter'] = pygame.time.get_ticks()
                            state['jogador'].passou_menu = True
                            pygame.mixer.Sound.play(assets['door'])  # Efeito sonoro da porta quando a senha está certa
                            
               
                        elif self.porta.user_text.strip().lower() == self.porta.senha and state['jogador'].status == 'SEGUNDA FASE':
                            state['jogador'].status = 'TERCEIRA FASE'
                            state['jogador'].passou_menu = True
                            state['last_enter'] = pygame.time.get_ticks()
                            pygame.mixer.Sound.play(assets['door']) # Efeito sonoro da porta quando a senha está certa
                           
                        
                        elif self.porta.user_text.strip().lower() == self.porta.senha and state['jogador'].status == 'TERCEIRA FASE':
                            state['jogador'].status = 'VITORIA'
                            pygame.mixer.Sound.play(assets['door']) # Efeito sonoro da porta quando a senha está certa
                            state['tempo_final'] = (pygame.time.get_ticks () - state['primeiro_tempo'])/60000
                            state['tempo_final'] = str(f"{state['tempo_final']:.2f} minutos")

                            
                        self.porta.user_text = ''  # Após a tentativa, caso estiver errado, apaga a qualquer coisa que já estriver escrito na porta 
                        self.porta.esta = False   
                        self.olha = True


                if ev.key == pygame.K_SPACE and state['jogador'].pode_abrir(self.porta) and (self.porta.esta == False): # Verifica se o jogador pode interagir com a porta

                    self.porta.esta = True
                    pygame.mixer.Sound.play(assets['interacao']) # Efeito sonoro das interacoes

                elif ev.key == pygame.K_SPACE and  state['jogador'].pode_abrir(self.porta) and (self.porta.esta == True):
                    self.porta.esta = False
                    


                for item in self.itens:



                


                    if ev.key == pygame.K_SPACE and state['jogador'].pode_abrir(item) and (item.status == False): # Verifica se o jogador pode interagir com intens.
                        
                       
                         
                        item.status = True
                        pygame.mixer.Sound.play(assets['interacao']) # Efeito sonoro das interacoes
                    elif ev.key == pygame.K_SPACE and state['jogador'].pode_abrir(item) and item.status:
                        item.status = False

                    else :
                        item.status = False



            if ev.type == pygame.KEYUP : # Verifica se o usuario soltou alguma tecla e então altera o estado de movimentacao dele. 
                if ev.key == pygame.K_UP :
                    state['jogador'].up_pressed = False
                if ev.key == pygame.K_DOWN :
                    state['jogador'].down_pressed = False
                if ev.key == pygame.K_LEFT :
                    state['jogador'].left_pressed = False
                if ev.key == pygame.K_RIGHT :
                    state['jogador'].right_pressed = False
        

        return True

                

        
class Item :
    '''CRIACAO DA CLASSE DOS ITENS DO JOGO'''
    def __init__(self, img, ponto, dica):  
        '''PASSAMOS TODOS OS PARAMETROS PARA A CRIACAO DOS ITENS'''
        self.img = img
        self.ponto = ponto
        self.larg, self.alt = self.img[0].get_size()
        self.rect = pygame.Rect(ponto, (self.larg, self.alt))
        self.mensagem = dica
        self.status = False




class Porta :
    '''CRICAO DA CLASSE DAS PORTAS DO JOGO'''
    def __init__(self, img, ponto, mensagem,mensagem2, senha):
        '''PASSAMOS TODOS OS PARAMETROS PARA A CRIACAO DAS PORTAS'''
        self.mensagem = mensagem
        self.mensagem2 = mensagem2
        self.senha = senha
        self.img = img
        self.ponto = ponto 
        self.esta = False
        self.user_text = ''
        self.larg, self.alt = self.img.get_size()
        self.rect = pygame.Rect(ponto, (self.larg, self.alt+20))


    def desenha (self, window, fase, portas): 
        '''DESENHA A TELA DE INTERACAO COM AS PORTAS'''
        pygame.draw.rect(window, AZULESCURO, (390,406,500,320))
        pygame.draw.rect(window, BLACK,  (400,416, 480,300))
        pygame.draw.rect(window, WHITE, (410,646,460 ,40))
        text_digite_senha = PORTAFONT.render(portas[fase].mensagem, True, WHITE)
        text_digite_senha2=PORTAFONT.render(portas[fase].mensagem2, True, WHITE)
        text_user = PORTAFONT.render(portas[fase].user_text, True, BLACK)
        window.blit(text_digite_senha, (420, 450))
        window.blit(text_digite_senha2, (420, 606))
        window.blit(text_user, (420,656))
        pygame.display.flip()


    



class Player(pygame.sprite.Sprite) :
    '''CRIACAO DA CLASSE DO JOGADOR'''
    def __init__(self, x, y):
        '''PASSAMOS OS PARAMETROS PARA A CRICAO DO JOGADOR'''
        self.pos_x = x
        self.pos_y = y
        self.vel = 10
        self.left_pressed = False 
        self.right_pressed = False 
        self.up_pressed = False 
        self.down_pressed = False 
        self.status = 'menu_principal'
        self.passou_menu = False
        self.tempo_sprite = 0
        self.estado_sprite = 0

        larg, alt = (60,40)
        self.rect = pygame.Rect((self.pos_x,self.pos_y), (larg, alt))

    def anda (self):
        '''FUNCAO QUE PERMITE A ATUALIZACAO DA POSICAO DO JOGADOR NA TELA'''
        
        
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
        '''FUNCAO QUE DESENHA O JOGADOR NA TELA'''


        tempo_desconto = pygame.time.get_ticks() #Controle de tempo para a animacao do personagem

        # Condicoes para altear as imagens do jogador a depender da direcao em que ele esta andando e elas seguem o mesmo padrao de alternancia entre imagens porem mudam as imagens a depender da direcao 
        if self.left_pressed and not self.right_pressed:
            window.blit(assets['ladoe'][self.estado_sprite], (self.pos_x, self.pos_y))
            if tempo_desconto - self.tempo_sprite  > 750: #Condicao que depende do tempo para altear a imagem do jogador e fazer a animacao
                if self.estado_sprite <2:
                    self.estado_sprite +=1
                else:
                    self.estado_sprite = 0
        
        elif self.right_pressed and not self.left_pressed:
            window.blit(assets['ladod'][self.estado_sprite], (self.pos_x, self.pos_y))
            if tempo_desconto - self.tempo_sprite  > 750:
                if self.estado_sprite <2:
                    self.estado_sprite +=1
                else:
                    self.estado_sprite = 0
        elif self.up_pressed and not self.down_pressed:
            window.blit(assets['costa'][self.estado_sprite], (self.pos_x, self.pos_y))
            if tempo_desconto - self.tempo_sprite  > 750:
                if self.estado_sprite <2:
                    self.estado_sprite +=1
                else:
                    self.estado_sprite = 0
        elif self.down_pressed and not self.up_pressed:
            window.blit(assets['frente'][self.estado_sprite], (self.pos_x, self.pos_y))
            if tempo_desconto - self.tempo_sprite  > 750:
                if self.estado_sprite <2:
                    self.estado_sprite +=1
                else:
                    self.estado_sprite = 0
        else:

            window.blit(assets['frente'][0], (self.pos_x, self.pos_y))


    def pode_abrir (self, item):

        '''FUNCAO QUE VERIFICA SE O JOGADOR PODE INTERAGIR COM O ITEM'''

        if pygame.Rect.colliderect(item.rect, self.rect) : #Verifica a colicao do jogador com o item na tela para saber se ele está na area para a interaçao ou nao
            return True
        return False
