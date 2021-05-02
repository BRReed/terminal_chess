from chess import Chess

class Game():
    def __init__(self):
        c = Chess()

    def start_game(self, player1, player2):
        self.white = player1
        self.black = player2

    def move(self, player, piece, c_coords, d_coords):
        if self.get_piece(player, piece) not in c.current_state(c_coords):
            return False
        

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