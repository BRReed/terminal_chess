# **Terminal Chess**

Terminal Chess is a game of chess you and friends can play against each other
using SSH.

Each player will play the board from their perspective.

<img src="./images/example.png">

Project status: Beta version working on main.

## Table of Contents

1. [Installation](#installation) 
2. [Configuring Powershell](#configuring-powershell) 
3. [How to Play](#how-to-play)
4. [To Do](#to-do)



## Installation 
** Be Aware **:
This runs natively on shells that support UTF-8. 
Tested on fresh installs of:
* `Bash`
* `Fish`
* `Ksh`
* `sh`
* `Tcsh`
* `Zsh`

If you insist on using `PowerShell` please scroll to the `PowerShell Configure` section and follow the instructions there. 

* Install the following files into the same directory:
  * `game_flow.py`
  * `game_logic.py`
  * `game_view.py`
  * `currentgames.json`
  * `users.json`
* Call game_view directly in your shell with `python3 \<dir>\game_view.py`

I chose to serve it to a specific user when they sign in through ssh to my server. 

## Configuring Powershell:

* Run `intl.cpl` in console
* Click `Administrative` tab
* Click `Change system locale...` button
* Check `Beta: Use Unicode UTF-8` box
* Click `OK`
* Restart machine
* Once restarted run `Set-ItemProperty HKCU:\Console VirtualTerminalLevel -Type DWORD 1`
* Change default font to `DejaVu Sans Mono`
* Open a new console for changes to take affect
* Play

## How to play

* Use long algebraic notation to move pieces
* Movement format = starting square, ending square: `b2a3`
* Castling king side enter: `0-0` castling queen side enter: `0-0-0`
* To request a draw you can enter `draw` or `(=)`. Your opponent will have to 
  accept for the draw to go through
* To resign enter `resign` or `xx`


## To Do

- [X] Kick out after 3 failed password attempts
- [ ] Implement temporary ban after failed password attempts
- [ ] Clean up rules
- [ ] Change 'commands' to 'h', 'help', '-h' and integrate with rules section
- [ ] Make powershell script to automate powershell configuration
- [ ] Implement AI to play against
- [ ] Separate Piece logic into per-piece files
- [ ] Make bash script to spin up and destroy a working instance of this project from procuring local physical space to sign on screen