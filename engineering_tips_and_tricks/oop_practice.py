from enum import Enum
import random


class Suit(Enum):
    HEART = "Heart"
    DIAMOND = "Diamond"
    CLUB = "Club"
    SPADE = "Spade"


class Value(Enum):
    one = "A"
    two = "2"
    three = "3"
    four = "4"
    five = "5"
    six = "6"
    seven = "7"
    eight = "8"
    nine = "9"
    ten = "10"
    eleven = "J"
    twelve = "Q"
    thirteen = "K"


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def print_card(self):
        print(self.suit.value, self.value.value)


class Deck:
    def __init__(self):
        self.cards = list()
        for suit in Suit:
            for value in Value:
                self.cards.append(Card(suit, value))

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
            print("Can't shuffle! Deck doesn't contain 52 cards!")

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

card_deck.shuffle_cards()  # This should not shuffle successfully
