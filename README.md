# Terminal Chess

Terminal Chess is a game of chess you and a friend can play against each other
using SSH.

Each player will play the board from their perspective.

<img src="./images/example.png">

Project status: Beta testing. Working version on main branch.


## Installation and Play
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
* Call game_view directly in your shell with `python3 \<dir\>\\game_view.py

I chose to serve it to a specific user when they sign in through ssh to my server. 

## How to play

* Use long algebraic notation to move pieces
* Movement format = starting square, ending square: `b2a3`
* Castling king side enter: `0-0` castling queen side enter: `0-0-0`
* To request a draw you can enter `draw` or `(=)`. Your opponent will have to 
  accept for the draw to go through
* To resign enter `resign` or `xx`

## Powershell configure:

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