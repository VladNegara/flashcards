from typing import Sequence

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QBoxLayout,
    QHBoxLayout,
    QSizePolicy,
)

from card import Card
from card_widget import CardWidget


class DeckWidget(QWidget):
    def __init__(
            self,
            cards: list[Card],
            ) -> None:
        super().__init__()

        self.cards: Sequence[Card | None] = cards or [None]

        self.index: int = 0

        self.card_widget = CardWidget(cards[0])
        self.card_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)

        self.card_counter = QLabel('')
        self.card_counter.setFont(QFont('Georgia', pointSize=12))
        self.card_counter.setAlignment(Qt.AlignmentFlag.AlignRight)

        know_button = QPushButton('Know')
        know_button.clicked.connect(self._on_know_button_clicked)
        dont_know_button = QPushButton('Don\'t know')
        dont_know_button.clicked.connect(self._on_dont_know_button_clicked)

        button_layout = QHBoxLayout()
        button_layout.setSpacing(24)
        button_layout.addWidget(know_button)
        button_layout.addWidget(dont_know_button)


        # Initialize navigation buttons
        navigation_layout = QHBoxLayout()

        first_button = QPushButton('First')
        first_button.clicked.connect(self._on_first_button_clicked)
        navigation_layout.addWidget(first_button)

        previous_unknown_button = QPushButton('Previous unknown')
        previous_unknown_button.clicked.connect(self._on_previous_unknown_button_clicked)
        navigation_layout.addWidget(previous_unknown_button)

        previous_button = QPushButton('Previous')
        previous_button.clicked.connect(self._on_previous_button_clicked)
        navigation_layout.addWidget(previous_button)

        next_button = QPushButton('Next')
        next_button.clicked.connect(self._on_next_button_clicked)
        navigation_layout.addWidget(next_button)

        next_unknown_button = QPushButton('Next unknown')
        next_unknown_button.clicked.connect(self._on_next_unknown_button_clicked)
        navigation_layout.addWidget(next_unknown_button)

        last_button = QPushButton('Last')
        last_button.clicked.connect(self._on_last_button_clicked)
        navigation_layout.addWidget(last_button)


        reset_button = QPushButton('Reset deck')
        reset_button.clicked.connect(self._on_reset_button_clicked)

        layout = QBoxLayout(QBoxLayout.Direction.TopToBottom)
        layout.addWidget(self.card_widget)
        layout.addWidget(self.card_counter)
        layout.addLayout(button_layout)
        layout.addLayout(navigation_layout)
        layout.addWidget(reset_button)

        self.setLayout(layout)

        self._refresh()

    
    def _refresh(self):
        self.index = max(0, min(self.index, len(self.cards) - 1))
        self.card_widget.set_card(self.cards[self.index])
        self.card_counter.setText(f'{self.index + 1}/{len(self.cards)}')


    def _first_card(self):
        self.index = 0
        self._refresh()


    def _previous_card(self):
        self.index -= 1
        self._refresh()


    def _previous_unknown_card(self):
        self.index -= 1
        while self.index > 0:
            card = self.cards[self.index]
            if card is not None and not card.known:
                break
            self.index -= 1
        
        self._refresh()


    def _next_unknown_card(self):
        self.index += 1
        while self.index > 0:
            card = self.cards[self.index]
            if card is not None and not card.known:
                break
            self.index += 1
        
        self._refresh()

    
    def _next_card(self):
        self.index += 1
        self._refresh()


    def _last_card(self):
        self.index = len(self.cards) - 1
        self._refresh()


    def _reset(self):
        for card in self.cards:
            if card is None:
                continue
            card.known = None

        self._first_card()
    

    def _on_know_button_clicked(self):
        self.card_widget.set_known(True)
        self._next_card()
    

    def _on_dont_know_button_clicked(self):
        self.card_widget.set_known(False)
        self._next_card()


    def _on_first_button_clicked(self):
        self._first_card()


    def _on_previous_unknown_button_clicked(self):
        self._previous_unknown_card()


    def _on_previous_button_clicked(self):
        self._previous_card()


    def _on_next_button_clicked(self):
        self._next_card()


    def _on_next_unknown_button_clicked(self):
        self._next_unknown_card()


    def _on_last_button_clicked(self):
        self._last_card()

    
    def _on_reset_button_clicked(self):
        self._reset()
