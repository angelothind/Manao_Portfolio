import pytest
import sys
import sys
import os
sys.path.insert(0, os.path.abspath('Battleship_modules'))
from components import initialise_board, create_battleships, place_battleships


def test_initalise_board_correct_size():
    size = 10
    board = initialise_board(size=size)
    assert len(board) == 10, "Number of Rows is incorrect"
    assert len(board[0]) == 10, "Number of columns is incorrect"

def test_initalise_board_valid_input():
    size ="Invalid"
    with pytest.raises(ValueError):
        initialise_board(size=size)

def test_create_battleships_correct_dictionary():
    dictionary = create_battleships()
    assert dictionary == {"Aircraft_Carrier":5,"Battleship":4,"Cruiser":3,"Submarine":3,"Destroyer":2}
    
def test_create_battleships_file_error():
    file ="Invalid"
    with pytest.raises(ValueError):
        create_battleships(file)

def test_place_battleships_random_all_placed():
    board = [[None,None,None,None,None,None,None,None,None,None],
             [None,None,None,None,None,None,None,None,None,None],
             [None,None,None,None,None,None,None,None,None,None],
             [None,None,None,None,None,None,None,None,None,None],
             [None,None,None,None,None,None,None,None,None,None],
             [None,None,None,None,None,None,None,None,None,None],
             [None,None,None,None,None,None,None,None,None,None]]
    dictionary = create_battleships()
    checking_dict = {}
    finished_board =  place_battleships(board,dictionary,"random")
    for ship in dictionary:
        checking_dict[ship] = 0
    for row in finished_board:
        for element in row:
            if element in checking_dict:
                checking_dict[element] = checking_dict[element] + 1
    assert checking_dict == dictionary, "Not all ships placed or not all ships placed correctly"
