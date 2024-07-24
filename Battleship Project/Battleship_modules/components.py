import random
from random import randint
import json

"""This module has functions which initalise the objects needed to play the battleship game, board, battleships. 
It also contains a function to place the ships"""

def initialise_board(size:int =10):
    """
    Takes a paraameter, size, creates a 2d array of size size*size. Returns this array.

    :param size: An integer that dictates the number of rows and columns in the 2d array
    """
    while True:
        try:
            int(size)
            break
        except TypeError or ValueError:
            size = int(input())

    board = [[None for i in range(size)] for i in range(size)]
    return board


def create_battleships(filename:str = "Battleship_modules/componentfiles/battleships.txt"):
    """
    Takes a file name as a parameter, reads this file and creates a dictionary.
    This dictionary has keys as ship names and corresponding values of the ships size 

    :param filenmae: The path to the .txt file which contains data on ships 
       """
    #initialise dictionary and open file#
    ships_dict = {}
    try:
        f = open(filename,'r')
        line = f.readline().strip()
        #reads each line in .txt file, removes colon using .split()
    except FileNotFoundError:
        print("ERROR: File has not been found, change path or change filename")
        #If file not found shows error message
    while line != "":
        # removes colon using .split() and stores return values as the corresponding shipname and length
        shipname, length = line.split(':')
        ships_dict[shipname] = int(length)
        line = f.readline().strip()
    f.close()
    #ships_dict = {"ship name": number of pieces that make up this ship}
    return ships_dict

def place_battleships(board, ships: dict, type:str ='simple'):
    """
    Places battleship in one of three ways simple, random, or custom.

    :param board: Is the 2d array that represents the board
    :param ships: Dictionary containing data on ships
    :param type: A string of either "simple", "custom" or "random" to determine how ships will be placed
    """
    
    while type!= "simple" and type!= "custom" and type!="random":
        type = input("Please enter either simple custom or random")
    # Verifying input #
    if type == 'simple':
       row = -1
       for ship in ships:
        #for every ship, place it on the next line horizontally #
        row = row + 1
        for i in range(ships[ship]):
               board[row][i] = ship
    elif type == "random":
        ships_key = iter(ships)
        ships_placed = 0
        size = len(board)
        #Ships key is the type of ships, "submarine" etc.
        # Ships placed helps verify if all ships have been placed # 
        while ships_placed != len(ships):
            # while not all ships have been placed #
            ship_placed = False
            #ship_placed is an indicator if the current ships that is being placed has finished being placed #
            ship = next(ships_key)
            while ship_placed == False:
                direction = random.choice(['horizontal', 'vertical'])
                # choose randomly between horizontal and vertical#
                coordinates = []
                placeable = True
                if direction == 'horizontal':
                    column_limit =size - ships[ship]
                    # makes sure that ship does not go outside of board #
                    row = randint(0,size -1)
                    column = randint(0, column_limit)
                    for segment in range(ships[ship]):
                        if board[row][column] != None:
                            #check if there is a ship there already #
                            coordinates = []
                            placeable = False
                            break
                        else:
                            #add this free coordinate space to coordinates
                            coordinates.append([row,column])
                            column = column + 1
                    if placeable == True:        
                        for coordinate in coordinates:
                            board[coordinate[0]][coordinate[1]] = ship 
                        ships_placed = ships_placed + 1
                        ship_placed = True
                #if ship placed == false then the process repeats for the same ship, function does not itterate to next ship because of ship_placed value #
                else:
                    # same process but for vertical
                    row_limit = size - ships[ship]
                    row = randint(0,row_limit)
                    column = randint(0, size - 1)
                    for segment in range(ships[ship]):
                            if board[row][column] != None:
                                coordinates = []
                                placeable = False
                                break
                            else:
                                coordinates.append([row,column])
                                row = row + 1
                    if placeable == True:        
                        for coordinate in coordinates:
                            board[coordinate[0]][coordinate[1]] = ship 
                        ships_placed = ships_placed + 1
                        ship_placed = True
    else:
        with open('Battleship_modules/componentfiles/placement.json','r') as file:
            #uses a json file to place ships #
            configdata = json.loads(file.read())
            # reads file #
            for ship in ships:
                counter = 0 
                startX = int(configdata[ship][0])
                startY = int(configdata[ship][1]) 
                if configdata[ship][2] == "h":
                    for placement in range(int(ships[ship])):
                        board[startY][startX + counter] = ship
                        # placement of ship#
                        counter = counter + 1
                else:
                    for placement in range(int(ships[ship])):
                        board[startY+counter][startX] = ship
                        #placement of ship#
                        counter = counter + 1
    return board




















