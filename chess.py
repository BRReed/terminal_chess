

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

        self.b_k = ' \u2654 '
        self.b_q = ' \u2655 '
        self.b_r = ' \u2656 '
        self.b_b = ' \u2657 '
        self.b_n = ' \u2658 '
        self.b_p = ' \u2659 '
        #

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
        piece = '   '
        for row in range(1, 9):
            for column in range(1, 9):
                if (row + column) % 2 == 0:
                    self.board_dict[f'{row}{column}'] = (
                            '\033[48;2;0;0;0m', f'{piece}', '\033[0m')
                else:
                    self.board_dict[f'{row}{column}'] = (
                            '\033[48;2;128;128;128m', f'{piece}', '\033[0m')

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
                          self.board_dict[f'{r}{c}'][1] +
                          self.board_dict[f'{r}{c}'][2])
                z += (f'{b}\n')
            z += '    A  B  C  D  E  F  G  H '
        elif perspective == 'black':
            for r in range(1, 9):
                b = f' {r} '
                for c in range(8, 0, -1):
                    b += (self.board_dict[f'{r}{c}'][0] +
                          self.board_dict[f'{r}{c}'][1] +
                          self.board_dict[f'{r}{c}'][2])
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