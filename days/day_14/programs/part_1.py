from common import *
import numpy as np


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        matrix = np.array(open_file_str_matrix(filepath))

        rows = len(matrix)

        round_rock_list = [list(x) for x in np.transpose(np.where(matrix == "O"))]
        square_rock_list = [list(x) for x in np.transpose(np.where(matrix == "#"))]

        for cur_rock in round_rock_list:
            cur_rock_row, cur_rock_col = cur_rock
            cur_round_positions = [x[0] for x in round_rock_list if x != cur_rock and x[1] == cur_rock_col and x[0] < cur_rock_row]
            cur_square_positions = [x[0] for x in square_rock_list if x[1] == cur_rock_col and x[0] < cur_rock_row]
            cur_obstacles = cur_round_positions + cur_square_positions

            cur_rock[0] = max(cur_obstacles) + 1 if len(cur_obstacles) > 0 else 0

        return sum([rows - x[0] for x in round_rock_list])


p1 = Part_1()
p1.test(136)
p1.execute()
