import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QStackedLayout

from card import Card

class CardWidget(QPushButton):
    def __init__(
            self,
            card: Card | None,
            ) -> None:
        super().__init__()

        self.set_card(card)

        self.clicked.connect(self._on_button_clicked)

    
    def set_card(self, card: Card | None):
        self.card = card
        self.showing_definition = False
        self.refresh()
    

    def refresh(self):
        if self.card is not None:
            self.setText(self.card.definition if self.showing_definition else self.card.term)
            self.setEnabled(True)
        else:
            self.setText('No more cards :(')
            self.setEnabled(False)


    def _on_button_clicked(self):
        self.showing_definition = not self.showing_definition
        self.refresh()


class DeckWidget(QWidget):
    def __init__(
            self,
            cards: list[Card],
            ) -> None:
        super().__init__()

        self.cards: list[Card] = cards

        self.index: int = 0

        self.stacked_card_layout = QStackedLayout()
        for card in self.cards:
            self.stacked_card_layout.addWidget(CardWidget(card))
        self.stacked_card_layout.addWidget(CardWidget(None))

        know_button = QPushButton('Know')
        know_button.clicked.connect(self._on_know_button_clicked)
        dont_know_button = QPushButton('Don\'t know')
        dont_know_button.clicked.connect(self._on_dont_know_button_clicked)

        button_layout = QHBoxLayout()
        button_layout.addWidget(know_button)
        button_layout.addWidget(dont_know_button)

        previous_button = QPushButton('Previous card')
        previous_button.clicked.connect(self._on_previous_button_clicked)

        reset_button = QPushButton('Reset deck')
        reset_button.clicked.connect(self._on_reset_button_clicked)

        layout = QVBoxLayout()
        layout.addLayout(self.stacked_card_layout)
        layout.addLayout(button_layout)
        layout.addWidget(previous_button)
        layout.addWidget(reset_button)

        self.setLayout(layout)

    
    def _refresh(self):
        self.index = max(0, min(self.index, len(self.cards)))
        self.stacked_card_layout.setCurrentIndex(self.index)

    
    def _next_card(self):
        self.index += 1
        self._refresh()
    

    def _previous_card(self):
        self.index -= 1
        self._refresh()
    

    def _on_know_button_clicked(self):
        self._next_card()
    

    def _on_dont_know_button_clicked(self):
        self._next_card()


    def _on_previous_button_clicked(self):
        self._previous_card()

    
    def _on_reset_button_clicked(self):
        self.index = 0
        self._refresh()



class MainWindow(QMainWindow):
    def __init__(self, cards: list[Card]):
        super().__init__()

        self.setWindowTitle('Flashcards')

        deck_widget = DeckWidget(cards)
        self.setCentralWidget(deck_widget)


if __name__ == '__main__':
    app = QApplication([])

    if len(sys.argv) < 2:
        raise Exception('No file path argument provided!')

    file_path: str = sys.argv[1]
    cards = Card.from_csv(file_path)

    window = MainWindow(cards)
    window.show()

    app.exec()
