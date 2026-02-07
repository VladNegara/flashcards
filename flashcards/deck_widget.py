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

        previous_button = QPushButton('Previous card')
        previous_button.clicked.connect(self._on_previous_button_clicked)

        reset_button = QPushButton('Reset deck')
        reset_button.clicked.connect(self._on_reset_button_clicked)

        layout = QBoxLayout(QBoxLayout.Direction.TopToBottom)
        layout.addWidget(self.card_widget)
        layout.addWidget(self.card_counter)
        layout.addLayout(button_layout)
        layout.addWidget(previous_button)
        layout.addWidget(reset_button)

        self.setLayout(layout)

        self._refresh()

    
    def _refresh(self):
        self.index = max(0, min(self.index, len(self.cards) - 1))
        self.card_widget.set_card(self.cards[self.index])
        self.card_counter.setText(f'{self.index + 1}/{len(self.cards)}')

    
    def _next_card(self):
        self.index += 1
        self._refresh()
    

    def _previous_card(self):
        self.index -= 1
        self._refresh()
    

    def _on_know_button_clicked(self):
        self.card_widget.set_known(True)
        self._next_card()
    

    def _on_dont_know_button_clicked(self):
        self.card_widget.set_known(False)
        self._next_card()


    def _on_previous_button_clicked(self):
        self._previous_card()

    
    def _on_reset_button_clicked(self):
        self.index = 0
        self._refresh()
