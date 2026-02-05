import csv

from card import Card

class Deck:
    def __init__(
            self,
            cards: list[Card] = []
            ) -> None:
        """
        Initialize a deck of cards.
        """
        self.cards: list[Card] = cards
    
    @classmethod
    def from_csv(
            cls,
            file_path: str
            ):
        """
        Create a deck of cards from a CSV file.
        
        :param file_path: The path to the CSV file.
        :type file_path: str
        """
        cards: list[Card] = []
        with open(file_path, newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                cards.append(Card.from_sequence(row))
        return Deck(cards)
