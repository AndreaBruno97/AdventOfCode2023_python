from common import *


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        input_list = open_file_lines(filepath)

        instruction_list = list(input_list[0])

        graph = {}
        for cur_line in input_list[2:]:
            start_node, end_couple = cur_line.split(" = ")
            end_node_left, end_node_right = end_couple.replace("(", "").replace(")", "").split(", ")

            graph[start_node] = (end_node_left, end_node_right)

        modulus = len(instruction_list)
        steps_num = 0
        cur_node = "AAA"

        while cur_node != "ZZZ":
            cur_turn = instruction_list[steps_num % modulus]

            if cur_turn == "L":
                cur_node = graph[cur_node][0]
            else:
                cur_node = graph[cur_node][1]

            steps_num += 1

        return steps_num


p1 = Part_1()
p1.test(2, [("example_2.txt", 6)])
p1.execute()
