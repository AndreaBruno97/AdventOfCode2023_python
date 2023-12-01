from common import *
import re


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        file_lines = open_file_lines(filepath)

        # "^\D*(\d).*(\d)\D*$" matches the case with two different digits
        # "^\D*(\d)\D*$" matches the case with a single digit
        regex_pattern = r"^\D*(\d).*(\d)\D*$|^\D*(\d)\D*$"
        total = 0

        for cur_line in file_lines:
            cur_match = re.search(regex_pattern, cur_line)
            first_num = cur_match.group(1)
            second_num = cur_match.group(2)
            double_num = cur_match.group(3)

            string_to_convert = first_num + second_num if double_num is None else double_num * 2

            total += int(string_to_convert)

        return total


p1 = Part_1()
p1.test(142)
p1.execute()
