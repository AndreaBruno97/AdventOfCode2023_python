from common import *
from itertools import combinations


class Hailstone:
    px = 0
    py = 0
    pz = 0
    vx = 0
    vy = 0
    vz = 0

    a = 0
    b = 0

    def __init__(self, init_str):
        self.px, self.py, self.pz, self.vx, self.vy, self.vz = [int(x) for x in init_str.replace(" @ ", ", ").split(", ")]

        self.a = self.vy / self.vx
        self.b = ((self.py * self.vx) - (self.px * self.vy)) / self.vx

    def __str__(self):
        return "<" + str(self.px) + ", " + \
               str(self.py) + ", " + \
               str(self.pz) + " # " + \
               str(self.vx) + ", " + \
               str(self.vy, ) + ", " + \
               str(self.vz) + ">"

    def __repr__(self):
        return "<" + str(self.px) + ", " + \
               str(self.py) + ", " + \
               str(self.pz) + " # " + \
               str(self.vx) + ", " + \
               str(self.vy, ) + ", " + \
               str(self.vz) + ">"


def get_collision_time_1d(pos1, pos2, vel1, vel2):
    if vel1 == vel2:
        return None

    return (pos2 - pos1) / (vel1 - vel2)


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        if "example" in filepath:
            min_pos = 7
            max_pos = 27
        else:
            min_pos = 200000000000000
            max_pos = 400000000000000

        hailstone_list = []

        for line in open_file_lines(filepath):
            hailstone_list.append(Hailstone(line))

        total = 0

        for stone1, stone2 in list(combinations(hailstone_list, 2)):
            a1, b1 = stone1.a, stone1.b
            a2, b2 = stone2.a, stone2.b

            if a1 == a2:
                # Parallel lines
                continue

            cur_x = (b2 - b1) / (a1 - a2)
            cur_y = ((a1 * b2) - (b1 * a2)) / (a1 - a2)

            if cur_x < min_pos or cur_x > max_pos or cur_y < min_pos or cur_y > max_pos:
                # Crossing outside the boundary
                continue

            t1_x = (cur_x - stone1.px) / stone1.vx
            t1_y = (cur_y - stone1.py) / stone1.vy

            if t1_x < 0 or t1_y < 0:
                # Crossed in the past for first stone
                continue

            t2_x = (cur_x - stone2.px) / stone2.vx
            t2_y = (cur_y - stone2.py) / stone2.vy

            if t2_x < 0 or t2_y < 0:
                # Crossed in the past for second stone
                continue

            total += 1

        return total


p1 = Part_1()
p1.test(2)
p1.execute()
