import sys
from random import shuffle

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QFont
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QStackedLayout, QLayout

from card import Card

class CardWidget(QPushButton):
    def __init__(
            self,
            card: Card | None,
            ) -> None:
        super().__init__()

        # Initialize the stacked layout
        self.stacked_layout = QStackedLayout(self)
        self.stacked_layout.setVerticalSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)


        # Initialize the front without example and add it to the layout
        self.term_no_example = QLabel('')
        self.term_no_example.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stacked_layout.addWidget(self.term_no_example)


        # Initialize the front with example and add it to the layout
        self.term_with_example = QWidget()
        term_with_example_layout = QVBoxLayout(self.term_with_example)

        self.term = QLabel('')
        self.term.setAlignment(Qt.AlignmentFlag.AlignCenter)
        term_with_example_layout.addWidget(self.term)

        term_as_in = QLabel('as in')
        term_as_in.setFont(QFont('Georgia', pointSize=16))
        term_as_in.setAlignment(Qt.AlignmentFlag.AlignCenter)
        term_with_example_layout.addWidget(term_as_in)

        self.term_example = QLabel('')
        self.term_example.setFont(QFont('Georgia', pointSize=20, italic=True))
        self.term_example.setAlignment(Qt.AlignmentFlag.AlignCenter)
        term_with_example_layout.addWidget(self.term_example)

        self.stacked_layout.addWidget(self.term_with_example)


        # Initialize the back without example and add it to the layout
        self.definition_no_example = QLabel('')
        self.definition_no_example.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stacked_layout.addWidget(self.definition_no_example)


        # Initialize the back with example and add it to the layout
        self.definition_with_example = QWidget()
        definition_with_example_layout = QVBoxLayout(self.definition_with_example)

        self.definition = QLabel('')
        self.definition.setAlignment(Qt.AlignmentFlag.AlignCenter)
        definition_with_example_layout.addWidget(self.definition)

        definition_as_in = QLabel('as in')
        definition_as_in.setFont(QFont('Georgia', pointSize=16))
        definition_as_in.setAlignment(Qt.AlignmentFlag.AlignCenter)
        definition_with_example_layout.addWidget(definition_as_in)

        self.definition_example = QLabel('')
        self.definition_example.setFont(QFont('Georgia', pointSize=20, italic=True))
        self.definition_example.setAlignment(Qt.AlignmentFlag.AlignCenter)
        definition_with_example_layout.addWidget(self.definition_example)

        self.stacked_layout.addWidget(self.definition_with_example)


        # Initialize the None display and add it to the layout
        self.none_card = QLabel('No more cards to display :(')
        self.none_card.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stacked_layout.addWidget(self.none_card)


        # Connect button signal
        self.clicked.connect(self._on_button_clicked)

        # Set the card passed as parameter
        self.set_card(card)


    def set_card(self, card: Card | None):
        self.card = card

        if self.card is not None:
            if self.card.term_example:
                self.term.setText(self.card.term)
                self.term_example.setText(f'"{self.card.term_example}"')
            else:
                self.term_no_example.setText(self.card.term)

            if self.card.definition_example:
                self.definition.setText(self.card.definition)
                self.definition_example.setText(f'"{self.card.definition_example}"')
            else:
                self.definition_no_example.setText(self.card.definition)

        self._refresh()


    def _refresh(self):
        if self.card is not None:
            self.setEnabled(True)

            if not self.card.flipped:
                if not self.card.term_example:
                    self.stacked_layout.setCurrentWidget(self.term_no_example)
                else:
                    self.stacked_layout.setCurrentWidget(self.term_with_example)
            else:
                if not self.card.definition_example:
                    self.stacked_layout.setCurrentWidget(self.definition_no_example)
                else:
                    self.stacked_layout.setCurrentWidget(self.definition_with_example)
        else:
            self.setEnabled(False)
            self.stacked_layout.setCurrentWidget(self.none_card)


    def _on_button_clicked(self):
        if self.card:
            self.card.flipped = not self.card.flipped
        self._refresh()


class DeckWidget(QWidget):
    def __init__(
            self,
            cards: list[Card],
            ) -> None:
        super().__init__()

        self.cards: list[Card | None] = cards + [None]

        self.index: int = 0

        self.card_widget = CardWidget(cards[0])

        know_button = QPushButton('Know')
        know_button.clicked.connect(self._on_know_button_clicked)
        dont_know_button = QPushButton('Don\'t know')
        dont_know_button.clicked.connect(self._on_dont_know_button_clicked)

        button_layout = QHBoxLayout()
        button_layout.setSpacing(24)
        button_layout.addWidget(know_button)
        button_layout.addWidget(dont_know_button)

        previous_button = QPushButton('Previous card')
        previous_button.clicked.connect(self._on_previous_button_clicked)

        reset_button = QPushButton('Reset deck')
        reset_button.clicked.connect(self._on_reset_button_clicked)

        layout = QVBoxLayout()
        layout.addWidget(self.card_widget)
        layout.addLayout(button_layout)
        layout.addWidget(previous_button)
        layout.addWidget(reset_button)

        self.setLayout(layout)

    
    def _refresh(self):
        self.index = max(0, min(self.index, len(self.cards)))
        self.card_widget.set_card(self.cards[self.index])

    
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
