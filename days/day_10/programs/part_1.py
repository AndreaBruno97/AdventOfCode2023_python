from common import *
import numpy as np
from enum import Enum


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


class Part_1(BaseClass):

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

            if matrix[cur_row][cur_col] == 'S':
                break

        return int(step_count/2)


p1 = Part_1()
p1.test(4, [("example_2.txt", 8)])
p1.execute()
