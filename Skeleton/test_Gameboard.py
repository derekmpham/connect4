import unittest
from Gameboard import Gameboard

class Test_TestGameboard(unittest.TestCase):
    def test_simple_correct_move(self):
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

    def test_complex_correct_moves(self):
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


if __name__ == '__main__':
    unittest.main()
