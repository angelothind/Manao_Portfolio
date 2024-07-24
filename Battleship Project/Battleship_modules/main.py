from flask import Flask, request, render_template
from components import create_battleships, place_battleships, initialise_board
from game_engine import attack as attack_method
from flask.json import jsonify
import random
import json
app = Flask(__name__)


@app.route('/',methods=['GET'])
def root():
    global players_board
    players_board = place_battleships(initialise_board(board_size),ships=ships,type="custom")
    return render_template("main.html",player_board = players_board)

@app.route('/attack',methods=['GET'])
def process_attack():
    """Gets coordinates and processes them and sents a json object depending on if a ship was hit"""
    if request.args:
        x = request.args.get('x')
        y = request.args.get('y')
        # x and y are the coordinates that the player has picked #
        player_attack = (int(x),int(y))
        global attacks
        coordinate = (random.randint(0,9),
                    random.randint(0,9))
        while coordinate in attacks:
            coordinate = (random.randint(0,9), random.randint(0,9))
        attacks.append(coordinate)
        AI_attack = coordinate
        global num_AI_pieces, num_player_pieces
        if attack_method(player_attack,AI_board,AI_ships) == True :
            num_AI_pieces = num_AI_pieces - 1
            if num_AI_pieces == 0:
                return jsonify({"hit":True,"AI_Turn": AI_attack,"finished":"Player has won the game" })
            else:
                if attack_method(AI_attack,players_board,ships) == True:
                    num_player_pieces = num_player_pieces -1
                    if num_player_pieces == 0:
                        return jsonify({"hit":True,"AI_Turn": AI_attack,"finished":"AI has won the game" })
                return jsonify({"hit":True,"AI_Turn": AI_attack})
        else:
            if attack_method(AI_attack,players_board,ships) == True:
                num_player_pieces = num_player_pieces -1
                if num_player_pieces == 0:
                    return jsonify({"hit":False,"AI_Turn": AI_attack,"finished":"AI has won the game" })
                else:
                    return jsonify({"hit":False,"AI_Turn": AI_attack})
            return jsonify({"hit":False,"AI_Turn": AI_attack})



@app.route('/placement', methods=['GET', 'POST'])
def placement_interface():
    """Runs a URL to place ships on a board"""
    global config
    if request.method == 'GET':
        return render_template("placement.html",ships= ships, board_size = board_size)
    #if method is GET hen return the placement template #
    if request.method == 'POST':
        config = request.get_json()
        json_object = json.dumps(config)
        with open("Battleship_modules/componentfiles/placement.json", "w") as placementfile:
            placementfile.write(json_object)
        
    return jsonify({'message': 'Received'}), 200

if __name__ == '__main__':
    attacks = []
    ships = create_battleships()
    number_of_pieces = 0
    for ship in ships:
        number_of_pieces = number_of_pieces + ships[ship]
    num_player_pieces = number_of_pieces
    num_AI_pieces = num_player_pieces
    config = []
    board_size = 10
    AI_board = place_battleships(initialise_board(board_size),ships=ships,type="random")
    AI_ships = ships
    app.template_folder = "templates"   
    app.run()

