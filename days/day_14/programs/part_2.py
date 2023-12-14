from common import *
import numpy as np
import operator
import math

LOOP_SIZE = 1000000000


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        matrix = np.array(open_file_str_matrix(filepath))

        rows = len(matrix)
        cols = len(matrix[0])

        round_rock_list = [list(x) for x in np.transpose(np.where(matrix == "O"))]
        square_rock_list = [list(x) for x in np.transpose(np.where(matrix == "#"))]

        cycle_result_list = []

        for iter_num in range(LOOP_SIZE):
            # North tilt
            round_rock_list.sort(key=operator.itemgetter(0, 1))
            for cur_rock in round_rock_list:
                cur_rock_row, cur_rock_col = cur_rock
                cur_round_positions = [x[0] for x in round_rock_list if
                                       x != cur_rock and x[1] == cur_rock_col and x[0] < cur_rock_row]
                cur_square_positions = [x[0] for x in square_rock_list if x[1] == cur_rock_col and x[0] < cur_rock_row]
                cur_obstacles = cur_round_positions + cur_square_positions

                cur_rock[0] = max(cur_obstacles) + 1 if len(cur_obstacles) > 0 else 0

            # West tilt
            round_rock_list.sort(key=operator.itemgetter(1, 0))
            for cur_rock in round_rock_list:
                cur_rock_row, cur_rock_col = cur_rock
                cur_round_positions = [x[1] for x in round_rock_list if
                                       x != cur_rock and x[0] == cur_rock_row and x[1] < cur_rock_col]
                cur_square_positions = [x[1] for x in square_rock_list if
                                        x[0] == cur_rock_row and x[1] < cur_rock_col]
                cur_obstacles = cur_round_positions + cur_square_positions

                cur_rock[1] = max(cur_obstacles) + 1 if len(cur_obstacles) > 0 else 0

            # South tilt
            round_rock_list.sort(reverse=True, key=operator.itemgetter(0, 1))
            for cur_rock in round_rock_list:
                cur_rock_row, cur_rock_col = cur_rock
                cur_round_positions = [x[0] for x in round_rock_list if
                                       x != cur_rock and x[1] == cur_rock_col and x[0] > cur_rock_row]
                cur_square_positions = [x[0] for x in square_rock_list if
                                        x[1] == cur_rock_col and x[0] > cur_rock_row]
                cur_obstacles = cur_round_positions + cur_square_positions

                cur_rock[0] = min(cur_obstacles) - 1 if len(cur_obstacles) > 0 else rows - 1

            # East tilt
            round_rock_list.sort(reverse=True, key=operator.itemgetter(1, 0))
            for cur_rock in round_rock_list:
                cur_rock_row, cur_rock_col = cur_rock
                cur_round_positions = [x[1] for x in round_rock_list if
                                       x != cur_rock and x[0] == cur_rock_row and x[1] > cur_rock_col]
                cur_square_positions = [x[1] for x in square_rock_list if
                                        x[0] == cur_rock_row and x[1] > cur_rock_col]
                cur_obstacles = cur_round_positions + cur_square_positions

                cur_rock[1] = min(cur_obstacles) - 1 if len(cur_obstacles) > 0 else cols - 1

            cycle_result_list.append(sum([rows - x[0] for x in round_rock_list]))

            length = iter_num + 1
            for cycle_len in range(2, math.floor(length)):
                cur_pos = length - cycle_len
                if cycle_result_list[cur_pos:] == cycle_result_list[cur_pos-cycle_len:cur_pos]:
                    # Termination condition
                    cycle = cycle_result_list[cur_pos:]
                    return cycle[((LOOP_SIZE - length) % cycle_len) - 1]

        return -1


p2 = Part_2()
p2.test(64)
p2.execute()
