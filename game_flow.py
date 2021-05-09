from game_logic import Chess

class Game():
    def __init__(self):
        c = Chess()

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
            c_coords (str): row x column space in chessboard, start coords
            d_coords (str): row x column space in chessboard, end coords

        Returns:
            BOOL: True if move was allowed and completed, else False
        """
        if not c.bs.check_coords(d_coords) or not c.bs.check_coords(c_coords):
            return False
        if not c.bs.coords_valid(d_coords) or not c.bs.coords_valid(c_coords):
            return False
        if not c.bs.coords_not_equal(c_coords, d_coords):
            return False

        p_is_black = c.bs.is_black(player['color'])
        piece = c.current_state[c_coords][2]
        if piece == c.bs.empty:
            return False
        if c.bs.is_black(piece) != p_is_black:
            return False

        temp_board = copy(c.current_state)
        temp_board = c.bs.move_piece(piece, c_coords, d_coords, temp_board)
        if c.bs.in_check(c.bs.is_black(player), temp_board):
            return False
        if c.bs.piece_movement(piece, c_coords, d_coords):
            c.bs.check_en_passant(p_is_black, c_coords, d_coords,
                c.current_state)
            c.move_piece(piece, c_coords, d_coords)
            c.bs.check_castling_valid(c.current_state)
            return True
        else:
            return False

    def list_moves(self, player, piece, c_coords):
        """returns list of all possible moves for piece in c_coords"""
        pass

    def resignation(self, player):
        """allows player to resign"""
        pass

    def castle(self, player, dir):
        """allows player to castle"""
        p_is_black = c.bs.is_black(player['color'])
        if p_is_black:
            pass
    
    def draw(self, player):
        """allows player to call draw"""
        pass

    def get_piece(player, piece):
        """takes player and piece, returns color piece"""
        pass