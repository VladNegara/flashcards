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
        self.index: int = 0


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


    def current_card(
            self,
            ) -> Card | None:
        """
        Get the current card in the deck.
        
        :return: The current card if the index is valid, `None` otherwise.
        :rtype: Card | None
        """
        try:
            return self.cards[self.index]
        except Exception:
            return None


    def change_card(
            self,
            ) -> None:
        """Change the current card to the next one."""
        self.index += 1
    

    def reset(
            self,
            ) -> None:
        """Reset the current card to the first."""
        self.index = 0
