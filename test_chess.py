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

class TestCoordsValid(unittest.TestCase):

    def test_valid_spaces(self):
        self.assertTrue(c.coords_valid('11'))
        self.assertTrue(c.coords_valid('12'))
        self.assertTrue(c.coords_valid('13'))
        self.assertTrue(c.coords_valid('14'))
        self.assertTrue(c.coords_valid('15'))
        self.assertTrue(c.coords_valid('16'))
        self.assertTrue(c.coords_valid('17'))
        self.assertTrue(c.coords_valid('18'))
        self.assertTrue(c.coords_valid('21'))
        self.assertTrue(c.coords_valid('22'))
        self.assertTrue(c.coords_valid('23'))
        self.assertTrue(c.coords_valid('24'))
        self.assertTrue(c.coords_valid('25'))
        self.assertTrue(c.coords_valid('26'))
        self.assertTrue(c.coords_valid('27'))
        self.assertTrue(c.coords_valid('28'))
        self.assertTrue(c.coords_valid('31'))
        self.assertTrue(c.coords_valid('32'))
        self.assertTrue(c.coords_valid('33'))
        self.assertTrue(c.coords_valid('34'))
        self.assertTrue(c.coords_valid('35'))
        self.assertTrue(c.coords_valid('36'))
        self.assertTrue(c.coords_valid('37'))
        self.assertTrue(c.coords_valid('38'))
        self.assertTrue(c.coords_valid('41'))
        self.assertTrue(c.coords_valid('42'))
        self.assertTrue(c.coords_valid('43'))
        self.assertTrue(c.coords_valid('44'))
        self.assertTrue(c.coords_valid('45'))
        self.assertTrue(c.coords_valid('46'))
        self.assertTrue(c.coords_valid('47'))
        self.assertTrue(c.coords_valid('48'))
        self.assertTrue(c.coords_valid('51'))
        self.assertTrue(c.coords_valid('52'))
        self.assertTrue(c.coords_valid('53'))
        self.assertTrue(c.coords_valid('54'))
        self.assertTrue(c.coords_valid('55'))
        self.assertTrue(c.coords_valid('56'))
        self.assertTrue(c.coords_valid('57'))
        self.assertTrue(c.coords_valid('58'))
        self.assertTrue(c.coords_valid('61'))
        self.assertTrue(c.coords_valid('62'))
        self.assertTrue(c.coords_valid('63'))
        self.assertTrue(c.coords_valid('64'))
        self.assertTrue(c.coords_valid('65'))
        self.assertTrue(c.coords_valid('66'))
        self.assertTrue(c.coords_valid('67'))
        self.assertTrue(c.coords_valid('68'))
        self.assertTrue(c.coords_valid('71'))
        self.assertTrue(c.coords_valid('72'))
        self.assertTrue(c.coords_valid('73'))
        self.assertTrue(c.coords_valid('74'))
        self.assertTrue(c.coords_valid('75'))
        self.assertTrue(c.coords_valid('76'))
        self.assertTrue(c.coords_valid('77'))
        self.assertTrue(c.coords_valid('78'))
        self.assertTrue(c.coords_valid('81'))
        self.assertTrue(c.coords_valid('82'))
        self.assertTrue(c.coords_valid('83'))
        self.assertTrue(c.coords_valid('84'))
        self.assertTrue(c.coords_valid('85'))
        self.assertTrue(c.coords_valid('86'))
        self.assertTrue(c.coords_valid('87'))
        self.assertTrue(c.coords_valid('88'))
    
    def test_invalid_spaces(self):
        self.assertFalse(c.coords_valid('00'))
        self.assertFalse(c.coords_valid('01'))
        self.assertFalse(c.coords_valid('02'))
        self.assertFalse(c.coords_valid('03'))
        self.assertFalse(c.coords_valid('04'))
        self.assertFalse(c.coords_valid('05'))
        self.assertFalse(c.coords_valid('06'))
        self.assertFalse(c.coords_valid('07'))
        self.assertFalse(c.coords_valid('08'))
        self.assertFalse(c.coords_valid('09'))
        self.assertFalse(c.coords_valid('90'))
        self.assertFalse(c.coords_valid('91'))
        self.assertFalse(c.coords_valid('92'))
        self.assertFalse(c.coords_valid('93'))
        self.assertFalse(c.coords_valid('94'))
        self.assertFalse(c.coords_valid('95'))
        self.assertFalse(c.coords_valid('96'))
        self.assertFalse(c.coords_valid('97'))
        self.assertFalse(c.coords_valid('98'))
        self.assertFalse(c.coords_valid('99'))
    
    def test_not_int(self):
        self.assertFalse(c.coords_valid('a1'))
        self.assertFalse(c.coords_valid('1a'))
        self.assertFalse(c.coords_valid('1['))
        self.assertFalse(c.coords_valid('[1'))
        self.assertFalse(c.coords_valid('1*'))
        self.assertFalse(c.coords_valid('*1'))

class TestMovePiece(unittest.TestCase):
    
    def test_move(self):
        pass
        
if __name__ == '__main__':
    c = Chess()
    unittest.main()
