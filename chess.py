

class Chess():
    def __init__(self):
        self.create_pieces()
        self.create_board_dict()


    def create_pieces(self):
        """Assign variables to unicode representations of chess pieces
        Vars: self.x_y = unicode_char 
            x = single char piece color; w = white, b = black
            y = single char piece; n = knight; else first char of piece name
        """
        self.w_k = '\033[38;2;255;255;255m \u265A \033[38;0m'
        self.w_q = '\033[38;2;255;255;255m \u265B \033[38;0m'
        self.w_r = '\033[38;2;255;255;255m \u265C \033[38;0m'
        self.w_b = '\033[38;2;255;255;255m \u265D \033[38;0m'
        self.w_n = '\033[38;2;255;255;255m \u265E \033[38;0m'
        self.w_p = '\033[38;2;255;255;255m \u265F \033[38;0m'

        self.w_pieces = [self.w_k, self.w_q, self.w_r, self.w_b, self.w_n,
                         self.w_p]

        self.b_k = '\033[38;2;0;0;0m \u265A \033[38;0m'
        self.b_q = '\033[38;2;0;0;0m \u265B \033[38;0m'
        self.b_r = '\033[38;2;0;0;0m \u265C \033[38;0m'
        self.b_b = '\033[38;2;0;0;0m \u265D \033[38;0m'
        self.b_n = '\033[38;2;0;0;0m \u265E \033[38;0m'
        self.b_p = '\033[38;2;0;0;0m \u265F \033[38;0m'

        self.b_pieces = [self.b_k, self.b_q, self.b_r, self.b_b, self.b_n,
                         self.b_p]

        self.empty = '   '

    def create_board_dict(self):
        """Create dictionary of chess board elements
        Vars:
            self.board_dict:
                keys = [rc] where row is r and column is c. Both represented 
                    by a number
                values = (RGB BG colorcode, unicode chess piece,
                    colorcode reset)
        """
        self.board_dict = {}
        for row in range(1, 9):
            for column in range(1, 9):
                if (row + column) % 2 == 0:
                    self.board_dict[f'{row}{column}'] = [
                            '\033[48;2;57;78;112m', '\033[0m',
                            f'{self.populate_start(row, column)}']
                else:
                    self.board_dict[f'{row}{column}'] = [
                            '\033[48;2;66;135;245m', '\033[0m',
                            f'{self.populate_start(row, column)}']
    
    def populate_start(self, r, c):
        """Populates pieces on board at start of round
        Args:
            r (string): row on chess board
            c (string): column on chess board
        Returns:
            Var equal to chess piece
        """
        if r == 1:
            if c == 1 or c == 8:
                return self.w_r
            elif c == 2 or c == 7:
                return self.w_n
            elif c == 3 or c == 6:
                return self.w_b
            elif c == 4:
                return self.w_q
            elif c == 5:
                return self.w_k
            else:
                print(f'well, this is bad r, c = {r}, {c}')
                return
        elif r == 2:
            return self.w_p
        elif r == 7: 
            return self.b_p
        elif r == 8:
            if c == 1 or c == 8:
                return self.b_r
            elif c == 2 or c == 7:
                return self.b_n
            elif c == 3 or c == 6:
                return self.b_b
            elif c == 4:
                return self.b_q
            elif c == 5:
                return self.b_k
            else:
                print(f'well, this is bad r, c = {r}, {c}')
        else:
            return '   '


    def print_board_dict(self, perspective):
        """Creates printed representation of current chess board

        Args:
            perspective (string): either 'black' or 'white' flips board 
                to show proper perspective to player
        """
        z = ''
        if perspective == 'white':
            for r in range(8, 0, -1):
                b = f' {r} '
                for c in range(1, 9):
                    b += (self.board_dict[f'{r}{c}'][0] +
                          self.board_dict[f'{r}{c}'][2] +
                          self.board_dict[f'{r}{c}'][1])
                z += (f'{b}\n')
            z += '    A  B  C  D  E  F  G  H '
        elif perspective == 'black':
            for r in range(1, 9):
                b = f' {r} '
                for c in range(8, 0, -1):
                    b += (self.board_dict[f'{r}{c}'][0] +
                          self.board_dict[f'{r}{c}'][2] +
                          self.board_dict[f'{r}{c}'][1])
                z += (f'{b}\n')
            z += '    H  G  F  E  D  C  B  A '
        print(z)
    
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

    def piece_in_coords(self, piece, d_coords):
        """Checks if space is empty or if space occupied and is opponent

        Args:
            piece (string): chess piece to be moved
            d_coords (string): destination row x column 'rc'

        Returns:
            Bool: True if movement is allowed; else False
            Bool: True if space is empty; else False
        """
        white = '38;2;255;255;255m'
        black = '38;2;0;0;0m'
        repr_d_coords = repr(self.board_dict[d_coords])
        if self.empty in repr_d_coords:
            return True, True
        if white in repr(piece):
            if black in repr_d_coords:
                return True, False
            elif white in repr_d_coords:
                return False, False
            else:
                print(f'piece_in_coords error piece:{piece}, ' +
                      f'dest: {d_coords}')
        elif black in repr(piece):
            if white in repr_d_coords:
                return True, False
            elif black in repr_d_coords:
                return False, False
            else:
                print(f'piece_in_coords error piece:{piece}, ' +
                      f'dest: {d_coords}')
        else:
            print('lose')

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
        if piece == self.w_k or piece == self.b_k:
            if (abs(x1 - x2), abs(y1 - y2)) in [(0,1), (1,0), (1,1)]:
                return True
            else:
                return False
        # queen movement definitions
        elif piece == self.w_q or piece == self.b_q:
            if x1 == x2 or y1 == y2:
                return True
            elif abs(x1 - x2) == abs(y1 - y2):
                return True
            else:
                return False
        # bishop movement definitions
        elif piece == self.w_b or piece == self.b_b:
            if abs(x1 - x2) == abs(y1 - y2):
                return True
            else:
                return False
        # knight movement definitions
        elif piece == self.w_n or piece == self.b_n:
            if (abs(x1 - x2), abs(y1 - y2)) in [(2,1), (1,2)]:
                return True
            else:
                return False
        # rook movement definitions
        elif piece == self.w_r or piece == self.b_r:
            if x1 == x2 or y1 == y2:
                return True
            else:
                return False
        # pawn white movement definitions
        elif piece == self.w_p:
            if x2 - x1 == 1 and abs(y2 - y1) <= 1:
                return True
            else:
                return False
        # pawn black movement definitions
        elif piece == self.b_p:
            if x1 - x2 == 1 and abs(y2 - y1) <= 1:
                return True
            else:
                return False
        else:
            print(f'Uh oh!, d_coords = {d_coords}, c_coords = {c_coords}, ' + 
                  f'piece = {piece}')
            return False

    def move_piece(self, piece, c_coords, d_coords):
        """Move piece on board

        Args:
            piece (string): unicode chess piece 
            c_coords (string): row x column 'rc'
            d_coords (string): row x column 'rc'
        """
        self.board_dict[d_coords][2] = piece 
        self.board_dict[c_coords][2] = self.empty
    
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

    def is_friendly(self, coords, is_black):
        """checks if piece in coords is friendly

        Args:
            coords (string): row x column 'rc'
            is_black (bool): True if piece in movement is black; else False

        Returns:
            Bool: If piece in bounds is same color as piece in coords True;
                  else False
        """
        if is_black == self.is_black(self.board_dict[coords][2]):
            return True
        else:
            return False

    def is_enemy(self, coords, is_black):
        """checks if piece in coords is enemy

        Args:
            coords (string): row x column 'rc'
            is_black (bool): True if piece in movement is black; else False

        Returns:
            [type]: [description]
        """
        if is_black != self.is_black(self.board_dict[coords][2]):
            return True
        else:
            return False

    def is_empty(self, coords):
        """checks if coords is empty

        Args:
            coords (string): row x column 'rc'

        Returns:
            Bool: True if space is empty; else False
        """
        if self.empty in self.board_dict[coords][2]:
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

    def in_check(self, coords, is_black):
        pass

    def find_piece(self, piece, is_black):
        for space in self.board_dict:
            if piece in self.board_dict[space][2] and (
                is_black == self.is_black(self.board_dict[space][2])):
                return space
        return 



    def moves_dir(self, coords, shift, is_black):
        """checks all possible moves for piece

        Args:
            coords (string): row x column 'rc'
            shift (tuple): amount to shift (row, column)
            is_black (bool): if piece in movement is black: True; else False

        Returns:
            list: possible moves based on shift and coords
        """
        moves = []
        coords = self.add_coords(coords, shift)
        while True:
            try:
                if self.is_empty(coords):
                    moves.append(coords)
                    coords = self.add_coords(coords, shift)
                    continue
                elif self.is_enemy(coords, is_black):
                    moves.append(coords)
                    break
                elif self.is_friendly(coords, is_black):
                    break
                else:
                    break
            except KeyError:
                break
        return moves

    def possible_moves(self, piece, coords):
        """Given current board state check all possible moves

        Args:
            piece (string): unicode chess piece
            coords (string): row x column 'rc'
        """
        moves = []
        diag = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        horz_vert = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # king moves
        if piece in [self.w_k, self.b_k]:
            for shift in diag:
                moves += (self.moves_dir(coords, shift, self.is_black(piece)))
            for shift in horz_vert:
                moves += (self.moves_dir(coords, shift, self.is_black(piece)))
        # queen moves
        elif piece in [self.w_q, self.b_q]:
            for shift in diag:
                moves += (self.moves_dir(coords, shift, self.is_black(piece)))
            for shift in horz_vert:
                moves += (self.moves_dir(coords, shift, self.is_black(piece)))
        # bishop moves
        elif piece in [self.w_b, self.b_b]:
            for shift in diag:
                moves += self.moves_dir(coords, shift, self.is_black(piece))
        # rook moves
        elif piece in [self.w_r, self.b_r]:
            for shift in horz_vert:
                moves += self.moves_dir(coords, shift, self.is_black(piece))
        # knight moves
        elif piece in [self.w_n, self.b_n]:
            knight_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), 
                            (1, 2), (1, -2), (-1, 2), (-1, -2)]
            for shift in knight_moves:
                moves += self.moves_dir(coords, shift, self.is_black(piece))
        # white pawn moves
        elif piece is self.w_p:
            pawn_moves = []
            x, y = self.str_coords_to_int(coords)
            fwd = f'{x + 1}{y}'
            diag_minus = f'{x + 1}{y - 1}'
            diag_plus = f'{x + 1}{y + 1}'
            if not self.is_enemy(fwd, self.is_black(piece)):
                pawn_moves.append((1, 0))
            if self.is_enemy(diag_minus, self.is_black(piece)):
                pawn_moves.append((1, -1))
            if self.is_enemy(diag_plus, self.is_black(piece)):
                pawn_moves.append((1, 1))
            for shift in pawn_moves:
                moves += self.moves_dir(coords, shift, self.is_black(piece))
        # black pawn moves
        elif piece is self.b_p:
            pawn_moves = []
            x, y = self.str_coords_to_int(coords)
            fwd = f'{x - 1}{y}'
            diag_minus = f'{x - 1}{y - 1}'
            diag_plus = f'{x - 1}{y + 1}'
            if not self.is_enemy(fwd, self.is_black(piece)):
                pawn_moves.append((-1, 0))
            if self.is_enemy(diag_minus, self.is_black(piece)):
                pawn_moves.append((-1, -1))
            if self.is_enemy(diag_plus, self.is_black(piece)):
                pawn_moves.append((-1, 1))
            for shift in pawn_moves:
                moves += self.moves_dir(coords, shift, self.is_black(piece))

        m = moves.copy()
        for move in m:
            if not self.piece_movement(piece, coords, move):
                moves.remove(move)
        # add function for not putting self in check
        return moves





c = Chess()

print(c.possible_moves(c.w_q, '66'))
c.print_board_dict('white')
# c.possible_moves(c.w_k, '55')
# c.possible_moves(c.w_q, '56')
