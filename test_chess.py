import unittest
from collections import Counter
from game_logic import Chess
from game_flow import Game
# import game_view as gv


def reset_board():
    c.current_state = c.bs.create_start_state()
    c.bs.w_king_side_castle = True
    c.bs.w_queen_side_castle = True
    c.bs.b_king_side_castle = True
    c.bs.b_queen_side_castle = True

def reset_game_board():
    g.c.current_state = c.bs.create_start_state()
    g.c.bs.w_king_side_castle = True
    g.c.bs.w_queen_side_castle = True
    g.c.bs.b_king_side_castle = True
    g.c.bs.b_queen_side_castle = True

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
        self.assertTrue(c.bs.piece_movement(c.bs.wk, '22', '12'))
        self.assertTrue(c.bs.piece_movement(c.bs.wk, '22', '21'))
        self.assertTrue(c.bs.piece_movement(c.bs.wk, '22', '31'))
        self.assertTrue(c.bs.piece_movement(c.bs.wk, '22', '32'))
        self.assertTrue(c.bs.piece_movement(c.bs.wk, '22', '33'))
        self.assertTrue(c.bs.piece_movement(c.bs.wk, '22', '11'))

        self.assertFalse(c.bs.piece_movement(c.bs.wk, '22', '24'))
        self.assertFalse(c.bs.piece_movement(c.bs.wk, '22', '42'))
        self.assertFalse(c.bs.piece_movement(c.bs.wk, '22', '34'))
        self.assertFalse(c.bs.piece_movement(c.bs.wk, '22', '44'))

    def test_queen_move(self):
        self.assertTrue(c.bs.piece_movement(c.bs.wq, '33', '77'))
        self.assertTrue(c.bs.piece_movement(c.bs.wq, '11', '88'))
        self.assertTrue(c.bs.piece_movement(c.bs.wq, '33', '38'))
        self.assertTrue(c.bs.piece_movement(c.bs.wq, '33', '38'))

        self.assertFalse(c.bs.piece_movement(c.bs.wq, '33', '52'))
        self.assertFalse(c.bs.piece_movement(c.bs.wq, '11', '23'))

    def test_bishop_move(self):
        self.assertTrue(c.bs.piece_movement(c.bs.wb, '33', '77'))
        self.assertTrue(c.bs.piece_movement(c.bs.wb, '43', '87'))
        self.assertTrue(c.bs.piece_movement(c.bs.wb, '81', '18'))

        self.assertFalse(c.bs.piece_movement(c.bs.wb, '11', '21'))
        self.assertFalse(c.bs.piece_movement(c.bs.wb, '51', '23'))

    def test_knight_move(self):
        self.assertTrue(c.bs.piece_movement(c.bs.wn, '11', '32'))
        self.assertTrue(c.bs.piece_movement(c.bs.wn, '11', '23'))

        self.assertFalse(c.bs.piece_movement(c.bs.wn, '11', '33'))
        self.assertFalse(c.bs.piece_movement(c.bs.wn, '11', '78'))

    def test_rook_move(self):
        self.assertTrue(c.bs.piece_movement(c.bs.wr, '11', '17'))
        self.assertTrue(c.bs.piece_movement(c.bs.wr, '11', '71'))

        self.assertFalse(c.bs.piece_movement(c.bs.wr, '11', '72'))
        self.assertFalse(c.bs.piece_movement(c.bs.wr, '11', '65'))

    def test_pawn_white_move(self):
        self.assertTrue(c.bs.piece_movement(c.bs.wp, '11', '12'))
        self.assertTrue(c.bs.piece_movement(c.bs.wp, '11', '22'))
        self.assertTrue(c.bs.piece_movement(c.bs.wp, '22', '13'))
        self.assertTrue(c.bs.piece_movement(c.bs.wp, '22', '33'))

        self.assertFalse(c.bs.piece_movement(c.bs.wp, '22', '32'))
        self.assertTrue(c.bs.piece_movement(c.bs.wp, '22', '24'))

    def test_pawn_black_move(self):
        self.assertTrue(c.bs.piece_movement(c.bs.bp, '12', '11'))
        self.assertTrue(c.bs.piece_movement(c.bs.bp, '22', '11'))
        self.assertTrue(c.bs.piece_movement(c.bs.bp, '13', '22'))
        self.assertTrue(c.bs.piece_movement(c.bs.bp, '33', '22'))

        self.assertFalse(c.bs.piece_movement(c.bs.wp, '32', '22'))
        self.assertFalse(c.bs.piece_movement(c.bs.wp, '24', '22'))


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
        self.assertFalse(c.bs.coords_not_equal('56', '56'))
        self.assertFalse(c.bs.coords_not_equal('24', '24'))
        self.assertFalse(c.bs.coords_not_equal('78', '78'))
        self.assertFalse(c.bs.coords_not_equal('37', '37'))

    def test_coords_are_not_equal(self):
        self.assertTrue(c.bs.coords_not_equal('11', '22'))
        self.assertTrue(c.bs.coords_not_equal('09', '19'))
        self.assertTrue(c.bs.coords_not_equal('56', '45'))
        self.assertTrue(c.bs.coords_not_equal('21', '12'))


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
        self.assertTrue(c.bs.is_friendly('78', c.bs.is_black(c.bs.bq),
                                         c.current_state))
        self.assertTrue(c.bs.is_friendly('17', c.bs.is_black(c.bs.bp),
                                         c.current_state))

    def test_white_to_white(self):
        self.assertTrue(c.bs.is_friendly('71', c.bs.is_black(c.bs.wq),
                                         c.current_state))
        self.assertTrue(c.bs.is_friendly('82', c.bs.is_black(c.bs.wk),
                                         c.current_state))

    def test_black_to_white(self):
        self.assertFalse(c.bs.is_friendly('71', c.bs.is_black(c.bs.bn),
                                          c.current_state))
        self.assertFalse(c.bs.is_friendly('22', c.bs.is_black(c.bs.br),
                                          c.current_state))

    def test_white_to_black(self):
        self.assertFalse(c.bs.is_friendly('78', c.bs.is_black(c.bs.wp),
                                          c.current_state))
        self.assertFalse(c.bs.is_friendly('27', c.bs.is_black(c.bs.wq),
                                          c.current_state))


class TestIsEnemy(unittest.TestCase):


    def setUp(self):
        reset_board()

    def test_black_to_black(self):
        self.assertFalse(c.bs.is_enemy('18', c.bs.is_black(c.bs.bk),
                                       c.current_state))
        self.assertFalse(c.bs.is_enemy('67', c.bs.is_black(c.bs.bq),
                                       c.current_state))

    def test_white_to_white(self):
        self.assertFalse(c.bs.is_enemy('21', c.bs.is_black(c.bs.wp),
                                       c.current_state))
        self.assertFalse(c.bs.is_enemy('62', c.bs.is_black(c.bs.wr),
                                       c.current_state))

    def test_black_to_white(self):
        self.assertTrue(c.bs.is_enemy('21', c.bs.is_black(c.bs.bn),
                                      c.current_state))
        self.assertTrue(c.bs.is_enemy('82', c.bs.is_black(c.bs.bb),
                                      c.current_state))

    def test_white_to_black(self):
        self.assertTrue(c.bs.is_enemy('68', c.bs.is_black(c.bs.wp),
                                      c.current_state))
        self.assertTrue(c.bs.is_enemy('47', c.bs.is_black(c.bs.wk),
                                      c.current_state))


class TestIsEmpty(unittest.TestCase):


    def setUp(self):
        reset_board()

    def test_space_is_empty(self):
        self.assertTrue(c.bs.is_empty('76', c.current_state))
        self.assertTrue(c.bs.is_empty('34', c.current_state))

    def test_space_is_occupied(self):
        self.assertFalse(c.bs.is_empty('41', c.current_state))
        self.assertFalse(c.bs.is_empty('38', c.current_state))


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
        self.assertEqual(c.bs.moves_dir('13', (1, 1), True, c.current_state),
                                     ['24', '35', '46'])
        self.assertEqual(c.bs.moves_dir('74', (1, 1), True, c.current_state),
                                     ['85'])

    def test_move_diag_rposi_cposi_white(self):
        self.assertEqual(c.bs.moves_dir('55', (1, 1), False, c.current_state),
                                     ['66', '77'])
        self.assertEqual(c.bs.moves_dir('13', (1, 1), False, c.current_state),
                                     ['24', '35', '46', '57'])
        self.assertEqual(c.bs.moves_dir('74', (1, 1), False, c.current_state),
                                     ['85'])

    def test_move_diag_rposi_cneg_black(self):
        self.assertEqual(c.bs.moves_dir('55', (-1, 1), True, c.current_state),
                                     ['46'])
        self.assertEqual(c.bs.moves_dir('63', (-1, 1), True, c.current_state),
                                     ['54', '45', '36'])
        self.assertEqual(c.bs.moves_dir('74', (-1, 1), True, c.current_state),
                                     ['65', '56'])

    def test_move_diag_rposi_cneg_white(self):
        self.assertEqual(c.bs.moves_dir('55', (-1, 1), False, c.current_state),
                                     ['46', '37'])
        self.assertEqual(c.bs.moves_dir('63', (-1, 1), False, c.current_state),
                                     ['54', '45', '36', '27'])
        self.assertEqual(c.bs.moves_dir('74', (-1, 1), False, c.current_state),
                                     ['65', '56', '47'])

    def test_move_diag_rneg_cneg_black(self):
        self.assertEqual(c.bs.moves_dir('44', (-1, -1), True, c.current_state),
                                     ['33', '22'])
        self.assertEqual(c.bs.moves_dir('87', (-1, -1), True, c.current_state),
                                     ['76', '65', '54', '43', '32'])
        self.assertEqual(c.bs.moves_dir('13', (-1, -1), True, c.current_state),
                                     [])

    def test_move_diag_rneg_cneg_white(self):
        self.assertEqual(c.bs.moves_dir('44', (-1, -1), False,
                                        c.current_state), ['33'])
        self.assertEqual(c.bs.moves_dir('87', (-1, -1), False,
                         c.current_state),['76', '65', '54', '43'])
        self.assertEqual(c.bs.moves_dir('13', (-1, -1), False,
                         c.current_state), [])

    def test_move_vert_rneg_cconst_black(self):
        self.assertEqual(c.bs.moves_dir('44', (0, -1), True, c.current_state),
                                     ['43', '42'])
        self.assertEqual(c.bs.moves_dir('87', (0, -1), True, c.current_state),
                                     ['86', '85', '84', '83', '82'])
        self.assertEqual(c.bs.moves_dir('13', (0, -1), True, c.current_state),
                                     ['12'])

    def test_move_vert_rneg_cconst_white(self):
        self.assertEqual(c.bs.moves_dir('44', (0, -1), False, c.current_state),
                                     ['43'])
        self.assertEqual(c.bs.moves_dir('87', (0, -1), False, c.current_state),
                                     ['86', '85', '84', '83'])
        self.assertEqual(c.bs.moves_dir('31', (0, -1), False, c.current_state),
                                     [])

    def test_move_vert_rposi_cconst_black(self):
        self.assertEqual(c.bs.moves_dir('44', (0, 1), True, c.current_state),
                                     ['45', '46'])
        self.assertEqual(c.bs.moves_dir('87', (0, 1), True, c.current_state),
                                     [])
        self.assertEqual(c.bs.moves_dir('13', (0, 1), True, c.current_state),
                                     ['14', '15', '16'])

    def test_move_vert_rposi_cconst_white(self):
        self.assertEqual(c.bs.moves_dir('44', (0, 1), False, c.current_state),
                                     ['45', '46', '47'])
        self.assertEqual(c.bs.moves_dir('87', (0, 1), False, c.current_state),
                                     ['88'])
        self.assertEqual(c.bs.moves_dir('13', (0, 1), False, c.current_state),
                                     ['14', '15', '16', '17'])

    def test_move_horz_rconst_cneg_black(self):
        self.assertEqual(c.bs.moves_dir('13', (-1, 0), True, c.current_state),
                                     [])
        self.assertEqual(c.bs.moves_dir('87', (-1, 0), True, c.current_state),
                                     [])
        self.assertEqual(c.bs.moves_dir('44', (-1, 0), True, c.current_state),
                                     ['34', '24', '14'])

    def test_move_horz_rconst_cneg_white(self):
        self.assertEqual(c.bs.moves_dir('13', (-1, 0), False, c.current_state),
                                     [])
        self.assertEqual(c.bs.moves_dir('87', (-1, 0), False, c.current_state),
                                     ['77'])
        self.assertEqual(c.bs.moves_dir('44', (-1, 0), False, c.current_state),
                                     ['34', '24', '14'])

    def test_move_horz_rconst_cposi_black(self):
        self.assertEqual(c.bs.moves_dir('23', (1, 0), True, c.current_state),
                                     ['33', '43', '53', '63', '73', '83'])
        self.assertEqual(c.bs.moves_dir('67', (1, 0), True, c.current_state),
                                     [])
        self.assertEqual(c.bs.moves_dir('44', (1, 0), True, c.current_state),
                                     ['54', '64', '74', '84'])

    def test_move_horz_rconst_cposi_white(self):
        self.assertEqual(c.bs.moves_dir('13', (1, 0), False, c.current_state),
                                    ['23', '33', '43', '53', '63', '73', '83'])
        self.assertEqual(c.bs.moves_dir('67', (1, 0), False, c.current_state),
                                    ['77'])
        self.assertEqual(c.bs.moves_dir('44', (1, 0), False, c.current_state),
                                    ['54', '64', '74', '84'])


class TestFindPiece(unittest.TestCase):


    def setUp(self):
        reset_board()

    def test_find_white_queen(self):
        self.assertEqual(c.bs.find_piece(c.bs.wq, False, c.current_state), 
                                         '41')

    def test_find_black_queen(self):
        self.assertEqual(c.bs.find_piece(c.bs.bq, True, c.current_state), '48')


class TestInCheck(unittest.TestCase):


    def setUp(self):
        reset_board()

    def test_black_king_in_check_white_knight(self):
        c.move_piece(c.bs.wn, '21', '46')
        self.assertTrue(c.in_check(True, c.current_state))

    def test_white_king_in_check_black_queen(self):
        c.move_piece(c.bs.wp, '42', '43')
        c.move_piece(c.bs.bq, '48', '15')
        self.assertTrue(c.in_check(False, c.current_state))

    def test_white_king_not_in_check(self):
        self.assertFalse(c.in_check(False, c.current_state))
        c.move_piece(c.bs.br, '18', '53')
        self.assertFalse(c.in_check(False, c.current_state))
        c.move_piece(c.bs.bq, '48', '73')
        self.assertFalse(c.in_check(False, c.current_state))
        c.move_piece(c.bs.bb, '68', '33')
        self.assertFalse(c.in_check(False, c.current_state))

    def test_black_king_not_in_check(self):
        self.assertFalse(c.in_check(True, c.current_state))
        c.move_piece(c.bs.wb, '31', '76')
        self.assertFalse(c.in_check(True, c.current_state))
        c.move_piece(c.bs.wq, '41', '56')
        self.assertFalse(c.in_check(True, c.current_state))


class TestCheckMate(unittest.TestCase):


    def setUp(self):
        reset_board()

    def test_black_king_not_mate(self):
        self.assertFalse(c.check_mate(True, c.current_state))

    def test_white_king_not_mate(self):
        self.assertFalse(c.check_mate(False, c.current_state))

    def test_black_king_mate_white_knight(self):
        c.move_piece(c.bs.wn, '21', '46')
        self.assertTrue(c.check_mate(True, c.current_state))

    def test_white_king_mate_black_knight(self):
        c.move_piece(c.bs.bn, '28', '43')
        self.assertTrue(c.check_mate(False, c.current_state))

    def test_white_king_not_in_check_black_queen_attacking(self):
        c.move_piece(c.bs.bq, '48', '15')
        c.move_piece(c.bs.wp, '42', '43')
        c.move_piece(c.bs.wp, '52', '53')
        self.assertFalse(c.check_mate(False, c.current_state))


class TestPossibleMoves(unittest.TestCase):


    def setUp(self):
        reset_board()

    def test_white_king_no_moves(self):
        self.assertEqual(c.bs.possible_moves(c.bs.wk, '51', c.current_state),
                                             [])

    def test_white_pawn_no_target(self):
        actual_moves = c.bs.possible_moves(c.bs.wp, '12', c.current_state)
        expected_moves = ['13', '14']
        actual = Counter(actual_moves)
        expected = Counter(expected_moves)
        assert actual == expected

    def test_white_pawn_blocked(self):
        c.move_piece(c.bs.bp, '17', '13')
        self.assertEqual(c.bs.possible_moves(c.bs.wp, '12', c.current_state),
                                             [])

    def test_black_pawn_target(self):
        c.move_piece(c.bs.wp, '22', '26')
        actual_moves = c.bs.possible_moves(c.bs.bp, '17', c.current_state)
        expected_moves = ['16', '26', '15']
        actual = Counter(actual_moves)
        expected = Counter(expected_moves)
        assert actual == expected

    def test_white_queen_from_54(self):
        c.move_piece(c.bs.wq, '41', '54')
        actual_moves = c.bs.possible_moves(c.bs.wq, '54', c.current_state)
        expected_moves = ['55', '56', '57', '53', '44', '34', '24', '14',
                          '64', '74', '84', '43', '65', '76', '87', '63',
                          '45', '36', '27']
        actual = Counter(actual_moves)
        expected = Counter(expected_moves)
        assert actual == expected

    def test_black_queen_from_25(self):
        c.move_piece(c.bs.bq, '48', '25')
        actual_moves = c.bs.possible_moves(c.bs.bq, '25', c.current_state)
        expected_moves = ['15', '16', '26', '36', '35', '45', '55', '65',
                          '75', '85', '34', '43', '52', '24', '14', '23',
                          '22']
        actual = Counter(actual_moves)
        expected = Counter(expected_moves)
        assert actual == expected

    def test_white_bishop_from_44(self):
        c.move_piece(c.bs.wb, '31', '44')
        actual_moves = c.bs.possible_moves(c.bs.wb, '44', c.current_state)
        expected_moves = ['33', '53', '35', '26', '17', '55', '66', '77']
        actual = Counter(actual_moves)
        expected = Counter(expected_moves)
        assert actual == expected

    def test_black_knight_from_33(self):
        c.move_piece(c.bs.bn, '28', '33')
        actual_moves = c.bs.possible_moves(c.bs.bn, '33', c.current_state)
        expected_moves = ['21', '41', '12', '52', '14', '54', '25', '45']
        actual = Counter(actual_moves)
        expected = Counter(expected_moves)
        assert actual == expected

    def test_black_rook_from_65(self):
        c.move_piece(c.bs.br, '88', '65')
        actual_moves = c.bs.possible_moves(c.bs.br, '65', c.current_state)
        expected_moves = ['66', '64', '63', '62', '75', '85', '55', '45',
                          '35', '25', '15']
        actual = Counter(actual_moves)
        expected = Counter(expected_moves)
        assert actual == expected

    def test_white_king_from_44(self):
        c.move_piece(c.bs.wk, '51', '44')
        actual_moves = c.bs.possible_moves(c.bs.wk, '44', c.current_state)
        expected_moves = ['35', '45', '55', '34', '54', '53', '43', '33']
        actual = Counter(actual_moves)
        expected = Counter(expected_moves)
        assert actual == expected


class TestBlockCheck(unittest.TestCase):


    def setUp(self):
        reset_board()
        self.test_passed = False

    def test_black_block_check_white_bishop(self):
        c.move_piece(c.bs.bp, '47', '45')
        c.move_piece(c.bs.wb, '31', '56')
        self.assertTrue(c.bs.block_check(True, c.current_state))

    def test_black_block_check_knight_takes_knight_attacker(self):
        c.move_piece(c.bs.bp, '37', '35')
        c.move_piece(c.bs.bp, '57', '55')
        c.move_piece(c.bs.bn, '78', '57')
        c.move_piece(c.bs.bn, '28', '25')
        c.move_piece(c.bs.wn, '21', '46')
        self.assertTrue(c.bs.block_check(True, c.current_state))

    def test_black_block_check_king_takes_pawn_attacker(self):
        c.move_piece(c.bs.wp, '12', '54')
        c.move_piece(c.bs.bk, '48', '45')
        self.assertTrue(c.bs.block_check(True, c.current_state))

    def test_black_block_check_king_moves_away(self):
        c.move_piece(c.bs.bk, '48', '45')
        c.move_piece(c.bs.wq, '41', '43')
        self.assertTrue(c.bs.block_check(True, c.current_state))

    def test_black_not_block_check_queen_attacker(self):
        c.move_piece(c.bs.wq, '41', '85')
        c.move_piece(c.bs.bp, '67', '66')
        c.move_piece(c.bs.bp, '77', '75')
        self.assertFalse(c.bs.block_check(True, c.current_state))

    def test_white_not_block_check_queen_attacker(self):
        c.bs.move_piece(c.bs.bq, '48', '84', c.current_state)
        c.bs.move_piece(c.bs.wp, '72', '74', c.current_state)
        c.bs.move_piece(c.bs.wp, '62', '64', c.current_state)
        self.assertFalse(c.bs.block_check(False, c.current_state))

    def test_black_not_block_check_pawn_protect_attacker(self):
        c.bs.move_piece(c.bs.wp, '72', '76', c.current_state)
        c.bs.move_piece(c.bs.bp, '67', '66', c.current_state)
        c.bs.move_piece(c.bs.wp, '62', '67', c.current_state)
        self.assertFalse(c.bs.block_check(True, c.current_state))

    def test_white_not_block_check_pawn_protect_attacker(self):
        c.bs.move_piece(c.bs.wp, '62', '63', c.current_state)
        c.bs.move_piece(c.bs.wp, '82', '83', c.current_state)
        c.bs.move_piece(c.bs.bp, '67', '62', c.current_state)
        c.bs.move_piece(c.bs.bp, '77', '73', c.current_state)
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
        c.move_piece(c.bs.wb, '61', '63')
        c.move_piece(c.bs.wn, '71', '83')
        self.assertTrue(c.bs.check_castling(False, 'king', c.current_state))

    def test_white_queen_side_protected_free(self):
        c.move_piece(c.bs.wq, '41', '43')
        c.move_piece(c.bs.wb, '31', '33')
        c.move_piece(c.bs.wn, '21', '13')
        self.assertTrue(c.bs.check_castling(False, 'queen', c.current_state))

    def test_black_king_side_protected_free(self):
        c.move_piece(c.bs.bb, '68', '66')
        c.move_piece(c.bs.bn, '78', '86')
        self.assertTrue(c.bs.check_castling(True, 'king', c.current_state))

    def test_black_queen_side_protected_free(self):
        c.move_piece(c.bs.bq, '48', '46')
        c.move_piece(c.bs.bb, '38', '36')
        c.move_piece(c.bs.bn, '28', '16')
        self.assertTrue(c.bs.check_castling(True, 'queen', c.current_state))

    def test_white_king_side_rook_attacked(self):
        c.move_piece(c.bs.wb, '61', '63')
        c.move_piece(c.bs.wn, '71', '53')
        c.move_piece(c.bs.wp, '82', '73')
        c.move_piece(c.bs.bp, '87', '76')
        self.assertTrue(c.bs.check_castling(False, 'king', c.current_state))

    def test_white_king_side_king_landing_space_attacked(self):
        c.move_piece(c.bs.wb, '61', '63')
        c.move_piece(c.bs.wn, '71', '53')
        c.move_piece(c.bs.wp, '72', '64')
        c.move_piece(c.bs.br, '88', '76')
        self.assertFalse(c.bs.check_castling(False, 'king', c.current_state))

    def test_white_king_side_in_check(self):
        c.move_piece(c.bs.wb, '61', '63')
        c.move_piece(c.bs.wn, '71', '64')
        c.move_piece(c.bs.wp, '82', '73')
        c.move_piece(c.bs.bp, '87', '76')
        c.move_piece(c.bs.wp, '52', '43')
        c.move_piece(c.bs.br, '88', '56')
        self.assertFalse(c.bs.check_castling(False, 'king', c.current_state))

    def test_white_queen_side_rook_attacked(self):
        c.move_piece(c.bs.wq, '41', '43')
        c.move_piece(c.bs.wb, '31', '33')
        c.move_piece(c.bs.wn, '21', '34')
        c.move_piece(c.bs.wp, '22', '13')
        c.move_piece(c.bs.br, '88', '26')
        self.assertTrue(c.bs.check_castling(False, 'queen', c.current_state))

    def test_black_queen_side_king_move_space_attacked(self):
        c.move_piece(c.bs.bq, '48', '56')
        c.move_piece(c.bs.bp, '47', '55')
        c.move_piece(c.bs.wq, '41', '43')
        c.move_piece(c.bs.bb, '38', '36')
        c.move_piece(c.bs.bn, '28', '16')
        self.assertFalse(c.bs.check_castling(True, 'queen', c.current_state))

    def test_black_queen_side_rook_attacked(self):
        c.move_piece(c.bs.bp, '27', '16')
        c.move_piece(c.bs.bq, '48', '56')
        c.move_piece(c.bs.bb, '38', '36')
        c.move_piece(c.bs.bn, '28', '16')
        c.move_piece(c.bs.wq, '41', '23')
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
        c.move_piece(c.bs.wk, '51', '53')
        c.bs.check_castling_valid(c.current_state)
        assert c.bs.w_king_side_castle == False
        assert c.bs.w_queen_side_castle == False
        assert c.bs.b_king_side_castle == True
        assert c.bs.b_queen_side_castle == True

    def white_king_side_rook_moved(self):
        c.move_piece(c.bs.wr, '88', '86')
        c.bs.check_castling_valid(c.current_state)
        assert c.bs.w_king_side_castle == False
        assert c.bs.w_queen_side_castle == True
        assert c.bs.b_king_side_castle == True
        assert c.bs.b_queen_side_castle == True

    def white_queen_side_rook_moved(self):
        c.move_piece(c.bs.wr, '18', '16')
        c.bs.check_castling_valid(c.current_state)
        assert c.bs.w_king_side_castle == True
        assert c.bs.w_queen_side_castle == False
        assert c.bs.b_king_side_castle == True
        assert c.bs.b_queen_side_castle == True

    def black_king_moved(self):
        c.move_piece(c.bs.bk, '58', '56')
        c.bs.check_castling_valid(c.current_state)
        assert c.bs.w_king_side_castle == True
        assert c.bs.w_queen_side_castle == True
        assert c.bs.b_king_side_castle == False
        assert c.bs.b_queen_side_castle == False

    def black_king_side_rook_moved(self):
        c.move_piece(c.bs.br, '81', '83')
        c.bs.check_castling_valid(c.current_state)
        assert c.bs.w_king_side_castle == True
        assert c.bs.w_queen_side_castle == True
        assert c.bs.b_king_side_castle == False
        assert c.bs.b_queen_side_castle == True

    def black_queen_side_rook_moved(self):
        c.move_piece(c.bs.br, '11', '13')
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
        c.move_piece(c.bs.bp, '17', '14')
        c.bs.check_en_passant(False, '22', '24', c.current_state)
        assert c.bs.w_en_passant == [True, '23']
        assert c.bs.b_en_passant == [False, '']

    def test_black_en_passant_true(self):
        c.move_piece(c.bs.wp, '12', '15')
        c.bs.check_en_passant(True, '27', '25', c.current_state)
        assert c.bs.w_en_passant == [False, '']
        assert c.bs.b_en_passant == [True, '26']


class TestCastleMove(unittest.TestCase):


    def setUp(self):
        reset_board()

    def test_is_black_king_side(self):
        c.castle_move(True, 'king')
        king_actual = find_pieces(c.bs.bk, True, c.current_state)
        king_expected = ['78']
        rook_actual = set(find_pieces(c.bs.br, True, c.current_state))
        rook_expected = set(['18', '68'])
        assert king_actual == king_expected
        assert rook_actual == rook_expected

    def test_is_black_queen_side(self):
        c.castle_move(True, 'queen')
        king_actual = find_pieces(c.bs.bk, True, c.current_state)
        king_expected = ['38']
        rook_actual = set(find_pieces(c.bs.br, True, c.current_state))
        rook_expected = set(['48', '88'])
        assert king_actual == king_expected
        assert rook_actual == rook_expected

    def test_not_is_black_king_side(self):
        c.castle_move(False, 'king')
        king_actual = find_pieces(c.bs.wk, False, c.current_state)
        king_expected = ['71']
        rook_actual = set(find_pieces(c.bs.wr, False, c.current_state))
        rook_expected = set(['11', '61'])
        assert king_actual == king_expected
        assert rook_actual == rook_expected

    def test_not_is_black_queen_side(self):
        c.castle_move(False, 'queen')
        king_actual = find_pieces(c.bs.wk, False, c.current_state)
        king_expected = ['31']
        rook_actual = set(find_pieces(c.bs.wr, False, c.current_state))
        rook_expected = set(['41', '81'])
        assert king_actual == king_expected
        assert rook_actual == rook_expected


class TestMovePiece(unittest.TestCase):


    def setUp(self):
        reset_board()

    def test_move_white_bishop(self):
        c.move_piece(c.bs.wb, '31', '63')
        self.assertTrue(c.bs.is_empty('31', c.current_state))
        wb = find_pieces(c.bs.wb, False, c.current_state)
        assert '63' in wb
        assert '55' not in wb

    def test_move_black_pawn(self):
        c.move_piece(c.bs.bp, '17', '15')
        self.assertTrue(c.bs.is_empty('17', c.current_state))
        bp = find_pieces(c.bs.bp, True, c.current_state)
        assert '15' in bp
        assert '17' not in bp


# Tests for move function in Game class in game_flow file
class TestMove(unittest.TestCase):


    def setUp(self):
        reset_game_board()
        reset_board()

    def test_queen_side_white_knight_to_13(self):
        is_black = False
        g.move(is_black, '21', '13')
        self.assertTrue(c.bs.is_empty('21', g.c.current_state))
        self.assertFalse(c.bs.is_empty('13', g.c.current_state))
        wn = find_pieces(c.bs.wn, is_black, g.c.current_state)
        assert '13' in wn
        assert '21' not in wn

    def test_queen_side_white_knight_to_33(self):
        is_black = False
        g.move(is_black, '21', '33')
        self.assertTrue(c.bs.is_empty('21', g.c.current_state))
        self.assertFalse(c.bs.is_empty('33', g.c.current_state))
        wn = find_pieces(c.bs.wn, is_black, g.c.current_state)
        assert '33' in wn
        assert '21' not in wn

    def test_king_side_white_knight_to_83(self):
        is_black = False
        g.move(is_black, '71', '83')
        self.assertTrue(c.bs.is_empty('71', g.c.current_state))
        self.assertFalse(c.bs.is_empty('83', g.c.current_state))
        wn = find_pieces(c.bs.wn, is_black, g.c.current_state)
        assert '83' in wn
        assert '71' not in wn

    def test_king_side_white_knight_to_63(self):
        is_black = False
        g.move(is_black, '71', '63')
        self.assertTrue(c.bs.is_empty('71', g.c.current_state))
        self.assertFalse(c.bs.is_empty('63', g.c.current_state))
        wn = find_pieces(c.bs.wn, is_black, g.c.current_state)
        assert '63' in wn
        assert '71' not in wn

    def test_queen_side_black_knight(self):
        is_black = True
        g.move(is_black, '28', '36')
        bn = find_pieces(c.bs.bn, True, g.c.current_state)
        assert '36' in bn
        g.move(is_black, '36', '15')
        bn = find_pieces(c.bs.bn, True, g.c.current_state)
        assert '15' in bn
        g.move(is_black, '15', '34')
        bn = find_pieces(c.bs.bn, True, g.c.current_state)
        assert '34' in bn
        g.move(is_black, '34', '42')
        bn = find_pieces(c.bs.bn, True, g.c.current_state)
        assert '42' in bn
        past_spaces = ['28', '36', '15', '34']
        assert not any(space in past_spaces for space in bn)
        wp = find_pieces(c.bs.wp, False, g.c.current_state)
        assert '42' not in wp

    def test_queen_side_white_bishop(self):
        is_black = False
        g.move(is_black, '22', '23')
        self.assertTrue(c.bs.is_empty('22', g.c.current_state))
        self.assertFalse(c.bs.is_empty('23', g.c.current_state))
        g.move(is_black, '31', '13')
        self.assertTrue(c.bs.is_empty('31', g.c.current_state))
        g.move(is_black, '13', '57')
        wb = find_pieces(c.bs.wb, False, g.c.current_state)
        bp = find_pieces(c.bs.bp, True, g.c.current_state)
        assert '13' not in wb
        assert '57' not in bp

    def test_black_side_queen(self):
        is_black = True
        g.move(True, '47', '45')
        g.move(True, '48', '46')
        g.move(True, '46', '76')
        g.move(True, '76', '32')
        bq = find_pieces(c.bs.bq, True, g.c.current_state)
        assert '32' in bq
        past_spaces = ['47', '45', '48', '46', '76']
        assert not any(space in past_spaces for space in bq)

    def test_king_side_black_rook(self):
        is_black = True
        g.move(is_black, '87', '85')
        g.move(is_black, '88', '86')
        g.move(is_black, '86', '36')
        g.move(is_black, '36', '32')
        br = find_pieces(c.bs.br, True, g.c.current_state)
        assert '32' in br
        past_spaces = ['88', '86', '36']
        assert not any(space in past_spaces for space in br)


class TestCheckPromotion(unittest.TestCase):


    def setUp(self):
        reset_board()
        reset_game_board()
    
    def test_black_pawn_11(self):
        is_black = True
        g.move(is_black, '17', '15')
        g.move(is_black, '15', '14')
        g.move(is_black, '14', '13')
        g.move(is_black, '13', '22')
        g.move(is_black, '22', '11')
        check_bool, check_space = c.bs.check_promotion(True, g.c.current_state)
        assert [check_bool, check_space] == [True, '11']

    def test_white_pawn_78(self):
        is_black = False
        g.move(is_black, '52', '53')
        g.move(is_black, '53', '54')
        g.move(is_black, '54', '55')
        g.move(is_black, '55', '56')
        g.move(is_black, '56', '67')
        g.move(is_black, '67', '78')
        check_bool, check_space = c.bs.check_promotion(False, g.c.current_state)
        assert [check_bool, check_space] == [True, '78']

    def test_white_false(self):
        check_bool, check_space = c.bs.check_promotion(False, g.c.current_state)
        assert [check_bool, check_space] == [False, '00']

    def test_black_false(self):
        check_bool, check_space = c.bs.check_promotion(True, g.c.current_state)
        assert [check_bool, check_space] == [False, '00']

class TestAlphaCoordsToNums(unittest.TestCase):

    def setUp(self):
        reset_board()
        reset_game_board()
    
    def test_valid_coords(self):
        assert c.bs.alpha_coords_to_nums("a1b1") == "1121"
        assert c.bs.alpha_coords_to_nums("b1b1") == "2121"
        assert c.bs.alpha_coords_to_nums("c1b1") == "3121"
        assert c.bs.alpha_coords_to_nums("d1b1") == "4121"
        assert c.bs.alpha_coords_to_nums("e1b1") == "5121"
        assert c.bs.alpha_coords_to_nums("f1b1") == "6121"
        assert c.bs.alpha_coords_to_nums("g1b1") == "7121"
        assert c.bs.alpha_coords_to_nums("h1b1") == "8121"
        assert c.bs.alpha_coords_to_nums("a1a1") == "1111"
        assert c.bs.alpha_coords_to_nums("a1c1") == "1131"
        assert c.bs.alpha_coords_to_nums("a1d1") == "1141"
        assert c.bs.alpha_coords_to_nums("a1e1") == "1151"
        assert c.bs.alpha_coords_to_nums("a1f1") == "1161"
        assert c.bs.alpha_coords_to_nums("a1g1") == "1171"
        assert c.bs.alpha_coords_to_nums("a1h1") == "1181"
        assert c.bs.alpha_coords_to_nums("a2b1") == "1221"
        assert c.bs.alpha_coords_to_nums("a3b1") == "1321"
        assert c.bs.alpha_coords_to_nums("a4b1") == "1421"
        assert c.bs.alpha_coords_to_nums("a5b1") == "1521"
        assert c.bs.alpha_coords_to_nums("a6b1") == "1621"
        assert c.bs.alpha_coords_to_nums("a7b1") == "1721"
        assert c.bs.alpha_coords_to_nums("a8b1") == "1821"
        assert c.bs.alpha_coords_to_nums("a1b2") == "1122"
        assert c.bs.alpha_coords_to_nums("a1b3") == "1123"
        assert c.bs.alpha_coords_to_nums("a1b4") == "1124"
        assert c.bs.alpha_coords_to_nums("a1b5") == "1125"
        assert c.bs.alpha_coords_to_nums("a1b6") == "1126"
        assert c.bs.alpha_coords_to_nums("a1b7") == "1127"
        assert c.bs.alpha_coords_to_nums("a1b8") == "1128"

    def test_invalid_coords(self):
        assert c.bs.alpha_coords_to_nums("t1b1") == False
        assert c.bs.alpha_coords_to_nums("adb1") == False
        assert c.bs.alpha_coords_to_nums("a1bv") == False
        assert c.bs.alpha_coords_to_nums("31b1") == False
        assert c.bs.alpha_coords_to_nums("a161") == False
        assert c.bs.alpha_coords_to_nums("!1b1") == False
        assert c.bs.alpha_coords_to_nums("a%b1") == False
    
    def test_invalid_length(self):
        assert c.bs.alpha_coords_to_nums("a1b1a") == False
        assert c.bs.alpha_coords_to_nums("a") == False
        assert c.bs.alpha_coords_to_nums("a2") == False
        assert c.bs.alpha_coords_to_nums("a1b") == False
        assert c.bs.alpha_coords_to_nums("a1b1a3b3") == False

class TestCheckStaleMate(unittest.TestCase):

    def setUp(self):
        reset_board()
        reset_game_board()

    def test_stalemate_true_1(self):
        is_black = True
        for space in g.c.current_state:
            piece = g.c.current_state[space][2]
            g.c.move_piece(piece, space, space)
        g.c.move_piece(g.c.bs.bk, '11', '58')
        g.c.move_piece(g.c.bs.wp, '11', '57')
        g.c.move_piece(g.c.bs.wk, '11', '56')
        assert g.c.bs.check_stalemate(is_black, g.c.current_state) == True
    
    def test_stalemate_true_2(self):
        is_black = False
        for space in g.c.current_state:
            piece = g.c.current_state[space][2]
            g.c.move_piece(piece, space, space)
        g.c.move_piece(g.c.bs.bk, '64', '65')
        g.c.move_piece(g.c.bs.wp, '83', '84')
        g.c.move_piece(g.c.bs.wk, '86', '85')
        g.c.move_piece(g.c.bs.bp, '67', '66')
        g.c.move_piece(g.c.bs.bp, '78', '77')
        assert g.c.bs.check_stalemate(is_black, g.c.current_state) == True

    def test_stalemate_true_3(self):
        is_black = False
        for space in g.c.current_state:
            piece = g.c.current_state[space][2]
            g.c.move_piece(piece, space, space)
        g.c.move_piece(g.c.bs.bk, '11', '65')
        g.c.move_piece(g.c.bs.bp, '11', '64')
        g.c.move_piece(g.c.bs.br, '11', '22')
        g.c.move_piece(g.c.bs.wk, '11', '63')
        assert g.c.bs.check_stalemate(is_black, g.c.current_state) == True

    def test_stalemate_true_4(self):
        is_black = True
        for space in g.c.current_state:
            piece = g.c.current_state[space][2]
            g.c.move_piece(piece, space, space)
        g.c.move_piece(g.c.bs.br, '11', '88')
        g.c.move_piece(g.c.bs.bn, '11', '78')
        g.c.move_piece(g.c.bs.bb, '11', '68')
        g.c.move_piece(g.c.bs.bq, '11', '87')
        g.c.move_piece(g.c.bs.bp, '11', '77')
        g.c.move_piece(g.c.bs.bp, '11', '57')
        g.c.move_piece(g.c.bs.br, '11', '86')
        g.c.move_piece(g.c.bs.bk, '11', '76')
        g.c.move_piece(g.c.bs.bp, '11', '66')
        g.c.move_piece(g.c.bs.wq, '11', '56')
        g.c.move_piece(g.c.bs.bp, '11', '85')
        g.c.move_piece(g.c.bs.wp, '11', '84')
        assert g.c.bs.check_stalemate(is_black, g.c.current_state) == True

    def test_stalemate_false_1(self):
        is_black = False
        assert g.c.bs.check_stalemate(is_black, g.c.current_state) == False

    def test_stalemate_false_2(self):
        is_black = True
        for space in g.c.current_state:
            piece = g.c.current_state[space][2]
            g.c.move_piece(piece, space, space)
        g.c.move_piece(g.c.bs.bk, '11', '65')
        g.c.move_piece(g.c.bs.bp, '11', '64')
        g.c.move_piece(g.c.bs.br, '11', '22')
        g.c.move_piece(g.c.bs.wk, '11', '63')
        assert g.c.bs.check_stalemate(is_black, g.c.current_state) == False


# game_view.py tests below



if __name__ == '__main__':
    g = Game()
    c = Chess()
    unittest.main()