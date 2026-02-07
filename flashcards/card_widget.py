from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QStackedLayout,
    QLayout,
)

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
        self.none_card = QLabel('No cards to display :(')
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
