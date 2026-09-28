# TIC-TAC-TOE
# Tic Tac Toe Game

This is a simple Tic Tac Toe game made using Python. It is a two-player game where one player uses `X` and the other uses `O`.

The game is played on a 3 × 3 board. Players take turns entering the row and column where they want to place their symbol.

## How the Game Works

1. Player 1 uses `X`.
2. Player 2 uses `O`.
3. Players enter the row and column number to place their symbol.
4. A player wins if they get three of their symbols in a row, column, or diagonal.
5. If all the positions are filled and nobody wins, the game is a draw.
6. After each game, the score is displayed.
7. The players can choose whether they want to play again.

## Features

1. 3 × 3 Tic Tac Toe board
2. Two-player gameplay
3. Checks for invalid inputs
4. Does not allow a player to select an already occupied position
5. Checks rows, columns and diagonals for a winner
6. Detects a draw
7. Keeps track of the score
8. Option to play multiple rounds

## Requirements

You only need Python installed on your computer.

No extra libraries are required.

## How to Run

1. Save the code in a Python file, for example:

```text
tic_tac_toe.py
```

2. Open the terminal or command prompt in the folder where the file is saved.

3. Run:

```bash
python tic_tac_toe.py
```

4. Follow the instructions shown on the screen.

## Example

The board looks something like this:

```text
     1   2   3
   +---+---+---+
 1  |   |   |   |
   +---+---+---+
 2  |   |   |   |
   +---+---+---+
 3  |   |   |   |
   +---+---+---+
```

For example, if Player X enters row `1` and column `2`, X will be placed in that position.

# Functions Used

# create_board()

Creates an empty 3 × 3 board.

# print_board(board)

Displays the current board in the terminal.

# play(board, Player)

Takes the row and column input from the player and places their symbol on the board.

# check_winner(board, Player)

Checks whether the current player has won the game.

### `is_board_full(board)`

Checks whether all the positions on the board are filled.

### `play_game()`

Runs one complete game of Tic Tac Toe.

### `main()`

Keeps track of the scores and allows the players to play multiple games.

## Score

The game keeps three scores:

```text
X
O
Draw
```

The score is updated after every game.

## Author
SHREYA KUMARI
