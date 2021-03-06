import random

# Card suits and Ranks
SUITS = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
RANKS = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

# Card values
VALUES = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = VALUES[rank]

    def __str__(self):
        return  f"{self.rank} of {self.suit}"

    def __eq__(self, other):
        if isinstance(other, int):
            return other == VALUES[self.rank]
        return other.rank == self.rank


class Deck:
    all_cards = []

    def __init__(self):
        for suit in SUITS:
            for rank in RANKS:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if isinstance(new_cards, list):
            # List od multiple Card obj
            self.all_cards.extend(new_cards)
        else:
            # For a single card obj
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'

# GAME SETUP

player_one = Player('One')
player_two = Player('Two')

new_deck = Deck()
new_deck.shuffle()

for card in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
round_number = 0

while game_on:
    round_number += 1
    print (f'Currently round {round_number}')

    if len(player_one.all_cards) == 0:
        print(player_one)
        print('Lost the game')
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print(player_two)
        print('Lost the game')
        game_on = False
        break

    # start new round
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True

    while at_war:

        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_two_cards)
            player_two.add_cards(player_one_cards)

            at_war = False
        else:
            print("WAR!")

            if len(player_one.all_cards) < 5:
                print("Player One not able to declare a war!")
                print("Player Two wins!")
                game_on = False
                break
            elif len(player_two.all_cards) < 5:
                print("Player Two not able to declare a war!")
                print("Player One wins!")
                game_on = False
                break
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())

