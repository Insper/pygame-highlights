import pygame
from random import randint

class Horse():
    def __init__(self, window, x, y, speed, index):
        self.window = window
        self.hourse = pygame.transform.scale(pygame.image.load(f'images/horses/{index}.png'), (60,60))
        self.x = x
        self.y = y
        self.speed = speed
        self.index = index

    def desenha(self):
        self.window.blit(self.hourse, (self.x, self.y))

    def movimenta(self, delta):
        self.x += self.speed * delta

class BetButton():
    def __init__(self, window, x, y, index):
        self.window = window
        self.button = pygame.rect.Rect(x - 30, y, 120, 30)
        self.x = x
        self.y = y
        self.index = index

    def desenha(self):
        pygame.draw.rect(self.window, (255, 255, 255), self.button)
        font = pygame.font.Font(pygame.font.get_default_font(), 20)
        text_surface = font.render(f'Cavalo {self.index}', True, (0, 0, 0))
        x = self.x + (self.button.width // 2) - (text_surface.get_width() // 2) - 30
        y = self.y + (self.button.height // 2) - (text_surface.get_height() // 2)
        self.window.blit(text_surface, (x, y))

class HorseRace():
    def __init__(self, window):
        self.isInBetMenu = True
        self.window = window
        self.horses = [Horse(self.window, 100, i * 100, randint(100, 120), i) for i in range(1, 3)]
        self.horses2 = (Horse(self.window, 100, i * 100 + 125, randint(100, 120), i) for i in range(3, 5))
        self.horses += self.horses2
        self.horseWinner = None
        self.lastTick = 0
        self.messageWinner = ''
        self.bet = 0
        self.font = pygame.font.Font(pygame.font.get_default_font(), 20)
        self.horsesBets = [Horse(self.window, 250 * i, 330, 0, i) for i in range(1, 5)]
        self.betsButton = [BetButton(self.window, 250 * i, 400, i) for i in range(1, 5)]
        self.playButton = pygame.rect.Rect((1280 // 2) - 60, 720 // 1.25, 120, 30)
        self.background = pygame.transform.scale(pygame.image.load('images/horserace.png'), (1280,720))
        self.resetButton = pygame.rect.Rect((1280 // 2) - 60, 720 // 2 + 150, 120, 60)
        self.giveMoney = False
        self.money = 0
        self.podiumImage = pygame.image.load('images/horse_race/podio.png')
        self.podium = []
        self.showPodium = False
        self.podiumHorses = []
        self.addHorses = False

    def desenha(self):
        self.window.fill((0,0,0))
        moneyRect = pygame.rect.Rect(0, 0, 175, 35)
        pygame.draw.rect(self.window, (255, 255, 255), moneyRect)
        tick = pygame.time.get_ticks()
        delta = (tick - self.lastTick) / 1000
        self.lastTick = tick
        if not self.isInBetMenu:
            self.window.blit(self.background, (0, 0))
            moneyRect = pygame.rect.Rect(0, 0, 175, 35)
            pygame.draw.rect(self.window, (255, 255, 255), moneyRect)
            for horse in self.horses:
                horse.desenha()
                horse.movimenta(delta)
                if horse.x >= 1200:
                    if not horse.index in self.podium:
                        self.podium.append(horse.index)
                    if len(self.podium) == 4 and not self.addHorses:
                        self.showPodium = True
                        self.podiumHorses = [Horse(self.window, (1280 // 2) - 15, 278, 0, self.podium[0]), Horse(self.window, (1280 // 2) - 117, 300, 0, self.podium[1]), Horse(self.window, (1280 // 2) + 85, 318, 0, self.podium[2])]
                    if self.messageWinner == '':
                        if horse.index == self.bet:
                            self.money = 400
                        else:
                            self.money = -100
                        self.messageWinner = f'O cavalo {horse.index} ganhou! Você ganhou R$ 400,00' if horse.index == self.bet else f'O cavalo {horse.index} ganhou! Você perdeu R$ 100,00'
                    horse.x = 1200
            if self.showPodium:
                self.window.fill((0,0,0))
                moneyRect = pygame.rect.Rect(0, 0, 175, 35)
                pygame.draw.rect(self.window, (255, 255, 255), moneyRect)
                font = pygame.font.Font(pygame.font.get_default_font(), 36)
                text_surface = font.render(self.messageWinner, True, (255, 255, 255))
                x =  (1280 // 2) - (text_surface.get_width() // 2)
                y = (720 // 2) - (text_surface.get_height() // 2) - 150
                self.window.blit(text_surface, (x, y))
                self.window.blit(self.podiumImage, ((1280 // 2 )- (350 // 2), (720 // 2) - (350 // 2)))
                if self.messageWinner != '':
                    pygame.draw.rect(self.window, (255, 255, 255), self.resetButton)
                    text_surface = self.font.render(f'Reiniciar', True, (0, 0, 0))
                    x = (1280 // 2) - 60 + (self.resetButton.width // 2) - (text_surface.get_width() // 2)
                    y = 720 // 2 + 150 + (self.resetButton.height // 2) - (text_surface.get_height() // 2)
                    self.window.blit(text_surface, (x, y))
                    for horse in self.podiumHorses:
                        horse.desenha()
            if self.horses[0].x >= 600 and self.horseWinner == None:
                self.horseWinner = randint(0, 4)
                self.horses[self.horseWinner - 1].speed += (120 - self.horses[self.horseWinner - 1].speed) + 30
        else:
            for horse in self.horsesBets:
                horse.desenha()
            for button in self.betsButton:
                button.desenha()
                if button.index == self.bet:
                    pygame.draw.circle(self.window, (0, 0, 0), (button.x - 30 + (button.button[2] // 2), button.y + (button.button[3] // 2)), 7)
            font = pygame.font.Font(pygame.font.get_default_font(), 36)
            text_surface = font.render(f'Seja bem vindo a corrida de cavalo', True, (255, 255, 255))
            x =  (1280 // 2) - (text_surface.get_width() // 2)
            y = (720 // 5) - (text_surface.get_height() // 2)
            self.window.blit(text_surface, (x, y))
            text_surface = self.font.render(f'Para apostar em um cavalo, clique no botão embaixo dele.', True, (255, 255, 255))
            x =  (1280 // 2) - (text_surface.get_width() // 2)
            y = (720 // 3.5) - (text_surface.get_height() // 2)
            self.window.blit(text_surface, (x, y))
            if self.bet != 0:
                text_surface = self.font.render(f'Você está apostando no cavalo {self.bet}', True, (255, 255, 255))
                x =  (1280 // 2) - (text_surface.get_width() // 2)
                y = (720 // 1.35) - (text_surface.get_height() // 2)
                self.window.blit(text_surface, (x, y))
                pygame.draw.rect(self.window, (255, 255, 255), self.playButton)
                text_surface = self.font.render(f'Jogar', True, (0, 0, 0))
                x = (1280 // 2) - 60 + (self.playButton.width // 2) - (text_surface.get_width() // 2)
                y = 720 // 1.25 + (self.playButton.height // 2) - (text_surface.get_height() // 2)
                self.window.blit(text_surface, (x, y))

    def resetGame(self):
        self.isInBetMenu = True
        self.horses = [Horse(self.window, 100, i * 100, randint(100, 120), i) for i in range(1, 3)]
        self.horses2 = (Horse(self.window, 100, i * 100 + 125, randint(100, 120), i) for i in range(3, 5))
        self.horses += self.horses2
        self.horseWinner = None
        self.messageWinner = ''
        self.bet = 0
        self.money = 0
        self.giveMoney = False
        self.podium = []
        self.showPodium = False
        self.podiumHorses = []
        self.addHorses = False

    def interacoes(self):
        """
        Faz todas as interações do jogo
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.isInBetMenu:
                    for button in self.betsButton:
                        if button.button.collidepoint(event.pos):
                            if self.bet == button.index:
                                self.bet = 0
                            else:
                                self.bet = button.index
                            break
                    if self.playButton.collidepoint(event.pos):
                        self.isInBetMenu = False
                else:
                    if self.resetButton.collidepoint(event.pos):
                        self.resetGame()
        return True

if __name__ == '__main__':
    playing = True
    pygame.init()
    window = pygame.display.set_mode((1280, 720), vsync=True, flags=pygame.SCALED)
    horseRace = HorseRace(window)

    while playing:
        if not horseRace.interacoes():
            playing = False
            break

        horseRace.desenha()

        pygame.display.update()
        
    pygame.quit()