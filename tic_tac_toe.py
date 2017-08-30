#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
from builtins import input

from copy import deepcopy
from enum import Enum

import random

class Symbol(Enum):
    X = 'X'
    O = 'O'

class Player(Enum):
    PLAYER = 1
    CPU = 2

def rb(board, i):
    symbol = board[i]
    if symbol != 'X' and symbol != 'O':
        return {
            '1': '₁',
            '2': '₂',
            '3': '₃',
            '4': '₄',
            '5': '₅',
            '6': '₆',
            '7': '₇',
            '8': '₈',
            '9': '₉'
        }[str(i)]
    else:
        return symbol

def draw_board(board):
    print("\n")
    print('                          |     |')
    print('                       ' + rb(board,7) + '  |  ' + rb(board,8) + '  |  ' + rb(board,9))
    print('                          |     |')
    print('                     -----------------')
    print('                          |     |')
    print('                       ' + rb(board,4) + '  |  ' + rb(board,5) + '  |  ' + rb(board,6))
    print('                          |     |')
    print('                     -----------------')
    print('                          |     |')
    print('                       ' + rb(board,1) + '  |  ' + rb(board,2) + '  |  ' + rb(board,3))
    print('                          |     |')

def make_move(board, symbol, move):
    board[move] = symbol.name

def winning_criteria(b, s):
    return ((b[7] == s and b[8] == s and b[9] == s) or
    (b[4] == s and b[5] == s and b[6] == s) or
    (b[1] == s and b[2] == s and b[3] == s) or
    (b[7] == s and b[4] == s and b[1] == s) or
    (b[8] == s and b[5] == s and b[2] == s) or
    (b[9] == s and b[6] == s and b[3] == s) or
    (b[7] == s and b[5] == s and b[3] == s) or
    (b[9] == s and b[5] == s and b[1] == s))

def is_space_free(board, move):
    return board[move] == ' '

def get_player_move(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(move)):
        move = input("\nYOUR MOVE. [ 1 - 9 ]\n")
    return int(move)

def select_random_move(board, move_list):
    possible_moves = []
    for i in move_list:
        if is_space_free(board, i):
            possible_moves.append(i)
    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None

def test_fork_move(board, cpu_symbol, i):
    copy  = deepcopy(board)
    board[i] = cpu_symbol
    winning_moves = 0
    for j in range(1, 10):
        make_move(copy, cpu_symbol, j)
        if is_space_free(copy, j):
            if winning_criteria(copy, cpu_symbol.name):
                winning_moves += 1
    return winning_moves >= 2

def get_cpu_move(board, cpu_symbol):
    player_symbol = Symbol.X if cpu_symbol is Symbol.O else Symbol.O

    for i in range(1, 10):
        copy = deepcopy(board)
        if is_space_free(copy, i):
            make_move(copy, cpu_symbol, i)
            if winning_criteria(copy, cpu_symbol.name):
                return i

    for i in range(1, 10):
        copy = deepcopy(board)
        if is_space_free(copy, i):
            make_move(copy, player_symbol, i)
            if winning_criteria(copy, player_symbol.name):
                return i

    for i in range(0, 9):
        if is_space_free(copy, i):
            if test_fork_move(copy, cpu_symbol, i):
                return i

    if is_space_free(board, 5):
        return 5

    move = select_random_move(board, [1, 3, 7, 9])
    if move != None:
        return move

    return select_random_move(board, [2, 4, 6, 8])

def is_board_full(board):
    for i in range(1, 10):
        if is_space_free(board, i):
            return False
    return True


GLOBAL_MAP = (
"\n"
"  __________--^-^-\              ___                     __-/^^\\\n"
" /.                \__.      ___/   ||                __/     _/ _-_\n"
" \                    \.    /      /         _    __/^       /__/   \/^^\___-__\n"
" /                     L-^-/      /         | \_--                             \\\n"
"/                                (          /                                /\/\n"
"|                                |        _/                           __ __/\n"
"\                               /        /                         ___/_//\n"
" \__                           /         |                        /    \/\n"
"    \________         __ _____ \         \_           __--_   ^\_ \    \n"
"             \__     /  V     \ \          \__      _/     \-/   //\n"
"                \   /          \/             \   _/            //\n"
"                 \_/                           \_/             \n"
"\n"
"          UNITED STATES                        SOVIET UNION\n"
)

NUKE = """
                              ____                      
                      __,-~~/~    `---.                 
                    _/_,---(      ,    )                
                __ /        <    /   )  \___            
               ====------------------===;;;==           
                   \/  ~"~"~"~"~"~\~"~)~",1/            
                   (_ (   \  (     >    \)              
                    \_( _ <         >_>'                
                       ~ `-i' ::>|--"                   
                           I;|.|.|                      
                          <|i::|i|>                     
                           |[::|.|                      
                            ||: |     

                          GAME OVER
"""

print(GLOBAL_MAP)
print("\nGREETINGS PROFESSOR FALKEN.  IT'S BEEN A LONG TIME.")
print("\nSHALL WE PLAY A GAME?")
print("\nWELCOME TO GLOBALTHERMONUCLEAR WA-- I MEAN, TIC-TAC-TOE!")

while True:
    game_board = [' '] * 10

    player_symbol = None
    while not (player_symbol is Symbol.X or player_symbol is Symbol.O):
        try:
            player_symbol = Symbol(input("\nCHOOSE YOUR SYMBOL [ X | O ]\n\t").upper())
        except:
            print("IDENTIFICATION NOT RECOGNISED BY SYSTEM")

    cpu_symbol = Symbol.X if player_symbol is Symbol.O else Symbol.O

    if random.randint(0, 1) == 0:
        current_player = Player.CPU
        print("\nI WILL GO FIRST.\n")
    else:
        current_player = Player.PLAYER
        print("\nYOU WILL GO FIRST.\n")

    game_in_session = True

    while game_in_session:
        if current_player is Player.PLAYER:
            draw_board(game_board)
            move = get_player_move(game_board)
            make_move(game_board, player_symbol, move)

            if winning_criteria(game_board, player_symbol.name):
                draw_board(game_board)
                print("\nINCONCEIVABLE! YOU HAVE WON THE GAME!")
                game_in_session = False
            else:
                if is_board_full(game_board):
                    draw_board(game_board)
                    print("\nA STRANGE GAME.\n\nTHE ONLY WINNING MOVE IS TO NOT PLAY.")
                    break
                else:
                    current_player = Player.CPU

        else:
            move = get_cpu_move(game_board, cpu_symbol)
            make_move(game_board, cpu_symbol, move)

            if winning_criteria(game_board, cpu_symbol.name):
                draw_board(game_board)
                print(NUKE)
                game_in_session = False
            else:
                if is_board_full(game_board):
                    draw_board(game_board)
                    print("\nA STRANGE GAME.\n\nTHE ONLY WINNING MOVE IS TO NOT PLAY.")
                    break
                else:
                    current_player = Player.PLAYER

    if not input("\nWOULD YOU LIKE TO PLAY A GAME? [ Y | N ]\n\t").lower().startswith('y'):
        break

print("\nGOODBYE PROFESSOR FALKEN.\n--CONNECTION TERMINATED--\n")
