from sys import argv, exit
import json

def cleanup_ip(ipInfo):
    cleanIP = f"{ipInfo}"
    cleanIP = cleanIP.strip("['")
    cleanIP = cleanIP.split(" ")
    get_info(cleanIP[0])


def welcome_screen():

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
    """
    
    """
    welcome_screen()
    print("""
Please enter 1 to create an account, or 2 if you already have one.
    """)
    i = 0
    while True:
        if i >= 10:
            exit_game(userIP, True, "Too many unsuccessful get info attempts")
        try:
            sign_in_up = get_input(userIP)
            if sign_in_up not in ("1", "2"):
                i += 1
                print("You must enter the number '1' or the number '2'.")
                continue
            else:
                break
        
        except:
            i += 1
            continue
    if sign_in_up == "1":
        create_account(userIP)
    elif sign_in_up == "2":
        sign_in(userIP)
    else:
        print("unknown error getting user input")
        exit()


def get_input(userIP):
    """returns string entered by user. if input is "exit" program will exit 

    Returns:
        (str): input from the user
    """
    i = input(">")
    if i == "exit":
        exit_game(userIP, False)
    return i


def create_account(userIP):
    pass


def sign_in(userIP):
    pass


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




cleanup_ip(argv[1:])
