import random


class Deck:
    suits = ["H", "D", "C", "S"]
    values = [str(i) for i in range(2, 11)] + ["J", "Q", "K", "A"]

    def __init__(self):
        self.cards = []
        self.fill_deck()

    def fill_deck(self):
        for suit in Deck.suits:
            for value in Deck.values:
                card = value + suit
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, n):
        dealt_cards = []

        for i in range(n):
            if len(self.cards) == 0:
                break

            card = self.cards.pop()
            dealt_cards.append(card)

        return dealt_cards

    def sort_by_suit(self):
        cards_by_suit = {"H": [], "D": [], "C": [], "S": []}

        for card in self.cards:
            suit = card[-1]
            cards_by_suit[suit].append(card)

        self.cards = (
            cards_by_suit["H"] +
            cards_by_suit["D"] +
            cards_by_suit["C"] +
            cards_by_suit["S"]
        )

    def contains(self, card):
        return card in self.cards

    def copy(self):
        new_deck = Deck()
        new_deck.cards = self.cards[:]
        return new_deck

    def get_cards(self):
        return self.cards[:]

    def __len__(self):
        return len(self.cards)
