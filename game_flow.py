from game_logic import Chess
from copy import deepcopy

class Game():
    def __init__(self):
        self.c = Chess()

    def create_new_game(self):
        return self.c.current_state

    def start_game(self, player1, player2):
        """assigns vars for start of game

        Args:
            player1 (dict): user: unique user id, color: unicode white
            player2 ([type]): user: unique user id, color: unicode black
        """
        self.p1 = player1
        self.p2 = player2

    def end_game(self, winner):
        """ends current game
        Args:
            winner: (bool): True if winner is black, else False

        """
        if winner:
            print("black wins")
        else:
            print("white wins")

    def move(self, player, c_coords, d_coords):
        """allows player to move piece

        Args:
            player (str): color of player pieces 'white' or 'black'
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

        if player == 'black':
            p_is_black = True
        else:
            p_is_black = False
        piece = self.c.current_state[c_coords][2]
        if piece == self.c.bs.empty:
            return False
        if self.c.bs.is_black(piece) != p_is_black:
            return False

        temp_board = deepcopy(self.c.current_state)
        temp_board = self.c.bs.move_piece(piece, c_coords, d_coords,
            temp_board)
        possible_moves = self.c.bs.possible_moves(piece, c_coords,
                                                  self.c.current_state)
        if self.c.bs.in_check(p_is_black, temp_board):
            return False
        if (self.c.bs.piece_movement(piece, c_coords, d_coords) and
            d_coords in possible_moves):
            self.c.bs.check_en_passant(p_is_black, c_coords, d_coords,
                self.c.current_state)
            self.c.move_piece(piece, c_coords, d_coords)
            self.c.bs.check_castling_valid(self.c.current_state)
            if self.c.bs.in_check(not p_is_black, self.c.current_state):
                if self.c.check_mate(not p_is_black, self.c.current_state):
                    self.end_game(p_is_black)
                else:
                    print('in check') # change to specify player in check
            return True
        else:
            return False

    def list_moves(self, player, piece, c_coords):
        """returns list of all possible moves for piece in c_coords"""
        pass

    def resignation(self, player):
        """allows player to resign"""
        if self.c.bs.is_black(player['color']):
            self.end_game(False)
        else:
            self.end_game(True)

    def castle(self, is_black, side):
        """allows player to castle

        Args:
            is_black (bool): True if player is black, else False
            side (str): 'queen' or 'king'
        Returns:
            bool: True if castling was allowed and completed, else False
        """
        if not self.castle_valid(is_black, side):
            return False
        if self.c.bs.check_castling(is_black, side, self.c.current_state):
            self.c.castle_move(is_black, side)
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

    def input_parse(self, user_turn, user_input):
        """Calls method based on player input
        """
        if not user_turn:
            valid_commands = ["(=)", "draw", "xx", "resign", "back"]
        elif user_turn:
            valid_commands = ["(=)", "draw", "xx", "resign", "back", "0-0", "0-0-0"]
        input_valid = self.validate_command(user_turn, user_input, valid_commands)
        if not input_valid:
            return False
        # if input valid parse text
            
            

    def validate_command(self, user_turn, user_input, valid_commands):
        """Returns True if user input is valid, else returns False

        Args:
            g (cls): instance of a game
            user_turn (bool): if it is the user's turn True, else False
            user_input (str): input from user
            valid_commands (list): list of valid commands aside from coords

        Returns:
            bool: True if input is valid, else False
        """
        if user_input in valid_commands:
            return True
        if user_turn:
            return self.c.bs.alpha_coords_to_nums(user_input)
        return False



