from common import *
import numpy as np


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        engine = np.matrix(open_file_str_matrix(filepath))
        rows, cols = engine.shape

        total = 0

        for cur_row in range(rows):
            cur_num = 0
            is_valid = False

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

                if cur_num != 0 and is_valid and ((cur_symbol.isdigit() is False) or cur_col + 1 == cols):
                    # The number is valid (is surrounded by at least a symbol
                    # This is the end of the row, or the number is interrupted by a symbol
                    #
                    # Update the counter
                    total += cur_num

                if cur_symbol.isdigit() is False:
                    # The current symbol is not a digit, reset the current number
                    cur_num = 0
                    is_valid = False

        return total


p1 = Part_1()
p1.test(4361)
p1.execute()
