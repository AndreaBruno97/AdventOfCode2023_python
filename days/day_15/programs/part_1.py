from common import *


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        step_list = open_file(filepath).split(",")

        total = 0

        for step in step_list:
            value = 0

            for cur_char in list(step):
                value += ord(cur_char)
                value *= 17
                value = value % 256

            total += value

        return total


p1 = Part_1()
p1.test(1320, [("example_2.txt", 52)])
p1.execute()
