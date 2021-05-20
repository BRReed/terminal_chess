import unittest
from collections import Counter
from game_logic import Chess


def reset_board():
    c.current_state = c.bs.create_start_state()
    c.bs.w_king_side_castle = True
    c.bs.w_queen_side_castle = True
    c.bs.b_king_side_castle = True
    c.bs.b_queen_side_castle = True

def find_pieces(piece, is_black, board_state):
    spaces = []
    for space in board_state:
        if piece in board_state[space][2] and (
            is_black == c.bs.is_black(board_state[space][2])):
            spaces.append(space)
    return spaces

class TestPieceMovement(unittest.TestCase):

    def setUp(self):
        reset_board()

    def test_king_move(self):
        self.assertTrue(c.bs.piece_movement(c.bs.wk, '22', '21'))
        self.assertTrue(c.bs.piece_movement(c.bs.wk, '22', '12'))
        self.assertTrue(c.bs.piece_movement(c.bs.wk, '22', '13'))
        self.assertTrue(c.bs.piece_movement(c.bs.wk, '22', '32'))
        self.assertTrue(c.bs.piece_movement(c.bs.wk, '22', '33'))
        self.assertTrue(c.bs.piece_movement(c.bs.wk, '22', '11'))

        self.assertFalse(c.bs.piece_movement(c.bs.wk, '22', '42'))
        self.assertFalse(c.bs.piece_movement(c.bs.wk, '22', '24'))
        self.assertFalse(c.bs.piece_movement(c.bs.wk, '22', '43'))
        self.assertFalse(c.bs.piece_movement(c.bs.wk, '22', '44'))

    def test_queen_move(self):
        self.assertTrue(c.bs.piece_movement(c.bs.wq, '33', '77'))
        self.assertTrue(c.bs.piece_movement(c.bs.wq, '11', '88'))
        self.assertTrue(c.bs.piece_movement(c.bs.wq, '33', '38'))
        self.assertTrue(c.bs.piece_movement(c.bs.wq, '33', '83'))
        
        self.assertFalse(c.bs.piece_movement(c.bs.wq, '33', '25'))
        self.assertFalse(c.bs.piece_movement(c.bs.wq, '11', '32'))

    def test_bishop_move(self):
        self.assertTrue(c.bs.piece_movement(c.bs.wb, '33', '77'))
        self.assertTrue(c.bs.piece_movement(c.bs.wb, '34', '78'))
        self.assertTrue(c.bs.piece_movement(c.bs.wb, '18', '81'))

        self.assertFalse(c.bs.piece_movement(c.bs.wb, '11', '12'))
        self.assertFalse(c.bs.piece_movement(c.bs.wb, '15', '32'))

    def test_knight_move(self):
        self.assertTrue(c.bs.piece_movement(c.bs.wn, '11', '23'))
        self.assertTrue(c.bs.piece_movement(c.bs.wn, '11', '32'))

        self.assertFalse(c.bs.piece_movement(c.bs.wn, '11', '33'))
        self.assertFalse(c.bs.piece_movement(c.bs.wn, '11', '87'))

    def test_rook_move(self):
        self.assertTrue(c.bs.piece_movement(c.bs.wr, '11', '17'))
        self.assertTrue(c.bs.piece_movement(c.bs.wr, '11', '71'))

        self.assertFalse(c.bs.piece_movement(c.bs.wr, '11', '27'))
        self.assertFalse(c.bs.piece_movement(c.bs.wr, '11', '56'))

    def test_pawn_white_move(self):
        self.assertTrue(c.bs.piece_movement(c.bs.wp, '11', '21'))
        self.assertTrue(c.bs.piece_movement(c.bs.wp, '11', '22'))
        self.assertTrue(c.bs.piece_movement(c.bs.wp, '22', '31'))
        self.assertTrue(c.bs.piece_movement(c.bs.wp, '22', '33'))

        self.assertFalse(c.bs.piece_movement(c.bs.wp, '22', '23'))
        self.assertTrue(c.bs.piece_movement(c.bs.wp, '22', '42'))

    def test_pawn_black_move(self):
        self.assertTrue(c.bs.piece_movement(c.bs.bp, '21', '11'))
        self.assertTrue(c.bs.piece_movement(c.bs.bp, '22', '11'))
        self.assertTrue(c.bs.piece_movement(c.bs.bp, '31', '22'))
        self.assertTrue(c.bs.piece_movement(c.bs.bp, '33', '22'))

        self.assertFalse(c.bs.piece_movement(c.bs.wp, '23', '22'))
        self.assertFalse(c.bs.piece_movement(c.bs.wp, '42', '22'))


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
        self.assertTrue(c.bs.is_friendly('87', c.bs.is_black(c.bs.bq),
                                         c.current_state))
        self.assertTrue(c.bs.is_friendly('71', c.bs.is_black(c.bs.bp),
                                         c.current_state))
    
    def test_white_to_white(self):
        self.assertTrue(c.bs.is_friendly('17', c.bs.is_black(c.bs.wq),
                                         c.current_state))
        self.assertTrue(c.bs.is_friendly('28', c.bs.is_black(c.bs.wk),
                                         c.current_state))

    def test_black_to_white(self):
        self.assertFalse(c.bs.is_friendly('17', c.bs.is_black(c.bs.bn),
                                          c.current_state))
        self.assertFalse(c.bs.is_friendly('22', c.bs.is_black(c.bs.br),
                                          c.current_state))

    def test_white_to_black(self):
        self.assertFalse(c.bs.is_friendly('87', c.bs.is_black(c.bs.wp),
                                          c.current_state))
        self.assertFalse(c.bs.is_friendly('72', c.bs.is_black(c.bs.wq),
                                          c.current_state))

class TestIsEnemy(unittest.TestCase):
    

    def setUp(self):
        reset_board()

    def test_black_to_black(self):
        self.assertFalse(c.bs.is_enemy('81', c.bs.is_black(c.bs.bk),
                                       c.current_state))
        self.assertFalse(c.bs.is_enemy('76', c.bs.is_black(c.bs.bq),
                                       c.current_state))

    def test_white_to_white(self):
        self.assertFalse(c.bs.is_enemy('12', c.bs.is_black(c.bs.wp),
                                       c.current_state))
        self.assertFalse(c.bs.is_enemy('26', c.bs.is_black(c.bs.wr),
                                       c.current_state))
    
    def test_black_to_white(self):
        self.assertTrue(c.bs.is_enemy('12', c.bs.is_black(c.bs.bn),
                                      c.current_state))
        self.assertTrue(c.bs.is_enemy('28', c.bs.is_black(c.bs.bb),
                                      c.current_state))

    def test_white_to_black(self):
        self.assertTrue(c.bs.is_enemy('86', c.bs.is_black(c.bs.wp),
                                      c.current_state))
        self.assertTrue(c.bs.is_enemy('74', c.bs.is_black(c.bs.wk),
                                      c.current_state))

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
        self.assertEqual(c.bs.moves_dir('44', (-1, -1), False,
                                        c.current_state), ['33'])
        self.assertEqual(c.bs.moves_dir('78', (-1, -1), False, 
                         c.current_state),['67', '56', '45', '34'])
        self.assertEqual(c.bs.moves_dir('31', (-1, -1), False,
                         c.current_state), [])

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
        self.assertEqual(c.bs.find_piece(c.bs.wq, False, c.current_state), 
                                         '14')
    
    def test_find_black_queen(self):
        self.assertEqual(c.bs.find_piece(c.bs.bq, True, c.current_state), '84')

class TestInCheck(unittest.TestCase):

    def setUp(self):
        reset_board()

    def test_black_king_in_check_white_knight(self):
        c.move_piece(c.bs.wn, '12', '64')
        self.assertTrue(c.in_check(True, c.current_state))

    def test_white_king_in_check_black_queen(self):
        c.move_piece(c.bs.wp, '24', '34')
        c.move_piece(c.bs.bq, '84', '51')
        self.assertTrue(c.in_check(False, c.current_state))

    def test_white_king_not_in_check(self):
        self.assertFalse(c.in_check(False, c.current_state))
        c.move_piece(c.bs.br, '81', '35')
        self.assertFalse(c.in_check(False, c.current_state))
        c.move_piece(c.bs.bq, '84', '37')
        self.assertFalse(c.in_check(False, c.current_state))
        c.move_piece(c.bs.bb, '86', '33')
        self.assertFalse(c.in_check(False, c.current_state))

    def test_black_king_not_in_check(self):
        self.assertFalse(c.in_check(True, c.current_state))
        c.move_piece(c.bs.wb, '13', '67')
        self.assertFalse(c.in_check(True, c.current_state))
        c.move_piece(c.bs.wq, '14', '65')
        self.assertFalse(c.in_check(True, c.current_state))

class TestCheckMate(unittest.TestCase):

    def setUp(self):
        reset_board()
    
    def test_black_king_not_mate(self):
        self.assertFalse(c.check_mate(True, c.current_state))
    
    def test_white_king_not_mate(self):
        self.assertFalse(c.check_mate(False, c.current_state))

    def test_black_king_mate_white_knight(self):
        c.move_piece(c.bs.wn, '12', '64')
        self.assertTrue(c.check_mate(True, c.current_state))
    
    def test_white_king_mate_black_knight(self):
        c.move_piece(c.bs.bn, '82', '34')
        self.assertTrue(c.check_mate(False, c.current_state))

    def test_white_king_not_in_check_black_queen_attacking(self):
        c.move_piece(c.bs.bq, '84', '51')
        c.move_piece(c.bs.wp, '24', '34')
        c.move_piece(c.bs.wp, '25', '35')
        self.assertFalse(c.check_mate(False, c.current_state))
    
    

class TestPossibleMoves(unittest.TestCase):
    def setUp(self):
        reset_board()

    def test_white_king_no_moves(self):
        self.assertEqual(c.bs.possible_moves(c.bs.wk, '15', c.current_state), 
                                             [])

    def test_white_pawn_no_target(self):
        actual_moves = c.bs.possible_moves(c.bs.wp, '21', c.current_state)
        expected_moves = ['31', '41']
        actual = Counter(actual_moves)
        expected = Counter(expected_moves)
        assert actual == expected
        
    
    def test_white_pawn_blocked(self):
        c.move_piece(c.bs.bp, '71', '31')
        self.assertEqual(c.bs.possible_moves(c.bs.wp, '21', c.current_state),
                                             [])

    def test_black_pawn_target(self):
        c.move_piece(c.bs.wp, '22', '62')
        actual_moves = c.bs.possible_moves(c.bs.bp, '71', c.current_state)
        expected_moves = ['61', '62', '51']
        actual = Counter(actual_moves)
        expected = Counter(expected_moves)
        assert actual == expected

    def test_white_queen_from_45(self):
        c.move_piece(c.bs.wq, '14', '45')
        actual_moves = c.bs.possible_moves(c.bs.wq, '45', c.current_state)
        expected_moves = ['55', '65', '75', '35', '44', '43', '42', '41',
                          '46', '47', '48', '34', '56', '67', '78', '36',
                          '54', '63', '72']
        actual = Counter(actual_moves)
        expected = Counter(expected_moves)
        assert actual == expected
    
    def test_black_queen_from_52(self):
        c.move_piece(c.bs.bq, '84', '52')
        actual_moves = c.bs.possible_moves(c.bs.bq, '52', c.current_state)
        expected_moves = ['51', '61', '62', '63', '53', '54', '55', '56', 
                          '57', '58', '43', '34', '25', '42', '41', '32', 
                          '22']
        actual = Counter(actual_moves)
        expected = Counter(expected_moves)
        assert actual == expected

    def test_white_bishop_from_44(self):
        c.move_piece(c.bs.wb, '13', '44')
        actual_moves = c.bs.possible_moves(c.bs.wb, '44', c.current_state)
        expected_moves = ['33', '35', '53', '62', '71', '55', '66', '77']
        actual = Counter(actual_moves)
        expected = Counter(expected_moves)
        assert actual == expected

    def test_black_knight_from_33(self):
        c.move_piece(c.bs.bn, '82', '33')
        actual_moves = c.bs.possible_moves(c.bs.bn, '33', c.current_state)
        expected_moves = ['12', '14', '21', '25', '41', '45', '52', '54']
        actual = Counter(actual_moves)
        expected = Counter(expected_moves)
        assert actual == expected

    def test_black_rook_from_56(self):
        c.move_piece(c.bs.br, '88', '56')
        actual_moves = c.bs.possible_moves(c.bs.br, '56', c.current_state)
        expected_moves = ['66', '46', '36', '26', '57', '58', '55', '54', 
                          '53', '52', '51']
        actual = Counter(actual_moves)
        expected = Counter(expected_moves)
        assert actual == expected

    def test_white_king_from_44(self):
        c.move_piece(c.bs.wk, '15', '44')
        actual_moves = c.bs.possible_moves(c.bs.wk, '44', c.current_state)
        expected_moves = ['53', '54', '55', '43', '45', '35', '34', '33']
        actual = Counter(actual_moves)
        expected = Counter(expected_moves)
        assert actual == expected

class TestBlockCheck(unittest.TestCase):
    def setUp(self):
        reset_board()
        self.test_passed = False

    def test_black_block_check_white_bishop(self):
        c.move_piece(c.bs.bp, '74', '54')
        c.move_piece(c.bs.wb, '13', '65')
        self.assertTrue(c.bs.block_check(True, c.current_state))

    def test_black_block_check_knight_takes_knight_attacker(self):
        c.move_piece(c.bs.bp, '73', '53')
        c.move_piece(c.bs.bp, '75', '55')
        c.move_piece(c.bs.bn, '87', '75')
        c.move_piece(c.bs.bn, '82', '52')
        c.move_piece(c.bs.wn, '12', '64')
        self.assertTrue(c.bs.block_check(True, c.current_state))

    def test_black_block_check_king_takes_pawn_attacker(self):
        c.move_piece(c.bs.wp, '21', '45') 
        c.move_piece(c.bs.bk, '84', '54')
        self.assertTrue(c.bs.block_check(True, c.current_state))

    def test_black_block_check_king_moves_away(self):
        c.move_piece(c.bs.bk, '84', '54')
        c.move_piece(c.bs.wq, '14', '34')
        self.assertTrue(c.bs.block_check(True, c.current_state))

    def test_black_not_block_check_queen_attacker(self):
        c.move_piece(c.bs.wq, '14', '58')
        c.move_piece(c.bs.bp, '76', '66')
        c.move_piece(c.bs.bp, '77', '57')
        self.assertFalse(c.bs.block_check(True, c.current_state))

    def test_white_not_block_check_queen_attacker(self):
        c.bs.move_piece(c.bs.bq, '84', '48', c.current_state)
        c.bs.move_piece(c.bs.wp, '27', '47', c.current_state)
        c.bs.move_piece(c.bs.wp, '26', '46', c.current_state)
        self.assertFalse(c.bs.block_check(False, c.current_state))
    
    def test_black_not_block_check_pawn_protect_attacker(self):
        c.bs.move_piece(c.bs.wp, '27', '67', c.current_state)
        c.bs.move_piece(c.bs.bp, '76', '66', c.current_state)
        c.bs.move_piece(c.bs.wp, '26', '76', c.current_state)
        self.assertFalse(c.bs.block_check(True, c.current_state))

    def test_white_not_block_check_pawn_protect_attacker(self):
        c.bs.move_piece(c.bs.wp, '26', '36', c.current_state)
        c.bs.move_piece(c.bs.bp, '76', '26', c.current_state)
        c.bs.move_piece(c.bs.bp, '77', '37', c.current_state)
        self.assertFalse(c.bs.block_check(False, c.current_state))

class TestCheckCastling(unittest.TestCase):
    def setUp(self):
        reset_board()

    def test_white_king_side_spaces_occupied(self):
        self.assertFalse(c.bs.check_castling(False, 'king', c.current_state))

    def test_white_queen_side_spaces_occupied(self):
        self.assertFalse(c.bs.check_castling(False, 'queen', c.current_state))
    
    def test_black_king_side_spaces_occupied(self):
        self.assertFalse(c.bs.check_castling(True, 'king', c.current_state))
    
    def test_black_queen_side_spaces_occupied(self):
        self.assertFalse(c.bs.check_castling(True, 'queen', c.current_state))

    def test_white_king_side_protected_free(self):
        c.move_piece(c.bs.wb, '16', '36')
        c.move_piece(c.bs.wn, '17', '38')
        self.assertTrue(c.bs.check_castling(False, 'king', c.current_state))

    def test_white_queen_side_protected_free(self):
        c.move_piece(c.bs.wq, '14', '34')
        c.move_piece(c.bs.wb, '13', '33')
        c.move_piece(c.bs.wn, '12', '31')
        self.assertTrue(c.bs.check_castling(False, 'queen', c.current_state))

    def test_black_king_side_protected_free(self):
        c.move_piece(c.bs.bb, '86', '66')
        c.move_piece(c.bs.bn, '87', '68')
        self.assertTrue(c.bs.check_castling(True, 'king', c.current_state))

    def test_black_queen_side_protected_free(self):
        c.move_piece(c.bs.bq, '84', '64')
        c.move_piece(c.bs.bb, '83', '63')
        c.move_piece(c.bs.bn, '82', '61')
        self.assertTrue(c.bs.check_castling(True, 'queen', c.current_state))
    
    def test_white_king_side_rook_attacked(self):
        c.move_piece(c.bs.wb, '16', '36')
        c.move_piece(c.bs.wn, '17', '35')
        c.move_piece(c.bs.wp, '28', '37')
        c.move_piece(c.bs.bp, '78', '67')
        self.assertTrue(c.bs.check_castling(False, 'king', c.current_state))

    def test_white_king_side_king_landing_space_attacked(self):
        c.move_piece(c.bs.wb, '16', '36')
        c.move_piece(c.bs.wn, '17', '35')
        c.move_piece(c.bs.wp, '27', '46')
        c.move_piece(c.bs.br, '88', '67')
        self.assertFalse(c.bs.check_castling(False, 'king', c.current_state))

    def test_white_king_side_in_check(self):
        c.move_piece(c.bs.wb, '16', '36')
        c.move_piece(c.bs.wn, '17', '46')
        c.move_piece(c.bs.wp, '28', '37')
        c.move_piece(c.bs.bp, '78', '67')
        c.move_piece(c.bs.wp, '25', '34')
        c.move_piece(c.bs.br, '88', '65')
        self.assertFalse(c.bs.check_castling(False, 'king', c.current_state))
    
    def test_white_queen_side_rook_attacked(self):
        c.move_piece(c.bs.wq, '14', '34')
        c.move_piece(c.bs.wb, '13', '33')
        c.move_piece(c.bs.wn, '12', '43')
        c.move_piece(c.bs.wp, '22', '31')
        c.move_piece(c.bs.br, '88', '62')
        self.assertTrue(c.bs.check_castling(False, 'queen', c.current_state))

    def test_black_queen_side_king_move_space_attacked(self):
        c.move_piece(c.bs.bq, '84', '65')
        c.move_piece(c.bs.bp, '74', '55')
        c.move_piece(c.bs.wq, '14', '34')
        c.move_piece(c.bs.bb, '83', '63')
        c.move_piece(c.bs.bn, '82', '61')
        self.assertFalse(c.bs.check_castling(True, 'queen', c.current_state))

    def test_black_queen_side_rook_attacked(self):
        c.move_piece(c.bs.bp, '72', '61')
        c.move_piece(c.bs.bq, '84', '65')
        c.move_piece(c.bs.bb, '83', '63')
        c.move_piece(c.bs.bn, '82', '61')
        c.move_piece(c.bs.wq, '14', '32')
        self.assertTrue(c.bs.check_castling(True, 'queen', c.current_state))

class TestCheckCastlingValid(unittest.TestCase):

    def setUp(self):
        reset_board()

    def no_changes(self):
        c.bs.check_castling_valid(c.current_state)
        assert c.bs.w_king_side_castle == True
        assert c.bs.w_queen_side_castle == True
        assert c.bs.b_king_side_castle == True
        assert c.bs.b_queen_side_castle == True
    
    def white_king_moved(self):
        c.move_piece(c.bs.wk, '15', '35')
        c.bs.check_castling_valid(c.current_state)
        assert c.bs.w_king_side_castle == False
        assert c.bs.w_queen_side_castle == False
        assert c.bs.b_king_side_castle == True
        assert c.bs.b_queen_side_castle == True
    
    def white_king_side_rook_moved(self):
        c.move_piece(c.bs.wr, '88', '68')
        c.bs.check_castling_valid(c.current_state)
        assert c.bs.w_king_side_castle == False
        assert c.bs.w_queen_side_castle == True
        assert c.bs.b_king_side_castle == True
        assert c.bs.b_queen_side_castle == True

    def white_queen_side_rook_moved(self):
        c.move_piece(c.bs.wr, '81', '61')
        c.bs.check_castling_valid(c.current_state)
        assert c.bs.w_king_side_castle == True
        assert c.bs.w_queen_side_castle == False
        assert c.bs.b_king_side_castle == True
        assert c.bs.b_queen_side_castle == True

    def black_king_moved(self):
        c.move_piece(c.bs.bk, '85', '65')
        c.bs.check_castling_valid(c.current_state)
        assert c.bs.w_king_side_castle == True
        assert c.bs.w_queen_side_castle == True
        assert c.bs.b_king_side_castle == False
        assert c.bs.b_queen_side_castle == False

    def black_king_side_rook_moved(self):
        c.move_piece(c.bs.br, '18', '38')
        c.bs.check_castling_valid(c.current_state)
        assert c.bs.w_king_side_castle == True
        assert c.bs.w_queen_side_castle == True
        assert c.bs.b_king_side_castle == False
        assert c.bs.b_queen_side_castle == True

    def black_queen_side_rook_moved(self):
        c.move_piece(c.bs.br, '11', '31')
        c.bs.check_castling_valid(c.current_state)
        assert c.bs.w_king_side_castle == True
        assert c.bs.w_queen_side_castle == True
        assert c.bs.b_king_side_castle == True
        assert c.bs.b_queen_side_castle == False

class TestCheckEnPassant(unittest.TestCase):

    def setUp(self):
        reset_board()
    
    def tearDown(self):
        c.bs.w_en_passant = [False, '']
        c.bs.b_en_passant = [False, '']

    def test_white_en_passant_true(self):
        c.move_piece(c.bs.bp, '71', '41')
        c.bs.check_en_passant(False, '22', '42', c.current_state)
        assert c.bs.w_en_passant == [True, '32']
        assert c.bs.b_en_passant == [False, '']
    
    def test_black_en_passant_true(self):
        c.move_piece(c.bs.wp, '21', '51')
        c.bs.check_en_passant(True, '72', '52', c.current_state)
        assert c.bs.w_en_passant == [False, '']
        assert c.bs.b_en_passant == [True, '62']

class TestCastleMove(unittest.TestCase):

    def setUp(self):
        reset_board()
    
    def test_is_black_king_side(self):
        c.castle_move(True, 'king')
        king_actual = find_pieces(c.bs.bk, True, c.current_state)
        king_expected = ['87']
        rook_actual = set(find_pieces(c.bs.br, True, c.current_state))
        rook_expected = set(['81', '86'])
        assert king_actual == king_expected
        assert rook_actual == rook_expected

    def test_is_black_queen_side(self):
        c.castle_move(True, 'queen')
        king_actual = find_pieces(c.bs.bk, True, c.current_state)
        king_expected = ['83']
        rook_actual = set(find_pieces(c.bs.br, True, c.current_state))
        rook_expected = set(['84', '88'])
        assert king_actual == king_expected
        assert rook_actual == rook_expected

    def test_not_is_black_king_side(self):
        c.castle_move(False, 'king')
        king_actual = find_pieces(c.bs.wk, False, c.current_state)
        king_expected = ['17']
        rook_actual = set(find_pieces(c.bs.wr, False, c.current_state))
        rook_expected = set(['11', '16'])
        assert king_actual == king_expected
        assert rook_actual == rook_expected

    def test_not_is_black_queen_side(self):
        c.castle_move(False, 'queen')
        king_actual = find_pieces(c.bs.wk, False, c.current_state)
        king_expected = ['13']
        rook_actual = set(find_pieces(c.bs.wr, False, c.current_state))
        rook_expected = set(['14', '18'])
        assert king_actual == king_expected
        assert rook_actual == rook_expected


if __name__ == '__main__':
    c = Chess()
    unittest.main()
