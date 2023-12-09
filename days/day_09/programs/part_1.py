from common import *
import numpy as np


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def next_number(self, cur_list):
        if np.all(cur_list == 0):
            return 0

        cur_last_num = cur_list[-1]
        next_num = self.next_number(np.diff(cur_list))
        return cur_last_num + next_num

    def execute_internal(self, filepath):
        history_list = [np.array([int(y) for y in x.split(" ")]) for x in open_file_lines(filepath)]

        total = 0
        for cur_history in history_list:
            total += self.next_number(cur_history)

        return total


p1 = Part_1()
p1.test(114)
p1.execute()
