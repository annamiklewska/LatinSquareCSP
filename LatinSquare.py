import numpy as np


class LatinSquare:

    def __init__(self, size):
        self.size = size
        self.square = np.zeros(size)

    def show_square(self):
        print(self.square)

    def show_square_as_matrix(self):


    def check_field(self, index):
        row = ((index+1)/self.size)-1
        col = index % self.size
        return row, col
