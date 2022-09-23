# Tic-Tac-Toe
# Created by: Logan Simmons

import os

def main():
    player = turn("")
    board = new_board()
    while not (winner(board) or stale(board)):
        draw_board(board)
        move(player, board)
        player = turn(player)
    draw_board(board)
    print('GG no RE.')

def turn(now):
    if now == "" or now == '\033[33m' + "O" + '\033[0m':
        return '\033[91m' + "X" + '\033[0m'
    else: 
        return '\033[33m' + "O" + '\033[0m'

def draw_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-----')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-----')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()

def new_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

def move(player, board):
    square = int(input(f"It is {player}'s turn:"))
    board[square - 1] = player

def winner(board):
    if (board[0] == board[1] == board[2] or
        board[3] == board[4] == board[5] or
        board[6] == board[7] == board[8] or
        board[0] == board[3] == board[6] or
        board[1] == board[4] == board[7] or
        board[2] == board[5] == board[8] or
        board[0] == board[4] == board[8] or
        board[2] == board[4] == board[6]):
        return True
    else: 
        return False

def stale(board):
    for square in range(9):
        if board[square] != 'X' and board[square] != 'O':
            return False
        else: 
            return True

the_sun = 'hot'

if the_sun == "hot":
    main()