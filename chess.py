

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

        self.b_k = '\033[38;2;0;0;0m \u265A \033[38;0m'
        self.b_q = '\033[38;2;0;0;0m \u265B \033[38;0m'
        self.b_r = '\033[38;2;0;0;0m \u265C \033[38;0m'
        self.b_b = '\033[38;2;0;0;0m \u265D \033[38;0m'
        self.b_n = '\033[38;2;0;0;0m \u265E \033[38;0m'
        self.b_p = '\033[38;2;0;0;0m \u265F \033[38;0m'



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

    def piece_in_coords(self, piece, coords):
        """Checks if space is empty or if space occupied and is opponent

        Args:
            piece (string): chess piece to be moved
            coords (string): row x column 'rc'
        
        Returns:
            Bool: True if movement is allowed; else False
        """
        pass

    def piece_movement(self, piece, c_coords, d_coords):
        """Validate movement of a piece

        Args:
            piece (string): a unicode chess piece
            c_coords (string): current coordinates of piece
            d_coords ([type]): destination coordinates of piece

        Returns:
            Boolean: True if move is valid based on piece movement restrictions
                else; False
        """
        # confirm dest coords is a valid board space
        if ((int(d_coords[0]) >= 1 and int(d_coords[0]) <= 8) and (
            int(d_coords[1]) >= 1 and int(d_coords[1]) <= 8
            )) and (int(d_coords) != int(c_coords)):
            pass
        else:
            return False
        # confirm dest coords is not same as current coords
        if int(d_coords) == int(c_coords):
            return False
        # king movement definitions
        if piece == self.w_k or piece == self.b_k:
            if (int(d_coords[0]) == (int(c_coords[0]))) or (
                int(d_coords[0]) == (int(c_coords[0]) - 1)) or (
                int(d_coords[0]) == (int(c_coords[0]) + 1)) and (
                int(d_coords[1]) == (int(c_coords[1]))) or (
                int(d_coords[1]) == (int(c_coords[1]) - 1)) or (
                int(d_coords[1]) == (int(c_coords[1]) + 1)
            ):
                return True
            else:
                return False
        # queen movement definitions
        elif piece == self.w_q or piece == self.b_q:
            if (int(d_coords[0]) == (int(c_coords[0]))) or (
                int(d_coords[1]) == (int(c_coords[1]))):
                return True
            elif abs(int(d_coords[0]) - int(c_coords[0])) == (
                 abs(int(d_coords[1]) - int(c_coords[1]))
            ):
                return True
            else:
                return False
        # bishop movement definitions
        elif piece == self.w_b or piece == self.b_b:
            if abs(int(d_coords[0]) - int(c_coords[0])) == (
               abs(int(d_coords[1]) - int(c_coords[1]))
            ):
                return True
            else:
                return False
        # knight movement definitions
        elif piece == self.w_n or piece == self.b_n:
            if ((abs(int(d_coords[0]) - int(c_coords[0])) == 2) and (
                 abs(int(d_coords[1]) - int(c_coords[1])) == 1)) or ((
                 abs(int(d_coords[0]) - int(c_coords[0])) == 1) and (
                 abs(int(d_coords[1]) - int(c_coords[1])) == 2)
            ):
                return True
            else:
                return False










c = Chess()
print('**********white persp')
c.print_board_dict('white')
print('**********black persp')
c.print_board_dict('black')
print(c.board_dict['11'][2])
c.board_dict['11'][2] = 'Friendship'
print(c.board_dict['11'][2])

print(c.piece_movement(c.w_k, '22', '22')) # true
print(c.piece_movement(c.w_k, '22', '13')) # true
print(c.piece_movement(c.w_k, '22', '34')) # false
print(c.piece_movement(c.w_k, '18', '09')) # false
print(c.piece_movement(c.w_q, '14', '47')) # true
print(c.piece_movement(c.w_q, '14', '54')) # true
print(c.piece_movement(c.w_q, '14', '87')) # false
print(c.piece_movement(c.w_b, '11', '44')) # true
print(c.piece_movement(c.w_b, '84', '51')) # true
print(c.piece_movement(c.w_b, '55', '46')) # true
print(c.piece_movement(c.w_b, '65', '14')) # false
print(c.piece_movement(c.w_n, '65', '14')) # false
print(c.piece_movement(c.w_n, '65', '84')) # true
print(c.piece_movement(c.w_n, '65', '53')) # true
print(c.piece_movement(c.w_n, '82', '74')) # true
print(abs(6 - 5))
print(abs(5 - 3))