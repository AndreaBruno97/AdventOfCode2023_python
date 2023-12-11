from common import *
import numpy as np
import itertools


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        matrix = np.array(open_file_str_matrix(filepath))

        # Expand rows
        matrix = np.repeat(matrix, [2 if np.all(row == '.') else 1 for row in matrix], axis=0)
        # Expand columns
        matrix = np.repeat(matrix, [2 if np.all(col == '.') else 1 for col in matrix.T], axis=1)

        galaxy_list = [(x[0], x[1]) for x in np.transpose(np.where(matrix == '#'))]
        galaxy_couples = set(itertools.combinations(galaxy_list, 2))

        total = 0
        for start_galaxy, end_galaxy in galaxy_couples:
            start_galaxy_x, start_galaxy_y = start_galaxy
            end_galaxy_x, end_galaxy_y = end_galaxy
            # Manhattan distance
            total += abs(end_galaxy_x - start_galaxy_x) + abs(end_galaxy_y - start_galaxy_y)

        return total


p1 = Part_1()
p1.test(374)
p1.execute()
