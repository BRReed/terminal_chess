from game_logic import Chess

class Game():
    def __init__(self):
        c = Chess()

    def start_game(self, player1, player2):
        self.white = player1
        self.black = player2

    def move(self, player, piece, c_coords, d_coords):
        """allows player to move piece

        Args:
            player ([type]): [description]
            piece ([type]): [description]
            c_coords ([type]): [description]
            d_coords ([type]): [description]

        Returns:
            [type]: [description]
        """
        if self.get_piece(player, piece) not in c.current_state(c_coords):
            return False
        if not c.bs.check_coords(d_coords):
            return False
        if not c.bs.coords_valid(d_coords):
            return False
        if not c.bs.coords_not_equal(c_coords, d_coords):
            return False
        if c.bs.piece_movement(piece, c_coords, d_coords):
            c.move_piece(piece, c_coords, d_coords)
            return True

    def list_moves(self, player, piece, c_coords):
        """returns list of all possible moves for piece in c_coords"""
        pass

    def resignation(self, player):
        """allows player to resign"""
        pass

    def castle(self, player, dir):
        """allows player to castle"""
        pass
    
    def draw(self, player):
        """allows player to call draw"""
        pass

    def get_piece(player, piece):
        """takes player and piece, returns color piece"""
        pass