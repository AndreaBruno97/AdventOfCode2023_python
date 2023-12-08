from common import *
import math


class Part_2(BaseClass):

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
        cur_node_set = set([x for x in graph.keys() if x[2] == "A"])
        path_length_list = []

        for cur_node in cur_node_set:
            steps_num = 0
            while cur_node[2] != "Z":
                cur_turn = instruction_list[steps_num % modulus]

                if cur_turn == "L":
                    cur_node = graph[cur_node][0]
                else:
                    cur_node = graph[cur_node][1]

                steps_num += 1
            path_length_list.append(steps_num)

        return math.lcm(*path_length_list)


p2 = Part_2()
p2.test(2, [("example_2.txt", 6), ("example_3.txt", 6)])
p2.execute()
