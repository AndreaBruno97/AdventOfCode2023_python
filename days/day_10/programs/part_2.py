from common import *
import numpy as np
from enum import Enum


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


def get_result_coordinate(coord):
    return 1 + (3 * (coord - 1))


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    # Map with the movements allowed for each symbol.
    # The direction is given by the point of view of the current point moving towards the new one.
    direction_map = {
        '|': {
            Direction.NORTH: Direction.NORTH,
            Direction.EAST: None,
            Direction.SOUTH: Direction.SOUTH,
            Direction.WEST: None,
        },
        '-': {
            Direction.NORTH: None,
            Direction.EAST: Direction.EAST,
            Direction.SOUTH: None,
            Direction.WEST: Direction.WEST,
        },
        'L': {
            Direction.NORTH: None,
            Direction.EAST: None,
            Direction.SOUTH: Direction.EAST,
            Direction.WEST: Direction.NORTH,
        },
        'J': {
            Direction.NORTH: None,
            Direction.EAST: Direction.NORTH,
            Direction.SOUTH: Direction.WEST,
            Direction.WEST: None,
        },
        '7': {
            Direction.NORTH: Direction.WEST,
            Direction.EAST: Direction.SOUTH,
            Direction.SOUTH: None,
            Direction.WEST: None,
        },
        'F': {
            Direction.NORTH: Direction.EAST,
            Direction.EAST: None,
            Direction.SOUTH: None,
            Direction.WEST: Direction.SOUTH,
        },
        '.': {
            Direction.NORTH: None,
            Direction.EAST: None,
            Direction.SOUTH: None,
            Direction.WEST: None,
        },
        'S': {
            Direction.NORTH: Direction.NORTH,
            Direction.EAST: Direction.EAST,
            Direction.SOUTH: Direction.SOUTH,
            Direction.WEST: Direction.WEST,
        }
    }
    direction_delta = {
        Direction.NORTH: (-1, 0),
        Direction.EAST: (0, 1),
        Direction.SOUTH: (1, 0),
        Direction.WEST: (0, -1),
    }

    def execute_internal(self, filepath):
        matrix = np.pad(np.array(open_file_str_matrix(filepath)), pad_width=((1, 1), (1, 1)), mode='constant', constant_values='.')
        # Possible tiles:
        #   'O' -> Outside
        #   ' ' -> Empty
        #   '#' -> Border
        # All tiles start as "Empty", except for the external ones.
        # Tiles belonging to the loop are marked as "Border"
        # The result matrix is an "expanded" map in which all border tiles are represented as a 3 by 3 tilesets
        # Example, 7 becomes this set of tiles (',' is a generic tile)
        #           ,,,
        #           ##,
        #           ,#,
        # This allows all external zones to be explicitly connected to the outer ring.
        result_matrix = np.pad(np.full((matrix.shape[0]*3, matrix.shape[1]*3), ' '), pad_width=((1, 1), (1, 1)), mode='constant', constant_values='O')

        step_count = 0
        cur_row, cur_col = [x[0] for x in np.where(matrix == 'S')]
        last_row, last_col = cur_row, cur_col

        for cur_direction in Direction:
            next_row = cur_row + self.direction_delta[cur_direction][0]
            next_col = cur_col + self.direction_delta[cur_direction][1]
            next_symbol = matrix[next_row, next_col]
            next_pipe_direction = self.direction_map[next_symbol][cur_direction]

            if (next_row, next_col) != (last_row, last_col) and next_pipe_direction is not None:
                next_direction = cur_direction
                break

        while True:

            next_row = cur_row + self.direction_delta[next_direction][0]
            next_col = cur_col + self.direction_delta[next_direction][1]
            next_symbol = matrix[next_row, next_col]
            next_direction = self.direction_map[next_symbol][next_direction]

            step_count += 1
            cur_row, cur_col = next_row, next_col
            result_row = get_result_coordinate(cur_row)
            result_col = get_result_coordinate(cur_col)
            result_matrix[result_row, result_col] = '#'
            for cur_dir in [x for x in self.direction_map[next_symbol].values() if x is not None]:
                delta_row_to_update, delta_col_to_update = self.direction_delta[cur_dir]
                result_matrix[result_row + delta_row_to_update, result_col + delta_col_to_update] = '#'

            if matrix[cur_row][cur_col] == 'S':
                break

        # Fill all outside elements with "O"

        continue_fill = True
        while continue_fill:
            continue_fill = False
            for cur_x, cur_y in np.concatenate((np.argwhere(result_matrix == ' '), np.flip(np.argwhere(result_matrix == ' '), axis=0)), axis=0):
                prev_row = max(0, cur_x-1)
                prev_col = max(0, cur_y-1)
                next_row = min(result_matrix.shape[0], cur_x+2)
                next_col = min(result_matrix.shape[1], cur_y+2)
                if np.any(result_matrix[prev_row:next_row, prev_col:next_col] == 'O'):
                    result_matrix[cur_x, cur_y] = 'O'
                    continue_fill = True

        # Expand all border tiles, leave only groups of 3x3 internal tiles,
        # that correspond to the ones that are actually internal in the starting matrix
        starting_border_tiles = np.argwhere(result_matrix == '#')
        for cur_x, cur_y in starting_border_tiles:
            result_matrix[cur_x-1:cur_x+2, cur_y-1:cur_y+2] = '#'

        # [print(' '.join(x)) for x in result_matrix]
        return int(np.count_nonzero(result_matrix == ' ')/9)


p2 = Part_2()
p2.test(1, [("example_2.txt", 1), ("example_3.txt", 4), ("example_4.txt", 4), ("example_5.txt", 8), ("example_6.txt", 10)])
p2.execute()
