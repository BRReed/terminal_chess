

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

    def piece_move_main(self, piece, c_coords, d_coords):
        """Takes coordinates and checks if piece to coords is a legitimate move

        Args:
            piece (string): The piece to move
            c_coords (string): Where the piece is currently
            d_coords (string): Where the piece wants to move
        """
        pass

    def piece_in_coords(self, piece, c_coords, d_coords):
        """Checks if space is empty or if space occupied and is opponent

        Args:
            piece (string): chess piece to be moved
            d_coords (string): destination row x column 'rc'
            c_coords (string): current row x column 'rc'
        
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
                      f'dest: {d_coords} current: {c_coords}')
        elif black in repr(piece):
            if white in repr_d_coords:
                return True, False
            elif black in repr_d_coords:
                return False, False
            else:
                print(f'piece_in_coords error piece:{piece}, ' +
                      f'dest: {d_coords} current: {c_coords}')
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
        try:
            x1 = int(c_coords[0])
            y1 = int(c_coords[1])
            x2 = int(d_coords[0])
            y2 = int(d_coords[1])
        except ValueError:
            return False
        # confirm dest coords is a valid board space
        if ((x2 >= 1 and x2 <= 8) and (y2 >= 1 and y2 <= 8)):
            pass
        else:
            return False
        # confirm dest coords is not same as current coords
        if x1 == x2 and y1 == y2:
            return False
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

    def possible_moves(self, piece, coords):
        """Given current board state check all possible moves

        Args:
            piece (string): unicode chess piece
            coords (string): row x column 'rc'
        """
        moves = []
        t = []
        x1 = int(coords[0])
        y1 = int(coords[1])
        diag = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        horz_vert = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        if piece in [self.w_b, self.b_b, self.w_q, self.b_q]:
            for xy in diag:
                t.append(xy)
        if piece in [self.w_r, self.b_r, self.w_q, self.b_q]:
            for xy in horz_vert:
                t.append(xy)
        for drc in t:
            x2 = x1
            y2 = y1
            x_dir = drc[0]
            y_dir = drc[1]
            for _ in range(1, 9):
                if (f'{x2 + x_dir}{y2 + y_dir}') in self.board_dict:
                    x2 += x_dir
                    y2 += y_dir
                    c_move, c_piece  = c.piece_in_coords(piece, coords, f'{x2}{y2}')
                    if c_move and c_piece:
                        moves.append(f'{x2}{y2}')
                    elif c_move and not c_piece:
                        moves.append(f'{x2}{y2}')
                        break
                    elif not c_move:
                        break
                    else:
                        print('what went wrong here?')
                else:
                    break
        print(moves)








c = Chess()

c.possible_moves(c.w_q, '56')
# c.possible_moves(c.w_k, '55')
# c.possible_moves(c.w_q, '56')
