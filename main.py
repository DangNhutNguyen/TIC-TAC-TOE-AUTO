import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print(" -------  ")

def check_winner(board, player):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] == player:
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] == player:
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] == player:
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] == player:
        return True

    return False

def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def get_empty_cells(board):
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                empty_cells.append((i, j))
    return empty_cells

def make_move(board, row, col, player):
    if board[row][col] == " ":
        board[row][col] = player
        return True
    return False

def player_move(board):
    while True:
        row = int(input("Enter the row (0, 1, 2): "))
        col = int(input("Enter the column (0, 1, 2): "))
        if make_move(board, row, col, "X"):
            break
        else:
            print("Cell already taken, try again.")

def ai_move(board):
    empty_cells = get_empty_cells(board)
    move = random.choice(empty_cells)
    make_move(board, move[0], move[1], "O")

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]

    while True:
        print_board(board)
        player_move(board)
        if check_winner(board, "X"):
            print_board(board)
            print("Player X wins!")
            break
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        ai_move(board)
        if check_winner(board, "O"):
            print_board(board)
            print("Player O (AI) wins!")
            break
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

tic_tac_toe()
