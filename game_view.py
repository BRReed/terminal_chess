



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

def sign_in():
    print("""
Please enter 1 to create an account, or 2 if you already have one.
    """)
    i = 0
    while True:
        if i >= 10:
            exit_game()
        try:
            sign_in_or_up = input(">")
            if sign_in_or_up not in (1, 2):
                i += 1
                print("You must enter the number '1' or the number '2'.")
                continue
        except:
            i += 1
            pass

def exit_game():
    pass # close ssh connection, time user out for 20 minutes

welcome_screen()