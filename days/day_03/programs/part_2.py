from common import *
import numpy as np


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        engine = np.matrix(open_file_str_matrix(filepath))
        rows, cols = engine.shape

        total = 0

        # map of all gears (with at least one adjacent number):
        # key is the coordinate, value is an array of adjacent numbers
        gears_map = {}

        for cur_row in range(rows):
            cur_num = 0
            is_valid = False
            # array of coordinates of gears near the current number
            gears_near = set()

            for cur_col in range(cols):
                cur_symbol = engine[cur_row, cur_col]

                if cur_symbol.isdigit():
                    # The current symbol is a digit, construct the number and check if it's valid

                    prev_row = max(0, cur_row-1)
                    prev_col = max(0, cur_col-1)
                    next_row = min(rows, cur_row+2)
                    next_col = min(cols, cur_col+2)
                    adjacent_symbols = engine[prev_row:next_row, prev_col:next_col]

                    cur_num = (10 * cur_num) + int(cur_symbol)

                    adjacent_list = np.array(adjacent_symbols).flatten()
                    if any(x.isdigit() is False and x != "." for x in adjacent_list):
                        is_valid = True
                    for cur_coord in np.transpose((adjacent_symbols == "*").nonzero()):
                        cur_coord = cur_coord + (prev_row, prev_col)
                        gears_near.add((cur_coord[0], cur_coord[1]))

                if cur_num != 0 and is_valid and ((cur_symbol.isdigit() is False) or cur_col + 1 == cols):
                    # The number is valid (is surrounded by at least a symbol
                    # This is the end of the row, or the number is interrupted by a symbol
                    #
                    # Update the map of gears
                    for cur_gear in gears_near:
                        if cur_gear in gears_map:
                            gears_map[cur_gear].append(cur_num)
                        else:
                            gears_map[cur_gear] = [cur_num]

                if cur_symbol.isdigit() is False:
                    # The current symbol is not a digit, reset the current number
                    cur_num = 0
                    is_valid = False
                    gears_near = set()

        # Get numbers only from gears which have exactly two numbers
        filtered_list_of_gear_nums = [val for val in gears_map.values() if len(val) == 2]
        # Sum of product of number couples
        return sum([val[0] * val[1] for val in filtered_list_of_gear_nums])


p2 = Part_2()
p2.test(467835)
p2.execute()
