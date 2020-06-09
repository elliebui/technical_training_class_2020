from enum import Enum
import random


class Suit(Enum):
    HEART = "Heart"
    DIAMOND = "Diamond"
    CLUB = "Club"
    SPADE = "Spade"


class Value(Enum):
    ACE = "A"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "10"
    JACK = "J"
    QUEEN = "Q"
    KING = "K"


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def print_card(self):
        print(self.suit.value, self.value.value)


class Deck:
    def __init__(self):
        self.cards = self.create_deck()
        self.size = len(self.cards)

    def deal_card(self):
        # a deal method to deal a single card from the deck
        # After a card is dealt, it is removed from the deck.
        self.cards.pop(self.size - 1)
        self.size -= 1
        return self.cards

    def shuffle_cards(self):
        # a shuffle method which makes sure the deck of cards has all 52 cards
        # and then rearranges them randomly
        if self.size == 52:
            random.shuffle(self.cards)
            return self.cards
        else:
            self.cards = self.create_deck()
            self.size = len(self.cards)
            self.shuffle_cards()

    @staticmethod
    def create_deck():
        cards = list()
        for suit in Suit:
            for value in Value:
                cards.append(Card(suit, value))

        return cards

    def print_deck(self):
        for card in self.cards:
            card.print_card()


card_deck = Deck()
card_deck.print_deck()  # This should print complete deck (52 cards) in order
print(card_deck.size)  # This should be 52 cards
print("\n")

card_deck.shuffle_cards()  # This should shuffle successfully since the deck has all 52 cards
card_deck.print_deck()  # This should print complete deck (52 cards) in shuffled order
print(card_deck.size)  # This should be 52 cards
print("\n")

card_deck.deal_card()  # This should remove last card from deck
card_deck.print_deck()  # This should print incomplete deck (51 cards) in shuffled order
print(card_deck.size)  # This should be 51 cards
print("\n")

card_deck.shuffle_cards()  # This should make a new deck with 52 cards and then shuffle
card_deck.print_deck()  # This should print complete deck (52 cards) in shuffled order
print(card_deck.size)  # This should be 52 cards
