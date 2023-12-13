from common import *
import numpy as np


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        matrix_list_str = open_file(filepath).split("\n\n")
        matrix_list = [np.array([list(y) for y in x.split("\n")]) for x in matrix_list_str]

        total = 0
        for matrix in matrix_list:
            rows, cols = matrix.shape

            # test vertical symmetry
            for cur_col in range(1, cols):
                cols_to_compare = min(cur_col, cols-cur_col)
                left_sub_matrix = matrix[:, cur_col-cols_to_compare:cur_col]
                right_sub_matrix = matrix[:, cur_col:cur_col+cols_to_compare]

                if np.array_equal(left_sub_matrix, right_sub_matrix[:, ::-1]):
                    total += cur_col
                    continue

            # test horizontal symmetry
            for cur_row in range(1, rows):
                rows_to_compare = min(cur_row, rows - cur_row)
                top_sub_matrix = matrix[cur_row - rows_to_compare:cur_row, :]
                bottom_sub_matrix = matrix[cur_row:cur_row + rows_to_compare, :]

                if np.array_equal(top_sub_matrix, bottom_sub_matrix[::-1, :]):
                    total += cur_row * 100
                    continue

        return total


p1 = Part_1()
p1.test(405)
p1.execute()
