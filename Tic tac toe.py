# Tic Tac Toe Game
def create_board():
    board=[]
    for i in range(3):
        row=["","",""]
        board.append(row)
    return board

def print_board(board):
    print()
    print("     1   2   3")
    for i in range(3):
        print("   +---+---+---+")
        print(" " + str(i + 1) + "  |  " + board[i][0] + " | " + board[i][1] + "  |  " + board[i][2] + " | ")
    print("   +---+---+---+")
    print()

def play(board,Player):
    while True:
        print("Player", Player, "Your Turn")
        row=int(input("Enter Row(1-3):"))
        column=int(input("Enter Column(1-3):"))
        if row<1 or row>3 or column<1 or column>3:
            print("INVALID INPUT! TRY AGAIN")
        elif board[row-1][column-1] !="":
            print("POSITION ALREADY TAKEn! PLEASE Try Again")
        else:
            board[row-1][column-1]=Player
            return row-1, column-1
        
def check_winner(board,Player):
    for i in range(3): 
        if board[i][0]==Player  and  board[i][1]==Player  and  board[i][2]==Player:
            return True
        
    for j in range(3):
        if board[0][j]==Player  and  board[1][j]==Player  and  board[2][j]==Player:
            return True 
        
        if board[0][0]==Player  and  board[1][1]==Player  and  board[2][2]==Player:
            return True 
        
        if board[0][2]==Player and  board[1][1]==Player  and  board[2][0]==Player:
            return True
        return False

def is_board_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j]=="":
                return False
    return True

def play_game():
    board=create_board()
    current="X"

    print(" TIC TAC TOE ")
    print("Player1 is X and Player2 is O")
    print_board(board)

    while True:
        row, column=play(board, current)
        print_board(board)

        if check_winner(board, current):
            print("PLAYeR", current, "WINs! CONGRATULATIONs!")
            return current 
        if is_board_full(board):
            print("It's a draw")
            return "Draw"

        if current=="X":
            current="O"
        else:
            current="X"

def main():
    scores={"X":0,"O":0,"Draw":0}
    while True:
        result=play_game()
        scores[result]=scores[result]+1
        print("SCORE = X:", scores["X"], "|O:", scores["O"], "|Draw:", scores["Draw"])
        again=input("PLAY AGAIN? (yes/no):").lower()
        if again!="yes":
            print("Thank You")
            break
main()