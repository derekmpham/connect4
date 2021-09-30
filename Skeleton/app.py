from flask import Flask, render_template, request, redirect, jsonify
from json import dump
from Gameboard import Gameboard
import db


app = Flask(__name__)

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

game = Gameboard()

'''
Implement '/' endpoint
Method Type: GET
return: template player1_connect.html and status = "Pick a Color."
Initial Webpage where gameboard is initialized
'''


@app.route('/', methods=['GET'])
def player1_connect():
    global game
    game = Gameboard()
    return render_template('player1_connect.html', status='Pick a Color.')


'''
Helper function that sends to all boards don't modify
'''


@app.route('/autoUpdate', methods=['GET'])
def updateAllBoards():
    try:
        return jsonify(move=game.board, winner=game.game_result,
                       color=game.player1)
    except Exception:
        return jsonify(move="")


'''
Implement '/p1Color' endpoint
Method Type: GET
return: template player1_connect.html and status = <Color picked>
Assign player1 their color
'''


@app.route('/p1Color', methods=['GET'])
def player1_config():
    color = request.args.get('color')
    game.player1 = color
    return render_template('player1_connect.html', status=color)


'''
Implement '/p2Join' endpoint
Method Type: GET
return: template p2Join.html and status = <Color picked> or Error
if P1 didn't pick color first

Assign player2 their color
'''


@app.route('/p2Join', methods=['GET'])
def p2Join():
    color = ""
    if game.player1 == "red":
        color = "yellow"
    elif game.player1 == "yellow":
        color = "red"
    else:
        color = "Error"
    game.player2 = color
    return render_template('p2Join.html', status=color)


'''
Implement '/move1' endpoint
Method Type: POST
return: jsonify (move=<CurrentBoard>,
invalid=True or False, winner = <currWinner>)
If move is valid --> invalid = False else invalid = True
If invalid == True, also return reason= <Why Move is Invalid>

Process Player 1's move
'''


@app.route('/move1', methods=['POST'])
def p1_move():
    m1 = request.get_json()
    valid_status = game.validate_move(m1['column'], 'p1')
    is_invalid = valid_status[0]
    if is_invalid:
        return jsonify(
            move=game.board, invalid=is_invalid,
            reason=valid_status[1], winner=game.game_result
            )
    else:
        added_pos = game.add_move(m1['column'], game.player1)
        game.check_winner(added_pos)
        game.switch_turn()
        return jsonify(
            move=game.board, invalid=is_invalid,
            winner=game.game_result
            )


'''
Same as '/move1' but instead proccess Player 2
'''


@app.route('/move2', methods=['POST'])
def p2_move():
    m2 = request.get_json()
    valid_status = game.validate_move(m2['column'], 'p2')
    is_invalid = valid_status[0]
    if is_invalid:
        return jsonify(
            move=game.board, invalid=is_invalid,
            reason=valid_status[1], winner=game.game_result
            )
    else:
        added_pos = game.add_move(m2['column'], game.player2)
        game.check_winner(added_pos)
        game.switch_turn()
        return jsonify(
            move=game.board, invalid=is_invalid,
            winner=game.game_result
            )


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
