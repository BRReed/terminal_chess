import unittest
from chess import Chess

class TestPieceMovement(unittest.TestCase):

    def test_valid_space(self):
        self.assertFalse(c.piece_movement(c.w_k, '11', '01'))
        self.assertFalse(c.piece_movement(c.w_k, '11', '10'))
        self.assertFalse(c.piece_movement(c.w_k, '11', '00'))
        self.assertFalse(c.piece_movement(c.w_k, '11', '11'))
        self.assertFalse(c.piece_movement(c.w_q, '33', '99'))

    def test_king_move(self):
        self.assertTrue(c.piece_movement(c.w_k, '22', '21'))
        self.assertTrue(c.piece_movement(c.w_k, '22', '12'))
        self.assertTrue(c.piece_movement(c.w_k, '22', '13'))
        self.assertTrue(c.piece_movement(c.w_k, '22', '32'))
        self.assertTrue(c.piece_movement(c.w_k, '22', '33'))
        self.assertTrue(c.piece_movement(c.w_k, '22', '11'))

        self.assertFalse(c.piece_movement(c.w_k, '22', '42'))
        self.assertFalse(c.piece_movement(c.w_k, '22', '24'))
        self.assertFalse(c.piece_movement(c.w_k, '22', '43'))
        self.assertFalse(c.piece_movement(c.w_k, '22', '44'))

    def test_queen_move(self):
        self.assertTrue(c.piece_movement(c.w_q, '33', '77'))
        self.assertTrue(c.piece_movement(c.w_q, '11', '88'))
        self.assertTrue(c.piece_movement(c.w_q, '33', '38'))
        self.assertTrue(c.piece_movement(c.w_q, '33', '83'))
        
        self.assertFalse(c.piece_movement(c.w_q, '33', '25'))
        self.assertFalse(c.piece_movement(c.w_q, '11', '32'))

    def test_bishop_move(self):
        self.assertTrue(c.piece_movement(c.w_b, '33', '77'))
        self.assertTrue(c.piece_movement(c.w_b, '34', '78'))
        self.assertTrue(c.piece_movement(c.w_b, '18', '81'))

        self.assertFalse(c.piece_movement(c.w_b, '11', '12'))
        self.assertFalse(c.piece_movement(c.w_b, '15', '32'))

    def test_knight_move(self):
        self.assertTrue(c.piece_movement(c.w_n, '11', '23'))
        self.assertTrue(c.piece_movement(c.w_n, '11', '32'))

        self.assertFalse(c.piece_movement(c.w_n, '11', '33'))
        self.assertFalse(c.piece_movement(c.w_n, '11', '87'))

    def test_rook_move(self):
        self.assertTrue(c.piece_movement(c.w_r, '11', '17'))
        self.assertTrue(c.piece_movement(c.w_r, '11', '71'))

        self.assertFalse(c.piece_movement(c.w_r, '11', '27'))
        self.assertFalse(c.piece_movement(c.w_r, '11', '56'))

    def test_pawn_white_move(self):
        self.assertTrue(c.piece_movement(c.w_p, '11', '21'))
        self.assertTrue(c.piece_movement(c.w_p, '11', '22'))
        self.assertTrue(c.piece_movement(c.w_p, '22', '31'))
        self.assertTrue(c.piece_movement(c.w_p, '22', '33'))

        self.assertFalse(c.piece_movement(c.w_p, '22', '23'))
        self.assertFalse(c.piece_movement(c.w_p, '22', '42'))

    def test_pawn_black_move(self):
        self.assertTrue(c.piece_movement(c.b_p, '21', '11'))
        self.assertTrue(c.piece_movement(c.b_p, '22', '11'))
        self.assertTrue(c.piece_movement(c.b_p, '31', '22'))
        self.assertTrue(c.piece_movement(c.b_p, '33', '22'))

        self.assertFalse(c.piece_movement(c.w_p, '23', '22'))
        self.assertFalse(c.piece_movement(c.w_p, '42', '22'))
    
class TestPieceInCoords(unittest.TestCase):
    
    def test_white_piece_to_empty(self):
        self.assertEqual(c.piece_in_coords(c.w_p, '31'), (True, True))
        self.assertEqual(c.piece_in_coords(c.w_p, '68'), (True, True))

    def test_black_piece_to_empty(self):
        self.assertEqual(c.piece_in_coords(c.b_p, '31'), (True, True))
        self.assertEqual(c.piece_in_coords(c.b_p, '68'), (True, True))

    def test_white_piece_to_black(self):
        self.assertEqual(c.piece_in_coords(c.w_p, '81'), (True, False))
        self.assertEqual(c.piece_in_coords(c.w_p, '82'), (True, False))

    def test_black_piece_to_white(self):
        self.assertEqual(c.piece_in_coords(c.b_p, '11'), (True, False))
        self.assertEqual(c.piece_in_coords(c.b_p, '22'), (True, False))

    def test_white_piece_to_white(self):
        self.assertEqual(c.piece_in_coords(c.w_p, '21'), (False, False))
        self.assertEqual(c.piece_in_coords(c.w_p, '28'), (False, False))

    def test_black_piece_to_black(self):
        self.assertEqual(c.piece_in_coords(c.b_p, '87'), (False, False))
        self.assertEqual(c.piece_in_coords(c.b_p, '86'), (False, False))

class TestMovePiece(unittest.TestCase):
    
    def test_move(self):
        pass
        
if __name__ == '__main__':
    c = Chess()
    unittest.main()
