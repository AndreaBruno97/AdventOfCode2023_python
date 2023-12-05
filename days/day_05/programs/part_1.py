from common import *


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        file_str = open_file(filepath)
        file_list = file_str.split("\n\n")

        starting_seeds_string = file_list[0].replace("seeds: ", "")
        next_seeds = [int(x) for x in starting_seeds_string.split(" ")]

        for cur_map in file_list[1:]:
            cur_seeds = next_seeds.copy()

            for cur_row in cur_map.split("\n")[1:]:
                dest_range_start, src_range_start, range_len = [int(x) for x in cur_row.split(" ")]
                for cur_seed in [x for x in cur_seeds if src_range_start <= x < src_range_start + range_len]:
                    cur_seeds.remove(cur_seed)
                    next_seeds.remove(cur_seed)
                    next_seeds.append(cur_seed + (dest_range_start - src_range_start))

        return min(next_seeds)


p1 = Part_1()
p1.test(35)
p1.execute()
