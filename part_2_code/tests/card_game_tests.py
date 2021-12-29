import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def test_check_for_ace(self):
        card = Card("Diamonds", 1)
        result = CardGame.check_for_ace(self, card)
        self.assertEqual(result, True)

    def test_check_not_for_ace(self):
        card = Card("Diamonds", 5)
        result = CardGame.check_for_ace(self, card)
        self.assertEqual(result, False)

    def test_highest_card(self):
        card1 = Card("Hearts", 3)
        card2 = Card("Clubs", 9)
        result = CardGame.highest_card(self, card1, card2)
        self.assertEqual(result, card2)

    def test_cards_total(self):
        cards = [ Card("Spades",10), Card("Spades",7), Card("Spades",3) ]
        result = CardGame.cards_total(self, cards)
        self.assertEqual( result, 20 )