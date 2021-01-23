

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
        self.w_k = ' \u265A '
        self.w_q = ' \u265B '
        self.w_r = ' \u265C '
        self.w_b = ' \u265D '
        self.w_n = ' \u265E '
        self.w_p = ' \u265F '

        self.b_k = '\033[38;2;0;0;0m \u265A '
        self.b_q = '\033[38;2;0;0;0m \u265B '
        self.b_r = '\033[38;2;0;0;0m \u265C '
        self.b_b = '\033[38;2;0;0;0m \u265D '
        self.b_n = '\033[38;2;0;0;0m \u265E '
        self.b_p = '\033[38;2;0;0;0m \u265F '



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

    def piece_placement(self, piece, c_coords, d_coords):
        """Takes coordinates and checks if piece to coords is a legitimate move

        Args:
            piece (string): The piece to move
            c_coords (string): Where the piece is currently
            d_coords (string): Where the piece wants to move
        """
        pass

    def piece_in_coords(self, piece, coords):
        """Checks if space is empty or if space occupied and is opponent

        Args:
            piece (string): chess piece to be moved
            coords (string): row x column 'rc'
        
        Returns:
            Bool: True if movement is allowed; else False
        """
        pass






c = Chess()
print(f'\033[48;2;128;128;128m' + f'\033[38;2;255;255;255m' +
       '\u2654 \u2655 \u2656 \u2657 \u2658 \u2659',
       '\u265A \u265B \u265C \u265D \u265E \u265F ' + f'\033[0m')
print(f'\033[48;2;0;0;0m' + f'\033[38;2;255;255;255m' +
       '\u2654 \u2655 \u2656 \u2657 \u2658 \u2659',
       '\u265A \u265B \u265C \u265D \u265E \u265F ' + f'\033[0m')

print('**********white persp')

c.print_board_dict('white')
print('**********black persp')
c.print_board_dict('black')