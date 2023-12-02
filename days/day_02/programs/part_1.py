from common import *


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        file_lines = open_file_lines(filepath)

        max_cubes = {}
        # The first line of the input contains the list of supposed amount of cubes per color
        for cur_cube in file_lines[0].split(", "):
            cur_max_num, cur_color = cur_cube.split(" ")
            max_cubes[cur_color] = int(cur_max_num)

        id_sum = 0

        for cur_game in file_lines[1:]:
            game_str, round_list_str = cur_game.split(": ")
            cur_game = int(game_str.replace("Game ", ""))

            found = False
            for cur_round in round_list_str.split("; "):

                for cur_cube in cur_round.split(", "):
                    cur_cube_num, cur_cube_color = cur_cube.split(" ")

                    if int(cur_cube_num) > max_cubes[cur_cube_color]:
                        found = True
                        break

                if found is True:
                    break

            if found is False:
                id_sum += cur_game

        return id_sum


p1 = Part_1()
p1.test(8)
p1.execute()
