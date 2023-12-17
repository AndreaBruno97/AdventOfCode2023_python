from common import *
import sys
import numpy as np
import enum

NO_DIRECTION = 100


class Direction(Enum):
    NORTH = 0,
    EAST = 1,
    SOUTH = 2,
    WEST = 3


opposite_direction = {
    Direction.NORTH: Direction.SOUTH,
    Direction.EAST: Direction.WEST,
    Direction.SOUTH: Direction.NORTH,
    Direction.WEST: Direction.EAST,
    NO_DIRECTION: 200
}


direction_delta = {
    Direction.NORTH: (-1, 0),
    Direction.EAST: (0, 1),
    Direction.SOUTH: (1, 0),
    Direction.WEST: (0, -1)
}


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        matrix = open_file_int_matrix(filepath)
        rows = len(matrix)
        cols = len(matrix[0])

        min_distance_matrix = [[sys.maxsize for y in x] for x in matrix]
        prev_node_matrix = [[(0, 0) for y in x] for x in matrix]
        min_distance_matrix[0][0] = 0

        # List of nodes to visit
        # Tuple with the following elements:
        #   - couple with the next node's coordinates
        #   - Direction from which the path is coming
        #   - number of previous consecutive straight steps before arriving in the node
        nodes_to_visit = [((0, 0), NO_DIRECTION, 1)]

        while len(nodes_to_visit) > 0:
            cur_node, prev_direction, prev_straight = nodes_to_visit.pop()
            cur_row, cur_col = cur_node
            cur_path_len = min_distance_matrix[cur_row][cur_col]

            if cur_node == (0, 3) and cur_path_len == 8:
                a = 1

            for new_direction in Direction:
                delta_row, delta_col = direction_delta[new_direction]
                new_row = cur_row + delta_row
                new_col = cur_col + delta_col

                if (new_direction == prev_direction and prev_straight >= 3):
                    b = 0

                if 0 <= new_row < rows and 0 <= new_col < cols and\
                        new_direction != opposite_direction[prev_direction] and \
                        (new_direction != prev_direction or prev_straight < 3):
                    new_path_len = cur_path_len + matrix[new_row][new_col]
                    if new_path_len < min_distance_matrix[new_row][new_col]:
                        min_distance_matrix[new_row][new_col] = new_path_len
                        prev_node_matrix[new_row][new_col] = cur_node
                        nodes_to_visit.append((
                            (new_row, new_col),
                            new_direction,
                            prev_straight+1 if new_direction == prev_direction else 0))

        result_matrix = [['  ' for y in x] for x in matrix]
        result_matrix[-1][-1] = str(min_distance_matrix[-1][-1])
        cur_node = (rows-1, cols-1)
        new_node = prev_node_matrix[-1][-1]

        while cur_node != new_node:
            result_matrix[new_node[0]][new_node[1]] = str(min_distance_matrix[new_node[0]][new_node[1]])
            cur_node = new_node
            new_node = prev_node_matrix[new_node[0]][new_node[1]]

        for x in prev_node_matrix:
            for y in x:
                print(y, end=" ")
            print()
        print(np.array(result_matrix))

        return min_distance_matrix[-1][-1]


p1 = Part_1()
p1.test(102)
p1.execute()
