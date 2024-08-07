# Tic Tac Toe Game

This is a simple command-line based Tic Tac Toe game implemented in Python. The game allows two players to play against each other in a 3x3 grid.

## Features
- Two-player mode
- Input validation
- Display of game board after each move
- Check for win or draw conditions

## Requirements
- Python 3

## How to Run
1. Clone the repository:
    bash
    git clone https://github.com/RachaSaikrishna/Tic-Tac-Toe-Game.git
    
2. Navigate to the project directory:
    bash
    cd Tic-Tac-Toe-Game
    
3. Run the game:
    bash
    python tic_tac_toe.py
    

## How to Play
1. The game will prompt Player 1 (X) to enter their move by specifying a row and column number (both ranging from 0 to 2).
2. Player 2 (O) will then be prompted to enter their move.
3. The game will continue until there is a win or a draw.
4. The game will display the updated game board after each move.
5. The game will announce the result at the end: either a win for one of the players or a draw.

## Game Rules
- Players take turns placing their symbol (X or O) on the board.
- The first player to get three of their symbols in a row (vertically, horizontally, or diagonally) wins the game.
- If the board is full and no player has three in a row, the game is a draw.

## Example Gameplay

Player 1 (X) move: Enter row and column (1-9): 1 
 X |   |  
-----------
   |   |  
-----------
   |   |  

Player 2 (O) move: Enter row and column (1-9): 5
 X |   |  
-----------
   | O |  
-----------
   |   |  
   
Player 1 (X) move: Enter row and column (1-9): 2
 X | X |  
-----------
   | O |  
-----------
   |   |  
