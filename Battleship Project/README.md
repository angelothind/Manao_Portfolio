# Welcome to Battleship!

Here all main features that are given within the specifications should be functioning. This is a simple implementation of battleship on python, it can be run with or without a GUI.


# Prerequisites

This project requires the use of python version 3.9, installation of python's virtual environment package, and flask. For the flask to work it requires the use of a virtual environment.

## Installation

To download these modules you can run:
pip install Flask
pip install virtualenv

## How to run

Using virtual studio code, open the "Battleship project" directory so that it is the working directory. If the folder venv does not exist this means you need to start a activate a virtual environment. To do this press the "shift+command+p" keys then select then select "Python: Create Environment". Now run the file main.py. In the terminal a url "http://127.0.0.1:5000" should appear. You can copy and paste this root url, then add "/placement" to the end of the url. This is the ship placement page. Now you can add your ships, pressing r to rotate, then press send game. This will direct you to where you can play the game. Now place your ships, then press send then play on.

## Developer documentation
### components. py
Has functions necessary to initialise and boads, battleships, and place battleships.

### game_engine.py
Has functions to get command line coordinate inputs, process those inputs as attacks and run a simple one sided game loop

### mp_game_engine.py
Initialises a dictionary structure that contains player and AI boards and ships dictionaries.
Contains functions to automatically generate attack coordinates, and play a command line level game of battleship.

## How to test
A seperate test folder to the source code contains a test file. This file has some tests for the components.py file. 

## Acknowledgements
Author: Angelo Singh Thind
Part of ECM1400 course

```
