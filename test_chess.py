import unittest
from chess import Chess, BoardState


def reset_board():
    c.current_state = c.bs.create_start_state()

class TestPieceMovement(unittest.TestCase):

    def setUp(self):
        reset_board()

    def test_king_move(self):
        self.assertTrue(c.bs.piece_movement(c.wk, '22', '21'))
        self.assertTrue(c.bs.piece_movement(c.wk, '22', '12'))
        self.assertTrue(c.bs.piece_movement(c.wk, '22', '13'))
        self.assertTrue(c.bs.piece_movement(c.wk, '22', '32'))
        self.assertTrue(c.bs.piece_movement(c.wk, '22', '33'))
        self.assertTrue(c.bs.piece_movement(c.wk, '22', '11'))

        self.assertFalse(c.bs.piece_movement(c.wk, '22', '42'))
        self.assertFalse(c.bs.piece_movement(c.wk, '22', '24'))
        self.assertFalse(c.bs.piece_movement(c.wk, '22', '43'))
        self.assertFalse(c.bs.piece_movement(c.wk, '22', '44'))

    def test_queen_move(self):
        self.assertTrue(c.bs.piece_movement(c.wq, '33', '77'))
        self.assertTrue(c.bs.piece_movement(c.wq, '11', '88'))
        self.assertTrue(c.bs.piece_movement(c.wq, '33', '38'))
        self.assertTrue(c.bs.piece_movement(c.wq, '33', '83'))
        
        self.assertFalse(c.bs.piece_movement(c.wq, '33', '25'))
        self.assertFalse(c.bs.piece_movement(c.wq, '11', '32'))

    def test_bishop_move(self):
        self.assertTrue(c.bs.piece_movement(c.wb, '33', '77'))
        self.assertTrue(c.bs.piece_movement(c.wb, '34', '78'))
        self.assertTrue(c.bs.piece_movement(c.wb, '18', '81'))

        self.assertFalse(c.bs.piece_movement(c.wb, '11', '12'))
        self.assertFalse(c.bs.piece_movement(c.wb, '15', '32'))

    def test_knight_move(self):
        self.assertTrue(c.bs.piece_movement(c.wn, '11', '23'))
        self.assertTrue(c.bs.piece_movement(c.wn, '11', '32'))

        self.assertFalse(c.bs.piece_movement(c.wn, '11', '33'))
        self.assertFalse(c.bs.piece_movement(c.wn, '11', '87'))

    def test_rook_move(self):
        self.assertTrue(c.bs.piece_movement(c.wr, '11', '17'))
        self.assertTrue(c.bs.piece_movement(c.wr, '11', '71'))

        self.assertFalse(c.bs.piece_movement(c.wr, '11', '27'))
        self.assertFalse(c.bs.piece_movement(c.wr, '11', '56'))

    def test_pawn_white_move(self):
        self.assertTrue(c.bs.piece_movement(c.wp, '11', '21'))
        self.assertTrue(c.bs.piece_movement(c.wp, '11', '22'))
        self.assertTrue(c.bs.piece_movement(c.wp, '22', '31'))
        self.assertTrue(c.bs.piece_movement(c.wp, '22', '33'))

        self.assertFalse(c.bs.piece_movement(c.wp, '22', '23'))
        self.assertFalse(c.bs.piece_movement(c.wp, '22', '42'))

    def test_pawn_black_move(self):
        self.assertTrue(c.bs.piece_movement(c.bp, '21', '11'))
        self.assertTrue(c.bs.piece_movement(c.bp, '22', '11'))
        self.assertTrue(c.bs.piece_movement(c.bp, '31', '22'))
        self.assertTrue(c.bs.piece_movement(c.bp, '33', '22'))

        self.assertFalse(c.bs.piece_movement(c.wp, '23', '22'))
        self.assertFalse(c.bs.piece_movement(c.wp, '42', '22'))


class TestCoordsValid(unittest.TestCase):

    def setUp(self):
        reset_board()

    def test_valid_spaces(self):
        self.assertTrue(c.bs.coords_valid('11'))
        self.assertTrue(c.bs.coords_valid('12'))
        self.assertTrue(c.bs.coords_valid('13'))
        self.assertTrue(c.bs.coords_valid('14'))
        self.assertTrue(c.bs.coords_valid('15'))
        self.assertTrue(c.bs.coords_valid('16'))
        self.assertTrue(c.bs.coords_valid('17'))
        self.assertTrue(c.bs.coords_valid('18'))
        self.assertTrue(c.bs.coords_valid('21'))
        self.assertTrue(c.bs.coords_valid('22'))
        self.assertTrue(c.bs.coords_valid('23'))
        self.assertTrue(c.bs.coords_valid('24'))
        self.assertTrue(c.bs.coords_valid('25'))
        self.assertTrue(c.bs.coords_valid('26'))
        self.assertTrue(c.bs.coords_valid('27'))
        self.assertTrue(c.bs.coords_valid('28'))
        self.assertTrue(c.bs.coords_valid('31'))
        self.assertTrue(c.bs.coords_valid('32'))
        self.assertTrue(c.bs.coords_valid('33'))
        self.assertTrue(c.bs.coords_valid('34'))
        self.assertTrue(c.bs.coords_valid('35'))
        self.assertTrue(c.bs.coords_valid('36'))
        self.assertTrue(c.bs.coords_valid('37'))
        self.assertTrue(c.bs.coords_valid('38'))
        self.assertTrue(c.bs.coords_valid('41'))
        self.assertTrue(c.bs.coords_valid('42'))
        self.assertTrue(c.bs.coords_valid('43'))
        self.assertTrue(c.bs.coords_valid('44'))
        self.assertTrue(c.bs.coords_valid('45'))
        self.assertTrue(c.bs.coords_valid('46'))
        self.assertTrue(c.bs.coords_valid('47'))
        self.assertTrue(c.bs.coords_valid('48'))
        self.assertTrue(c.bs.coords_valid('51'))
        self.assertTrue(c.bs.coords_valid('52'))
        self.assertTrue(c.bs.coords_valid('53'))
        self.assertTrue(c.bs.coords_valid('54'))
        self.assertTrue(c.bs.coords_valid('55'))
        self.assertTrue(c.bs.coords_valid('56'))
        self.assertTrue(c.bs.coords_valid('57'))
        self.assertTrue(c.bs.coords_valid('58'))
        self.assertTrue(c.bs.coords_valid('61'))
        self.assertTrue(c.bs.coords_valid('62'))
        self.assertTrue(c.bs.coords_valid('63'))
        self.assertTrue(c.bs.coords_valid('64'))
        self.assertTrue(c.bs.coords_valid('65'))
        self.assertTrue(c.bs.coords_valid('66'))
        self.assertTrue(c.bs.coords_valid('67'))
        self.assertTrue(c.bs.coords_valid('68'))
        self.assertTrue(c.bs.coords_valid('71'))
        self.assertTrue(c.bs.coords_valid('72'))
        self.assertTrue(c.bs.coords_valid('73'))
        self.assertTrue(c.bs.coords_valid('74'))
        self.assertTrue(c.bs.coords_valid('75'))
        self.assertTrue(c.bs.coords_valid('76'))
        self.assertTrue(c.bs.coords_valid('77'))
        self.assertTrue(c.bs.coords_valid('78'))
        self.assertTrue(c.bs.coords_valid('81'))
        self.assertTrue(c.bs.coords_valid('82'))
        self.assertTrue(c.bs.coords_valid('83'))
        self.assertTrue(c.bs.coords_valid('84'))
        self.assertTrue(c.bs.coords_valid('85'))
        self.assertTrue(c.bs.coords_valid('86'))
        self.assertTrue(c.bs.coords_valid('87'))
        self.assertTrue(c.bs.coords_valid('88'))
    
    def test_invalid_spaces(self):
        self.assertFalse(c.bs.coords_valid('00'))
        self.assertFalse(c.bs.coords_valid('01'))
        self.assertFalse(c.bs.coords_valid('02'))
        self.assertFalse(c.bs.coords_valid('03'))
        self.assertFalse(c.bs.coords_valid('04'))
        self.assertFalse(c.bs.coords_valid('05'))
        self.assertFalse(c.bs.coords_valid('06'))
        self.assertFalse(c.bs.coords_valid('07'))
        self.assertFalse(c.bs.coords_valid('08'))
        self.assertFalse(c.bs.coords_valid('09'))
        self.assertFalse(c.bs.coords_valid('90'))
        self.assertFalse(c.bs.coords_valid('91'))
        self.assertFalse(c.bs.coords_valid('92'))
        self.assertFalse(c.bs.coords_valid('93'))
        self.assertFalse(c.bs.coords_valid('94'))
        self.assertFalse(c.bs.coords_valid('95'))
        self.assertFalse(c.bs.coords_valid('96'))
        self.assertFalse(c.bs.coords_valid('97'))
        self.assertFalse(c.bs.coords_valid('98'))
        self.assertFalse(c.bs.coords_valid('99'))

class TestCoordsNotEqual(unittest.TestCase):

    def setUp(self):
        reset_board()

    def test_coords_are_equal(self):
        self.assertFalse(c.bs.coords_not_equal('11', '11'))
        self.assertFalse(c.bs.coords_not_equal('65', '65'))
        self.assertFalse(c.bs.coords_not_equal('42', '42'))
        self.assertFalse(c.bs.coords_not_equal('87', '87'))
        self.assertFalse(c.bs.coords_not_equal('73', '73'))

    def test_coords_are_not_equal(self):
        self.assertTrue(c.bs.coords_not_equal('11', '22'))
        self.assertTrue(c.bs.coords_not_equal('90', '91'))
        self.assertTrue(c.bs.coords_not_equal('65', '54'))
        self.assertTrue(c.bs.coords_not_equal('12', '21'))

class TestCheckCoords(unittest.TestCase):

    def setUp(self):
        reset_board()

    def test_ints(self):
        self.assertTrue(c.bs.check_coords('11'))
        self.assertTrue(c.bs.check_coords('99'))
    
    def test_symb(self):
        self.assertFalse(c.bs.check_coords('1['))
        self.assertFalse(c.bs.check_coords('[3'))
        self.assertFalse(c.bs.check_coords('5?'))
        self.assertFalse(c.bs.check_coords('1/'))
        self.assertFalse(c.bs.check_coords('1\\'))
    
    def test_alpha(self):
        self.assertFalse(c.bs.check_coords('1g'))
        self.assertFalse(c.bs.check_coords('h6'))
        self.assertFalse(c.bs.check_coords('jj'))
        self.assertFalse(c.bs.check_coords('l2'))

class TestIsBlack(unittest.TestCase):


    def setUp(self):
        reset_board()

    def test_black(self):
        self.assertTrue(c.bs.is_black('\033[38;2;0;0;0m'))
    
    def test_white(self):
        self.assertFalse(c.bs.is_black('\033[38;2;255;255;255m'))
    
    def test_empty(self):
        self.assertFalse(c.bs.is_black('   '))

class TestIsFriendly(unittest.TestCase):


    def setUp(self):
        reset_board()

    def test_black_to_black(self):
        self.assertTrue(c.bs.is_friendly('87', c.bs.is_black(c.bq), c.current_state))
        self.assertTrue(c.bs.is_friendly('71', c.bs.is_black(c.bp), c.current_state))
    
    def test_white_to_white(self):
        self.assertTrue(c.bs.is_friendly('17', c.bs.is_black(c.wq), c.current_state))
        self.assertTrue(c.bs.is_friendly('28', c.bs.is_black(c.wk), c.current_state))

    def test_black_to_white(self):
        self.assertFalse(c.bs.is_friendly('17', c.bs.is_black(c.bn), c.current_state))
        self.assertFalse(c.bs.is_friendly('22', c.bs.is_black(c.br), c.current_state))

    def test_white_to_black(self):
        self.assertFalse(c.bs.is_friendly('87', c.bs.is_black(c.wp), c.current_state))
        self.assertFalse(c.bs.is_friendly('72', c.bs.is_black(c.wq), c.current_state))

class TestIsEnemy(unittest.TestCase):
    

    def setUp(self):
        reset_board()

    def test_black_to_black(self):
        self.assertFalse(c.bs.is_enemy('81', c.bs.is_black(c.bk), c.current_state))
        self.assertFalse(c.bs.is_enemy('76', c.bs.is_black(c.bq), c.current_state))

    def test_white_to_white(self):
        self.assertFalse(c.bs.is_enemy('12', c.bs.is_black(c.wp), c.current_state))
        self.assertFalse(c.bs.is_enemy('26', c.bs.is_black(c.wr), c.current_state))
    
    def test_black_to_white(self):
        self.assertTrue(c.bs.is_enemy('12', c.bs.is_black(c.bn), c.current_state))
        self.assertTrue(c.bs.is_enemy('28', c.bs.is_black(c.bb), c.current_state))

    def test_white_to_black(self):
        self.assertTrue(c.bs.is_enemy('86', c.bs.is_black(c.wp), c.current_state))
        self.assertTrue(c.bs.is_enemy('74', c.bs.is_black(c.wk), c.current_state))

class TestIsEmpty(unittest.TestCase):
    

    def setUp(self):
        reset_board()

    def test_space_is_empty(self):
        self.assertTrue(c.bs.is_empty('67', c.current_state))
        self.assertTrue(c.bs.is_empty('43', c.current_state))

    def test_space_is_occupied(self):
        self.assertFalse(c.bs.is_empty('14', c.current_state))
        self.assertFalse(c.bs.is_empty('83', c.current_state))

class TestAddCoords(unittest.TestCase):
    
    def setUp(self):
        reset_board()

    def test_shift_add(self):
        self.assertEqual(c.bs.add_coords('11', (1, 1)), '22')
        self.assertEqual(c.bs.add_coords('32', (4, 3)), '75')

    def test_shift_subtract(self):
        self.assertEqual(c.bs.add_coords('45', (-1, -3)), '32')
        self.assertEqual(c.bs.add_coords('86', (-4, 0)), '46')

    

class TestMovesDir(unittest.TestCase):


    def setUp(self):
        reset_board()

    def test_move_diag_rposi_cposi_black(self):
        self.assertEqual(c.bs.moves_dir('55', (1, 1), True, c.current_state),
                                     ['66'])
        self.assertEqual(c.bs.moves_dir('31', (1, 1), True, c.current_state),
                                     ['42', '53', '64'])
        self.assertEqual(c.bs.moves_dir('47', (1, 1), True, c.current_state),
                                     ['58'])
    
    def test_move_diag_rposi_cposi_white(self):
        self.assertEqual(c.bs.moves_dir('55', (1, 1), False, c.current_state),
                                     ['66', '77'])
        self.assertEqual(c.bs.moves_dir('31', (1, 1), False, c.current_state),
                                     ['42', '53', '64', '75'])
        self.assertEqual(c.bs.moves_dir('47', (1, 1), False, c.current_state),
                                     ['58'])

    def test_move_diag_rposi_cneg_black(self):
        self.assertEqual(c.bs.moves_dir('55', (1, -1), True, c.current_state),
                                     ['64'])
        self.assertEqual(c.bs.moves_dir('36', (1, -1), True, c.current_state),
                                     ['45', '54', '63'])
        self.assertEqual(c.bs.moves_dir('47', (1, -1), True, c.current_state),
                                     ['56', '65'])

    def test_move_diag_rposi_cneg_white(self):
        self.assertEqual(c.bs.moves_dir('55', (1, -1), False, c.current_state),
                                     ['64', '73'])
        self.assertEqual(c.bs.moves_dir('36', (1, -1), False, c.current_state),
                                     ['45', '54', '63', '72'])
        self.assertEqual(c.bs.moves_dir('47', (1, -1), False, c.current_state),
                                     ['56', '65', '74'])

    def test_move_diag_rneg_cneg_black(self):
        self.assertEqual(c.bs.moves_dir('44', (-1, -1), True, c.current_state),
                                     ['33', '22'])
        self.assertEqual(c.bs.moves_dir('78', (-1, -1), True, c.current_state),
                                     ['67', '56', '45', '34', '23'])
        self.assertEqual(c.bs.moves_dir('31', (-1, -1), True, c.current_state),
                                     [])
    
    def test_move_diag_rneg_cneg_white(self):
        self.assertEqual(c.bs.moves_dir('44', (-1, -1), False, c.current_state),
                                     ['33'])
        self.assertEqual(c.bs.moves_dir('78', (-1, -1), False, c.current_state),
                                     ['67', '56', '45', '34'])
        self.assertEqual(c.bs.moves_dir('31', (-1, -1), False, c.current_state),
                                     [])

    def test_move_vert_rneg_cconst_black(self):
        self.assertEqual(c.bs.moves_dir('44', (-1, 0), True, c.current_state),
                                     ['34', '24'])
        self.assertEqual(c.bs.moves_dir('78', (-1, 0), True, c.current_state),
                                     ['68', '58', '48', '38', '28'])
        self.assertEqual(c.bs.moves_dir('31', (-1, 0), True, c.current_state),
                                     ['21'])
    
    def test_move_vert_rneg_cconst_white(self):
        self.assertEqual(c.bs.moves_dir('44', (-1, 0), False, c.current_state),
                                     ['34'])
        self.assertEqual(c.bs.moves_dir('78', (-1, 0), False, c.current_state),
                                     ['68', '58', '48', '38'])
        self.assertEqual(c.bs.moves_dir('31', (-1, 0), False, c.current_state),
                                     [])

    def test_move_vert_rposi_cconst_black(self):
        self.assertEqual(c.bs.moves_dir('44', (1, 0), True, c.current_state),
                                     ['54', '64'])
        self.assertEqual(c.bs.moves_dir('78', (1, 0), True, c.current_state),
                                     [])
        self.assertEqual(c.bs.moves_dir('31', (1, 0), True, c.current_state),
                                     ['41', '51', '61'])
    
    def test_move_vert_rposi_cconst_white(self):
        self.assertEqual(c.bs.moves_dir('44', (1, 0), False, c.current_state),
                                     ['54', '64', '74'])
        self.assertEqual(c.bs.moves_dir('78', (1, 0), False, c.current_state),
                                     ['88'])
        self.assertEqual(c.bs.moves_dir('31', (1, 0), False, c.current_state),
                                     ['41', '51', '61', '71'])
        
    def test_move_horz_rconst_cneg_black(self):
        self.assertEqual(c.bs.moves_dir('31', (0, -1), True, c.current_state),
                                     [])
        self.assertEqual(c.bs.moves_dir('78', (0, -1), True, c.current_state),
                                     [])
        self.assertEqual(c.bs.moves_dir('44', (0, -1), True, c.current_state),
                                     ['43', '42', '41'])

    def test_move_horz_rconst_cneg_white(self):
        self.assertEqual(c.bs.moves_dir('31', (0, -1), False, c.current_state),
                                     [])
        self.assertEqual(c.bs.moves_dir('78', (0, -1), False, c.current_state),
                                     ['77'])
        self.assertEqual(c.bs.moves_dir('44', (0, -1), False, c.current_state),
                                     ['43', '42', '41'])

    def test_move_horz_rconst_cposi_black(self):
        self.assertEqual(c.bs.moves_dir('32', (0, 1), True, c.current_state),
                                     ['33', '34', '35', '36', '37', '38'])
        self.assertEqual(c.bs.moves_dir('76', (0, 1), True, c.current_state),
                                     [])
        self.assertEqual(c.bs.moves_dir('44', (0, 1), True, c.current_state),
                                     ['45', '46', '47', '48'])

    def test_move_horz_rconst_cposi_white(self):
        self.assertEqual(c.bs.moves_dir('31', (0, 1), False, c.current_state),
                                    ['32', '33', '34', '35', '36', '37', '38'])
        self.assertEqual(c.bs.moves_dir('76', (0, 1), False, c.current_state),
                                    ['77'])
        self.assertEqual(c.bs.moves_dir('44', (0, 1), False, c.current_state),
                                    ['45', '46', '47', '48'])

class TestFindPiece(unittest.TestCase):
    
    def setUp(self):
        reset_board()

    def test_find_white_queen(self):
        self.assertEqual(c.bs.find_piece(c.wq, False, c.current_state), '14')
    
    def test_find_black_queen(self):
        self.assertEqual(c.bs.find_piece(c.bq, True, c.current_state), '84')

class TestInCheck(unittest.TestCase):

    def setUp(self):
        reset_board()

    def test_black_king_in_check_white_knight(self):
        c.move_piece(c.wn, '12', '64')
        self.assertTrue(c.in_check(True, c.current_state))

    def test_white_king_in_check_black_queen(self):
        c.move_piece(c.wp, '24', '34')
        c.move_piece(c.bq, '84', '51')
        self.assertTrue(c.in_check(False, c.current_state))

    def test_white_king_not_in_check(self):
        self.assertFalse(c.in_check(False, c.current_state))
        c.move_piece(c.br, '81', '35')
        self.assertFalse(c.in_check(False, c.current_state))
        c.move_piece(c.bq, '84', '37')
        self.assertFalse(c.in_check(False, c.current_state))
        c.move_piece(c.bb, '86', '33')
        self.assertFalse(c.in_check(False, c.current_state))

    def test_black_king_not_in_check(self):
        self.assertFalse(c.in_check(True, c.current_state))
        c.move_piece(c.wb, '13', '67')
        self.assertFalse(c.in_check(True, c.current_state))
        c.move_piece(c.wq, '14', '65')
        self.assertFalse(c.in_check(True, c.current_state))

class TestCheckMate(unittest.TestCase):

    def setUp(self):
        reset_board()
    
    def test_black_king_not_mate(self):
        self.assertFalse(c.check_mate(True, c.current_state))
    
    def test_white_king_not_mate(self):
        self.assertFalse(c.check_mate(False, c.current_state))

    def test_black_king_mate_white_knight(self):
        c.move_piece(c.wn, '12', '64')
        self.assertTrue(c.check_mate(True, c.current_state))
    
    def test_white_king_mate_black_knight(self):
        c.move_piece(c.bn, '82', '34')
        self.assertTrue(c.check_mate(False, c.current_state))

    def test_white_king_not_in_check_black_queen_attacking(self):
        c.move_piece(c.bq, '84', '51')
        c.move_piece(c.wp, '24', '34')
        c.move_piece(c.wp, '25', '35')
        self.assertFalse(c.check_mate(False, c.current_state))
    
    

class TestPossibleMoves(unittest.TestCase):
    pass

if __name__ == '__main__':
    c = Chess()
    unittest.main()
