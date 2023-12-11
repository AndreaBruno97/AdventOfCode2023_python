from common import *
import numpy as np
import itertools


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        matrix = np.array(open_file_str_matrix(filepath))

        # List of empty rows
        empty_rows_list = np.where([np.all(row == '.')for row in matrix])[0]
        # List of empty columns
        empty_cols_list = np.where([np.all(col == '.') for col in matrix.T])[0]

        # Add (1000000 - 1) to each coordinate value for each empty row/column before it
        # Each row/column is already counted once in the actual coordinate value of the galaxy
        expansion_factor = 1000000 if "example"not in filepath else 100
        galaxy_list = [(
            x[0] + ((expansion_factor - 1) * len(np.where(empty_rows_list < x[0])[0])),
            x[1] + ((expansion_factor - 1) * len(np.where(empty_cols_list < x[1])[0])))
            for x in np.transpose(np.where(matrix == '#'))]

        galaxy_couples = set(itertools.combinations(galaxy_list, 2))

        total = 0
        for start_galaxy, end_galaxy in galaxy_couples:
            start_galaxy_x, start_galaxy_y = start_galaxy
            end_galaxy_x, end_galaxy_y = end_galaxy
            # Manhattan distance
            total += abs(end_galaxy_x - start_galaxy_x) + abs(end_galaxy_y - start_galaxy_y)

        return total


p2 = Part_2()
p2.test(8410)   # Example with expansion factor of 100
p2.execute()
