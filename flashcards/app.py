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


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Flashcards')

        card = CardWidget(Card('Hello', 'World'))
        self.setCentralWidget(card)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
