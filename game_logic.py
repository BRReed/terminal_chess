from copy import deepcopy



class Chess():

    def __init__(self):
        self.bs = BoardState()
        self.current_state = self.bs.create_start_state()

    def print_current_state(self, perspective):
        """Creates printed representation of current chess board

        Args:
            perspective (string): either 'black' or 'white' flips board
            to show proper perspective
        """
        z = ''
        if perspective == 'white':
            for r in range(8, 0, -1):
                b = f' {r} '
                for c in range(1, 9):
                    b += (self.current_state[f'{c}{r}'][0] +
                        self.current_state[f'{c}{r}'][2] +
                        self.current_state[f'{c}{r}'][1])
                z += (f'{b}\n')
            z += '    A  B  C  D  E  F  G  H '
        elif perspective == 'black':
            for r in range(1, 9):
                b = f' {r} '
                for c in range(8, 0, -1):
                    b += (self.current_state[f'{c}{r}'][0] +
                        self.current_state[f'{c}{r}'][2] +
                        self.current_state[f'{c}{r}'][1])
                z += (f'{b}\n')
            z += '    H  G  F  E  D  C  B  A '
        print(z)

    def move_piece(self, piece, c_coords, d_coords):
        """Move piece on board

        Args:
            piece (string): unicode chess piece
            c_coords (string): column x row 'cr'
            d_coords (string): column x row 'cr'
        """
        self.current_state[d_coords][2] = piece
        self.current_state[c_coords][2] = self.bs.empty

    def castle_move(self, is_black, side):
        """Moves king and rook based on is_black and side

        Args:
            is_black (bool): if piece is_black True, else False
            side (string): king for king side castle, else queen
        """
        if is_black:
            if side == 'king':
                self.move_piece(self.bs.bk, '58', '78')
                self.move_piece(self.bs.br, '88', '68')
            if side == 'queen':
                self.move_piece(self.bs.bk, '58', '38')
                self.move_piece(self.bs.br, '18', '48')
        if not is_black:
            if side == 'king':
                self.move_piece(self.bs.wk, '51', '71')
                self.move_piece(self.bs.wr, '81', '61')
            if side == 'queen':
                self.move_piece(self.bs.wk, '51', '31')
                self.move_piece(self.bs.wr, '11', '41')

    def in_check(self, is_black, board_state):
        """check if king is in check

        Args:
            is_black (bool): if king is black True; else False
            board_state (dict): dictionary representation of a board state

        Returns:
            bool: True if king in check; else False
        """
        mov = []
        if is_black is True:
            king_space = self.bs.find_piece(self.bs.bk, is_black, board_state)
        else:
            king_space = self.bs.find_piece(self.bs.wk, is_black, board_state)
        for coords in board_state:
            if is_black != self.bs.is_black(board_state[coords][2]):
                mov += self.bs.possible_moves(board_state[coords][2], coords,
                    board_state)

        if king_space in mov:
            return True
        else:
            return False

    def check_mate(self, is_black, board_state):
        """check if king is check mated

        Args:
            is_black (bool): if king being checked is black True; else False
            board_state (dict): dictionary representation of a board state

        Returns:
            bool: True if check mate, else False
        """
        if self.in_check(is_black, board_state):
            pass
        else:
            return False
        mov = []
        if is_black is True:
            king_space = self.bs.find_piece(self.bs.bk, is_black, board_state)
            king_spaces = self.bs.possible_moves(self.bs.bk, king_space,
                board_state)
        else:
            king_space = self.bs.find_piece(self.bs.wk, is_black, board_state)
            king_spaces = self.bs.possible_moves(self.bs.wk, king_space,
                board_state)
        for coords in board_state:
            if is_black != self.bs.is_black(board_state[coords][2]):
                mov += self.bs.possible_moves(board_state[coords][2], coords,
                    board_state)
        for move in king_spaces:
            if move not in mov:
                return False
            else:
                continue
        return True


class BoardState():
    def __init__(self):
        self.wk = self.assign_piece(False, 'king')
        self.wq = self.assign_piece(False, 'queen')
        self.wr = self.assign_piece(False, 'rook')
        self.wb = self.assign_piece(False, 'bishop')
        self.wn = self.assign_piece(False, 'knight')
        self.wp = self.assign_piece(False, 'pawn')

        self.bk = self.assign_piece(True, 'king')
        self.bq = self.assign_piece(True, 'queen')
        self.br = self.assign_piece(True, 'rook')
        self.bb = self.assign_piece(True, 'bishop')
        self.bn = self.assign_piece(True, 'knight')
        self.bp = self.assign_piece(True, 'pawn')
        self.empty = '   '
        self.w_king_side_castle = True
        self.w_queen_side_castle = True
        self.b_king_side_castle = True
        self.b_queen_side_castle = True
        self.w_en_passant = [False, '']
        self.b_en_passant = [False, '']

    def assign_piece(self, is_black, piece):
        """create and return string of chess piece

        Args:
            is_black (bool): if piece is black, True, else False
            piece (string): accepts king, queen, rook, bishop, knight, pawn

        Returns:
            string: (rgb code for color) + (unicode for piece) + (color reset)
        """
        string = ''
        if is_black == True:
            string += '\033[38;2;0;0;0m'
        else:
            string += '\033[38;2;255;255;255m'
        if piece.lower() == 'king':
            string += ' \u265A '
        elif piece.lower() == 'queen':
            string += ' \u265B '
        elif piece.lower() == 'rook':
            string += ' \u265C '
        elif piece.lower() == 'bishop':
            string += ' \u265D '
        elif piece.lower() == 'knight':
            string += ' \u265E '
        elif piece.lower() == 'pawn':
            string += ' \u265F '
        string += '\033[38;0m'
        return string

    def create_start_state(self):
        """Create start game board state
        Vars:
            self.start_state:
                keys = [cr] where row is r and column is c. Both represented
                    by a number
                values = (RGB BG colorcode, unicode chess piece,
                    colorcode reset)
        """
        start_state = {}
        for row in range(1, 9):
            for column in range(1, 9):
                if (column + row) % 2 == 0:
                    start_state[f'{column}{row}'] = [
                        '\033[48;2;57;78;112m', '\033[0m',
                        f'{self.populate_start(column, row)}']
                else:
                    start_state[f'{column}{row}'] = [
                        '\033[48;2;66;135;245m', '\033[0m',
                        f'{self.populate_start(column, row)}']
        return start_state

    def populate_start(self, c, r):
        """Populates pieces on board at start of game

        Args:
            r (string): row on chess board
            c (string): column on chess board

        Returns:
            Var equal to chess piece
        """
        if r == 1:
            if c == 1 or c == 8:
                return self.wr
            elif c == 2 or c == 7:
                return self.wn
            elif c == 3 or c == 6:
                return self.wb
            elif c == 4:
                return self.wq
            elif c == 5:
                return self.wk
            else:
                print(f'well, this is bad c, r = {c}, {r}')
                return
        elif r == 2:
            return self.wp
        elif r == 7:
            return self.bp
        elif r == 8:
            if c == 1 or c == 8:
                return self.br
            elif c == 2 or c == 7:
                return self.bn
            elif c == 3 or c == 6:
                return self.bb
            elif c == 4:
                return self.bq
            elif c == 5:
                return self.bk
            else:
                print(f'well, this is bad c, r = {c}, {r}')
        else:
            return '   '

    def is_black(self, piece):
        """checks if a piece is black

        Args:
            piece (string): chess piece

        Returns:
            Bool: True if '\033[38;2;0;0;0m' in var piece; else False
        """
        if '\033[38;2;0;0;0m' in piece:
            return True
        else:
            return False

    def is_friendly(self, coords, is_black, board_state):
        """checks if piece in coords is friendly

        Args:
            coords (string): column x row 'cr'
            is_black (bool): True if piece in movement is black; else False
            board_state (dict): dictionary representation of a board state

        Returns:
            Bool: If piece in bounds is same color as piece in coords True;
                  else False
        """
        if is_black == self.is_black(board_state[coords][2]):
            return True
        else:
            return False

    def is_enemy(self, coords, is_black, board_state):
        """checks if piece in coords is enemy

        Args:
            coords (string): column x row 'cr'
            is_black (bool): True if piece in movement is black; else False
            board_state (dict): dictionary representation of a board state

        Returns:
            [type]: [description]
        """
        if self.is_empty(coords, board_state) or (
            is_black == self.is_black(board_state[coords][2])):
            return False
        elif is_black != self.is_black(board_state[coords][2]):
            return True

    def is_empty(self, coords, board_state):
        """checks if coords is empty

        Args:
            coords (string): column x row 'cr'
            board_state (dict): dictionary representation of a board state

        Returns:
            Bool: True if space is empty; else False
        """
        if self.empty in board_state[coords][2]:
            return True
        else:
            return False

    def check_coords(self, coords):
        """check coords are integers

        Args:
            coords (string): column x row 'cr'

        Returns:
            Bool: True if both positions in coords string are ints;
                  else False
        """
        try:
            int(coords[0])
            int(coords[1])
        except ValueError:
            return False
        return True

    def str_coords_to_int(self, coords):
        """change string coordinates into integers

        Args:
            coords (string): column x row 'cr'

        Returns:
            int : 0 position in coords
            int : 1 position in coords
        """
        x = int(coords[0])
        y = int(coords[1])
        return x, y


    def coords_valid(self, coords):
        """Validate coordinates

        Args:
            coords (string): row x column 'rc'

        Returns:
            Bool: True if coordinates is valid; else False
        """
        x, y = self.str_coords_to_int(coords)
        if ((x >= 1 and x <= 8) and (y >= 1 and y <= 8)):
            return True
        else:
            return False

    def coords_not_equal(self, c_coords, d_coords):
        """Check that current coords are not equal to destination coords

        Args:
            c_coords (string): destination row x column 'rc'
            d_coords (string): destination row x column 'rc'

        Returns:
            Bool: True if c_coords != d_coords; else False
        """
        if c_coords.lower() == d_coords.lower():
            return False
        else:
            return True

    def add_coords(self, coords, shift):
        """adds a shift to coords

        Args:
            coords (string): column x row 'cr'
            shift (tuple): amount to shift (row, column)

        Returns:
            string: coords with shift applied 'cr'
        """
        x, y = self.str_coords_to_int(coords)
        x += shift[0]
        y += shift[1]
        return f'{x}{y}'

    def move_piece(self, piece, c_coords, d_coords, board_state):
        """Move piece on board

        Args:
            piece (string): unicode chess piece
            c_coords (string): column x row 'cr'
            d_coords (string): column x row 'cr'

        Returns:
            Dict: board_state with applied movement changes
        """
        board_state[d_coords][2] = piece
        board_state[c_coords][2] = self.empty
        return board_state

    def moves_dir(self, coords, shift, is_black, board_state):
        """checks all possible moves for piece

        Args:
            coords (string): column x row 'cr'
            shift (tuple): amount to shift (column, row)
            is_black (bool): if piece in movement is black: True; else False
            board_state (dict): dictionary representation of a board state

        Returns:
            list: possible moves based on shift and coords
        """
        moves = []
        coords = self.add_coords(coords, shift)
        while True:
            try:
                if self.is_empty(coords, board_state):
                    moves.append(coords)
                    coords = self.add_coords(coords, shift)
                    continue
                elif self.is_enemy(coords, is_black, board_state):
                    moves.append(coords)
                    break
                elif self.is_friendly(coords, is_black, board_state):
                    break
                else:
                    break
            except KeyError:
                break
        return moves

    def piece_movement(self, piece, c_coords, d_coords):
        """Validate movement of a piece

        Args:
            piece (string): a unicode chess piece
            c_coords (string): current coordinates of piece
            d_coords (string): destination coordinates of piece

        Returns:
            Boolean: True if move is valid based on piece movement restrictions
                else; False
        """
        x1, y1 = self.str_coords_to_int(c_coords)
        x2, y2 = self.str_coords_to_int(d_coords)
        # king movement definitions
        if piece == self.wk or piece == self.bk:
            if (abs(x1 - x2), abs(y1 - y2)) in [(0,1), (1,0), (1,1)]:
                return True
            else:
                return False
        # queen movement definitions
        elif piece == self.wq or piece == self.bq:
            if x1 == x2 or y1 == y2:
                return True
            elif abs(x1 - x2) == abs(y1 - y2):
                return True
            else:
                return False
        # bishop movement definitions
        elif piece == self.wb or piece == self.bb:
            if abs(x1 - x2) == abs(y1 - y2):
                return True
            else:
                return False
        # knight movement definitions
        elif piece == self.wn or piece == self.bn:
            if (abs(x1 - x2), abs(y1 - y2)) in [(2,1), (1,2)]:
                return True
            else:
                return False
        # rook movement definitions
        elif piece == self.wr or piece == self.br:
            if x1 == x2 or y1 == y2:
                return True
            else:
                return False
        # pawn white movement definitions
        elif piece == self.wp:
            if y2 - y1 == 1 and abs(x2 - x1) <= 1:
                return True
            elif c_coords[1] == '2' and abs(y2 - y1) == 2 and x1 == x2:
                return True
            else:
                return False
        # pawn black movement definitions
        elif piece == self.bp:
            if y1 - y2 == 1 and abs(x2 - x1) <= 1:
                return True
            elif c_coords[1] == '7' and abs(y1 - y2) == 2 and x1 == x2:
                return True
            else:
                return False

    def possible_moves(self, piece, coords, board_state):
        """Given current board state check all possible moves

        Args:
            piece (string): unicode chess piece
            coords (string): row x column 'rc'
            board_state (dict): dictionary representation of a board state
        """
        moves = []
        diag = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        horz_vert = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # king moves
        if piece in [self.wk, self.bk]:
            for shift in diag:
                moves += (self.moves_dir(coords, shift, self.is_black(piece),
                    board_state))
            for shift in horz_vert:
                moves += (self.moves_dir(coords, shift, self.is_black(piece),
                    board_state))
        # queen moves
        elif piece in [self.wq, self.bq]:
            for shift in diag:
                moves += (self.moves_dir(coords, shift, self.is_black(piece),
                    board_state))
            for shift in horz_vert:
                moves += (self.moves_dir(coords, shift, self.is_black(piece),
                    board_state))
        # bishop moves
        elif piece in [self.wb, self.bb]:
            for shift in diag:
                moves += self.moves_dir(coords, shift, self.is_black(piece),
                    board_state)
        # rook moves
        elif piece in [self.wr, self.br]:
            for shift in horz_vert:
                moves += self.moves_dir(coords, shift, self.is_black(piece),
                    board_state)
        # knight moves
        elif piece in [self.wn, self.bn]:
            knight_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1),
                (1, 2), (1, -2), (-1, 2), (-1, -2)]
            for shift in knight_moves:
                moves += self.moves_dir(coords, shift, self.is_black(piece),
                    board_state)
        # white pawn moves
        elif piece == self.wp:
            pawn_moves = []
            x, y = self.str_coords_to_int(coords)
            fwd = f'{x}{y + 1}'
            fwd2 = f'{x}{y + 2}'
            diag_minus = f'{x - 1}{y + 1}'
            diag_plus = f'{x + 1}{y + 1}'
            try:
                if self.is_empty(fwd, board_state):
                    pawn_moves.append(fwd)
                    if self.is_empty(fwd2, board_state):
                        pawn_moves.append(fwd2)
            except KeyError:
                pass
            try:
                if self.is_empty(diag_minus, board_state):
                    pass
                elif self.is_enemy(diag_minus, self.is_black(piece),
                    board_state):
                    pawn_moves.append(diag_minus)
            except KeyError:
                pass
            try:
                if self.is_empty(diag_plus, board_state):
                    pass
                elif self.is_enemy(diag_plus, self.is_black(piece),
                    board_state):
                    pawn_moves.append(diag_plus)
            except KeyError:
                pass
            for move in pawn_moves:
                moves = pawn_moves
        # black pawn moves
        elif piece == self.bp:
            pawn_moves = []
            x, y = self.str_coords_to_int(coords)
            fwd = f'{x}{y - 1}'
            fwd2 = f'{x}{y - 2}'
            diag_minus = f'{x - 1}{y - 1}'
            diag_plus = f'{x + 1}{y - 1}'
            try:
                if self.is_empty(fwd, board_state):
                    pawn_moves.append(fwd)
                    if self.is_empty(fwd2, board_state):
                        pawn_moves.append(fwd2)
            except KeyError:
                pass
            try:
                if self.is_empty(diag_minus, board_state):
                    pass
                elif self.is_enemy(diag_minus, self.is_black(piece),
                    board_state):
                    pawn_moves.append(diag_minus)
            except KeyError:
                pass
            try:
                if self.is_empty(diag_plus, board_state):
                    pass
                elif self.is_enemy(diag_plus, self.is_black(piece),
                    board_state):
                    pawn_moves.append(diag_plus)
            except KeyError:
                pass
            moves = pawn_moves
        m = moves.copy()
        for move in m:
            if not self.piece_movement(piece, coords, move):
                moves.remove(move)
        return list(set(moves))

    def find_piece(self, piece, is_black, board_state):
        """find piece if exists on board. Returns location of only one piece

        Args:
            piece (string): unicode representation of a chess piece
            is_black (bool): True if piece is black; else False
            board_state (dict): dictionary representation of a board state

        Returns:
            string: row x column 'rc' if piece on board; else returns False
        """
        for space in board_state:
            if piece in board_state[space][2] and (
                is_black == self.is_black(board_state[space][2])):
                return space
        return False

    def check_en_passant(self, is_black, c_coords, d_coords, board_state):
        x1, y1 = self.str_coords_to_int(c_coords)
        x2, y2 = self.str_coords_to_int(d_coords)
        x_minus = f'{x2 - 1}{y2}'
        x_plus = f'{x2 + 1}{y2}'
        if abs(y1 - y2) != 2:
            return
        if not self.coords_valid(x_minus):
            pass
        elif not self.is_enemy(x_minus, is_black, board_state):
            pass
        elif not is_black:
            if board_state[x_minus][2] == self.bp:
                self.w_en_passant = [True, f'{x1}{y1 + 1}']
                return
        elif is_black:
            if board_state[x_minus][2] == self.wp:
                self.b_en_passant = [True, f'{x1}{y1 - 1}']
                return
        if not self.coords_valid(x_plus):
            pass
        elif not self.is_enemy(x_plus, is_black, board_state):
            pass
        elif not is_black:
            if self.bp in board_state[x_plus][2]:
                self.w_en_passant = [True, f'{x1}{y1 + 1}']
        elif is_black:
            if self.wp in board_state[x_plus][2]:
                self.b_en_passant = [True, f'{x1}{y1 - 1}']

    def check_promotion(self, is_black, board_state):
        """Checks if pawn has reached eighth rank

        Args:
            is_black (bool): if pawn checking is black True, else False
            board_state (dict): state of the board to check
        
        Returns:
            bool: True if a pawn can be promoted, else False
            string: if True 'xy' coords of pawn, else '00'
        """
        if is_black:
            piece = self.bp
            ranks = ['11', '21', '31', '41', '51', '61', '71', '81']
        else:
            piece = self.wp
            ranks = ['18', '28', '38', '48', '58', '68', '78', '88']
        
        for rank in ranks:
            if piece in board_state[rank]:
                return True, rank
        return False, '00'

    def check_castling(self, is_black, side, board_state):
        """Checks if king can castle

        Args:
            is_black (bool): if king to castle is black True, else False
            side (string): if king side 'king', if queen side 'queen'
            board_state (dict): state of the board to check

        Returns:
            bool: True if castling is valid, else False
        """
        if self.in_check(is_black, board_state):
            return False
        elif is_black:
            if side.lower() == 'king':
                if self.b_king_side_castle:
                    spaces = ['68', '78']
                else:
                    return False
            elif side.lower() == 'queen':
                if self.b_queen_side_castle:
                    spaces = ['48', '38', '28']
        elif not is_black:
            if side.lower() == 'king':
                if self.w_king_side_castle:
                    spaces = ['61', '71']
                else:
                    return False
            elif side.lower() == 'queen':
                if self.w_queen_side_castle:
                    spaces = ['31', '41', '21']
                else:
                    return False
        for space in spaces:
            if not self.is_empty(space, board_state):
                return False
        for space in board_state:
            if self.is_enemy(space, is_black, board_state):
                moves = self.possible_moves(board_state[space][2], space,
                    board_state)
                for move in moves:
                    if move == spaces[0] or move == spaces[1]:
                        return False
                    else:
                        continue
            else:
                continue
        return True

    def check_castling_valid(self, board_state):
        """checks if king or rooks move from their spots

            self.w_king_side_castle, self.w_queen_side_castle,
            self.b_king_side_castle, self.b_queen_side_castle change based on
            if king moves both vars of that color are False, if rook moves
            that direction that color is False
        """
        if self.w_king_side_castle or self.w_queen_side_castle:
            if self.wk not in board_state['51'][2]:
                self.w_king_side_castle = False
                self.w_queen_side_castle = False
            elif self.wr not in board_state['11'][2]:
                self.w_queen_side_castle = False
            elif self.wr not in board_state['81'][2]:
                self.w_king_side_castle = False

        if self.b_king_side_castle or self.b_queen_side_castle:
            if self.bk not in board_state['58'][2]:
                self.b_king_side_castle = False
                self.b_queen_side_castle = False
            elif self.br not in board_state['18'][2]:
                self.b_queen_side_castle = False
            if self.br not in board_state['88'][2]:
                self.b_king_side_castle = False

    def in_check(self, is_black, board_state):
        """check if king is in check

        Args:
            is_black (bool): if king is black True; else False
            board_state (dict): dictionary representation of a board state
        Returns:
            bool: True if king in check; else False
        """
        mov = []
        if is_black is True:
            king_space = self.find_piece(self.bk, is_black, board_state)
        else:
            king_space = self.find_piece(self.wk, is_black, board_state)
        for coords in board_state:
            if is_black != self.is_black(board_state[coords][2]):
                mov += self.possible_moves(board_state[coords][2], coords,
                    board_state)

        if king_space in mov:
            return True
        else:
            return False

    def print_current_state(self, perspective, board_state):
        """Creates printed representation of current chess board

        Args:
            perspective (string): either 'black' or 'white' flips board
                to show proper perspective
        """
        z = ''
        if perspective == 'white':
            for r in range(8, 0, -1):
                b = f' {r} '
                for c in range(1, 9):
                    b += (board_state[f'{r}{c}'][0] +
                        board_state[f'{r}{c}'][2] +
                        board_state[f'{r}{c}'][1])
                z += (f'{b}\n')
            z += '    A  B  C  D  E  F  G  H '
        elif perspective == 'black':
            for r in range(1, 9):
                b = f' {r} '
                for c in range(8, 0, -1):
                    b += (board_state[f'{r}{c}'][0] +
                        board_state[f'{r}{c}'][2] +
                        board_state[f'{r}{c}'][1])
                z += (f'{b}\n')
            z += '    H  G  F  E  D  C  B  A '
        print(z)

    def block_check(self, is_black, board_state):
        """check if friendly piece of king under attack can block

        Args:
            is_black (bool): if king is black True; else False
            board_state (dict): state of board to be tested

        Returns:
            bool: if friendly piece can block check True; else False
        """
        for space in board_state:
            if is_black == self.is_black(board_state[space][2]):
                moves = self.possible_moves(board_state[space][2], space,
                    board_state)
                for move in moves:
                    temp_board = deepcopy(board_state)
                    temp_board = self.move_piece(temp_board[space][2], space,
                        move, temp_board)
                    if self.in_check(is_black, temp_board):
                        pass
                    else:
                        return True
            else:
                continue
        return False

