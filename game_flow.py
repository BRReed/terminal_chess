from game_logic import Chess

class Game():
    def __init__(self):
        self.c = Chess()

    def start_game(self, player1, player2):
        """assigns vars for start of game

        Args:
            player1 (dict): user: unique user id, color: unicode white
            player2 ([type]): user: unique user id, color: unicode black
        """
        self.p1 = player1
        self.p2 = player2


    def move(self, player, c_coords, d_coords):
        """allows player to move piece

        Args:
            player (dict): dictionary containing user, color
            c_coords (str): column x row space in chessboard, start coords
            d_coords (str): column x row space in chessboard, end coords

        Returns:
            BOOL: True if move was allowed and completed, else False
        """
        if (not self.c.bs.check_coords(d_coords) or not
            self.c.bs.check_coords(c_coords)):
            return False
        if (not self.c.bs.coords_valid(d_coords) or not
            self.c.bs.coords_valid(c_coords)):
            return False
        if not self.c.bs.coords_not_equal(c_coords, d_coords):
            return False

        p_is_black = self.c.bs.is_black(player['color'])
        piece = self.c.current_state[c_coords][2]
        if piece == self.c.bs.empty:
            return False
        if self.c.bs.is_black(piece) != p_is_black:
            return False

        temp_board = self.c.current_state.copy()
        temp_board = self.c.bs.move_piece(piece, c_coords, d_coords, 
            temp_board)
        if self.c.bs.in_check(self.c.bs.is_black(player), temp_board):
            return False
        if self.c.bs.piece_movement(piece, c_coords, d_coords):
            self.c.bs.check_en_passant(p_is_black, c_coords, d_coords,
                self.c.current_state)
            self.c.move_piece(piece, c_coords, d_coords)
            self.c.bs.check_castling_valid(self.c.current_state)
            return True
        else:
            return False

    def list_moves(self, player, piece, c_coords):
        """returns list of all possible moves for piece in c_coords"""
        pass

    def resignation(self, player):
        """allows player to resign"""
        pass

    def castle(self, player, side):
        """allows player to castle

        Args:
            player (dict): user: unique user id, color: unicode black or white
            side (str): 'queen' or 'king'
        Returns:
            bool: True if castling was allowed and completed, else False
        """
        p_is_black = self.c.bs.is_black(player['color'])
        if not self.castle_valid(p_is_black, side):
            return False
        if self.c.bs.check_castling(p_is_black, side, self.c.current_state):
            self.c.castle_move(p_is_black, side)
            return True
        else:
            return False

    def castle_valid(self, is_black, side):
        """checks T/F castle vars in game_logic.BoardState 

        Args:
            is_black (bool): True if player is black, else False
            side (str): 'queen' or 'king'
        Returns:
            bool: True if player can castle to that side, else False
        """
        if is_black:
            if side == 'king':
                return self.c.bs.b_king_side_castle
            elif side == 'queen':
                return self.c.bs.b_queen_side_castle
        if not is_black:
            if side == 'king':
                return self.c.bs.w_king_side_castle
            elif side == 'queen':
                return self.c.bs.w_queen_side_castle

    def draw(self, player):
        """allows player to call draw"""
        pass

    def get_piece(self, player, piece):
        """takes player and piece, returns color piece"""
        pass