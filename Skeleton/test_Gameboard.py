import unittest
from Gameboard import Gameboard

class Test_TestGameboard(unittest.TestCase):
    def test_correct_move_simple(self):
        # Checks single correct move for each player
        game = Gameboard()
        game.player1 = "red"
        game.player2 = "yellow"

        p1_m = 'col1'
        p1_valid_status = game.validate_move(p1_m, game.current_turn)
        self.assertFalse(p1_valid_status[0])
        
        added_pos = game.add_move(p1_m, game.player1)
        game.check_winner(added_pos)
        game.switch_turn()

        p2_m = 'col2'
        p2_valid_status = game.validate_move(p2_m, game.current_turn)
        self.assertFalse(p2_valid_status[0])

    def test_correct_moves_complex(self):
        # Checks for all correct moves in a tie board
        moves = ['col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7',
                'col2', 'col1', 'col1', 'col2', 'col2', 'col1', 'col1',
                'col2', 'col1', 'col2', 'col6', 'col3', 'col3', 'col3',
                'col3', 'col4', 'col4', 'col4', 'col4', 'col5', 'col5',
                'col5', 'col5', 'col4', 'col3', 'col7', 'col7', 'col7',
                'col7', 'col6', 'col6', 'col6', 'col7', 'col6', 'col5']
        game = Gameboard()
        game.player1 = "red"
        game.player2 = "yellow"
        
        while game.remaining_moves > 0:
            m = moves.pop(0)
            p_valid_status = game.validate_move(m, game.current_turn)
            self.assertFalse(p_valid_status[0])

            pcolor = ""
            if game.current_turn == 'p1':
                pcolor = game.player1
            else:
                pcolor = game.player2
            added_pos = game.add_move(m, pcolor)
            game.check_winner(added_pos)
            self.assertEqual(game.game_result, "")
            game.switch_turn()

    def test_invalid_not_player_turn_simple(self):
        # Checks that player cannot make a move when it is not his/her turn
        game = Gameboard()
        game.player1 = "red"
        game.player2 = "yellow"
        
        p2_valid_status = game.validate_move('col1', 'p2')
        self.assertEqual(p2_valid_status[1], "Not your turn")

        p1_m = 'col1'
        added_pos = game.add_move(p1_m, game.player1)
        game.switch_turn()

        p1_valid_status = game.validate_move('col1', 'p1')
        self.assertEqual(p1_valid_status[1], "Not your turn")

    def test_invalid_not_player_turn_complex(self):
        # Checks that for every turn (42 total turns) player cannot make
        # move when it is not his/her turn
        game = Gameboard()
        game.player1 = "red"
        game.player2 = "yellow"
        moves = ['col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7',
                'col2', 'col1', 'col1', 'col2', 'col2', 'col1', 'col1',
                'col2', 'col1', 'col2', 'col6', 'col3', 'col3', 'col3',
                'col3', 'col4', 'col4', 'col4', 'col4', 'col5', 'col5',
                'col5', 'col5', 'col4', 'col3', 'col7', 'col7', 'col7',
                'col7', 'col6', 'col6', 'col6', 'col7', 'col6', 'col5']
        
        while game.remaining_moves > 0:
            m = moves.pop(0)
            
            pcolor = ""
            wrong_person = ''
            if game.current_turn == 'p1':
                pcolor = game.player1
                wrong_person = 'p2'
            else:
                pcolor = game.player2
                wrong_person = 'p1'

            p_valid_status = game.validate_move(m, wrong_person)
            self.assertEqual(p_valid_status[1], "Not your turn")

            added_pos = game.add_move(m, pcolor)
            game.switch_turn()

    def test_invalid_winner_declared(self):
        # Checks that player cannot make move when winner already declared
        game = Gameboard()
        game.player1 = "red"
        game.player2 = "yellow"

        p1_m, p2_m = 'col1', 'col2'
        while len(game.game_result) == 0:
            m = ''
            pcolor = ""
            if game.current_turn == 'p1':
                m = p1_m
                pcolor = game.player1
            else:
                m = p2_m
                pcolor = game.player2
            added_pos = game.add_move(m, pcolor)
            game.check_winner(added_pos)
            game.switch_turn()

        p2_valid_status = game.validate_move(p2_m, 'p2')
        self.assertEqual(p2_valid_status[1], "Winner already declared")

        game.switch_turn()
        p1_valid_status = game.validate_move(p1_m, 'p1')
        self.assertEqual(p1_valid_status[1], "Winner already declared")
            



if __name__ == '__main__':
    unittest.main()
