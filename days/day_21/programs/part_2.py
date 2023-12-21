from common import *
import numpy as np
import re


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):

        # The number of steps for the example is passed inside the file name, right before the file extension
        if "example" in filepath:
            match = re.findall(r'\d+', filepath)
            max_steps = 6 if match == [] else int(match[0])
            filepath = re.sub(r'\d+', "", filepath)

        else:
            max_steps = 26501365

        matrix = np.array(open_file_str_matrix(filepath))
        rows, cols = matrix.shape

        start_coord = np.argwhere(matrix == "S")[0]
        cur_position_list = {(start_coord[0], start_coord[1]): {(0, 0)}}
        new_position_list = {}

        for i in range(max_steps):
            new_position_list = {}
            for cur_coord, cur_matrix_set in cur_position_list.items():
                cur_row, cur_col = cur_coord

                for delta in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    delta_row, delta_col = delta
                    new_row_raw = cur_row + delta_row
                    new_col_raw = cur_col + delta_col
                    new_row = new_row_raw % rows
                    new_col = new_col_raw % cols
                    new_coord = (new_row, new_col)

                    delta_row = 0
                    delta_col = 0

                    if new_row_raw < 0:
                        delta_row = -1
                    elif new_row_raw == rows:
                        delta_row = +1

                    if new_col_raw < 0:
                        delta_col = -1
                    elif new_col_raw == rows:
                        delta_col = +1

                    new_matrix_set = cur_matrix_set \
                        if delta_row == 0 and delta_col == 0 else \
                        [(x[0] + delta_row, x[1] + delta_col) for x in cur_matrix_set]

                    if matrix[new_row, new_col] != "#":
                        if new_coord not in new_position_list:
                            new_position_list[new_coord] = set()

                        new_position_list[new_coord].update(new_matrix_set)

            cur_position_list = new_position_list

        return sum([len(x) for x in new_position_list.values()])


p2 = Part_2()
p2.test(16, [
    ("example10.txt", 50),
    ("example50.txt", 1594),
    ("example100.txt", 6536),
    ("example500.txt", 167004),
    ("example1000.txt", 668697),
    ("example5000.txt", 16733044)])
p2.execute()
