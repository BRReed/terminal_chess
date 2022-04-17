from game_flow import Game
from getpass import getpass
import json
from passlib.hash import bcrypt
from sys import argv, exit



def main(ip_info):
    user_ip = cleanup_ip(ip_info)

    welcome_screen()

    uname = get_info(user_ip)

    while True:

        game_list = display_games(uname)

        game_choice = choose_game(user_ip, uname, game_list)

        turn = game_choice['turn']

        perspective = check_game_info(game_choice, uname)

        g = load_game(game_choice, uname)

        g.c.print_current_state(perspective)
        user_turn = (game_choice[turn] == uname)
        is_black = (game_choice['black'] == uname)
        if user_turn:
            valid_commands = ["0-0", "0-0-0", "draw", "(=)", "resign", "xx"]
            print("It's your turn.")
        else:
            print("It's your opponent's turn. You can still draw or resign.")
            valid_commands = ["draw", "(=)", "resign", "xx"]
        user_move = input(">")
        if user_move in valid_commands:
            print(f"OH SHIT THIS WORKS {user_move}")
        else:
            pass

            
        #elif check_move(user_move): gameflow/input_parse?
            # confirm input is in a0b1 format
            # 
        #    pass





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


def create_account(user_ip):
    """take user input to create account 

    Args:
        user_ip (str): ip of user
    """
    print("Please enter your desired username.")
    data = get_json_info('users.json')
    while True:
        uname = get_input(user_ip)
        if uname not in data:
            break
        else:
            print("Sorry that user name already exists. Please choose another.")
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
                print(f"{i}. ID: {game['game_id']} vs {opp}. It's {opp}'s turn")
            else:
                print("Error with user/opp config")
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
        str: game_id the user chose
    """
    i = len(game_list)
    while True:
        game_choice = get_input(user_ip)
        if game_choice.isnumeric() and int(game_choice) <= (i-1):
            if int(game_choice) == 0:
                new_id = create_game(uname)
                game_list.append(new_id)
                game_choice = (len(game_list) - 1)
            break
        else:
            print('You entered a value that is out of bounds, please try again')
    return game_list[int(game_choice)]



def create_game(uname):
    """creates new instance of a chess game saving in user info.

    Args:
        uname (str): users name
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
        "turn": "white"}
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
** At Any time you can enter "commands" to display the commands available to 
   you, or "exit" to exit the program

* Use long algebraic notation to move pieces
* Movement format = starting square, ending square: `b2a3`
* Castling king side enter: `0-0` castling queen side enter: `0-0-0`
* To request a draw you can enter `draw` or `(=)`. Your opponent will have to 
  accept for the draw to go through
* To resign enter `resign` or `xx`
""")



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
