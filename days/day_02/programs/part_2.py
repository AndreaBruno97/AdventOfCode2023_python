from common import *
import functools as ft


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        file_lines = open_file_lines(filepath)

        power_sum = 0

        for cur_game in file_lines[1:]:
            min_cubes = {}
            _, round_list_str = cur_game.split(": ")

            for cur_round in round_list_str.split("; "):
                for cur_cube in cur_round.split(", "):
                    cur_cube_num, cur_cube_color = cur_cube.split(" ")
                    cur_cube_num = int(cur_cube_num)

                    if cur_cube_color not in min_cubes or cur_cube_num > min_cubes[cur_cube_color]:
                        min_cubes[cur_cube_color] = cur_cube_num

            power_sum += ft.reduce(lambda a, b: a*b, min_cubes.values())

        return power_sum


p2 = Part_2()
p2.test(2286)
p2.execute()
