from common import *
import numpy as np


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        max_steps = 6 if "example" in filepath else 64

        matrix = np.pad(np.array(open_file_str_matrix(filepath)), 1, 'constant', constant_values="#")
        rows, cols = matrix.shape

        start_coord = np.argwhere(matrix == "S")[0]
        cur_position_list = {(start_coord[0], start_coord[1])}
        new_position_list = set()

        for i in range(max_steps):
            new_position_list = set()
            for cur_coord in cur_position_list:
                cur_row, cur_col = cur_coord

                for delta in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    delta_row, delta_col = delta
                    new_row = cur_row + delta_row
                    new_col = cur_col + delta_col

                    if 0 < new_row < rows and 0 < new_col < cols and matrix[new_row, new_col] != "#":
                        new_position_list.add((new_row, new_col))

            cur_position_list = new_position_list

        return len(new_position_list)


p1 = Part_1()
p1.test(16)
p1.execute()
