from common import *
import numpy as np
import enum


class Direction(Enum):
    NORTH = 0,
    EAST = 1,
    SOUTH = 2,
    WEST = 3


direction_delta = {
    Direction.NORTH: (-1, 0),
    Direction.EAST: (0, 1),
    Direction.SOUTH: (1, 0),
    Direction.WEST: (0, -1)
}

direction_dictionary = {
    ".": {
        Direction.NORTH: [Direction.NORTH],
        Direction.EAST: [Direction.EAST],
        Direction.SOUTH: [Direction.SOUTH],
        Direction.WEST: [Direction.WEST]
    },
    "/": {
        Direction.NORTH: [Direction.EAST],
        Direction.EAST: [Direction.NORTH],
        Direction.SOUTH: [Direction.WEST],
        Direction.WEST: [Direction.SOUTH]
    },
    "\\": {
        Direction.NORTH: [Direction.WEST],
        Direction.EAST: [Direction.SOUTH],
        Direction.SOUTH: [Direction.EAST],
        Direction.WEST: [Direction.NORTH]
    },
    "|": {
        Direction.NORTH: [Direction.NORTH],
        Direction.EAST: [Direction.NORTH, Direction.SOUTH],
        Direction.SOUTH: [Direction.SOUTH],
        Direction.WEST: [Direction.NORTH, Direction.SOUTH]
    },
    "-": {
        Direction.NORTH: [Direction.EAST, Direction.WEST],
        Direction.EAST: [Direction.EAST],
        Direction.SOUTH: [Direction.EAST, Direction.WEST],
        Direction.WEST: [Direction.WEST]
    }
}


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        matrix = np.array(open_file_str_matrix(filepath))
        energized_matrix = np.zeros(matrix.shape)
        rows, cols = matrix.shape

        mirror_list = []
        mirror_visited_set = set()
        for (x, y), value in np.ndenumerate(matrix):
            if value != '.':
                mirror_list.append((x, y, value))

        beam_set = {(0, 0, Direction.EAST)}

        while len(beam_set) > 0:
            cur_beam = beam_set.pop()
            cur_row, cur_col, cur_direction = cur_beam

            if cur_row < 0 or cur_row >= rows or cur_col < 0 or cur_col >= cols or cur_beam in mirror_visited_set:
                continue

            mirror_visited_set.add(cur_beam)

            cur_tile = matrix[cur_row, cur_col]
            for new_direction in direction_dictionary[cur_tile][cur_direction]:
                if new_direction == Direction.NORTH:
                    coord_list = [x[0] for x in mirror_list if x[0] < cur_row and x[1] == cur_col]
                    new_coord = coord_list[-1] if len(coord_list) > 0 else -1
                    for new_row in range(new_coord if new_coord != -1 else 0, cur_row):
                        energized_matrix[new_row, cur_col] = 1

                    if new_coord != -1:
                        beam_set.add((new_coord, cur_col, new_direction))

                elif new_direction == Direction.EAST:
                    coord_list = [x[1] for x in mirror_list if x[0] == cur_row and x[1] > cur_col]
                    new_coord = coord_list[0] if len(coord_list) > 0 else cols
                    for new_col in range(cur_col, new_coord + 1 if new_coord != cols else cols):
                        energized_matrix[cur_row, new_col] = 1

                    if new_coord != cols:
                        beam_set.add((cur_row, new_coord, new_direction))

                elif new_direction == Direction.SOUTH:
                    coord_list = [x[0] for x in mirror_list if x[0] > cur_row and x[1] == cur_col]
                    new_coord = coord_list[0] if len(coord_list) > 0 else rows
                    for new_row in range(cur_row,  new_coord + 1 if new_coord != rows else rows):
                        energized_matrix[new_row, cur_col] = 1

                    if new_coord != rows:
                        beam_set.add((new_coord, cur_col, new_direction))

                elif new_direction == Direction.WEST:
                    coord_list = [x[1] for x in mirror_list if x[0] == cur_row and x[1] < cur_col]
                    new_coord = coord_list[-1] if len(coord_list) > 0 else -1
                    for new_col in range(new_coord if new_coord != -1 else 0, cur_col):
                        energized_matrix[cur_row, new_col] = 1

                    if new_coord != -1:
                        beam_set.add((cur_row, new_coord, new_direction))

        return int(energized_matrix.sum())


p1 = Part_1()
p1.test(46)
p1.execute()
