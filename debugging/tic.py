#!/usr/bin/python3

def print_board(board):
    """Prints the current state of the board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    """Checks if there is a winner on the board."""
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_full(board):
    """Checks if the board is full (for a draw)."""
    for row in board:
        if " " in row:
            return False
    return True

def get_valid_input(prompt):
    """Ensures input is an integer between 0 and 2."""
    while True:
        try:
            value = int(input(prompt))
            if value in [0, 1, 2]:
                return value
            else:
                print("Invalid input. Please enter 0, 1, or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def tic_tac_toe():
    """Main game loop."""
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while True:
        print_board(board)
        print(f"Player {player}'s turn.")
        
        row = get_valid_input("Enter row (0, 1, or 2): ")
        col = get_valid_input("Enter column (0, 1, or 2): ")

        if board[row][col] == " ":
            board[row][col] = player
            
            if check_winner(board):
                print_board(board)
                print(f"Player {player} wins!")
                break
            
            if is_full(board):
                print_board(board)
                print("It's a draw!")
                break
            
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")

if __name__ == "__main__":
    tic_tac_toe()
