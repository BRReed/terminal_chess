from game_logic import Chess
from copy import deepcopy

class Game():
    """A class to represent a game of Chess.
    """

    def __init__(self):
        self.c = Chess()

    def create_new_game(self):
        return self.c.current_state

    def move(self, is_black, c_coords, d_coords):
        """allows player to move piece.

        Args:
            is_black(bool): True if player is black, else False
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

        piece = self.c.current_state[c_coords][2]
        if piece == self.c.bs.empty:
            return False
        if self.c.bs.is_black(piece) != is_black:
            return False

        temp_board = deepcopy(self.c.current_state)
        temp_board = self.c.bs.move_piece(piece, c_coords, d_coords,
            temp_board)
        possible_moves = self.c.bs.possible_moves(piece, c_coords,
                                                  self.c.current_state)
        if self.c.bs.in_check(is_black, temp_board):
            return False
        if (self.c.bs.piece_movement(piece, c_coords, d_coords) and
            d_coords in possible_moves):
            self.c.bs.check_en_passant(is_black, c_coords, d_coords,
                self.c.current_state)
            self.c.move_piece(piece, c_coords, d_coords)
            self.c.bs.check_castling_valid(self.c.current_state)
            if self.c.bs.in_check(not is_black, self.c.current_state):
                if self.c.check_mate(not is_black, self.c.current_state):
                    return True
                else:
                    print('Opponent in check')
            return True
        else:
            return False

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

    def input_parse(self, is_black, user_turn, user_input):
        """Parses user input and checks validity of command

        Args:
            is_black (bool): True if player is black, else False
            user_turn (bool): True if it is player's turn, else False
            user_input (str): input from user

        Returns:
            bool: if input was valid True, else False
            bool: if board state or user turn was changed True, else False
            str: message to print to terminal
        """
        if not user_turn:
            valid_commands = ["(=)", "draw"]
        elif user_turn:
            valid_commands = ["(=)", "draw", "0-0", "0-0-0"]
        input_valid = self.validate_command(user_turn, user_input,
                                            valid_commands)
        if not input_valid:
            msg = f"You did not enter a valid command. Command = {user_input}"
            return False, False, msg
        if not user_turn:
            msg = f"Invalid command. Not your turn. Command = {user_input}"
            return False, False, msg
        if user_input in ["0-0", "0-0-0"]:
            if user_input == "0-0":
                side = "king"
            elif user_input == "0-0-0":
                side = "queen"
            valid_castle = self.castle(is_black, side)
            if not valid_castle:
                msg = f"Castling is not valid in {side}'s direction"
                return False, False, msg
            elif valid_castle:
                return True, True, f""
        if input_valid.isnumeric():
            c_coords = f"{input_valid[0]}{input_valid[1]}"
            d_coords = f"{input_valid[2]}{input_valid[3]}"
            move = self.move(is_black, c_coords, d_coords)
            if move == True:
                msg = f""
                return True, True, msg
            else:
                msg = f"Invalid move {user_input}"
                return True, False, msg
            
        

    def validate_command(self, user_turn, user_input, valid_commands):
        """Returns True if user input is valid, else returns False

        Args:
            g (cls): instance of a game
            user_turn (bool): if it is the user's turn True, else False
            user_input (str): input from user
            valid_commands (list): list of valid commands aside from coords

        Returns:
            bool/str: True if input is valid or 4 char str if valid move, 
            if invalid False
        """
        if user_input in valid_commands:
            return True
        if user_turn:
            return self.c.bs.alpha_coords_to_nums(user_input)
        return False