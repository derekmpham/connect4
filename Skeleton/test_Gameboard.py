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

if __name__ == '__main__':
    unittest.main()
