import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout

from card import Card
from deck import Deck

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
        else:
            self.setText('No more cards :(')
            self.setEnabled(False)


    def _on_button_clicked(self):
        self.showing_definition = not self.showing_definition
        self.refresh()


class DeckWidget(QWidget):
    def __init__(
            self,
            deck: Deck,
            ) -> None:
        super().__init__()

        self.deck = deck

        self.card_widget = CardWidget(self.deck.current_card())

        self.know_button = QPushButton('Know')
        self.know_button.clicked.connect(self._on_know_button_clicked)
        self.dont_know_button = QPushButton('Don\'t know')
        self.dont_know_button.clicked.connect(self._on_dont_know_button_clicked)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.know_button)
        button_layout.addWidget(self.dont_know_button)

        layout = QVBoxLayout()
        layout.addWidget(self.card_widget)
        layout.addLayout(button_layout)

        self.setLayout(layout)
    
    
    def refresh(self):
        current_card: Card | None = self.deck.current_card()
        self.card_widget.set_card(current_card)
    

    def _on_know_button_clicked(self):
        self.deck.change_card()
        self.refresh()
    

    def _on_dont_know_button_clicked(self):
        self.deck.change_card()
        self.refresh()



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Flashcards')

        card = DeckWidget(Deck([Card('Hello', 'World'), Card('1', '2')]))
        self.setCentralWidget(card)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
