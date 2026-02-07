import sys
from random import shuffle

from PySide6.QtCore import QSize
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
)

from card import Card
from deck_widget import DeckWidget


class MainWindow(QMainWindow):
    def __init__(self, cards: list[Card]):
        super().__init__()

        self.setWindowTitle('Flashcards')
        # 480p window
        self.setMinimumSize(QSize(854, 480))
        self.setFont(QFont('Georgia', pointSize=24))

        deck_widget = DeckWidget(cards)
        self.setCentralWidget(deck_widget)


if __name__ == '__main__':
    app = QApplication([])

    if len(sys.argv) < 2:
        raise Exception('No file path argument provided!')

    file_path: str = sys.argv[1]
    cards = Card.from_csv(file_path)
    shuffle(cards)

    window = MainWindow(cards)
    window.show()

    app.exec()
