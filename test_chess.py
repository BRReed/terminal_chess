import unittest
from chess import Chess

class TestPieceMovement(unittest.TestCase):

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

class TestCoordsNotEqual(unittest.TestCase):

    def test_coords_are_equal(self):
        self.assertFalse(c.coords_not_equal('11', '11'))
        self.assertFalse(c.coords_not_equal('65', '65'))
        self.assertFalse(c.coords_not_equal('42', '42'))
        self.assertFalse(c.coords_not_equal('87', '87'))
        self.assertFalse(c.coords_not_equal('73', '73'))

    def test_coords_are_not_equal(self):
        self.assertTrue(c.coords_not_equal('11', '22'))
        self.assertTrue(c.coords_not_equal('90', '91'))
        self.assertTrue(c.coords_not_equal('65', '54'))
        self.assertTrue(c.coords_not_equal('12', '21'))

class TestCheckCoords(unittest.TestCase):
    
    def test_ints(self):
        self.assertTrue(c.check_coords('11'))
        self.assertTrue(c.check_coords('99'))
    
    def test_symb(self):
        self.assertFalse(c.check_coords('1['))
        self.assertFalse(c.check_coords('[3'))
        self.assertFalse(c.check_coords('5?'))
        self.assertFalse(c.check_coords('1/'))
        self.assertFalse(c.check_coords('1\\'))
    
    def test_alpha(self):
        self.assertFalse(c.check_coords('1g'))
        self.assertFalse(c.check_coords('h6'))
        self.assertFalse(c.check_coords('jj'))
        self.assertFalse(c.check_coords('l2'))

class TestIsBlack(unittest.TestCase):

    def test_black(self):
        self.assertTrue(c.is_black('\033[38;2;0;0;0m'))
    
    def test_white(self):
        self.assertFalse(c.is_black('\033[38;2;255;255;255m'))
    
    def test_empty(self):
        self.assertFalse(c.is_black('   '))

class TestIsFriendly(unittest.TestCase):

    def test_black_to_black(self):
        self.assertTrue(c.is_friendly('87', c.is_black(c.b_q)))
        self.assertTrue(c.is_friendly('71', c.is_black(c.b_p)))
    
    def test_white_to_white(self):
        self.assertTrue(c.is_friendly('17', c.is_black(c.w_q)))
        self.assertTrue(c.is_friendly('28', c.is_black(c.w_k)))

    def test_black_to_white(self):
        self.assertFalse(c.is_friendly('17', c.is_black(c.b_n)))
        self.assertFalse(c.is_friendly('22', c.is_black(c.b_r)))

    def test_white_to_black(self):
        self.assertFalse(c.is_friendly('87', c.is_black(c.w_p)))
        self.assertFalse(c.is_friendly('72', c.is_black(c.w_q)))

class TestIsEnemy(unittest.TestCase):
    
    def test_black_to_black(self):
        self.assertFalse(c.is_enemy('81', c.is_black(c.b_k)))
        self.assertFalse(c.is_enemy('76', c.is_black(c.b_q)))

    def test_white_to_white(self):
        self.assertFalse(c.is_enemy('12', c.is_black(c.w_p)))
        self.assertFalse(c.is_enemy('26', c.is_black(c.w_r)))
    
    def test_black_to_white(self):
        self.assertTrue(c.is_enemy('12', c.is_black(c.b_n)))
        self.assertTrue(c.is_enemy('28', c.is_black(c.b_b)))

    def test_white_to_black(self):
        self.assertTrue(c.is_enemy('86', c.is_black(c.w_p)))
        self.assertTrue(c.is_enemy('74', c.is_black(c.w_k)))

class TestIsEmpty(unittest.TestCase):
    
    def test_space_is_empty(self):
        self.assertTrue(c.is_empty('67'))
        self.assertTrue(c.is_empty('43'))

    def test_space_is_occupied(self):
        self.assertFalse(c.is_empty('14'))
        self.assertFalse(c.is_empty('83'))

class TestAddCoords(unittest.TestCase):
    
    def test_shift_add(self):
        self.assertEqual(c.add_coords('11', (1, 1)), '22')
        self.assertEqual(c.add_coords('32', (4, 3)), '75')

    def test_shift_subtract(self):
        self.assertEqual(c.add_coords('45', (-1, -3)), '32')
        self.assertEqual(c.add_coords('86', (-4, 0)), '46')

    

class TestMovesDir(unittest.TestCase):

    def test_move_diag_rposi_cposi_black(self):
        self.assertEqual(c.moves_dir('55', (1, 1), True),
                                     ['66'])
        self.assertEqual(c.moves_dir('31', (1, 1), True),
                                     ['42', '53', '64'])
        self.assertEqual(c.moves_dir('47', (1, 1), True),
                                     ['58'])
    
    def test_move_diag_rposi_cposi_white(self):
        self.assertEqual(c.moves_dir('55', (1, 1), False),
                                     ['66', '77'])
        self.assertEqual(c.moves_dir('31', (1, 1), False),
                                     ['42', '53', '64', '75'])
        self.assertEqual(c.moves_dir('47', (1, 1), False),
                                     ['58'])

    def test_move_diag_rposi_cneg_black(self):
        self.assertEqual(c.moves_dir('55', (1, -1), True),
                                     ['64'])
        self.assertEqual(c.moves_dir('36', (1, -1), True),
                                     ['45', '54', '63'])
        self.assertEqual(c.moves_dir('47', (1, -1), True),
                                     ['56', '65'])

    def test_move_diag_rposi_cneg_white(self):
        self.assertEqual(c.moves_dir('55', (1, -1), False),
                                     ['64', '73'])
        self.assertEqual(c.moves_dir('36', (1, -1), False),
                                     ['45', '54', '63', '72'])
        self.assertEqual(c.moves_dir('47', (1, -1), False),
                                     ['56', '65', '74'])

    def test_move_diag_rneg_cneg_black(self):
        self.assertEqual(c.moves_dir('44', (-1, -1), True),
                                     ['33', '22'])
        self.assertEqual(c.moves_dir('78', (-1, -1), True),
                                     ['67', '56', '45', '34', '23'])
        self.assertEqual(c.moves_dir('31', (-1, -1), True),
                                     [])
    
    def test_move_diag_rneg_cneg_white(self):
        self.assertEqual(c.moves_dir('44', (-1, -1), False),
                                     ['33'])
        self.assertEqual(c.moves_dir('78', (-1, -1), False),
                                     ['67', '56', '45', '34'])
        self.assertEqual(c.moves_dir('31', (-1, -1), False),
                                     [])

    def test_move_vert_rneg_cconst_black(self):
        self.assertEqual(c.moves_dir('44', (-1, 0), True),
                                     ['34', '24'])
        self.assertEqual(c.moves_dir('78', (-1, 0), True),
                                     ['68', '58', '48', '38', '28'])
        self.assertEqual(c.moves_dir('31', (-1, 0), True),
                                     ['21'])
    
    def test_move_vert_rneg_cconst_white(self):
        self.assertEqual(c.moves_dir('44', (-1, 0), False),
                                     ['34'])
        self.assertEqual(c.moves_dir('78', (-1, 0), False),
                                     ['68', '58', '48', '38'])
        self.assertEqual(c.moves_dir('31', (-1, 0), False),
                                     [])

    def test_move_vert_rposi_cconst_black(self):
        self.assertEqual(c.moves_dir('44', (1, 0), True),
                                     ['54', '64'])
        self.assertEqual(c.moves_dir('78', (1, 0), True),
                                     [])
        self.assertEqual(c.moves_dir('31', (1, 0), True),
                                     ['41', '51', '61'])
    
    def test_move_vert_rposi_cconst_white(self):
        self.assertEqual(c.moves_dir('44', (1, 0), False),
                                     ['54', '64', '74'])
        self.assertEqual(c.moves_dir('78', (1, 0), False),
                                     ['88'])
        self.assertEqual(c.moves_dir('31', (1, 0), False),
                                     ['41', '51', '61', '71'])
        
    def test_move_horz_rconst_cneg_black(self):
        self.assertEqual(c.moves_dir('31', (0, -1), True),
                                     [])
        self.assertEqual(c.moves_dir('78', (0, -1), True),
                                     [])
        self.assertEqual(c.moves_dir('44', (0, -1), True),
                                     ['43', '42', '41'])

    def test_move_horz_rconst_cneg_white(self):
        self.assertEqual(c.moves_dir('31', (0, -1), False),
                                     [])
        self.assertEqual(c.moves_dir('78', (0, -1), False),
                                     ['77'])
        self.assertEqual(c.moves_dir('44', (0, -1), False),
                                     ['43', '42', '41'])

    def test_move_horz_rconst_cposi_black(self):
        self.assertEqual(c.moves_dir('32', (0, 1), True),
                                     ['33', '34', '35', '36', '37', '38'])
        self.assertEqual(c.moves_dir('76', (0, 1), True),
                                     [])
        self.assertEqual(c.moves_dir('44', (0, 1), True),
                                     ['45', '46', '47', '48'])

    def test_move_horz_rconst_cposi_white(self):
        self.assertEqual(c.moves_dir('31', (0, 1), False),
                                    ['32', '33', '34', '35', '36', '37', '38'])
        self.assertEqual(c.moves_dir('76', (0, 1), False),
                                    ['77'])
        self.assertEqual(c.moves_dir('44', (0, 1), False),
                                    ['45', '46', '47', '48'])

class TestPossibleMoves(unittest.TestCase):
    pass

if __name__ == '__main__':
    c = Chess()
    unittest.main()
