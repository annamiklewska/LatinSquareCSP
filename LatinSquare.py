import numpy as np
import math


class LatinSquare:

    def __init__(self, size):
        self.size = size
        self.length = size**2
        self.squares = np.zeros(size ** 2, int)

    def get_size(self):
        return self.size

    def get_square(self):
        return self.squares

    def show_square(self):
        print(self.squares)

    def show_square_as_matrix(self):
        #print("\n\n************************")
        print("\n\n\nLATIN SQUARE:")
        for i in range(0, self.length, self.size):
            print("\n")
            for j in range(i, i+self.size, 1):
                print(self.squares[j], end=' ')

    def get_field(self, index):
        row = math.ceil((index+1)/self.size)-1
        col = index % self.size
        return row, col

    def get_row(self, index):
        return math.ceil((index+1)/self.size)-1

    def get_column(self, index):
        return index % self.size

    def get_index(self, row, column):
        return row * self.size + column

    def is_latin_valid(self, index):  # index should be -1 at start

        for i in range(self.length - 1):  # i = next index
            rowToCompare = self.get_row(i)
            columnToCompare = self.get_column(i)

            if self.get_row(index) == rowToCompare or self.get_column(index) == columnToCompare:
                if self.squares[index] == self.squares[self.get_index(rowToCompare, columnToCompare)] and index is not i:
                    return False

        return True
