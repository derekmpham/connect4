import unittest
import db


class Test_Testdb(unittest.TestCase):
    def test_first_moves(self):
        # Checks if database is properly added
        # after each player makes a move
        db.clear()
        db.init_db()
        p1m_ct = 'p2'
        p1m_b = str([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], ['red', 0, 0, 0, 0, 0, 0]])
        gr = ""
        p1, p2 = "red", "yellow"
        rm = 41
        p1_m = (p1m_ct, p1m_b, gr, p1, p2, rm)
        db.add_move(p1_m)
        s1 = db.getMove()
        self.assertEqual(s1, p1_m)

        p2m_ct = 'p1'
        p2m_b = str([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], ['red', 'yellow', 0, 0, 0, 0, 0]])
        rm = 40
        p2_m = (p2m_ct, p2m_b, gr, p1, p2, rm)
        db.add_move(p2_m)
        s2 = db.getMove()
        self.assertEqual(s2, p2_m)

    # def test_db_persists(self):
    #     # Checks if database persists from first test
    #     p2m_ct = 'p1'
    #     p2m_b = str([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], ['red', 'yellow', 0, 0, 0, 0, 0]])
    #     gr = ""
    #     p1, p2 = "red", "yellow"
    #     rm = 40
    #     last_move = (p2m_ct, p2m_b, gr, p1, p2, rm)
    #     s = db.getMove()
    #     self.assertEqual(s, last_move)
    #     db.clear()

    def test_db_fail_get_move(self):
        db.clear()
        s = db.getMove()
        self.assertEqual(s, None)




if __name__ == '__main__':
    unittest.main()
