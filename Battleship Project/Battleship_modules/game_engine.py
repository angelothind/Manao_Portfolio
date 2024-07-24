from components import initialise_board, place_battleships, create_battleships

"""This module builds on components.py, adding functions needed to create a one way CLI battlships game."""


def attack(coordinate: tuple, board, battleships: dict):
    """
    Takes in a coordinate, the board being attacked and the corresponding dictionary

    :param coordinate: a tuple containing coordinates x followed by y
    :param board: The 2d array representing the board being attacked
    :param battleships: The dictionary containing battleships and the number of pieces that make them up
    """
    if board[coordinate[0]][coordinate[1]] != None:
        # checks if a ship has been hit #
        ship = board[coordinate[0]][coordinate[1]]
        #Stores which type of ship has been hit #
        board[coordinate[0]][coordinate[1]] = None
        # Changes the value on the board to None #
        battleships[ship] = battleships[ship] - 1 
        #decrements the hit ship vale in the dictionary passed
        return True
        #returns True if a ship is hit and vice versa #
    else:
        return False
    
def cli_coordinates_input():
    """ 
        Gets user input to return a tuple representing coordinates
    """
    while True:
        #While loop is used for input validation
        try:
            #Check if it is an integer that is entered
            x =  int(input("Please input your x coordinate to attack: "))

            break
        except ValueError:
            print("X Value entered in not an integer, please enter an integer")

    while True:
        #Repeat the same checks on the y value
        try:
            y =  int(input("Please input your y coordinate to attack: "))
            break
        except:
            print("Y Value entered in not an integer, please enter an integer")
    coordinates = (x,y)
    return coordinates

def simple_game_loop():
    """
        This function runs a one way game loop, where the user enters coordinates to hit the computer's board. 
    """
    print("Welcome to this simple version of Battleships")
    # Welcome message #
    board = initialise_board()
    ships = create_battleships()
    size = range(len(board))
    #initialising of board array and ships dictionary #
    place_battleships(board, ships)
    # Does a simple placement on a board #
    pieces_left = 0
    #Initialize peices left #
    for ship in ships:
        pieces_left = pieces_left + ships[ship]
        #Counts up the number total pieces that could be hit to be decremented later#
    while pieces_left != 0:
        coordinate = cli_coordinates_input()
        # Input validation of coordinates for size of board #
        while coordinate[0] not in size or coordinate[1] not in size:
                print("The coordinates given are not valid given size of board or may be negative")
                coordinate = cli_coordinates_input()            
        if attack(coordinate=coordinate, board= board, battleships= ships) == True:
            #if a ship is hit decrement number of pieces left#
            pieces_left = pieces_left -1
            print("hit")
        else:
            print("miss")
    print("game over")

