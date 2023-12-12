from common import *
import re


def count_configurations(spring: str, level: int, group_list: list[int], total: int):
    cur_group_list = [len(x) for x in re.findall(r"#+", spring)]

    if level == len(spring):
        if cur_group_list == group_list:
            total += 1
        return total

    total_damaged = sum(group_list)
    total_working = len(spring) - total_damaged
    cur_damaged = spring.count("#")
    cur_working = spring.count(".")

    if spring[level] != "?":
        return count_configurations(spring, level + 1, group_list, total)
    if total_damaged > cur_damaged:
        total = count_configurations(spring[:level] + "#" + spring[level+1:], level + 1, group_list, total)
    if total_working > cur_working:
        total = count_configurations(spring[:level] + "." + spring[level+1:], level + 1, group_list, total)

    return total


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        record_list = open_file_lines(filepath)

        total = 0

        for spring, groups_str in [x.split(" ") for x in record_list]:
            group_list = [int(x) for x in groups_str.split(",")]

            total += count_configurations(spring, 0, group_list, 0)

        return total


p1 = Part_1()
p1.test(21)
p1.execute()
