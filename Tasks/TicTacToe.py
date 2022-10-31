# Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP

from tictactoe import Board
import random
import os
from tictactoe.egtb import Generator


board = Board(dimensions=(3, 3))
os.system('cls')
print(board)
# print(board.possible_moves().all())

first_move = random.randint(-1,1)


def player_turn():
    while True:
        player_row = int(
            input('Введите номер клетки по горизонтали от 0 до 2: '))
        player_col = int(
            input('Введите номер клетки по вертикали от 0 до 2: '))
        if board.is_empty((player_row, player_col)):
            board.push((player_row, player_col))
            break


def bot_turn():
    while True:
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        if board.is_empty((x, y)):
            board.push((x, y))
            break


while True:
    if len(board.possible_moves()) > 0:
        if first_move <= 0:
            os.system('cls')
            bot_turn()
            print(board)
            print('Вы игрок 2, играете за "0"')
            first_move = 1
        player_turn()
        if board.has_won(1):
            os.system('cls')
            print('Победил 1 игрок')
            print(board)
            break
        bot_turn()
        if board.has_won(2):
            os.system('cls')
            print('Победил 2 игрок')
            print(board)
            break
        os.system('cls')
        print(board)
        # print(len(board.possible_moves()))
    else:
        print('Ничья')
        break
