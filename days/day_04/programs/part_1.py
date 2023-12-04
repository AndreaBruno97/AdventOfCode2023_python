from common import *
import re


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        card_list = open_file_lines(filepath)

        total = 0

        for card in card_list:
            _, winning_str_list, my_str_list = re.split(r" \| |: ", card)

            winning_list = [int(x) for x in re.split(r" +", winning_str_list) if x != ""]
            my_list = [int(x) for x in re.split(r" +", my_str_list) if x != ""]

            match_num = len(set(winning_list) & set(my_list))
            total += 2**(match_num-1) if match_num > 0 else 0

        return total


p1 = Part_1()
p1.test(13)
p1.execute()
