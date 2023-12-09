from common import *
import numpy as np


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def first_number(self, cur_list):
        if np.all(cur_list == 0):
            return 0

        cur_first_num = cur_list[0]
        prev_num = self.first_number(np.diff(cur_list))
        return cur_first_num - prev_num

    def execute_internal(self, filepath):
        history_list = [np.array([int(y) for y in x.split(" ")]) for x in open_file_lines(filepath)]

        total = 0
        for cur_history in history_list:
            total += self.first_number(cur_history)

        return total


p2 = Part_2()
p2.test(2)
p2.execute()
