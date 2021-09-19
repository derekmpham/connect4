import db

class Gameboard():
    def __init__(self):
        self.player1 = ""
        self.player2 = ""
        self.board = [[0 for x in range(7)] for y in range(6)]
        self.game_result = ""
        self.current_turn = 'p1'
        self.remaining_moves = 42

    def validate_move(self, col, curr_turn):
        i = int(col[-1]) - 1
        c = [r[i] for r in self.board]
        is_invalid = False
        err_message = None
        if 0 not in c:
            is_invalid = True
            err_message = "Column filled"
            return (is_invalid, err_message)

        if curr_turn != self.current_turn:
            is_invalid = True
            err_message = "Not your turn"
            return (is_invalid, err_message)

        return (is_invalid, err_message)


    

'''
Add Helper functions as needed to handle moves and update board and turns
'''


    
