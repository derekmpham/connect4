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

        if len(self.game_result) > 0:
            is_invalid = True
            err_message = "Winner already declared"
            return (is_invalid, err_message)

        return (is_invalid, err_message)

    def add_move(self, col, pcolor):
        i = int(col[-1]) - 1
        for r in reversed(range(len(self.board))):
            if self.board[r][i] == 0:
                self.board[r][i] = pcolor
                self.remaining_moves -= 1
                return (r, i)

    def check_winner(self, pos):
        r, c = pos[0], pos[1]
        pcolor = self.board[r][c]

        # Check horizontally
        for i in range(len(self.board[r])-3):
            if self.board[r][i] == pcolor and self.board[r][i+1] == pcolor and self.board[r][i+2] == pcolor and self.board[r][i+3] == pcolor:
                self.game_result = self.current_turn
                return

        # Check vertically
        for i in range(len(self.board)-3):
            if self.board[i][c] == pcolor and self.board[i+1][c] == pcolor and self.board[i+2][c] == pcolor and self.board[i+3][c] == pcolor:
                self.game_result = self.current_turn
                return

        # Check left diagonal
        for i in range(len(self.board[r])-3):
            for j in range(len(self.board)-3):
                if self.board[i][j] == pcolor and self.board[i+1][j+1] == pcolor and self.board[i+2][j+2] == pcolor and self.board[i+3][j+3] == pcolor:
                    self.game_result = self.current_turn
                    return

        # Check right diagonal
        for i in range(len(self.board[r])-3):
            for j in range(3, len(self.board)):
                if self.board[i][j] == pcolor and self.board[i+1][j-1] == pcolor and self.board[i+2][j-2] == pcolor and self.board[i+3][j-3] == pcolor:
                    self.game_result = self.current_turn
                    return

    def switch_turn(self):
        if self.current_turn == 'p1':
            self.current_turn = 'p2'
        else:
            self.current_turn = 'p1'


    

'''
Add Helper functions as needed to handle moves and update board and turns
'''


    
