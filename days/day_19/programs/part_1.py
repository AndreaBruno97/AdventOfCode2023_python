from common import *
import re


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        workflow_list, ratings_list = [x.split("\n") for x in open_file(filepath).split("\n\n")]

        # Dictionary of workflows:
        #   - Key: workflow name
        #   - Value: array of instructions
        #               Each instruction is an array of strings:
        #                   -   four strings for a normal instruction
        #                           (category, comparison symbol, value, next workflow)
        #                   -   a single string for A and R instructions
        workflow_dict = {}
        for cur_workflow in workflow_list:
            workflow_name, workflow_instruction_str = cur_workflow[:-1].split("{")
            workflow_dict[workflow_name] = []
            for instruction in workflow_instruction_str.split(","):
                if ":" in instruction:
                    category = instruction[0]
                    comparison_symbol = instruction[1]
                    value, next_workflow = instruction[2:].split(":")
                    value = int(value)

                    processed_instruction = [category, comparison_symbol, value, next_workflow]
                else:
                    processed_instruction = [instruction]
                workflow_dict[workflow_name].append(processed_instruction)

        total = 0

        for rating in ratings_list:
            x, m, a, s = [int(val) for val in re.findall(r"(\d+)", rating)]
            rating_dict = {"x": x, "m": m, "a": a, "s": s}

            cur_workflow_name = "in"

            while cur_workflow_name != "A" and cur_workflow_name != "R":
                cur_rule_list = workflow_dict[cur_workflow_name]

                for cur_rule in cur_rule_list:
                    if len(cur_rule) == 1:
                        cur_workflow_name = cur_rule_list[-1][0]
                        break

                    part_name, comparison_symbol, target, new_workflow_name = cur_rule
                    part = rating_dict[part_name]
                    comparison = part > target if comparison_symbol == ">" else part < target

                    if comparison:
                        cur_workflow_name = new_workflow_name
                        break

            if cur_workflow_name == "A":
                total += x + m + a + s

        return total


p1 = Part_1()
p1.test(19114)
p1.execute()
