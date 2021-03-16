def assign_piece(is_black, piece):
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







class Chess():
    def __init__(self):
        
        self.bs = BoardState()
        self.wk = assign_piece(False, 'king')
        self.wq = assign_piece(False, 'queen')
        self.wr = assign_piece(False, 'rook')
        self.wb = assign_piece(False, 'bishop')
        self.wn = assign_piece(False, 'knight')
        self.wp = assign_piece(False, 'pawn')

        self.bk = assign_piece(True, 'king')
        self.bq = assign_piece(True, 'queen')
        self.br = assign_piece(True, 'rook')
        self.bb = assign_piece(True, 'bishop')
        self.bn = assign_piece(True, 'knight')
        self.bp = assign_piece(True, 'pawn')
        self.empty = '   '
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
                    b += (self.current_state[f'{r}{c}'][0] +
                          self.current_state[f'{r}{c}'][2] +
                          self.current_state[f'{r}{c}'][1])
                z += (f'{b}\n')
            z += '    A  B  C  D  E  F  G  H '
        elif perspective == 'black':
            for r in range(1, 9):
                b = f' {r} '
                for c in range(8, 0, -1):
                    b += (self.current_state[f'{r}{c}'][0] +
                          self.current_state[f'{r}{c}'][2] +
                          self.current_state[f'{r}{c}'][1])
                z += (f'{b}\n')
            z += '    H  G  F  E  D  C  B  A '
        print(z)


    def move_piece(self, piece, c_coords, d_coords):
        """Move piece on board

        Args:
            piece (string): unicode chess piece 
            c_coords (string): row x column 'rc'
            d_coords (string): row x column 'rc'
        """
        self.current_state[d_coords][2] = piece 
        self.current_state[c_coords][2] = self.empty
    



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
            king_space = self.bs.find_piece(self.bk, is_black, board_state)
        else:
            king_space = self.bs.find_piece(self.wk, is_black, board_state)
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
            king_space = self.bs.find_piece(self.bk, is_black, board_state)
            king_spaces = self.bs.possible_moves(self.bk, king_space, board_state)
            
        else:
            king_space = self.bs.find_piece(self.wk, is_black, board_state)
            king_spaces = self.bs.possible_moves(self.wk, king_space, board_state)

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
        self.wk = assign_piece(False, 'king')
        self.wq = assign_piece(False, 'queen')
        self.wr = assign_piece(False, 'rook')
        self.wb = assign_piece(False, 'bishop')
        self.wn = assign_piece(False, 'knight')
        self.wp = assign_piece(False, 'pawn')

        self.bk = assign_piece(True, 'king')
        self.bq = assign_piece(True, 'queen')
        self.br = assign_piece(True, 'rook')
        self.bb = assign_piece(True, 'bishop')
        self.bn = assign_piece(True, 'knight')
        self.bp = assign_piece(True, 'pawn')
        self.empty = '   '

    def create_start_state(self):
        """Create start game board state
        Vars:
            self.start_state:
                keys = [rc] where row is r and column is c. Both represented 
                    by a number
                values = (RGB BG colorcode, unicode chess piece,
                    colorcode reset)
        """
        start_state = {}
        for row in range(1, 9):
            for column in range(1, 9):
                if (row + column) % 2 == 0:
                    start_state[f'{row}{column}'] = [
                            '\033[48;2;57;78;112m', '\033[0m',
                            f'{self.populate_start(row, column)}']
                else:
                    start_state[f'{row}{column}'] = [
                            '\033[48;2;66;135;245m', '\033[0m',
                            f'{self.populate_start(row, column)}']
        return start_state
    
    def populate_start(self, r, c):
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
                print(f'well, this is bad r, c = {r}, {c}')
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
                print(f'well, this is bad r, c = {r}, {c}')
        else:
            return '   '

    def check_coords(self, coords):
        """check coords are integers

        Args:
            coords (string): row x column 'rc'

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
            coords (string): row x column 'rc'

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

    def move_piece(self, piece, c_coords, d_coords, board_state):
        """Move piece on board

        Args:
            piece (string): unicode chess piece 
            c_coords (string): row x column 'rc'
            d_coords (string): row x column 'rc'
        """
        board_state[d_coords][2] = piece 
        board_state[c_coords][2] = self.empty
        return board_state

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
            coords (string): row x column 'rc'
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
            coords (string): row x column 'rc'
            is_black (bool): True if piece in movement is black; else False
            board_state (dict): dictionary representation of a board state
        Returns:
            [type]: [description]
        """
        if is_black != self.is_black(board_state[coords][2]):
            return True
        else:
            return False

    def is_empty(self, coords, board_state):
        """checks if coords is empty

        Args:
            coords (string): row x column 'rc'
            board_state (dict): dictionary representation of a board state
        Returns:
            Bool: True if space is empty; else False
        """
        if self.empty in board_state[coords][2]:
            return True
        else:
            return False

    def add_coords(self, coords, shift):
        """adds a shift to coords

        Args:
            coords (string): row x column 'rc'
            shift (tuple): amount to shift (row, column)

        Returns:
            string: coords with shift applied 'rc'
        """
        x, y = self.str_coords_to_int(coords)
        x += shift[0]
        y += shift[1]
        return f'{x}{y}'

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

    def moves_dir(self, coords, shift, is_black, board_state):
        """checks all possible moves for piece

        Args:
            coords (string): row x column 'rc'
            shift (tuple): amount to shift (row, column)
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
            if x2 - x1 == 1 and abs(y2 - y1) <= 1:
                return True
            else:
                return False
        # pawn black movement definitions
        elif piece == self.bp:
            if x1 - x2 == 1 and abs(y2 - y1) <= 1:
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
        elif piece is self.wp:
            pawn_moves = []
            x, y = self.str_coords_to_int(coords)
            fwd = f'{x + 1}{y}'
            diag_minus = f'{x + 1}{y - 1}'
            diag_plus = f'{x + 1}{y + 1}'
            try:
                if self.is_empty(fwd, board_state):
                    pawn_moves.append((1, 0))
            except KeyError:
                pass
            try:
                if self.is_empty(diag_minus, board_state):
                    pass
                elif self.is_enemy(diag_minus, self.is_black(piece), 
                                   board_state):
                    pawn_moves.append((1, -1))
            except KeyError:
                pass
            try:
                if self.is_empty(diag_plus, board_state):
                    pass
                elif self.is_enemy(diag_plus, self.is_black(piece), 
                                   board_state):
                    pawn_moves.append((1, 1))
            except KeyError:
                pass
            for shift in pawn_moves:
                moves += self.moves_dir(coords, shift, self.is_black(piece), 
                                        board_state)
        # black pawn moves
        elif piece is self.bp:
            pawn_moves = []
            x, y = self.str_coords_to_int(coords)
            fwd = f'{x - 1}{y}'
            diag_minus = f'{x - 1}{y - 1}'
            diag_plus = f'{x - 1}{y + 1}'
            try:
                if self.is_empty(fwd, board_state):
                    pawn_moves.append((-1, 0))
            except KeyError:
                pass
            try:
                if self.is_empty(diag_minus, board_state):
                    pass
                elif self.is_enemy(diag_minus, self.is_black(piece), 
                                   board_state):

                    pawn_moves.append((-1, -1))
            except KeyError:
                pass
            try:
                if self.is_empty(diag_plus, board_state):
                    pass
                elif self.is_enemy(diag_plus, self.is_black(piece), 
                                   board_state):
                    pawn_moves.append((-1, 1))
            except KeyError:
                pass
            
            for shift in pawn_moves:
                moves += self.moves_dir(coords, shift, self.is_black(piece), 
                                        board_state)
        m = moves.copy()
        for move in m:
            if not self.piece_movement(piece, coords, move):
                moves.remove(move)
        # add function for not putting self in check
        return moves

    def in_check(self, is_black, board_state):
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
                    temp_board = board_state.copy()
                    temp_board = self.move_piece(temp_board[space][2], space, 
                                                 move, temp_board)
                    if self.in_check(is_black, temp_board):
                        continue
                    else:
                        return True
            else:
                continue
        return False

