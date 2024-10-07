import pygame
import random
import os
from collections import Counter

# Definindo as constantes do caminho das imagens
CARD_PATH = "images/cards"  # Atualize isso para o caminho correto onde as imagens das cartas estão localizadas
CARD_BACK = "Backs"
CARD_SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]
CARD_VALUES = list(range(1, 14))  # 1 para Ás, 11 para Valete, 12 para Rainha, 13 para Rei

# Definindo a classe do jogo
class Poker:
    def __init__(self, window):
        self.window = window
        self.background_color = (0, 128, 0)
        self.player_hand = []
        self.dealer_hand = []
        self.deck = self.create_deck()
        self.bet = 50
        self.font = pygame.font.Font(None, 36)
        self.card_images = self.load_card_images()
        self.isInMenu = False
        self.animation = False
        self.animationIndex = 0
        self.lastTick = 0
        self.isInResultMenu = False
        self.resultMessage = ''
        self.resetButton = pygame.rect.Rect((1280 // 2) - 120, 720 // 2 + 50, 240, 60)
        self.foldButton = pygame.rect.Rect((1280 // 2) - 120 - 130, 720 // 2 + 50, 240, 60)
        self.surrenderButton = pygame.rect.Rect((1280 // 2) - 120 + 130, 720 // 2 + 50, 240, 60)
        self.giveMoney = False
        self.initGameButton = pygame.rect.Rect((1280 // 2) - 100, 720 // 1.9, 200, 50)
        self.isInGameMenu = True
        self.giveCardSound = pygame.mixer.Sound('musica/dando_carta.wav')
        self.setCardSound = pygame.mixer.Sound('musica/colocando_carta_mesa.wav')
        self.payments = {
            'Par': 100,
            'Dois Pares': 200,
            'Tripla': 300,
            'Straight': 400,
            'Flush': 500,
            'Full House': 700,
            'Quadra': 2000,
            'Straight Flush': 5000,
            'Royal Flush': 10000
        }

    def load_card_images(self):
        card_images = {}
        for suit in CARD_SUITS:
            for value in CARD_VALUES:
                card_name = f"{value}.png"
                card_images[(suit, value)] = pygame.transform.scale(pygame.image.load(os.path.join(CARD_PATH, suit, card_name)), (125, 181))
        return card_images

    def create_deck(self):
        # Cria um baralho completo com 52 cartas
        deck = [(suit, value) for suit in CARD_SUITS for value in CARD_VALUES]
        random.shuffle(deck)
        return deck

    def deal_cards(self):
        # Distribui cartas para o jogador e o dealer
        self.player_hand = [self.deck.pop() for _ in range(5)]
        self.dealer_hand = [self.deck.pop() for _ in range(5)]

    def desenha(self):
        if not self.isInGameMenu:
            self.window.fill(self.background_color)
            userCardsWidth = len(self.player_hand) * 150
            dealerCardsWidth = len(self.dealer_hand) * 150
            startXUser = (1280 - userCardsWidth) // 2
            startXDealer = (1280 - dealerCardsWidth) // 2
            for index, card in enumerate(self.player_hand):
                suit, value = card
                card_image = self.card_images[(suit, value)]
                self.window.blit(card_image, (startXUser + (index * 150), 500))
            for index, card in enumerate(self.dealer_hand):
                if self.isInMenu:
                    if index != 0:
                        card_image = pygame.transform.scale(pygame.image.load(os.path.join(CARD_PATH, CARD_BACK, "back.png")), (125, 181))
                    else:
                        suit, value = card
                        card_image = self.card_images[(suit, value)]
                else:
                    if self.animation:
                        timeDistance = (pygame.time.get_ticks() - self.lastTick) / 1000
                        if timeDistance >= 1:
                            self.setCardSound.play()
                            self.lastTick = pygame.time.get_ticks()
                            self.animationIndex += 1
                        if index <= self.animationIndex:
                            suit, value = card
                            card_image = self.card_images[(suit, value)]
                        else:
                            card_image = pygame.transform.scale(pygame.image.load(os.path.join(CARD_PATH, CARD_BACK, "back.png")), (125, 181))
                    else:
                        suit, value = card
                        card_image = self.card_images[(suit, value)]
                self.window.blit(card_image, (startXDealer + (index * 150), 50))
            if self.animation and self.animationIndex >= 4:
                self.animation = False
                self.isInMenu = False
                self.isInResultMenu = True
                if self.resultMessage == '':
                    self.resultMessage = self.checkWinner()
            if self.isInMenu:
                pygame.draw.rect(self.window, (55, 255, 1), self.foldButton)
                text_surface = self.font.render(f'Dobrar', True, (0, 0, 0))
                x = (1280 // 2) - 120 - 130 + (self.foldButton.width // 2) - (text_surface.get_width() // 2)
                y = 720 // 2 + 50 + (self.foldButton.height // 2) - (text_surface.get_height() // 2)
                self.window.blit(text_surface, (x, y))
                pygame.draw.rect(self.window, (255, 0, 0), self.surrenderButton)
                text_surface = self.font.render(f'Desistir', True, (0, 0, 0))
                x = (1280 // 2) - 120 + 130 + (self.surrenderButton.width // 2) - (text_surface.get_width() // 2)
                y = 720 // 2 + 50 + (self.surrenderButton.height // 2) - (text_surface.get_height() // 2)
                self.window.blit(text_surface, (x, y))
            if self.isInResultMenu:
                pygame.draw.rect(self.window, (0, 0, 0), self.resetButton)
                text_surface = self.font.render(f'Jogar novamente', True, (255, 255, 255))
                x = (1280 // 2) - 120 + (self.resetButton.width // 2) - (text_surface.get_width() // 2)
                y = 720 // 2 + 50 + (self.resetButton.height // 2) - (text_surface.get_height() // 2)
                self.window.blit(text_surface, (x, y))
                text_surface = self.font.render(self.resultMessage, True, (255, 255, 255))
                x = (1280 // 2) - (text_surface.get_width() // 2)
                y = 720 // 2 - (text_surface.get_height() // 2)
                self.window.blit(text_surface, (x, y))
        else:
            self.window.fill((0, 0, 0))
            font = pygame.font.Font(pygame.font.get_default_font(), 36)
            text_surface = font.render('Seja bem vindo ao poker, para começar clique no botão abaixo.', True, (255, 255, 255))
            x =  (1280 // 2) - (text_surface.get_width() // 2)
            y = (720 // 2) - (text_surface.get_height() // 1.4) - 50
            self.window.blit(text_surface, (x, y))
            pygame.draw.rect(self.window, (255, 255, 255), self.initGameButton)
            font = pygame.font.Font(pygame.font.get_default_font(), 20)
            text_surface = self.font.render(f'Jogar', True, (0, 0, 0))
            x = (1280 // 2) - 100 + (self.initGameButton.width // 2) - (text_surface.get_width() // 2)
            y = 720 // 1.9 + (self.initGameButton.height // 2) - (text_surface.get_height() // 2)
            self.window.blit(text_surface, (x, y))

    def has_king_and_ace_or_better(self, hand):
        rei = False
        a = False
        for suit, value in hand:
            if value == 1:
                a = True
            elif value == 12:
                rei = True
        if rei and a:
            return True
        if self.evaluate_hand(hand) != 'Maior Carta':
            return True
        return False

    def hand_rank(self, hand):
        hand_names = ["Maior Carta", "Par", "Dois Pares", "Tripla", "Straight", "Flush", "Full House", "Quadra", "Straight Flush", "Royal Flush"]
        name = self.evaluate_hand(hand)
        return hand_names.index(name)

    def compare_hands_same_rank(self, player_hand, dealer_hand):
        def get_value_counts(hand):
            values = [card[1] for card in hand]
            value_counts = Counter(values).most_common()
            return sorted(value_counts, key=lambda x: (x[1], x[0]), reverse=True)

        player_value_counts = get_value_counts(player_hand)
        dealer_value_counts = get_value_counts(dealer_hand)

        for (player_value, player_count), (dealer_value, dealer_count) in zip(player_value_counts, dealer_value_counts):
            if player_value > dealer_value:
                return "player"
            elif dealer_value > player_value:
                return "dealer"
        return "tie"

    def checkWinner(self):
        player_rank = self.hand_rank(self.player_hand)
        dealer_rank = self.hand_rank(self.dealer_hand)

        if player_rank > dealer_rank:
            hand = self.evaluate_hand(self.player_hand)
            self.bet = self.payments[hand]
            return f"Você venceu com {hand} e ganhou R$ {self.bet},00!"
        elif dealer_rank > player_rank:
            self.bet = -100
            return f"Dealer ganhou com {self.evaluate_hand(self.dealer_hand)} e você perdeu R$ 100,00!"
        else:
            winner = self.compare_hands_same_rank(self.player_hand, self.dealer_hand)
            if winner == "player":
                hand = self.evaluate_hand(self.player_hand)
                self.bet = self.payments[hand]
                return f"Você venceu com uma {hand} mais forte  e ganhou R$ {self.bet},00!"
            elif winner == "dealer":
                hand = self.evaluate_hand(self.dealer_hand)
                self.bet = -100
                return f"Dealer ganhou com uma {hand} mais forte e você perdeu R$ 100,00!"
            else:
                self.bet = 0
                return "O jogo empatou e a aposta foi cancelada!"

    def evaluate_hand(self, hand):
        values = [card[1] for card in hand]
        suits = [card[0] for card in hand]
        value_counts = Counter(values).most_common()
        suit_counts = Counter(suits).most_common()
        
        is_flush = suit_counts[0][1] == 5
        is_straight = sorted(values) == list(range(min(values), min(values) + 5))
        if is_flush and is_straight:
            return "Straight Flush" if min(values) != 1 else "Royal Flush"
        
        if value_counts[0][1] == 4:
            return "Quadra"
        if value_counts[0][1] == 3:
            if value_counts[1][1] == 2:
                return "Full House"
            return "Tripla"
        if is_flush:
            return "Flush"
        if is_straight:
            return "Straight"
        if value_counts[0][1] == 2:
            if value_counts[1][1] == 2:
                return "Dois Pares"
            return "Par"
        return "Maior Carta"

    def resetGame(self):
        self.player_hand = []
        self.dealer_hand = []
        if len(self.deck) < 10:
            self.deck = self.create_deck()
        self.isInMenu = True
        self.animation = False
        self.animationIndex = 0
        self.lastTick = 0
        self.resultMessage = ''
        self.isInResultMenu = False
        self.bet = 50
        self.giveMoney = False

    def interacoes(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.isInGameMenu:
                    if self.initGameButton.collidepoint(event.pos):
                        self.isInGameMenu = False
                        self.isInMenu = True
                        return True
                if self.isInResultMenu:
                    if self.resetButton.collidepoint(event.pos):
                        self.resetGame()
                        self.deal_cards()
                elif self.isInMenu:
                    if self.foldButton.collidepoint(event.pos):
                        self.bet *= 2
                        self.isInMenu = False
                        self.animation = True
                        self.lastTick = pygame.time.get_ticks()
                        if not self.has_king_and_ace_or_better(self.dealer_hand):
                            self.bet = 0
                            self.resultMessage = 'O dealer saiu e a aposta foi cancelada!'
                    elif self.surrenderButton.collidepoint(event.pos):
                        self.animation = True
                        self.isInMenu = False
                        self.bet = -50
                        self.resultMessage = 'Você desistiu e perdeu R$ 50,00!'
        return True

if __name__ == '__main__':
    pygame.init()
    screen_width = 1280
    screen_height = 720
    window = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Caribbean Poker')
    game = Poker(window)
    running = True
    game.deal_cards()
    while running:
        if not game.interacoes():
            running = False
            break
        game.desenha()
        pygame.display.flip()
    pygame.quit()
