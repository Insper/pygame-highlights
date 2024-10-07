import pygame
import os
import random
import math

class Zero():
    """
    Classe que representa o botão 0 da roleta
    """
    def __init__(self, x, y, value, window):
        self.x = x
        self.y = y
        self.value = value
        self.rect = pygame.rect.Rect(x, y, 36, 116)
        self.window = window
        
        self.font = pygame.font.Font(pygame.font.get_default_font(), 16)
    
    def desenha(self, isBlack):
        """
        Desenha o botão 0 da roleta
        """
        pygame.draw.rect(self.window, (0, 255, 0), self.rect)
        self.drawText(str(self.value), self.x + (18 - 6), self.y + (58 - 6), self.font, (0, 0, 0))

    def drawText(self, text, x, y, font, color):
        """
        Desenha um texto no centro do botão
        """
        text_surface = font.render(text, True, color)
        self.window.blit(text_surface, (x, y))

class Column():
    """
    Classe para representar as colunas da roleta
    """
    def __init__(self, x, y, text, value, window):
        self.x = x
        self.y = y
        self.value = value
        self.rect = pygame.rect.Rect(x, y, 72, 36)
        self.window = window
        self.text = text
        self.font = pygame.font.Font(pygame.font.get_default_font(), 12)
    
    def desenha(self, isBlack):
        """
        Desenha uma coluna da roleta
        """
        pygame.draw.rect(self.window, (0, 0, 0), self.rect)
        self.drawText(str(self.text), self.x + (36 - 12), self.y + (18 - 6), self.font, (255, 255, 255))

    def drawText(self, text, x, y, font, color):
        """
        Desenha um texto no centro do botão
        """
        text_surface = font.render(text, True, color)
        self.window.blit(text_surface, (x, y))

class Dozens():
    """
    Classe para representar as dúzias da roleta
    """
    def __init__(self, x, y, text, value, window):
        self.x = x
        self.y = y
        self.value = value
        self.rect = pygame.rect.Rect(x, y, 147, 36)
        self.window = window
        self.text = text
        self.font = pygame.font.Font(pygame.font.get_default_font(), 14)
    
    def desenha(self, isBlack):
        """
        Desenha a dúzia da roleta
        """
        pygame.draw.rect(self.window, (0, 0, 0), self.rect)
        self.drawText(str(self.text), self.x + ((147 // 2) - 12 - (len(self.text))), self.y + (18 - 6), self.font, (255, 255, 255))

    def drawText(self, text, x, y, font, color):
        """
        Desenha um texto no centro do botão
        """
        text_surface = font.render(text, True, color)
        self.window.blit(text_surface, (x, y))
class Buttons():
    """
    Classe para representar os botões da roleta
    """
    def __init__(self, x, y, value, window):
        self.x = x
        self.y = y
        self.value = value
        self.rect = pygame.rect.Rect(x, y, 36, 36)
        self.window = window
        self.font = pygame.font.Font(pygame.font.get_default_font(), 12)
    
    def desenha(self, isBlack):
        """
        Desenha o botão da roleta
        """
        if isBlack:
            pygame.draw.rect(self.window, (0, 0, 0), self.rect)
        else:
            pygame.draw.rect(self.window, (255, 0, 0), self.rect)
        self.drawText(str(self.value), self.x + (18 - 6), self.y + (18 - 6), self.font, (255, 255, 255))

    def drawText(self, text, x, y, font, color):
        """
        Desenha um texto no centro do botão
        """
        text_surface = font.render(text, True, color)
        self.window.blit(text_surface, (x, y))

class ColorButtons():
    """
    Classe para representar os botões de vermelho e preto da roleta
    """
    def __init__(self, x, y, text, value, window):
        self.x = x
        self.y = y
        self.value = value
        self.rect = pygame.rect.Rect(x, y, 147, 36)
        self.window = window
        self.text = text
        self.font = pygame.font.Font(pygame.font.get_default_font(), 14)
    
    def desenha(self, isBlack):
        """
        Desenha os botões coloridos da roleta
        """
        if self.value[1] == 'vermelho':
            pygame.draw.rect(self.window, (255, 0, 0), self.rect)
            self.drawText(str(self.text), self.x + ((147 // 2) - 20 - (len(self.text))), self.y + (18 - 6), self.font, (255, 255, 255))
        else:
            pygame.draw.rect(self.window, (0, 0, 0), self.rect)
            self.drawText(str(self.text), self.x + ((147 // 2) - 12 - (len(self.text))), self.y + (18 - 6), self.font, (255, 255, 255))

    def drawText(self, text, x, y, font, color):
        """
        Desenha um texto no centro do botão
        """
        text_surface = font.render(text, True, color)
        self.window.blit(text_surface, (x, y))

class JogarButton():
    """
    Classe para representar o botão de jogar da roleta
    """
    def __init__(self, x, y, text, value, window):
        self.x = x
        self.y = y
        self.value = value
        self.radius = 50
        self.window = window
        self.text = text
        self.font = pygame.font.Font(pygame.font.get_default_font(), 18)
        self.rect = pygame.rect.Rect(x - self.radius, y - self.radius, self.radius * 2, self.radius * 2)

    def desenha(self, isBlack):
        """
        Desenha o botão de jogar da roleta
        """
        pygame.draw.circle(self.window, (0, 0, 0), (self.x, self.y), self.radius)  # Desenha um círculo preto
        if not isBlack:
            pygame.draw.circle(self.window, (255, 0, 0), (self.x, self.y), self.radius - 5)  # Desenha um círculo vermelho menor no centro
        else:
            pygame.draw.circle(self.window, (0, 0, 0), (self.x, self.y), self.radius - 5)  # Desenha um círculo vermelho menor no centro
        self.drawText(self.text, self.x, self.y, self.font, (255, 255, 255))  # Centraliza o texto no centro do botão

    def drawText(self, text, x, y, font, color):
        """
        Desenha um texto no centro do botão
        """
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        self.window.blit(text_surface, text_rect)

class Roleta:
    """
    Classe para representar a roleta
    """
    def __init__(self, window):
        """
        Inicializa a roleta
        """
        self.window = window
        self.originalImage = pygame.transform.scale(pygame.image.load(os.path.join('images', 'objs', 'roleta.png')), (400, 400))
        self.roleta = pygame.transform.scale(pygame.image.load(os.path.join('images', 'objs', 'roleta.png')), (400, 400))
        self.roletaAngle = 0
        self.columns = [[1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34], [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35], [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]]
        self.dozens = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]]
        self.roulleteOrder = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]
        self.blackNumbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
        self.redNumbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        self.ballPos = [640, 250]
        self.isPlaying = False
        self.bets = []
        self.lastUptaded = 0
        self.actualAngle = 0
        self.expectedAngle = 1440
        self.sortedNumber = 0
        self.sorted = False
        self.radio = 150
        self.jogar = JogarButton(1100, 575, 'Jogar', 'Jogar', self.window)
        self.fechar = JogarButton(110, 575, 'Fechar', 'Fechar', self.window)
        self.resetGameButton = ColorButtons((1280 // 2) - 147 // 2, (720 // 2) + 250, 'Reiniciar', 'Reiniciar', self.window)
        self.resultMenu = False
        self.resultMessage = ''
        self.resultGive = False
        self.giveMoney = False
        self.money = 0
        self.sound = pygame.mixer.Sound('musica/bola_roleta.wav')
        self.betsButtons = [
            [Zero(387, 510, 0, self.window)],
            [Buttons(425 + (i * 37), 510, self.columns[2][i], self.window) for i in range(12)],
            [Buttons(425 + (i * 37), 550, self.columns[1][i], self.window) for i in range(12)],
            [Buttons(425 + (i * 37), 590, self.columns[0][i], self.window) for i in range(12)],
            [Column(869, 510, '2 to 1', ['coluna', 3], self.window), Column(869, 550, '2 to 1', ['coluna', 2], self.window), Column(869, 590, '2 to 1', ['coluna', 1], self.window)],
            [Dozens(425, 630, '1 to 12', ['duzia', 1], self.window), Dozens(573, 630, '13 to 24', ['duzia', 2], self.window), Dozens(721, 630, '25 to 36', ['duzia', 3], self.window)],
            [ColorButtons(500, 667, 'Vermelho', ['cor', 'vermelho'], self.window), ColorButtons(650, 667, 'Preto', ['cor', 'preto'], self.window)],
        ]

    def desenha(self):
        """
        Desenha a roleta
        """
        self.window.fill((2, 85, 0))

        roleta_rect = self.roleta.get_rect(center=(640, 250))
        self.window.blit(self.roleta, roleta_rect)
        time = pygame.time.get_ticks()
        if self.resultMessage == '':
            self.drawButtons()
            for number in self.bets:
                    for col in self.betsButtons:
                        for button in col:
                            if button.value == number:
                                pygame.draw.circle(self.window, (255, 255, 255), (button.x + (button.rect[2] // 2), button.y + (button.rect[3] // 2)), 7)
        if not self.isPlaying:
            self.fechar.desenha(True)
            if (time - self.lastUptaded) / 1000 >= 0.01:
                self.lastUptaded = time
                self.roletaAngle += 1
                if self.roletaAngle >= 360:
                    self.roletaAngle = 0
                self.roleta = pygame.transform.rotate(self.originalImage, self.roletaAngle)
            if len(self.bets) > 0:
                self.jogar.desenha(False)
        else:
            if not self.sorted:
                self.sorted = True
                index = random.randint(0, len(self.roulleteOrder) - 1)
                self.sortedNumber = self.roulleteOrder[index]
                if index != 0:
                    self.expectedAngle += (index / 37) * 360
                self.sound.play()
            self.roleta = self.originalImage
            if (time - self.lastUptaded) / 1000 >= 0.001:
                self.lastUptaded = time
                self.actualAngle += 5
                if self.actualAngle >= self.expectedAngle:
                    self.actualAngle = self.expectedAngle
                    if self.radio > 105:
                        self.radio -= 1
                    else:
                        self.sound.stop()
                        self.resultMenu = True
                self.ballPos[0] = 640 + math.sin(math.radians(self.actualAngle)) * self.radio
                self.ballPos[1] = 250 - math.cos(math.radians(self.actualAngle)) * self.radio
                
        pygame.draw.circle(self.window, (255, 255, 255), self.ballPos, 7)

        if self.resultMenu:
            if not self.resultGive:
                self.resultGive = True
                status = False
                winQnt = 0
                for bet in self.bets:
                    if isinstance(bet, int):
                        if bet == self.sortedNumber:
                            status = True
                            winQnt += 10 * 36
                    else:
                        if bet[0] == 'coluna':
                            if self.sortedNumber in self.columns[bet[1] - 1]:
                                status = True
                                winQnt += 10 * 3
                        elif bet[0] == 'duzia':
                            if self.sortedNumber in self.dozens[bet[1] - 1]:
                                status = True
                                winQnt += 10 * 3
                        elif bet[0] == 'cor':
                            if bet[1] == 'vermelho':
                                if self.sortedNumber in self.redNumbers:
                                    status = True
                                    winQnt += 10 * 2
                            else:
                                if self.sortedNumber in self.blackNumbers:
                                    status = True
                                    winQnt += 10 * 2
                if status:
                    self.resultMessage = f'Você ganhou R$ {winQnt:.2f}!'
                    self.money += winQnt
                else:
                    self.resultMessage = f'Você perdeu R${(len(self.bets) * 10):.2f}!'
            font = pygame.font.Font(pygame.font.get_default_font(), 36)
            text_surface = font.render(self.resultMessage, True, (255, 255, 255))
            text_width, text_height = text_surface.get_size()
            x = (1280 - text_width) // 2
            y = ((720 - text_height) // 2) + 200
            self.window.blit(text_surface, (x, y))
            self.resetGameButton.desenha(True)

    def drawButtons(self):
        """
        Desenha os botões da roleta
        """
        for col in self.betsButtons:
            for button in col:
                button.desenha(True if button.value in self.blackNumbers else False)

    def interacoes(self):
        """
        Faz todas as interações do jogo
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not self.isPlaying:
                    for col in self.betsButtons:
                        if self.fechar.rect.collidepoint(event.pos):
                            return False
                        for button in col:
                            if button.rect.collidepoint(event.pos):
                                if button.value not in self.bets:
                                    self.bets.append(button.value)
                                else:
                                    self.bets.remove(button.value)
                                return True
                    if self.jogar.rect.collidepoint(event.pos):
                        self.isPlaying = True
                        self.money = - (len(self.bets) * 10)
                else:
                    if self.resetGameButton.rect.collidepoint(event.pos):
                        self.resetGame()
        return True
    
    def resetGame(self):
        """
        Reseta o jogo
        """
        self.originalImage = pygame.transform.scale(pygame.image.load(os.path.join('images', 'objs', 'roleta.png')), (400, 400))
        self.roleta = pygame.transform.scale(pygame.image.load(os.path.join('images', 'objs', 'roleta.png')), (400, 400))
        self.roletaAngle = 0
        self.ballPos = [640, 250]
        self.isPlaying = False
        self.bets = []
        self.lastUptaded = 0
        self.actualAngle = 0
        self.expectedAngle = 1440
        self.sortedNumber = 0
        self.sorted = False
        self.radio = 150
        self.resultMenu = False
        self.resultMessage = ''
        self.resultGive = False
        self.giveMoney = False
        self.money = 0

if __name__ == '__main__':
    playing = True
    pygame.init()
    window = pygame.display.set_mode((1280, 720), vsync=True, flags=pygame.SCALED)
    roleta = Roleta(window)

    while playing:
        if not roleta.interacoes():
            playing = False
            break

        roleta.desenha()

        pygame.display.update()
        
    pygame.quit()