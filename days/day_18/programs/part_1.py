from common import *


class Part_1(BaseClass):

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
            direction, length, color = dig.split(" ")
            length = int(length)

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


p1 = Part_1()
p1.test(62)
p1.execute()
