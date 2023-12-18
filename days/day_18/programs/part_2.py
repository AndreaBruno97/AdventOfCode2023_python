from common import *


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        dig_list = open_file_lines(filepath)

        cur_coord = [0, 0]
        prev_direction = ""

        area = 0
        # The coordinate computation (vertex cross product) considers
        # the polygon created by the centers of each corner square.
        # The border is considered as increments for each corner and edge
        external_area = 0

        for dig in dig_list:
            _, _, color = dig.split(" ")
            length = int(color[2:7], 16)
            direction_code = color[7]
            if direction_code == "0":
                direction = "R"
            elif direction_code == "1":
                direction = "D"
            elif direction_code == "2":
                direction = "L"
            elif direction_code == "3":
                direction = "U"

            old_coord = cur_coord.copy()
            if direction == "U":
                cur_coord[0] += length
                new_external_area = 0.25 if prev_direction == "R" else 0.75
            elif direction == "D":
                cur_coord[0] -= length
                new_external_area = 0.25 if prev_direction == "L" else 0.75
            elif direction == "L":
                cur_coord[1] -= length
                new_external_area = 0.25 if prev_direction == "U" else 0.75
            elif direction == "R":
                cur_coord[1] += length
                new_external_area = 0.25 if prev_direction == "D" else 0.75

            area += ((old_coord[0] * cur_coord[1]) - (old_coord[1] * cur_coord[0]))
            external_area += new_external_area + (0.5 * (length - 1))
            prev_direction = direction

        area = int(abs(area/2))
        area += int(external_area)

        return area


p2 = Part_2()
p2.test(952408144115)
p2.execute()
