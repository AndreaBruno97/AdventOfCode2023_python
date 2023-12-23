from common import *
import itertools


def get_max_path_len(adjacent, cur_tile, end_tile, cur_len, max_len):
    if cur_tile == end_tile:
        return max(max_len, cur_len)

    for next_tile, next_len in adjacent[cur_tile]:
        max_len = get_max_path_len(adjacent, next_tile, end_tile, cur_len + next_len, max_len)

    return max_len


def get_key_from_coord(coord):
    return str(coord[0]) + "#" + str(coord[1])


def add_adjacent(adjacent, cur_coord, next_coord):
    cur_coord = get_key_from_coord(cur_coord)
    next_coord = get_key_from_coord(next_coord)

    if cur_coord not in adjacent:
        adjacent[cur_coord] = set()

    adjacent[cur_coord].add((next_coord, 1))


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        matrix = open_file_str_matrix(filepath)
        rows = len(matrix)
        cols = len(matrix[0])

        start_col = matrix[0].index(".")
        end_col = matrix[-1].index(".")
        start_str = get_key_from_coord((0, start_col))
        end_str = get_key_from_coord((rows-1, end_col))

        adjacent = {}
        add_adjacent(adjacent, (rows-1, end_col), (rows-1, end_col))

        slopes_list = []

        for cur_row, cur_col in itertools.product(range(rows), range(cols)):

            cur_tile = matrix[cur_row][cur_col]
            if cur_tile == "#":
                continue

            if cur_tile != "." and cur_tile != "#":
                slopes_list.append(get_key_from_coord((cur_row, cur_col)))

            for delta in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                if (cur_tile == "^" and delta != [-1, 0]) or \
                        (cur_tile == ">" and delta != [0, 1]) or \
                        (cur_tile == "v" and delta != [1, 0]) or \
                        (cur_tile == "<" and delta != [0, -1]):
                    continue

                new_row = cur_row + delta[0]
                new_col = cur_col + delta[1]

                if not (0 <= new_row < rows and 0 <= new_col < cols):
                    continue

                new_tile = matrix[new_row][new_col]

                if new_tile == "#":
                    continue

                if (new_tile == "^" and delta == [1, 0]) or \
                        (new_tile == ">" and delta == [0, -1]) or \
                        (new_tile == "v" and delta == [-1, 0]) or \
                        (new_tile == "<" and delta == [0, 1]):
                    continue
                add_adjacent(adjacent, (cur_row, cur_col), (new_row, new_col))

        # If a tile is adjacent only to another one (it can only go in one direction),
        # then the patch can be simplified, deleting the middle tile and connecting the current tile
        # to the ones adjacent to the one we are deleting
        straight_path_start_list = [start_str] + slopes_list

        for cur_coord in straight_path_start_list:
            next_adj_set = adjacent[cur_coord]
            prev_coord = cur_coord
            length = 1
            while len(next_adj_set) == 1:
                next_adj, cur_len = next_adj_set.pop()

                if next_adj == end_str:
                    next_adj_set.add((next_adj, length + cur_len))
                    length += cur_len
                    break

                next_adj_set = {x for x in adjacent[next_adj] if x[0] != prev_coord}
                prev_coord = next_adj
                length += cur_len

            adjacent[cur_coord] = {(x[0], length) for x in next_adj_set}

        [print(k, v) for k, v in adjacent.items() if k in straight_path_start_list]

        return get_max_path_len(adjacent, start_str, end_str, 0, 0)


p1 = Part_1()
p1.test(94)
p1.execute()
