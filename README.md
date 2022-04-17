# Terminal Chess

Terminal Chess is a game of chess you and a friend can play against each other
using SSH.

Each player will play the board from their perspective.

<img src="./images/example.png">

Project status: In development, no playable version

## Installation

TBD

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