from common import *


class Brick:
    x: 0
    y: 0
    z: 0

    def __init__(self, init_x, init_y, init_z):
        self.x = init_x
        self.y = init_y
        self.z = init_z

    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + "," + str(self.z) + ">"

    def __repr__(self):
        return "<" + str(self.x) + "," + str(self.y) + "," + str(self.z) + ">"


def overlap(a, b):
    # return max(a[0].x, b[0].x) <= min(a[1].x, b[1].x) and max(a[0].y, b[0].y) <= min(a[1].y, b[1].y)
    return (a[1].x >= b[0].x and a[0].x <= b[1].x) and (a[1].y >= b[0].y and a[0].y <= b[1].y)


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):

        # List of bricks (couples of Brick)
        brick_list = []
        for cur_line in open_file_lines(filepath):
            start_coord, end_coord = cur_line.split("~")
            start_x, start_y, start_z = [int(x) for x in start_coord.split(",")]
            end_x, end_y, end_z = [int(x) for x in end_coord.split(",")]

            brick_list.append((Brick(start_x, start_y, start_z), Brick(end_x, end_y, end_z)))

        brick_list.sort(key=lambda x: x[0].z)

        for cur_i, brick in enumerate(brick_list):
            lowest = brick[0].z
            obstacle_list = [
                br[1].z
                for br in brick_list
                if overlap(brick, br) and lowest > br[1].z
            ]
            first_obstacle_z = obstacle_list[-1] if len(obstacle_list) > 0 else 0

            delta_z = lowest - first_obstacle_z - 1

            brick[0].z -= delta_z
            brick[1].z -= delta_z

        supporting_bricks = []
        for brick in brick_list:
            cur_supporting_brick_list = [
                br
                for br in brick_list
                if overlap(brick, br) and brick[0].z == br[1].z + 1
            ]

            supporting_bricks.append(cur_supporting_brick_list)

        unsafe_brick_set = {a[0] for a in supporting_bricks if len(a) == 1}

        return len(brick_list) - len(unsafe_brick_set)


p1 = Part_1()
p1.test(5)
p1.execute()
