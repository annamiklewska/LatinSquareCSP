import LatinSquare as ls
import numpy as np


def backtracking(index, square):  # index should start with 0
    sq.show_square_as_matrix()
    if index == square.length:  # the board is finished
        return True
    # try all possible values [1;n]
    for i in range(1, square.size + 1, 1):
        a = square.squares
        b = square.temp_change_value(i, index).squares
        if square.is_latin_valid(square.temp_change_value(i, index), index):  # will the square be valid after change
            square.squares[index] = i  # if it is valid after change - do change
            if backtracking(index + 1, square):  # continue checking this path until it leads to a dead end
                return True
    square.squares[index] = 0  # undo


def backtracking_with_forward_checking(index, square):  # index should start with 0
    sq.show_square_as_matrix()
    print(" CHECKED: ", square.checked)
    if index == square.length:  # the board is finished
        return True
    # try all possible values [1;n]
    for i in range(1, square.size + 1, 1):
        if square.checked[i - 1] == 1:
            continue
        if square.is_latin_valid(square.temp_change_value(i, index), index):  # will the square be valid after change
            if square.squares[index] != 0:  # if it is valid but the place was previously occupied
                square.checked[square.squares[index] - 1] = 0
            square.squares[index] = i  # if it is valid after change - do change
            if (index + 1) % square.size == 0:
                square.checked = np.zeros(square.size, int)
            else:
                square.checked[i - 1] = 1
            if backtracking_with_forward_checking(index + 1, square):  # continue checking this path until it leads to a dead end
                return True
    square.squares[index] = 0  # undo


sq = ls.LatinSquare(3)
backtracking(0, sq)
backtracking_with_forward_checking(0, sq)
sq.show_square_as_matrix()

