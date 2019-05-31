import LatinSquare as ls
import numpy as np

found = False

used = set()

occupied = np.array([])


def backtracking_wrong(index, square):
    global found
    print("\n\n\nCHECK: ", found, " ", index)
    if found:
        return
    if index < 0 or square.is_latin_valid(index):
        if index == (square.length-1):
            print("\nDONE!\n")
            found = True
        else:
            for i in range(1, square.size + 1, 1):
                    square.squares[index + 1] = i
                    square.show_square_as_matrix()
                    backtracking_wrong((index + 1), square)



def backtracking(index, square):
    # the board is full
    sq.show_square_as_matrix()
    if index == square.length:
        return True
    # try all possible values 1-n
    for i in range(1, square.size + 1, 1):
        temp = square.squares[index]
        square.squares[index] = i
        if square.is_latin_valid(index):
            if backtracking(index + 1, square):
                return True
        else:
            square.squares[index] = temp
    square.squares[index] = 0  # undo



def backtracking_with_forward_checking(index, square):
    global found
    global used
    global occupied
    print("\n\n\nCHECK: ", found, " ", index)
    if found:
        return
    if index < 0 or square.is_latin_valid(index):
        if index == (square.length-1):
            print("\nDONE!\n")
            found = True
        else:
            for i in range(1, square.size + 1, 1):
                for j in range(square.size):
                    if square.get_row(index + 1) == square.get_row(j) or square.get_column(index + 1) == square.get_column(j):
                        np.append(occupied, square.squares[index + 1])
                        #occupied.append(square.squares[index + 1])

                for j in range(occupied.size):
                    if square.get_row(index+1) == square.get_row(j) or square.get_column(index + 1) == square.get_column(j):
                        occupied = []
                square.squares[index + 1] = i
                square.show_square_as_matrix()
                backtracking((index + 1), square)

sq = ls.LatinSquare(3)
#backtracking_new(0, sq)
#backtracking(0, sq)
#backtracking_with_forward_checking(-1, sq)
#sq.show_square_as_matrix()
#sq.squares = [0, 1, 2, 1, 2, 0, 2, 0, 1]
#sq.squares = [1,0,0,0,0,0,0,0,0]
#sq.squares = [3,3,3,3,3,0,0,0,0]
sq.show_square_as_matrix()
#print(sq.is_latin_valid(0))

