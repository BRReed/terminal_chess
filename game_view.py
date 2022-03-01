from game_flow import Game
from getpass import getpass
import json
from passlib.hash import bcrypt
from sys import argv, exit



def main(ipInfo):
    userIP = cleanup_ip(ipInfo)
    welcome_screen()
    uname = get_info(userIP)
    display_games(uname, userIP)


def cleanup_ip(ipInfo):
    """cleans IP info gained from argv

    Args:
        ipInfo (str): IP info of connected user

    Returns:
        (str): basic IP info of connected user
    """
    cleanIP = f"{ipInfo}"
    cleanIP = cleanIP.strip("['")
    cleanIP = cleanIP.split(" ")
    return cleanIP[0]


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


def get_info(userIP):
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
            exit_game(userIP, True, "Too many unsuccessful get info attempts")

        sign_in_up = get_input(userIP)
        if sign_in_up not in ("1", "2"):
            i += 1
            print("You must enter the number '1' or the number '2'.")
            i+=1
            continue
        else:
            break

    if sign_in_up == "1":
        uname = create_account(userIP)
    elif sign_in_up == "2":
        uname = sign_in(userIP)
    else:
        print("unknown error getting user input")
        exit()
    return uname


def get_input(userIP):
    """returns string entered by user. if input is "exit" program will exit 

    Returns:
        (str): input from the user
    """
    while True:
        print("Enter 'exit' to exit, or 'commands' for commands")
        i = input(">")
        if i == "exit":
            exit_game(userIP, False, "hey")
        elif i == "commands":
            commands()
            continue
        else:
            break
    return i


def create_account(userIP):
    """take user input to create account 

    Args:
        userIP (str): ip of user
    """
    print("Please enter your desired username.")
    data = get_json_info('users.json')
    while True:
        uname = get_input(userIP)
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
    #new_data = {uname: {'hashedpw': hashed_pw}}
    data[uname] = {'hashedpw': hashed_pw, 'currentgames': []}
    write_to_json('users.json', data)


def sign_in(userIP):
    print("Please enter your username.")
    data = get_json_info('users.json')
    while True:
        uname = get_input(userIP)
        if uname in data:
            hashedpw = data[uname]['hashedpw']
            break
        else:
            print("Sorry, that username isn't found in our system.")
            #FUTURE: enter create account to create account
    print("Please enter your password.")
    while True:
        pw = get_input(userIP)
        if bcrypt.verify(pw, hashedpw):
            break
        else:
            print("Sorry, password does not match username")
            #FUTURE: count and timeout for 20 minutes after 5 attempts
    return uname


def display_games(uname, userIP):
    """display games user is participating in

    Args:
        uname (string): the name of the verified user
    """
    print("""
Enter the corresponding number for the game you wish to play
or '0' to create a new game
    """)
    i=1
    game_list = ['create']
    user_data = get_json_info('users.json')
    games = user_data[uname]["currentgames"]
    games_data = get_json_info('currentgames.json')
    for game in games:
        pass

        i+=1
    # user enters number, 0 goes to create game, otherwise load gameID at 
    # corresponding number
    while True:
        game_choice = get_input(userIP)
        if game_choice.isnumeric() and int(game_choice) <= (i-1):
            create_game(uname)
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
    game_ID = games_data["nextID"]
    games_data['waitForOpponent'][game_ID] = {
        "gameID": game_ID, 
        "gameState": new_game,
        "white": uname,
        "black": None,
        "turn": "white"}
    games_data["nextID"] = game_ID + 1
    write_to_json('currentgames.json', games_data)
    user_games_data = get_json_info('users.json')
    user_games_data[uname]["currentgames"].append(game_ID)
    write_to_json('users.json', user_games_data)


def load_game(gameID):
    """gets game info using gameID

    Args:
        gameID (str): reference number for existing game
    
    Returns:
        (dict): game info in dict form
    """
    data = get_json_info['currentgames.json']
    if gameID in data['waitForOpponent'].keys():
        return data['waitForOpponent'][gameID]
    elif gameID in data['inProgress'].keys():
        return data['inProgress'].keys()


def commands():
    """prints commands to terminal
    """
    print("""
** At Any time you can enter "rules" to display the rules of chess, 
   "commands" to display the commands available to you, or "exit" to exit the 
   program

* Use long algebraic notation to move pieces
* Movement format = starting square, ending square: `b2a3`
* Castling king side enter: `0-0` castling queen side enter: `0-0-0`
* To request a draw you can enter `draw` or `(=)`. Your opponent will have to 
  accept for the draw to go through
* To resign enter `resign` or `xx`
""")



def exit_game(userIP, ban, reason="None"):
    """exits out of chess program

    Args:
        userIP (string): the IP of the user
        ban (bool): True if user is banned, else False
        reason (string): description of ban
    """
    if ban:
        banList = get_json_info('ban_list.json')
        banList['to_ban'].append({userIP: reason})
        write_to_json('ban_list.json', banList)
    exit()


def get_json_info(fileName):
    """get information in a json file

    Args:
        fileName (str): a json file

    Returns:
        (dict): contents of the json file
    """
    with open(fileName) as f:
        data = json.load(f)
    return data


def write_to_json(fileName, data):
    """writes to a json file

    Args:
        fileName (str): a json file
        data (dict): new contents of the json file
    """
    with open(fileName, 'w') as f:
        json.dump(data, f)
    return




main(argv[1:])
