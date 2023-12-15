from common import *
import re


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        step_list = open_file(filepath).split(",")

        # Dictionary of boxes:
        #   - key: box number
        #   - value: array of lenses (each one is a list of label and focal length)
        box_set = {}

        for step in step_list:
            label, operation, focal_len = re.search(r"([a-z]+)([=-])(\d?)", step).groups()

            box_num = 0
            for cur_char in list(label):
                box_num += ord(cur_char)
                box_num *= 17
                box_num = box_num % 256

            if operation == "-":
                # lens removal
                if box_num in box_set:
                    target_lens_list = box_set[box_num]
                    target_lens = next((i for i, v in enumerate(target_lens_list) if v[0] == label), -1)

                    if target_lens != -1:
                        # If present, remove the lens
                        del target_lens_list[target_lens]

            elif operation == "=":
                # lens insertion
                if box_num not in box_set:
                    box_set[box_num] = []

                target_lens_list = box_set[box_num]
                target_lens = next((i for i, v in enumerate(target_lens_list) if v[0] == label), -1)

                if target_lens == -1:
                    # Lens not present, add it
                    target_lens_list.append([label, int(focal_len)])
                else:
                    # Lens present, change its value
                    target_lens_list[target_lens][1] = int(focal_len)

        total = 0

        for box in box_set.items():
            box_num, lens_list = box
            if len(lens_list) > 0:
                for lens_position, lens in enumerate(lens_list):
                    total += (box_num + 1) * (lens_position + 1) * lens[1]
        return total


p2 = Part_2()
p2.test(145)
p2.execute()
