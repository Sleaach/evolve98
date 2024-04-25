import random
from colorama import Fore,Style
import os
op = os.name
class Deck:
    def __init__(self):
        self.cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def get_hand_value(self):
        value = 0
        num_aces = 0
        for card in self.hand:
            if card in ['J', 'Q', 'K']:
                value += 10
            elif card == 'A':
                num_aces += 1
                value += 11
            else:
                value += int(card)
        while value > 21 and num_aces:
            value -= 10
            num_aces -= 1
        return value

def print_game_status(player, dealer, show_dealer_hand=False):
    print("\n--- İstatistikler ---")
    print(f"Oyuncu Eli: {', '.join(player.hand)}")
    print(f"Oyuncu El Değeri: {player.get_hand_value()}")
    if show_dealer_hand:
        print(f"Krupiyer Eli: {', '.join(dealer.hand)}")
        print(f"Krupiyer El Değeri: {dealer.get_hand_value()}")
    else:
        print(f"Krupiyer El: {dealer.hand[0]}, ?")

def blackjack():
    deck = Deck()
    deck.shuffle()
    player = Player("Oyuncu")
    dealer = Player("Krupiyer")

    for _ in range(2):
        player.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())

    print_game_status(player, dealer)

    while player.get_hand_value() < 21:
        action = input("\nVurmak mı yoksa durmak mı istiyorsunuz? (h/s): ").lower()
        if action == 'h':
            player.add_card(deck.deal_card())
            print_game_status(player, dealer)
        elif action == 's':
            break
        else:
            print("Geçersiz giriş! Lütfen vurmak için 'h' veya durmak için 's' girin.")

    player_hand_value = player.get_hand_value()

    while dealer.get_hand_value() < 17:
        dealer.add_card(deck.deal_card())

    print_game_status(player, dealer, show_dealer_hand=True)

    dealer_hand_value = dealer.get_hand_value()

    if player_hand_value > 21:
        print("Oyuncu iflas etti! Krupiye kazandı.")
    elif dealer_hand_value > 21:
        print("Krupiyer iflas etti! Oyuncu kazandı.")
    elif player_hand_value == dealer_hand_value:
        print("Berabere!")
    elif player_hand_value > dealer_hand_value:
        print("Oyuncu Kazandı")
    else:
        print("Krupiyer Kazandı")
    replay = input("\nTekrar oynamak ister misin?: (e/h) ")
    if replay == "e":
        if op == "posix":
            os.system("clear")
            blackjack()

        else:
            os.system("cls")
            blackjack()

