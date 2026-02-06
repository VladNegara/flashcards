# Flashcards

A simple application for flashcards in the PySide6 GUI framework. This project was built as an exploration of PySide6 and git submodules, as well as for personal use.


## Installation

The project has only been tested on Linux systems.


### Linux

1. Make sure you have the necessary libraries installed for PySide6:

```bash
sudo apt install libxkbcommon-x11-0 libxcb-icccm4 libxcb-keysyms1
```

2. Clone the project.

3. Initialize the submodule:

```bash
git submodule update --init --recursive
```

4. Create a virtual environment:

```bash
python3 -m venv venv/
```

5. Activate the virtual environment:

```bash
source venv/bin/activate
```

6. Install the requirements:

```bash
pip install -r requirements.txt
```


## Running the app

To use the app, run the `flashcards/app.py` file and pass in the path to the CSV file containing the cards. For example, the command to run the app with the Dutch A1 cards included in the vocabulary submodule:

```bash
python3 flashcards/app.py cards/vocabulary/nl-en/nl-en-a1.csv
```


## User interface

The user interface is made up of four buttons:

- The topmost button is the current flashcard. This can be clicked to flip it over to the other side.
- The "Know" and "Don't know" buttons mark a card as known or unknown, and advance to the next card in the deck.
- The "Reset deck" button resets the deck to its initial state.


## File format

The CSV file containing the cards must be one of the two supported formats:

1. Two columns: `Term`, `Definition`.
2. Four columns: `Term`, `Term example`, `Definition`, `Definition example`.

Card files must not have headers.


## Vocabulary submodule

The app includes [this set of vocabulary flashcards](https://github.com/VladNegara/vocabulary-flashcards) as a git submodule.
