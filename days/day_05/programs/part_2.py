from common import *

'''
Both the starting seed ranges and the almanac's rules are coded as pairs of start-finish points of a range
The overlapping of the seed's range and the rule's range can be one of these configurations (seeds as first range):
               |-----------------|
  |-----|                                               No overlapping (the seeds stay the same)
                                       |------|         No overlapping (the seeds stay the same)
           |----------|                                 xYN overlapping
                            |---------|                 NYx overlapping
                    |----------|                        NYN overlapping
        |------------------------------|                xYx overlapping
        
where the symbols are:
    - x when the subrange should not be considered (seeds are not in this range)
    - Y when the rule changes the seeds
    - N when the rule doesn't change the seeds
    
For each pair of ranges [a1, a2] and [b1, b2], there are three sub-ranges (invalid ranges of size 0 are discarded):
    - [min(a1, b1), max(a1, b1)]
    - [max(a1, b1), min(a2, b2)]
    - [min(a2, b2), max(a2, b2)]
and for each sub-range, the graph above shows how it should be handled
'''


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        file_str = open_file(filepath)
        file_list = file_str.split("\n\n")

        starting_seeds_string = file_list[0].replace("seeds: ", "")
        cur_seeds = []
        next_seeds = []

        input_seed_list = [int(x) for x in starting_seeds_string.split(" ")]
        for cur_input_seed_start, cur_input_seed_len in zip(input_seed_list[::2], input_seed_list[1::2]):
            next_seeds.append((cur_input_seed_start, cur_input_seed_start + cur_input_seed_len - 1))

        for cur_map in file_list[1:]:
            cur_seeds.extend(next_seeds)
            next_seeds = []

            for cur_row in cur_map.split("\n")[1:]:
                dest_start, src_start, range_len = [int(x) for x in cur_row.split(" ")]
                src_end = src_start + range_len - 1

                # added to cycle on an unchanging array
                cur_seeds_tmp = cur_seeds.copy()
                for cur_seed in cur_seeds_tmp:
                    cur_seeds.remove(cur_seed)

                    seed_start, seed_end = cur_seed
                    if src_end < seed_start or src_start > seed_end:
                        # No overlapping
                        cur_seeds.append(cur_seed)
                    else:
                        if seed_start < src_start:
                            cur_seeds.append((seed_start, src_start))
                        if src_end < seed_end:
                            cur_seeds.append((src_end, seed_end))

                        changing_start = max(seed_start, src_start)
                        changing_end = min(src_end, seed_end)
                        if changing_start < changing_end:
                            next_seeds.append((
                                (changing_start + dest_start - src_start),
                                (changing_end + dest_start - src_start)
                            ))

        cur_seeds.extend(next_seeds)
        return min([x[0] for x in cur_seeds])


p2 = Part_2()
p2.test(46)
p2.execute()
