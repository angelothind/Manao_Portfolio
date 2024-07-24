import random
from components import place_battleships, create_battleships, initialise_board
from game_engine import cli_coordinates_input, attack

players = {"Player":{"P_battleships":None, "P_board":None},
           "AI":{"AI_battleships":None, "AI_board":None} }
#Initialise a dictionary containing the data initial data to play a battleship board game #



def generate_attack():
    """
        Generate attack creates a non repeating set of coordinates
    """
    global attacks
    attacks =[]
    # Stores previous attack coordinates
    coordinate = (random.randint(0,len(players["Player"])-1),
                  random.randint(0,len(players["Player"])-1))
    #Creates random coordiantes
    while coordinate in attacks:
        coordinate = (random.randint(0,len(players["Player"]-1)),
                      random.randint(0,len(players["Player"]-1)))
        #Validates and makes sure that the coordinate created is not a repeat #
    attacks.append(coordinate)
    #adds the latest coordinate to the list so it can be checked in the future #
    return coordinate


def ai_opponent_game_loop():
    """Runs A command line version of battleship."""

    print("WELCOME TO BATTLESHIP GAME!!!")
    battleship = create_battleships()
    while True:
        # User inputs board size #
        try:
            board_size =  int(input("Please input your size greater than or equal to 10: "))
            while board_size < 10:
                board_size =  int(input("Please input your size GREATER than or EQUAL to 10: "))
            break
        except ValueError:
            print("size entered in not an integer, please enter an integer")
    
    players["Player"]["P_battleships"] = battleship
    players["Player"]["P_board"] = place_battleships(initialise_board(board_size), battleship,'custom')
    players["AI"]["AI_battleships"] = battleship
    players["AI"]["AI_board"] = place_battleships(initialise_board(board_size), battleship, 'random')
    # Initializes board and ships values for AI and player
    n_piecesleft_AI = 0

    for ship in battleship:
        n_piecesleft_AI = n_piecesleft_AI + battleship[ship]

    n_piecesleft_player = n_piecesleft_AI
    # Storing the number of hits until a player loses #
    while n_piecesleft_AI > 0 and n_piecesleft_player > 0:
        # While no one has lose: #
        player_coord = cli_coordinates_input()
        while player_coord[0] not in range(board_size) or player_coord[1] not in range(board_size):
                print("The coordinates given are not valid given size of board or may be negative")
                #Check if input is valid
                player_coord = cli_coordinates_input()  
        hit_miss = attack(player_coord, players["AI"]["AI_board"], players["AI"]["AI_battleships"])
        # hit_miss = boolean value as a result of running attack on the AI board
        if hit_miss == True:
            print("You Hit")
            n_piecesleft_AI = n_piecesleft_AI -1 
        else:
            print("You Missed")
        hit_miss = attack(generate_attack(),players["Player"]["P_board"],players["Player"]["P_battleships"])
        # hit_miss = boolean value as a result of running attack on the AI board #
        if hit_miss == True:
            print("AI Hit")
            n_piecesleft_player = n_piecesleft_player -1 
        else:
            print("AI Missed")

        for i in players["Player"]["P_board"]:
            line = ""
            for x in i:
                if x != None:
                    line = line + ("0 ") 
                else:
                    line = line + ("S ") 
            print(line)
        #Prints a representation of player's board #

    if n_piecesleft_AI == 0:
        print("YOUVE WON")
    else:
        print("YOUVE LOST")

