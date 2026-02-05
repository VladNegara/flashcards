import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout

from card import Card
from deck import Deck

class CardWidget(QPushButton):
    def __init__(
            self,
            card: Card,
            ) -> None:
        super().__init__()

        self.card = card
        self.showing_definition = False
        self.refresh()

        self.clicked.connect(self._on_button_clicked)
    

    def refresh(self):
        self.setText(self.card.definition if self.showing_definition else self.card.term)


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
