import json
from game_flow import Game
from getpass import getpass
from passlib.hash import bcrypt
from sys import argv, exit


def main(ip_info):
    user_ip = cleanup_ip(ip_info)
    welcome_screen()
    uname = get_info(user_ip)

    while True:
        game_list = display_games(uname)
        game_choice = choose_game(user_ip, uname, game_list)
        if game_choice == False:
            continue
        game_id = game_choice['game_id']
        perspective = check_game_info(game_choice, uname)
        g = load_game(game_choice, uname)
        g.c.print_current_state(perspective)
        is_black = (game_choice['black'] == uname)
        if is_black:
            opponent = game_choice['white']
            op_color = 'white'
            user_color = 'black'
        else:
            opponent = game_choice['black']
            op_color = 'black'
            user_color = 'white'
        user_turn = (game_choice['turn'] == user_color)
        game_status = get_game_status(opponent)
        if game_choice['draw'][0] == True and game_choice['draw'][1] == uname:
            draw_response(uname, opponent, game_id, user_ip)
            continue

        while True:
            user_input = get_input(user_ip)
            if user_input == 'back':
                break
            if user_input in ["xx","resign"]: 
                end_game(opponent, uname, game_id)
                print(f"You have resigned from {game_id} against {opponent}")
                break
            if user_input in ['(=)', 'draw']:
                draw_request(uname, opponent, game_id)
                break
            input_valid, move, msg, = g.input_parse(is_black, user_turn, 
                                                    user_input)
            if not input_valid or not move:
                print(msg)
                continue
            if move == True:
                promo, p_space = g.c.bs.check_promotion(is_black, 
                                                        g.c.current_state)
                if promo == True:
                    promo_list = ['queen', 'rook', 'bishop', 'knight']
                    print("One of your pawns made it to your opponents back",
                          "row what would you like it to be promoted to?")
                    while True:
                        print("Enter queen, rook, bishop, or knight")
                        promo_choice = get_input(user_ip)
                        if promo_choice not in promo_list:
                            print("Invalid piece")
                            continue
                        g.c.current_state = g.c.bs.promotion(is_black, p_space,
                                                             promo_choice,
                                                             g.c.current_state)
                        break
                data = get_json_info('currentgames.json')
                data[game_status][game_id]['gameState'] = g.c.current_state
                data[game_status][game_id]['turn'] = op_color
                write_to_json('currentgames.json', data)
                g.c.print_current_state(perspective)
                if g.c.check_mate((not is_black), g.c.current_state):
                    print("Check mate! You won!")
                    end_game(opponent, uname, game_id)
                    break
                if g.c.bs.check_stalemate((not is_black), g.c.current_state):
                    print("Stalemate! This game is a draw.")
                    end_game(opponent, uname, game_id)
                    break
                break


def cleanup_ip(ip_info):
    """cleans IP info gained from argv

    Args:
        ip_info (str): IP info of connected user

    Returns:
        (str): basic IP info of connected user
    """
    clean_ip = f"{ip_info}"
    clean_ip = clean_ip.strip("['")
    clean_ip = clean_ip.split(" ")
    return clean_ip[0]


def welcome_screen():
    """prints "CHESS in the terminal" in ascii fonts
    """

    print("""
Welcome to
      ___           ___           ___           ___           ___     
     /  /\         /__/\         /  /\         /  /\         /  /\    
    /  /:/         \  \:\       /  /:/_       /  /:/_       /  /:/_   
   /  /:/           \__\:\     /  /:/ /\     /  /:/ /\     /  /:/ /\  
  /  /:/  ___   ___ /  /::\   /  /:/ /:/_   /  /:/ /::\   /  /:/ /::\ 
 /__/:/  /  /\ /__/\  /:/\:\ /__/:/ /:/ /\ /__/:/ /:/\:\ /__/:/ /:/\:\\
 \  \:\ /  /:/ \  \:\/:/__\/ \  \:\/:/ /:/ \  \:\/:/~/:/ \  \:\/:/~/:/
  \  \:\  /:/   \  \::/       \  \::/ /:/   \  \::/ /:/   \  \::/ /:/ 
   \  \:\/:/     \  \:\        \  \:\/:/     \__\/ /:/     \__\/ /:/  
    \  \::/       \  \:\        \  \::/        /__/:/        /__/:/   
     \__\/         \__\/         \__\/         \__\/         \__\/    

    _          __  __            __                      _             __
   (_)___     / /_/ /_  ___     / /____  _________ ___  (_)___  ____ _/ /
  / / __ \   / __/ __ \/ _ \   / __/ _ \/ ___/ __ `__ \/ / __ \/ __ `/ / 
 / / / / /  / /_/ / / /  __/  / /_/  __/ /  / / / / / / / / / / /_/ / /  
/_/_/ /_/   \__/_/ /_/\___/   \__/\___/_/  /_/ /_/ /_/_/_/ /_/\__,_/_/   
                                                                         

    """)


def get_info(user_ip):
    """start log in or account set up process for user

    Args:
        user_ip (str):ip of user in string format

    Returns:
        str: input from user (their username)
    """
    print("""
Enter:
1. Create an account
2. Sign in
    """)
    i = 0
    while True:
        if i >= 10:
            exit_game(user_ip, True, "Too many unsuccessful get info attempts")
        sign_in_up = get_input(user_ip)
        if sign_in_up not in ("1", "2"):
            i += 1
            print("You must enter the number '1' or the number '2'.")
            i+=1
            continue
        else:
            break

    if sign_in_up == "1":
        uname = create_account(user_ip)
    elif sign_in_up == "2":
        uname = sign_in(user_ip)
    else:
        print("unknown error getting user input")
        exit()
    return uname


def get_input(user_ip):
    """returns string entered by user. if input is "exit" program will exit

    Args:
        user_ip (str):ip of user in string format

    Returns:
        (str): input from the user
    """
    while True:
        print("Enter 'exit' to exit, or 'commands' for commands")
        i = input(">")
        if i == "exit":
            exit_game(user_ip, False, "hey")
        elif i == "commands":
            commands()
            continue
        else:
            break
    return i

def get_game_status(opponent):
    """if opponent == None return 'wait_for_opponent" else return in_progress

    Args:
        opponent (str/None): opponents name, else None

    Returns:
        str: status of game either "wait_for_opponent" or "in_progress"
    """
    if opponent == None:
        return 'wait_for_opponent'
    else:
        return 'in_progress'


def create_account(user_ip):
    """take user input to create account

    Args:
        user_ip (str): ip of user

    Returns:
        str: input from user (their username)
    """
    print("Please enter your desired username.")
    data = get_json_info('users.json')
    while True:
        uname = get_input(user_ip)
        if uname not in data:
            break
        else:
            print("Sorry that user name already exists. Please choose another."
            )
    print("""
Please enter your desired password. DO NOT ENTER A PASSWORD YOU HAVE USED OR
INTEND TO USE ELSEWHERE. SECURITY IS NOT GUARANTEED ON THIS SERVER.
    """)
    while True:
        p1 = getpass(prompt=">")
        print("Please enter your password again")
        p2 = getpass(prompt=">")
        if p1 == p2:
            break
        else:
            print("Sorry, passwords do not match. Please try again")
    hashed_pw = bcrypt.hash(p1)
    data[uname] = {'hashedpw': hashed_pw, 'currentgames': []}
    write_to_json('users.json', data)
    return uname


def sign_in(user_ip):
    """Allows user to sign in

    Args:
        user_ip (str): ip of user

    Returns:
        str: input from user (their username)
    """
    print("Please enter your username.")
    data = get_json_info('users.json')
    while True:
        uname = get_input(user_ip)
        if uname in data:
            hashedpw = data[uname]['hashedpw']
            break
        else:
            print("Sorry, that username isn't found in our system.")
            #FUTURE: enter create account to create account
    print("Please enter your password.")
    while True:
        pw = get_input(user_ip)
        if bcrypt.verify(pw, hashedpw):
            break
        else:
            print("Sorry, password does not match username")
            #FUTURE: count and timeout for 20 minutes after 5 attempts
    return uname


def display_games(uname):
    """display games user is participating in

    Args:
        uname (string): the name of the verified user
    Returns:
        list of available games
    """
    print("""
Enter the corresponding number for the game you wish to play
or '0' to create a new game
    """)
    i=1
    game_list = ['create']
    user_data = get_json_info('users.json')
    user_games = user_data[uname]['currentgames']
    games_data = get_json_info('currentgames.json')
    wait_games = []
    playing_games = []
    join_games = []
    for game in user_games:
        if game in games_data['wait_for_opponent']:
            wait_games.append(games_data['wait_for_opponent'][game])
        elif game in games_data['in_progress']:
            playing_games.append(games_data['in_progress'][game])
        else:
            print("error matching user game to current games data")
    if wait_games:
        print("These are the games you're waiting for an opponent:\n")
        for game in wait_games:
            game_list.append(game)
            if game['turn'] == 'white':
                print(f"{i}. ID: {game['game_id']} You can move before your " +
                      "opponent joins!")
            else:
                print(f"{i}. ID: {game['game_id']} You've already moved.")
            i+=1
    if playing_games:
        print("These are your games in progress:\n")
        for game in playing_games:
            game_list.append(game)
            if game['white'] != uname:
                opp = game['white']
                opp_color = 'white'
                user_color = 'black'
            elif game['white'] == uname:
                opp_color = 'black'
                user_color = 'white'
                opp = game['black']
            else:
                print("error matching user name to opponents in current " +
                "games data")
            if game['turn'] == user_color:
                print(f"{i}. ID: {game['game_id']} vs {opp}. It's your turn")
            elif game['turn'] == opp_color:
                print(f"{i}. ID: {game['game_id']} vs {opp}. It's {opp}'s turn"
                )
            else:
                print(f"Error with user/opp config")
            i+=1
    for game in games_data['wait_for_opponent']:
        if games_data['wait_for_opponent'][game]['white'] != uname:
            join_games.append(games_data['wait_for_opponent'][game])
    if join_games:
        print("These are other users games looking for an opponent:\n")
        for game in join_games:
            game_list.append(game)
            opp = game['white']
            if game['turn'] != 'white':
                print(f"{i}. ID: {game['game_id']} vs {opp}. {opp} has " +
                "already made thier first move!")
            elif game['turn'] == 'white':
                print(f"{i}. ID: {game['game_id']} vs {opp}. {opp} hasn't " +
                "made their first move.")
            i+=1
    return game_list



def check_game_info(game_dict, uname):
    """checks game information that uname is participating member of game and
    if not, adds the game to uname's currentgames and moves game from 
    waiting for opponent to in progress

    Args:
        game_dict (dict): game information
        uname (string): user name of player
    Returns:
        str: perspective of user on selected game
    """
    if game_dict['white'] == uname:
        return 'white'
    elif game_dict['black'] == uname:
        return 'black'
    elif game_dict['black'] == None:
        game_dict['black'] = uname
        if game_dict['turn'] == None:
            game_dict['turn'] = 'black'
        g = game_dict["game_id"]
        games_data = get_json_info('currentgames.json')
        games_data['in_progress'][g] = game_dict
        games_data['wait_for_opponent'].pop(g)
        write_to_json('currentgames.json', games_data)
        user_data = get_json_info('users.json')
        user_data[uname]['currentgames'].append(g)
        write_to_json('users.json', user_data)
        return 'black'
    else:
        print("Error user not in game")


def choose_game(user_ip, uname, game_list):
    """takes a list of game_id's and returns game_id user chooses

    Args:
        user_ip (str): IP of user
        game_list (list): list of valid game_id's

    Returns:
        dict: game_id the user chose
        False: if user wants to refresh list
    """
    i = len(game_list)
    while True:
        print("Enter 'r' or 'refresh' to update games list")
        game_choice = get_input(user_ip)
        if game_choice in ['r', 'refresh']:
            return False
        if game_choice.isnumeric() and int(game_choice) <= (i-1):
            if int(game_choice) == 0:
                new_id = create_game(uname)
                game_list.append(new_id)
                game_choice = (len(game_list) - 1)
            break
        else:
            print('You entered a value that is out of bounds, please try again'
            )
    return game_list[int(game_choice)]


def create_game(uname):
    """creates new instance of a chess game saving in user info.

    Args:
        uname (str): users name

    Returns:
        str: Game ID number
    """
    g = Game()
    new_game = g.create_new_game()
    games_data = get_json_info('currentgames.json')
    game_id = games_data["next_id"]
    games_data['wait_for_opponent'][game_id] = {
        "game_id": str(game_id), 
        "gameState": new_game,
        "white": uname,
        "black": None,
        "turn": "white",
        "draw": [False, None]}
    games_data["next_id"] = game_id + 1
    write_to_json('currentgames.json', games_data)
    user_games_data = get_json_info('users.json')
    user_games_data[uname]["currentgames"].append(str(game_id))
    write_to_json('users.json', user_games_data)
    return games_data['wait_for_opponent'][game_id]



def load_game(game_id, uname):
    """gets game info using game_id

    Args:
        game_id (dict): reference number for existing game
    
    Returns:
        (obj): game object
    """
    g = Game()
    g.c.current_state = game_id['gameState']
    return g


def commands():
    """prints commands to terminal
    """
    print("""
** At Any time you can enter `commands` to display the commands available to
   you, or `exit` to exit the program

* Use long algebraic notation to move pieces
* Movement format = starting square, ending square: `b2a3`
* Castling king side enter: `0-0` castling queen side enter: `0-0-0`
* To request a draw you can enter `draw` or `(=)`. Your opponent will have to
  accept for the draw to go through
* To resign enter `resign` or `xx`
* To choose a different game without making changes to the current game enter
  `back`
""")


def draw_request(uname, opponent, game_id):
    """requests draw by editing draw key in game_id to [True, opponent]

    Args:
        uname (str): user name of user requesting draw
        opponent (str): user name of opponent of uname
        game_id (str): id of the game
    """
    if opponent == None:
        print("No opponent. Please resign to end game")
        return
    game_data = get_json_info('currentgames.json')
    game_data['in_progress'][game_id]['draw'] = [True, opponent]
    write_to_json('currentgames.json', game_data)


def draw_response(uname, opponent, game_id, user_ip):
    """processes response to a draw request, removing game if draw is True, 
       editing draw key in game_id back to [False, None] if draw is False

    Args:
        uname (str): user name of user responding to draw request
        opponent (str): user name of user that made the request
        game_id (str): id of the game
        user_ip (str): ip of user
    """
    print(f"{opponent} has requested a draw. Enter '1' for yes, and '2' for no"
    )
    while True:
        user_input = get_input(user_ip)
        if user_input not in ['1', '2']:
            print("You must enter '1' or '2'")
            continue
        break
    if user_input == '1':
        end_game(uname, opponent, game_id)
    elif user_input == '2':
        game_data = get_json_info('currentgames.json')
        game_data['in_progress'][game_id]['draw'] = [False, None]
        write_to_json('currentgames.json', game_data)


def end_game(winner, loser, game_id):
    """resign from an in progress game

    Args:
        winner (str): name of user who won the game
        loser (str): name of user who lost the game
        game_id (str): id of the game being removed
    """
    user_data = get_json_info('users.json')
    if winner != None:
        user_data[winner]["currentgames"].remove(game_id)
    if loser != None:
        user_data[loser]["currentgames"].remove(game_id)
    write_to_json('users.json', user_data)
    games_data = get_json_info('currentgames.json')
    if winner != None and loser != None:
        games_data["in_progress"].pop(game_id)
    else:
        games_data["wait_for_opponent"].pop(game_id)
    write_to_json('currentgames.json', games_data)
    # future: add win to winner, loss to loser


def exit_game(user_ip, ban, reason="None"):
    """exits out of chess program

    Args:
        user_ip (string): the IP of the user
        ban (bool): True if user is banned, else False
        reason (string): description of ban
    """
    if ban:
        banList = get_json_info('ban_list.json')
        banList['to_ban'].append({user_ip: reason})
        write_to_json('ban_list.json', banList)
    exit()


def get_json_info(file_name):
    """get information in a json file

    Args:
        file_name (str): a json file

    Returns:
        (dict): contents of the json file
    """
    with open(file_name) as f:
        data = json.load(f)
    return data


def write_to_json(file_name, data):
    """writes to a json file

    Args:
        file_name (str): a json file
        data (dict): new contents of the json file
    """
    with open(file_name, 'w') as f:
        json.dump(data, f)
    return


main(argv[1:])
