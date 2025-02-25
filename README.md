# Hangman Game

## Description

Create a hangman game where the user guesses letters to form a hidden word.

Requirements
- The program should select a random word from a predefined list.
- It should display the word with underscores for unguessed letters.
- The user should guess letters until they either guess the word or run out of attempts.

### Example

![Example](./rsc/Captura.JPG)

### Libraries and Tools

Random module for word selection.

### Hints

- Use a list or set to keep track of guessed letters.
- Update the display as the user makes guesses.

### Topics to Study

- Random module
- String and list operations
- Control flow

### Methodological Steps
- Select a word: Use a list of words and randomly select one using random.choice().
- Initialize game state: Track guessed letters and remaining attempts.
- User interaction: Use a loop to repeatedly ask for guesses.
- Update display: Show the word with guessed letters and underscores for missing ones.
- Check game status: Determine if the user has won or lost.

### Best Practices

- Use clear displays: Make the game state easy to understand for the user.
- Validate inputs: Ensure the user enters valid guesses (letters only).
- Encourage code reuse: Use functions to handle repetitive tasks like updating the display.

## Project

The project replie the clasic hangman game, choose a random word from those in its database, and also allows more words to be added.

![Example](./rsc/Captura3.JPG)

**Play:**

The play option allows play with the default words.

![Example](./rsc/Captura2.JPG)

**Agregate a word to the options:**

Allows you to add an extra word to the list of possible words (added words are kept even after the program is closed).

![Example](./rsc/Captura1.JPG)

**See the options:**
This option print all the options of word.

![Example](./rsc/Captura4.JPG)

**Exit**

The exit option close the program.

![Example](./rsc/Captura5.JPG)

## Architecture

The project is divided into three folders: src (source code), db (database), and rsc (resources). In src, you will find the main file and the libs folder, which contains a series of modules. The "dbOperations" module includes several functions for working with databases. The "uiInterface" module contains a function responsible for all visual tasks. The "workWithWords" module processes all data inputs; it provides the graphical interface with the number of syllables in the selected word from the database, checks whether the letter you entered is in the word, and, if so, indicates its position, etc. In the db folder, there is the "options" file, which has the function of saving all the word options from which the game can choose; these can be modified. In the rsc folder, there are a couple of images that I have used in the readme.

## Run & Configure

### Requirements

pandas library

### Installation

### Clone the repository:

git clone https://github.com/kevin-pb/python-proyect-hangman-game.git

### Install dependencies:

pip install pandas

### Run

python main.py

## References

![Curso UML - Sesión 05 (Boundary, Control y Entidad)](https://www.youtube.com/watch?v=VDBhk5-erp0)
![RUP UML - Tipos de clases : Interfaz , Entidad y Control](https://www.youtube.com/watch?v=4d_fquQ9V2M)